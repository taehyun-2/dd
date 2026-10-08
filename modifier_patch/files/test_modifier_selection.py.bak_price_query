"""Offline targeted checks using the real app, schemas and RuntimeWorker."""
import copy
from contextlib import contextmanager
from unittest.mock import patch

import pytest

import drive_thru_app as app
from order_runtime_final import OrderStateManager
from order_update_schema import OrderUpdate
from runtime_worker import RuntimeWorker


def fixture_items():
    items = []
    for line, menu in enumerate(["cheese_burger", "cheese_burger", "bulgogi_burger", "chicken_burger", "chicken_burger"], 1):
        items.append(dict(line_id=line, item_type="burger", quantity=1, menu=menu,
                          type="single", add_toppings=["bacon"] if line == 1 else [], exclude=[]))
    items[2].update(type="set", drink="coke", drink_size="small", side="french_fries")
    return items


@pytest.fixture(autouse=True)
def reset_context():
    app.reset_modifier_context()
    yield
    app.reset_modifier_context()


@contextmanager
def real_worker(items):
    class RuntimeWithoutModel:
        def __init__(self):
            self.manager = OrderStateManager()
            actions = [{"operation": "add", "item": {k: v for k, v in i.items() if k not in {"line_id", "add_toppings", "exclude"}}, "toppings_add": i["add_toppings"], "exclude_add": i["exclude"]} for i in items]
            self.manager.apply(OrderUpdate.model_validate({"intent": "order", "actions": actions}))

        def process(self, text):
            raise AssertionError("Deterministic modifiers must not call the language model")

    worker = RuntimeWorker(RuntimeWithoutModel)
    try:
        yield worker
    finally:
        worker.stop()


def turn(worker, text):
    result = app.unified_modifier_flow(text, worker.snapshot()["state"])
    assert result is not None, text
    if result["kind"] == "apply":
        applied = worker.process_prebuilt(result["update"], source_text=result["source_text"])
        assert applied["llm_update"]["second_llm_call"] is False
        assert not applied.get("error")
    return result


@pytest.mark.parametrize("text,status,ids", [
    ("1번 4번", "resolved", [1, 4]),
    ("첫번째랑 세번째", "resolved", [1, 3]),
    ("마지막", "resolved", [5]),
    ("치즈버거", "ambiguous", [1, 2]),
    ("치즈버거 치킨버거", "ambiguous", [1, 2, 4, 5]),
    ("치즈버거 하나 치킨버거 하나", "resolved", [1, 4]),
    ("치즈버거 두개 치킨버거 하나", "resolved", [1, 2, 4]),
    ("베이컨 추가한 거", "resolved", [1]),
    ("콜라 들어간 세트", "resolved", [3]),
    ("둘 다", "invalid_count", [1, 2, 3, 4, 5]),
    ("전부", "resolved", [1, 2, 3, 4, 5]),
    ("두 개", "resolved", [1, 2]),
    ("베이컨 추가한 치즈버거 하나 치킨버거 하나", "resolved", [1, 4]),
    ("1번이랑 치킨버거 하나", "resolved", [1, 4]),
    ("첫번째랑 치킨버거 하나", "resolved", [1, 4]),
    ("1번 99번", "not_found", []),
    ("치즈버거 세개 치킨버거 하나", "invalid_count", [1, 2]),
    ("0개", "invalid_count", [1, 2, 3, 4, 5]),
])
def test_pure_selection(text, status, ids):
    items = fixture_items()
    original = copy.deepcopy(items)
    result = app._um_resolve_selection(text, items)
    assert (result["status"], [i["line_id"] for i in result["items"]]) == (status, ids)
    assert items == original


def test_case_a_feature_preserves_original_operation():
    with real_worker(fixture_items()) as worker:
        before = worker.snapshot()["state"]
        assert turn(worker, "토마토 빼주세요")["kind"] == "reply"
        assert turn(worker, "치즈버거요")["kind"] == "reply"
        assert worker.snapshot()["state"] == before
        result = turn(worker, "베이컨 추가한 거요")
        assert result["flow"]["operation"] == "exclude_add"
        assert result["flow"]["key"] == "tomato"
        assert [i["line_id"] for i in result["items"]] == [1]
        after = worker.snapshot()["state"]["items"]
        assert after[0]["exclude"] == ["tomato"]
        assert after[0]["add_toppings"] == ["bacon"]
        assert all(not i["exclude"] for i in after[1:])


OPERATIONS = [
    (op, key, label) for op, mapping in [
        ("topping_add", app.TOPPING_LABELS), ("topping_remove", app.TOPPING_LABELS),
        ("exclude_add", app.EXCLUDE_LABELS), ("exclude_remove", app.EXCLUDE_LABELS),
    ] for key, label in mapping.items()
]
SELECTORS = [
    (["1번"], [1]), (["1번 4번"], [1, 4]), (["불고기버거요"], [3]),
    (["치즈버거 치킨버거", "전부"], [1, 2, 4, 5]),
    (["치즈버거 하나 치킨버거 하나"], [1, 4]),
    (["두 개"], [1, 2]), (["전부"], [1, 2, 3, 4, 5]),
    (["콜라 들어간 세트"], [3]), (["치킨버거요", "둘 다요"], [4, 5]),
]


@pytest.mark.parametrize("operation,key,label", OPERATIONS)
@pytest.mark.parametrize("answers,expected", SELECTORS)
def test_all_operations_through_real_worker(operation, key, label, answers, expected):
    items = fixture_items()
    field = "add_toppings" if operation.startswith("topping") else "exclude"
    for item in items:
        item[field] = [key] if operation.endswith("remove") else []
    phrase = {
        "topping_add": f"{label} 토핑 추가해주세요",
        "topping_remove": f"{label} 토핑 빼주세요",
        "exclude_add": f"{label} 빼주세요",
        "exclude_remove": f"{label} 다시 넣어주세요",
    }[operation]
    with real_worker(items) as worker:
        before = worker.snapshot()["state"]
        assert turn(worker, phrase)["kind"] == "reply"
        for answer in answers:
            result = turn(worker, answer)
        assert result["kind"] == "apply"
        assert [i["line_id"] for i in result["items"]] == expected
        after = worker.snapshot()["state"]
        assert len(after["items"]) == 5
        for old, new in zip(before["items"], after["items"]):
            wanted = copy.deepcopy(old)
            if old["line_id"] in expected:
                wanted[field] = [] if operation.endswith("remove") else [key]
            assert new == wanted


@pytest.mark.parametrize("operation,key,label", OPERATIONS)
def test_topping_feature_is_generic_for_every_operation(operation, key, label):
    items = fixture_items()
    field = "add_toppings" if operation.startswith("topping") else "exclude"
    for item in items:
        item[field] = [key] if operation.endswith("remove") else []
    feature = next(x for x in app.TOPPING_LABELS if x != key)
    items[0]["add_toppings"].append(feature)
    state = {"items": items}
    app._unified_modifier_pending = dict(operation=operation, key=key, label=label, candidate_ids=[1, 2])
    result = app.unified_modifier_flow(f"{app.TOPPING_LABELS[feature]} 추가한 거요", state)
    assert result["kind"] == "apply"
    assert result["flow"]["operation"] == operation
    assert [i["line_id"] for i in result["items"]] == [1]


def test_patty_price_and_repeated_add_are_idempotent():
    with real_worker(fixture_items()) as worker:
        before = worker.snapshot()["state"]["items"]
        result = turn(worker, "1번 4번 패티 추가해주세요")
        assert result["kind"] == "apply"
        after = worker.snapshot()["state"]["items"]
        for index in (0, 3):
            assert app.unit_price(after[index]) - app.unit_price(before[index]) == 900
        snapshot = worker.snapshot()["state"]
        assert turn(worker, "1번 패티 추가해주세요")["kind"] == "reply"
        assert worker.snapshot()["state"] == snapshot


@pytest.mark.parametrize("answer", ["하나만요", "두개요", "두개 빼주세요"])
def test_quantity_answers_never_remove_burgers(answer):
    with real_worker(fixture_items()) as worker:
        turn(worker, "양파 빼주세요")
        turn(worker, answer)
        assert len(worker.snapshot()["state"]["items"]) == 5
        assert all(i["quantity"] == 1 for i in worker.snapshot()["state"]["items"])


def test_reverse_cases_and_empty_eligibility():
    items = fixture_items()[:4]
    items[1]["add_toppings"] = ["bacon"]
    items[2].update(menu="chicken_burger", type="single", drink=None, drink_size=None, side=None, exclude=["onion"])
    items[3]["exclude"] = ["onion"]
    with real_worker(items) as worker:
        turn(worker, "베이컨 토핑 빼주세요")
        assert [i["line_id"] for i in turn(worker, "치즈버거 하나")["items"]] == [1]
        assert turn(worker, "베이컨 추가한 거 전부 취소해주세요")["kind"] == "apply"
        turn(worker, "양파 다시 넣어주세요")
        assert [i["line_id"] for i in turn(worker, "치킨버거 하나")["items"]] == [3]
        assert turn(worker, "양파 다시 넣어주세요")["kind"] == "apply"
        before = worker.snapshot()["state"]
        assert turn(worker, "피클 다시 넣어주세요")["kind"] == "reply"
        assert worker.snapshot()["state"] == before


def test_new_request_replaces_context_and_reset_clears_it():
    state = {"items": fixture_items()}
    app.unified_modifier_flow("베이컨 추가해주세요", state)
    app.unified_modifier_flow("양파 빼주세요", state)
    result = app.unified_modifier_flow("1번", state)
    assert result["flow"]["key"] == "onion"
    app.unified_modifier_flow("베이컨 추가해주세요", state)
    app.reset_router_history()
    assert app._unified_modifier_pending is None


def test_explicit_ineligible_reference_never_retargets():
    state = {"items": fixture_items()}
    result = app.unified_modifier_flow("2번 베이컨 토핑 빼주세요", state)
    assert result["kind"] == "reply"
    assert app.unified_modifier_flow("두번째", state)["kind"] == "reply"


def test_noncontiguous_ids_match_display(capsys):
    items = fixture_items()
    items[3]["line_id"], items[4]["line_id"] = 6, 9
    app.show_current_order({"items": items})
    output = capsys.readouterr().out
    assert "6. " in output and "9. " in output
    assert app._um_resolve_selection("4번", items)["status"] == "not_found"
    assert app._um_resolve_selection("네번째", items)["items"][0]["line_id"] == 6


def test_two_groups_keep_their_own_features():
    items = fixture_items()
    items[3]["exclude"] = ["onion"]
    result = app._um_resolve_selection("베이컨 추가한 치즈버거 하나 양파 뺀 치킨버거 하나", items)
    assert result["status"] == "resolved"
    assert [i["line_id"] for i in result["items"]] == [1, 4]


def test_reject_unsupported_and_multiple_requests():
    state = {"items": fixture_items()}
    for text in ("토마토 토핑 추가해주세요", "토마토 토핑 취소해주세요", "토마토 토핑 빼주세요", "양파 빼고 베이컨 추가해주세요"):
        assert app.unified_modifier_flow(text, state)["kind"] == "reply"


def test_schema_capability_tables():
    from order_schema import Topping, Exclude
    from order_runtime_final import TOPPING_ALIASES
    assert {x.value for x in Topping} == set(app.TOPPING_LABELS) == set(app.TOPPING_PRICE) == set(TOPPING_ALIASES)
    assert {x.value for x in Exclude} == set(app.EXCLUDE_LABELS)


@pytest.mark.parametrize("text", [
    "치즈버거 말고 치킨버거 전부", "매운 버거 하나", "치즈버거 또는 치킨버거 하나",
    "치킨버거 없는 거", "1번이랑 모르는버거 하나",
    "모르는버거 그리고 치즈버거 하나",
])
def test_unsupported_selectors_never_partially_apply(text):
    state = {"items": fixture_items()}
    app.unified_modifier_flow("양파 빼주세요", state)
    assert app.unified_modifier_flow(text, state)["kind"] == "reply"


@pytest.mark.parametrize("text", [
    "치즈버거 하나 베이컨 추가해서 주세요", "치킨버거 하나 양파 없이 주세요",
    "치즈버거 하나 주세요", "치즈버거 취소해주세요",
])
def test_new_explicit_orders_leave_modifier_context(text):
    state = {"items": fixture_items()}
    app.unified_modifier_flow("양파 빼주세요", state)
    assert app.unified_modifier_flow(text, state) is None
    assert app._unified_modifier_pending is None


@pytest.mark.parametrize("operation,key,label", OPERATIONS)
def test_excluded_ingredient_feature_is_generic(operation, key, label):
    items = fixture_items()
    field = "add_toppings" if operation.startswith("topping") else "exclude"
    for item in items:
        item[field] = [key] if operation.endswith("remove") else []
    feature = next(x for x in app.EXCLUDE_LABELS if x != key)
    items[0]["exclude"].append(feature)
    app._unified_modifier_pending = dict(operation=operation, key=key, label=label, candidate_ids=[1, 2])
    result = app.unified_modifier_flow(f"{app.EXCLUDE_LABELS[feature]} 뺀 거요", {"items": items})
    assert result["kind"] == "apply"
    assert result["flow"]["operation"] == operation
    assert [i["line_id"] for i in result["items"]] == [1]


@pytest.mark.parametrize("method", ["vehicle_enter", "vehicle_exit", "finish_customer_order", "force_reset", "reset_current_order"])
def test_session_lifecycle_clears_context(method, monkeypatch):
    from unittest.mock import Mock
    session = app.VehicleSessionController.__new__(app.VehicleSessionController)
    session.runtime_worker = Mock()
    session.vehicle_present = False
    session.state = app.AppState.IDLE
    session._stop_stt = Mock()
    session._start_stt = Mock()
    for name in ("ui_reset_for_vehicle", "ui_set_voice_mode", "soomac_say", "show_idle", "show_waiting_for_exit"):
        monkeypatch.setattr(app, name, Mock())
    app.unified_modifier_flow("양파 빼주세요", {"items": fixture_items()})
    getattr(session, method)()
    assert app._unified_modifier_pending is None


@pytest.mark.parametrize("commands,field,key,ids", [
    (["토마토 빼주세요", "치즈버거요", "베이컨 추가한 거요"], "exclude", "tomato", [1]),
    (["양상추 빼주세요", "치킨버거 치즈버거", "전부"], "exclude", "lettuce", [1, 2, 4, 5]),
    (["양상추 빼주세요", "치즈버거 하나 치킨버거 하나"], "exclude", "lettuce", [1, 4]),
    (["양상추 빼주세요", "1번 4번"], "exclude", "lettuce", [1, 4]),
    (["베이컨 추가해주세요", "치킨버거요", "둘 다요"], "add_toppings", "bacon", [1, 4, 5]),
    (["패티 추가해주세요", "치즈버거 하나 치킨버거 하나"], "add_toppings", "patty", [1, 4]),
])
def test_actual_app_loop_skips_router_and_legacy(commands, field, key, ids, monkeypatch):
    from types import SimpleNamespace
    from unittest.mock import Mock
    with real_worker(fixture_items()) as worker:
        monkeypatch.setattr(app, "RuntimeWorker", lambda *a, **k: worker)
        monkeypatch.setattr(app, "VehicleSessionController", lambda *a, **k: SimpleNamespace(state=app.AppState.ORDERING))
        for name in ("RosSTTUDPInput", "SpeechInputWorker", "STTSessionController", "OrderHandoffManager",
                     "start_customer_ui_server", "stop_customer_ui_server", "soomac_say",
                     "ui_add_customer_message", "ui_set_voice_mode", "ui_set_order_items"):
            monkeypatch.setattr(app, name, Mock())
        forbidden = []
        for name in ("route_customer_utterance", "rewrite_reverse_modifier_target_followup",
                     "pre_router_reverse_modifier_request", "burger_target_followup_clarify_reply",
                     "rewrite_topping_target_followup", "rewrite_exclude_target_followup"):
            mock = Mock(side_effect=AssertionError("Unexpected model/legacy call: " + name))
            forbidden.append(mock)
            monkeypatch.setattr(app, name, mock)
        utterances = iter([*commands, "/quit"])
        monkeypatch.setattr(app, "get_customer_input", lambda *a: next(utterances))
        app.main()
        assert all(mock.call_count == 0 for mock in forbidden)
        state = worker.snapshot()["state"]
        assert [i["line_id"] for i in state["items"] if key in i[field]] == ids
        assert len(state["items"]) == 5


@pytest.mark.parametrize("text", ["콜라에 베이컨 추가해주세요", "치즈스틱에 치즈 추가해주세요"])
def test_non_burger_target_is_not_a_set_feature(text):
    with real_worker(fixture_items()) as worker:
        before = worker.snapshot()["state"]
        assert turn(worker, text)["kind"] == "reply"
        assert worker.snapshot()["state"] == before


def test_both_named_unique_groups():
    items = [fixture_items()[0], fixture_items()[3]]
    result = app._um_resolve_selection("치즈버거 치킨버거 둘 다", items)
    assert result["status"] == "resolved"
    assert [i["line_id"] for i in result["items"]] == [1, 4]


def test_finalize_leaves_pending_and_filler_request_works():
    state = {"items": fixture_items()}
    assert app.unified_modifier_flow("치즈 좀 넣어줘", state)["kind"] == "reply"
    result = app.unified_modifier_flow("그중 하나만", state)
    assert result["kind"] == "apply"
    assert result["flow"]["key"] == "cheese"
    app.unified_modifier_flow("양파 빼주세요", state)
    assert app.unified_modifier_flow("이대로 주문 확정할게요", state) is None
    assert app._unified_modifier_pending is None


@pytest.mark.parametrize("operation,key,label", OPERATIONS)
def test_explicit_target_eligibility_and_idempotency(operation, key, label):
    items = fixture_items()
    field = "add_toppings" if operation.startswith("topping") else "exclude"
    for item in items:
        item[field] = [key] if operation.endswith("remove") else []
    phrase = {"topping_add": "토핑 추가해주세요", "topping_remove": "토핑 빼주세요",
              "exclude_add": "빼주세요", "exclude_remove": "다시 넣어주세요"}[operation]
    with real_worker(items) as worker:
        result = turn(worker, f"1번 버거에 {label} {phrase}")
        assert result["kind"] == "apply"
        assert [i["line_id"] for i in result["items"]] == [1]
        after = worker.snapshot()["state"]
        assert turn(worker, f"1번 {label} {phrase}")["kind"] == "reply"
        assert worker.snapshot()["state"] == after
        assert all(len(i[field]) == len(set(i[field])) for i in after["items"])


def test_router_fastpath_patty_capability():
    from types import SimpleNamespace
    from router_fastpath import build_router_fastpath
    act = {"family": "order_action", "subtype": "modify", "commitment": "explicit",
           "resolution": "resolved", "target_domain": "topping", "target": "patty",
           "reference": {"source": "current_order", "resolved": True, "line_ids": [1]}}
    output = SimpleNamespace(model_dump=lambda **kwargs: {"acts": [copy.deepcopy(act)]})
    update, reason = build_router_fastpath(output, "패티 추가해주세요", {"items": fixture_items()}, None)
    assert update is not None, reason
    assert OrderUpdate.model_validate(update).actions[0].toppings_add[0].value == "patty"
    act["target"] = "tomato"
    update, reason = build_router_fastpath(output, "토마토 토핑 추가해주세요", {"items": fixture_items()}, None)
    assert update is None


def test_pending_candidate_cannot_apply_wrong_topping():
    items = fixture_items()
    items[3]["add_toppings"] = ["patty"]
    app._unified_modifier_pending = {
        "operation": "topping_remove",
        "key": "patty",
        "label": "패티",
        "candidate_ids": [1, 4],
    }
    result = app.unified_modifier_flow("베이컨 추가한 거요", {"items": items})
    assert result["kind"] == "reply"
    assert "적용할 수 없습니다" in result["text"] or "찾지 못했습니다" in result["text"]
    assert app._unified_modifier_pending is None


def test_single_topping_remove_selects_only_eligible_item():
    items = fixture_items()
    items[3]["add_toppings"] = ["patty"]
    result = app.unified_modifier_flow("패티 취소해줘", {"items": items})
    assert result["kind"] == "apply"
    assert [item["line_id"] for item in result["items"]] == [4]
    assert result["update"]["actions"][0]["toppings_remove"] == ["patty"]

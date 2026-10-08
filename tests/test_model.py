import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pytest

from scripts.validate_model import calculate_model


def test_completed_denominator_and_baseline():
    model = calculate_model({"B6": "A", "B9": 40, "B10": .75, "B15": 1, "B16": 5,
        "B17": 1.25, "B18": .1, "B19": 4, "B20": 8000, "B21": 12000,
        "B22": 2000, "B30": 0, "B34": 0, "B35": 0, "B36": 0, "B37": 0,
        "B41": 10, "B42": 0, "B46": .08, "B50": 20, "B51": .25,
        "B52": 15, "B53": 20, "B59": 300, "B68": 26160}, 60)
    assert model["completed"] == 30
    assert model["cogs"] == pytest.approx(454.33728)
    assert model["cost_per_job"] == pytest.approx(15.144576)
    assert model["price_floor"] == pytest.approx(45.433728)
    assert model["gross_margin"] == pytest.approx(.7475904)
    assert model["containment_gm60"] == pytest.approx(.473268)


@pytest.fixture
def inputs():
    import json
    return json.loads((Path(__file__).resolve().parents[1] / "data/workbook-inputs.json").read_text())["sheets"]["1_Cost_Job"]


def test_human_escalation_variant_b_and_overhead(inputs):
    a = calculate_model(inputs, 60)
    b = calculate_model(dict(inputs, B6="B"), 60)
    assert a["escalation"] == 0
    assert b["escalation"] == pytest.approx(66.6666666667)
    assert b["cost_per_job"] == pytest.approx(17.3667982222)
    assert a["cost_with_overhead"] == pytest.approx(25.144576)
    assert a["gross_margin"] == pytest.approx(.7475904)


def test_retry_and_cache_batch_cost(inputs):
    a = calculate_model(inputs, 60)
    assert a["llm"] == pytest.approx(.1004)
    assert a["retry"] == pytest.approx(.008032)
    assert a["qa"] == 50
    assert calculate_model(dict(inputs, B30=1), 60)["llm"] == pytest.approx(.0502)


@pytest.mark.parametrize("rate,expected", [(.5,22.716864), (.6,18.93072), (.7,16.2263314286), (.8,14.19804), (.9,12.62048)])
def test_sensitivity_uses_completed_denominator(inputs, rate, expected):
    result = calculate_model(dict(inputs, B10=rate), 60)
    assert result["cost_per_job"] == pytest.approx(expected)


@pytest.mark.parametrize("key,value", [("B10",0), ("B10",1.1), ("B10",-.1), ("B10","75%"),
    ("B9",0), ("B9",-1), ("B9",float("inf")), ("B19",0), ("B19",1.5),
    ("B41",-1), ("B41",None), ("B46",1.1), ("B46",float("nan")),
    ("B51",1.1), ("B6","C"), ("B30",.5), ("B59",-1), ("B15",True)])
def test_invalid_inputs_fail_closed(inputs, key, value):
    with pytest.raises(ValueError):
        calculate_model(dict(inputs, **{key:value}), 60)


def test_missing_cost_category_is_rejected(inputs):
    del inputs["B41"]
    with pytest.raises(ValueError, match="B41"):
        calculate_model(inputs, 60)


@pytest.mark.parametrize("price", [0,-1,None,float("nan"),True])
def test_price_must_be_positive_finite(inputs, price):
    with pytest.raises(ValueError):
        calculate_model(inputs, price)



def test_speech_telephony_and_retry_are_direct_costs(inputs):
    model = calculate_model(dict(inputs, B34=.01, B35=3, B36=50, B37=1000, B42=.02), 60)
    assert model["cogs"] == pytest.approx(460.19328)
    assert model["retry"] == pytest.approx(.014432)


@pytest.mark.parametrize("margin", [-.1, 1, 1.1, "60%", float("nan")])
def test_invalid_target_margin_is_rejected(inputs, margin):
    with pytest.raises(ValueError):
        calculate_model(inputs, 60, margin)


def test_variant_b_matches_original_lab_worked_example(inputs):
    ticket = dict(inputs, B6="B", B9=1000, B10=.82, B19=6, B20=3000, B21=1000,
                  B22=300, B41=.005, B50=9, B51=.05, B52=2, B53=6, B59=0)
    model = calculate_model(ticket, .99)
    assert model["llm"] == pytest.approx(.02025)
    assert model["cogs"] == pytest.approx(203.87)
    assert model["cost_per_job"] == pytest.approx(.2486219512195)
    assert model["containment_gm60"] == pytest.approx(.72675154321)

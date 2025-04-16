# test_bmi_calculator.py
import pytest
from bmi_calculator import calculate_bmi, interpret_bmi # Import from your refactored file


# --- Tests for calculate_bmi ---
def test_calculate_bmi_normal():
    assert calculate_bmi(weight=70, height=1.75) == 23 # 70 / (1.75*1.75) = 22.857 -> 23

def test_calculate_bmi_rounding_down():
    assert calculate_bmi(weight=70.5, height=1.7) == 24 # 70.5 / (1.7*1.7) = 24.39... -> 24

def test_calculate_bmi_rounding_up():
    # Note: round(24.5) -> 24, round(25.5) -> 26 (rounds to nearest even for .5 in Python 3)
    # Let's test something that clearly rounds up
    assert calculate_bmi(weight=72, height=1.7) == 25 # 72 / (1.7*1.7) = 24.91... -> 25

def test_calculate_bmi_zero_weight():
    with pytest.raises(ValueError, match="Weight must be positive"):
        calculate_bmi(weight=0, height=1.7)

def test_calculate_bmi_zero_height():
    with pytest.raises(ValueError, match="Height must be positive"):
        calculate_bmi(weight=60, height=0)

def test_calculate_bmi_negative_height():
    with pytest.raises(ValueError, match="Height must be positive"):
        calculate_bmi(weight=60, height=-1.7)

# Optional: Test negative weight if you didn't raise an error for it
# def test_calculate_bmi_negative_weight():
#     assert calculate_bmi(weight=-60, height=1.7) == -21 # Or whatever behavior you expect

# --- Tests for interpret_bmi ---
def test_interpret_underweight():
    assert interpret_bmi(17) == "Your BMI is 17, you are underweight."
    assert interpret_bmi(18) == "Your BMI is 18, you are underweight." # Boundary check

def test_interpret_normal_weight():
    assert interpret_bmi(19) == "Your BMI is 19, you have a normal weight." # Boundary check
    assert interpret_bmi(22) == "Your BMI is 22, you have a normal weight."
    assert interpret_bmi(24) == "Your BMI is 24, you have a normal weight." # Boundary check

def test_interpret_overweight():
    assert interpret_bmi(25) == "Your BMI is 25, you are overweight." # Boundary check
    assert interpret_bmi(30) == "Your BMI is 30, you are overweight."

def test_interpret_zero_bmi():
    assert interpret_bmi(0) == "Your BMI is 0, you are underweight."

# --- Integration style test (optional, tests combined logic) ---
def test_calculation_and_interpretation():
    weight = 50
    height = 1.7
    bmi = calculate_bmi(weight, height) # bmi = 17
    message = interpret_bmi(bmi)
    assert message == "Your BMI is 17, you are underweight."

    weight = 72
    height = 1.7
    bmi = calculate_bmi(weight, height) # bmi = 25
    message = interpret_bmi(bmi)
    assert message == "Your BMI is 25, you are overweight."
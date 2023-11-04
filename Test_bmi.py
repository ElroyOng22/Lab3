import Lab2.bmi as bmi
import pytest
def test_bmi_normal_weight():
    # Test the BMI classification for Normal Weight
    result = bmi.calculate_bmi(height=1.73, weight=70)
    assert result[1] == "Normal Weight"

def test_bmi_over_weight():
    # Test the BMI classification for Over Weight
    result = bmi.calculate_bmi(height=1.73, weight=80)
    assert result[1] == "Over Weight"

def test_bmi_under_weight():
    # Test the BMI classification for Under Weight
    result = bmi.calculate_bmi(height=1.73, weight=50)
    assert result[1] == "Under Weight"


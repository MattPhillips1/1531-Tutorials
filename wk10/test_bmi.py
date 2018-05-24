from bmi import calculate_bmi
import pytest


def test_calculate_bmi():
    result = calculate_bmi(70, 1.8)
    assert result == 21.604938271604937


def test_exception():
    with pytest.raises(ZeroDivisionError):
        calculate_bmi(70, 0)

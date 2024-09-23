import pytest
from src.Roman_Calculator.ErrorHandling import *
from src.Roman_Calculator.inttoroman import *


# Mock the error handler to raise an exception for invalid cases
def test_num2roman(monkeypatch):
    # Mock num2romanErrorHandler to avoid exiting the test
    def mock_error_handler(result):
        if result < 0:
            raise ValueError("Negative numbers can't be represented in Roman numerals.")
        elif result == 0:
            raise ValueError("0 does not exist in Roman numerals.")
        elif result > 3999:
            raise ValueError("You're going to need a bigger calculator.")

    monkeypatch.setattr("src.Roman_Calculator.ErrorHandling.num2romanErrorHandler", mock_error_handler)

    # Test for valid numbers
    assert num2roman(1) == "I"
    assert num2roman(2) == "II"
    assert num2roman(3) == "III"
    assert num2roman(4) == "IV"
    assert num2roman(5) == "V"
    assert num2roman(6) == "VI"
    assert num2roman(9) == "IX"
    assert num2roman(10) == "X"
    assert num2roman(40) == "XL"
    assert num2roman(50) == "L"
    assert num2roman(90) == "XC"
    assert num2roman(100) == "C"
    assert num2roman(500) == "D"
    assert num2roman(1000) == "M"
    assert num2roman(1999) == "MCMXCIX"
    assert num2roman(2023) == "MMXXIII"
    assert num2roman(3998) == "MMMCMXCVIII"
    assert num2roman(3999) == "MMMCMXCIX"

    with pytest.raises(ValueError, match="Negative numbers can't be represented in Roman numerals."):
        num2roman(-1)
    with pytest.raises(ValueError, match="0 does not exist in Roman numerals."):
        num2roman(0)
    with pytest.raises(ValueError, match="You're going to need a bigger calculator."):
        num2roman(4000)



def test_num2roman_error_handling(monkeypatch):
    # Mock num2romanErrorHandler to raise a ValueError instead of exiting
    def mock_error_handler(result):
        if result < 0:
            raise ValueError("Negative numbers can't be represented in Roman numerals.")
        elif result == 0:
            raise ValueError("0 does not exist in Roman numerals.")
        elif result > 3999:
            raise ValueError("You’re going to need a bigger calculator.")
    
    monkeypatch.setattr("src.Roman_Calculator.ErrorHandling.num2romanErrorHandler", mock_error_handler)

    # Test negative number
    with pytest.raises(ValueError, match="Negative numbers can't be represented in Roman numerals."):
        num2roman(-1)

    # Test zero
    with pytest.raises(ValueError, match="0 does not exist in Roman numerals."):
        num2roman(0)

    # Test number greater than 3999
    with pytest.raises(ValueError, match="You're going to need a bigger calculator."):
        num2roman(4000)
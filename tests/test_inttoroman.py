import pytest
from src.Roman_Calculator.ErrorHandling import *
from src.Roman_Calculator.inttoroman import *

def test_num2roman_valid_cases():
    # Test for valid conversions
    assert int2roman(1) == "I"
    assert int2roman(2) == "II"
    assert int2roman(3) == "III"
    assert int2roman(4) == "IV"
    assert int2roman(5) == "V"
    assert int2roman(9) == "IX"
    assert int2roman(10) == "X"
    assert int2roman(40) == "XL"
    assert int2roman(50) == "L"
    assert int2roman(90) == "XC"
    assert int2roman(100) == "C"
    assert int2roman(400) == "CD"
    assert int2roman(500) == "D"
    assert int2roman(900) == "CM"
    assert int2roman(1000) == "M"
    assert int2roman(1987) == "MCMLXXXVII"
    assert int2roman(2023) == "MMXXIII"
    assert int2roman(3999) == "MMMCMXCIX"

def test_num2roman_edge_cases():
    # Test for edge case of 0 (should raise error)
    with pytest.raises(ValueError, match="0 does not exist in Roman numerals."):
        int2roman(0)

    # Test for edge case of negative number
    with pytest.raises(ValueError, match="Negative numbers can't be represented in Roman numerals."):
        int2roman(-1)

    # Test for edge case of numbers above 3999
    with pytest.raises(ValueError, match="You're going to need a bigger calculator."):
        int2roman(4000)

def test_num2roman_invalid_input():
    # Test for non-integer inputs (if the function is supposed to handle this)
    with pytest.raises(TypeError):
        int2roman("string")
    with pytest.raises(TypeError):
        int2roman(3.5)

    # Test for float inputs (if applicable)
    with pytest.raises(TypeError):
        int2roman(3999.99)

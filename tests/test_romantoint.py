import pytest
from src.Roman_Calculator.romantoint import *  

# Test cases for the roman2int function
def test_single_characters():
    # Test single Roman numerals
    assert roman2int("I") == 1
    assert roman2int("V") == 5
    assert roman2int("X") == 10
    assert roman2int("L") == 50
    assert roman2int("C") == 100
    assert roman2int("D") == 500
    assert roman2int("M") == 1000

def test_basic_combinations():
    # Test simple combinations of Roman numerals
    assert roman2int("III") == 3
    assert roman2int("VIII") == 8
    assert roman2int("XII") == 12
    assert roman2int("XXVII") == 27

def test_subtractive_combinations():
    # Test combinations where subtraction is used
    assert roman2int("IV") == 4
    assert roman2int("IX") == 9
    assert roman2int("XL") == 40
    assert roman2int("XC") == 90
    assert roman2int("CD") == 400
    assert roman2int("CM") == 900

def test_complex_combinations():
    # Test more complex Roman numeral strings
    assert roman2int("MCMXCIV") == 1994
    assert roman2int("MMXXIII") == 2023
    assert roman2int("MMMCMXCIX") == 3999  # The largest possible valid Roman numeral

def test_empty_string():
    # Test that an empty string returns 0 (if that's the expected behavior)
    assert roman2int("") == 0

def test_invalid_characters():
    # Test that an invalid string raises an error (if you want to handle that case)
    with pytest.raises(KeyError):
        roman2int("ABC")
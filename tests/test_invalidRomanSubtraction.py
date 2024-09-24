import pytest
from src.Roman_Calculator.invalidRomanSubtraction import *  


def test_valid_numerals():
    # Valid Roman numeral expressions
    assert is_invalid_expression("XIV") == True
    assert is_invalid_expression("MCMXC") == True
    assert is_invalid_expression("MMXXIII") == True  # 2023
    assert is_invalid_expression("LXXXIX") == True   # 89
    assert is_invalid_expression("MMM") == True      # 3000

def test_invalid_repetitions():
    # Numerals with invalid repetitions
    with pytest.raises(ValueError, match="Invalid Numeral Repetition"):
        is_invalid_expression("IIII")  # More than 3 I's
    with pytest.raises(ValueError, match="Invalid Numeral Repetition"):
        is_invalid_expression("VV")  # V can't repeat
    with pytest.raises(ValueError, match="Invalid Numeral Repetition"):
        is_invalid_expression("XXXX")  # More than 3 X's
    with pytest.raises(ValueError, match="Invalid Numeral Repetition"):
        is_invalid_expression("LL")  # L can't repeat
    with pytest.raises(ValueError, match="Invalid Numeral Repetition"):
        is_invalid_expression("CCCC")  # More than 3 C's
    with pytest.raises(ValueError, match="Invalid Numeral Repetition"):
        is_invalid_expression("DD")  # D can't repeat

def test_invalid_subtractive_patterns():
    # Numerals with invalid subtractive patterns
    with pytest.raises(ValueError, match="Invalid Numeral Pattern Found"):
        is_invalid_expression("IC")  # Invalid pattern
    with pytest.raises(ValueError, match="Invalid Numeral Pattern Found"):
        is_invalid_expression("IL")  # Invalid pattern
    with pytest.raises(ValueError, match="Invalid Numeral Pattern Found"):
        is_invalid_expression("VC")  # Invalid pattern
    with pytest.raises(ValueError, match="Invalid Numeral Pattern Found"):
        is_invalid_expression("XD")  # Invalid pattern
    with pytest.raises(ValueError, match="Invalid Numeral Pattern Found"):
        is_invalid_expression("DM")  # Invalid pattern
    with pytest.raises(ValueError, match="Invalid Numeral Pattern Found"):
        is_invalid_expression("IM")  # Invalid pattern

def test_edge_cases():
    # Empty input or single numeral inputs (valid cases)
    assert is_invalid_expression("") == True
    assert is_invalid_expression("I") == True
    assert is_invalid_expression("V") == True
    assert is_invalid_expression("X") == True

    # Test for valid longer numeral with different combinations
    assert is_invalid_expression("MMDCLXVI") == True  # 2666
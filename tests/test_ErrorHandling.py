import pytest
from src.Roman_Calculator.ErrorHandling import * 



#Testing InputCheck() function.
def test_valid_expression():
    # Test case with a valid expression
    assert InputCheck("IV + XL - II") == True

def test_valid_expression_with_symbols():
    # Test case with valid Roman numerals and operators
    assert InputCheck("(IV + XL) / III") == True

def test_invalid_expression():
    # Test case with an invalid character
    with pytest.raises(ValueError, match="Error: Invalid Character Detected!"):
        InputCheck("IV + XL - II #")

def test_empty_expression():
    # Test case with an empty string (allowed)
    assert InputCheck("") == True

def test_expression_with_spaces():
    # Test case with spaces (allowed)
    assert InputCheck("I + V ") == True

# Test for IsWhole
def test_is_whole_with_integer():
    assert IsWhole(5) == True

def test_is_whole_with_float_whole_number():
    assert IsWhole(5.0) == True

def test_is_whole_with_float_non_whole_number():
    with pytest.raises(ValueError, match="There is no concept of a fractional number in Roman numerals."):
        IsWhole(5.5)

# Test for checkIfRoman
def test_check_if_roman_with_roman():
    assert checkIfRoman("X+V") == True

def test_check_if_roman_without_roman():
    with pytest.raises(SystemExit):
        checkIfRoman("+-/*")

# Test for duplicateOperator
def test_duplicate_operator_valid():
    assert duplicateOperator("X+V") == True

def test_duplicate_operator_invalid():
    with pytest.raises(SystemExit):
        duplicateOperator("X++V")

# Test for check_operator_by_roman
def test_check_operator_by_roman_valid():
    assert check_operator_by_roman("X+V") == True

def test_check_operator_by_roman_invalid_missing_roman_after_operator():
    with pytest.raises(SystemExit):
        check_operator_by_roman("X+")

def test_check_operator_by_roman_invalid_missing_roman_before_operator():
    with pytest.raises(SystemExit):
        check_operator_by_roman("+X")

# Test for findOperator
def test_find_operator_with_operator():
    assert findOperator("X+V") == True

def test_find_operator_without_operator(capsys):
    with pytest.raises(SystemExit):
        findOperator("X")

# Test for num2romanErrorHandler
def test_num2roman_error_negative_number():
    with pytest.raises(ValueError, match="Negative numbers can't be represented in Roman numerals."):
        num2romanErrorHandler(-5)

def test_num2roman_error_zero():
    with pytest.raises(ValueError, match="0 does not exist in Roman numerals."):
        num2romanErrorHandler(0)

def test_num2roman_error_too_large():
    with pytest.raises(ValueError, match="You're going to need a bigger calculator."):
        num2romanErrorHandler(4000)

def test_num2roman_valid():
    assert num2romanErrorHandler(1000) == True


import pytest
from src.Roman_Calculator.ErrorHandling import * 
from src.Roman_Calculator.romantoint import *



# Test for InputCheck function
def test_input_check_valid():
    assert InputCheck("(IV+X)*L") == True

def test_input_check_invalid_character():
    with pytest.raises(ValueError, match="Invalid Character Detected!"):
        InputCheck("(IV+X)*L@")

# Test for check_parentheses_balance function
def test_check_parentheses_balance_valid():
    assert check_parentheses_balance("(IV+X)*L") == True

def test_check_parentheses_balance_unbalanced_open():
    with pytest.raises(ValueError, match="Improper use of Parenthesis!"):
        check_parentheses_balance("(IV+X")

def test_check_parentheses_balance_unbalanced_close():
    with pytest.raises(ValueError, match="Improper use of Parenthesis!"):
        check_parentheses_balance("IV+X)")

# Test for check_brackets_balance function
def test_check_brackets_balance_valid():
    assert check_brackets_balance("[IV+X]*L") == True

def test_check_brackets_balance_unbalanced_open():
    with pytest.raises(ValueError, match="Improper use of Brackets!"):
        check_brackets_balance("[IV+X")

def test_check_brackets_balance_unbalanced_close():
    with pytest.raises(ValueError, match="Improper use of Brackets!"):
        check_brackets_balance("IV+X]")

# Test for IsWhole function
def test_is_whole_with_integer():
    assert IsWhole(10) == True

def test_is_whole_with_float_integer():
    assert IsWhole(10.0) == True

def test_is_whole_with_fractional():
    with pytest.raises(ValueError, match="There is no concept of a fractional number in Roman numerals."):
        IsWhole(10.5)

# Test for checkIfRoman function
def test_check_if_roman_present():
    assert checkIfRoman("IV + X") == True

def test_check_if_roman_absent():
    with pytest.raises(ValueError, match="No Roman Numeral Detected!"):  # Assuming exit(1) is used in your function.
        checkIfRoman("1 + 5")

# Test for duplicateOperator function
def test_duplicate_operator_no_consecutive():
    assert duplicateOperator("IV + X") == True

def test_duplicate_operator_consecutive():
    with pytest.raises(ValueError, match="Repitive Operators Found!"):  
        duplicateOperator("IV ++ X")

# Test for check_operator_by_roman function
def test_check_operator_by_roman_valid():
    assert check_operator_by_roman("IV+X") == True

def test_check_operator_by_roman_missing_numeral_before():
    with pytest.raises(ValueError, match="Operator Found With Missing Roman Numeral!"):  
        check_operator_by_roman("+ X")

def test_check_operator_by_roman_missing_numeral_after():
    with pytest.raises(ValueError, match="Operator Found With Missing Roman Numeral!"):
        check_operator_by_roman("IV + ")

# Test for findOperator function
def test_find_operator_present():
    assert findOperator("IV + X") == True

def test_find_operator_absent():
    with pytest.raises(SystemExit):  # Assuming exit(0) is used in your function after printing the number.
        findOperator("(X)")

# Test for num2romanErrorHandler function
def test_num2roman_negative_number():
    with pytest.raises(ValueError, match="Negative numbers can't be represented in Roman numerals."):
        int2romanErrorHandler(-5)

def test_num2roman_zero():
    with pytest.raises(ValueError, match="0 does not exist in Roman numerals."):
        int2romanErrorHandler(0)

def test_num2roman_large_number():
    with pytest.raises(ValueError, match="You're going to need a bigger calculator."):
        int2romanErrorHandler(4000)

def test_num2roman_valid_number():
    assert int2romanErrorHandler(3999) == True


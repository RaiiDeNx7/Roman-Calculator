import sys
import pytest
from src.Roman_Calculator.ErrorHandling import *  
from src.Roman_Calculator.inttoroman import *
from src.Roman_Calculator.mathfunctions import *
from src.Roman_Calculator.romantoint import *
from src.Roman_Calculator.stringManipulation import *

def test_main(monkeypatch):
    # Mock a valid Roman numeral expression with operators
    monkeypatch.setattr(sys, 'argv', ['main.py', 'IV+II'])

    # Test the main code flow with a simple valid input
    expression = sys.argv[1:]
    expression = ' '.join(expression).upper().strip().replace(" ", "").replace("[", "(").replace("]", ")")
    
    # Check that InputCheck does not raise any exceptions for valid input
    assert InputCheck(expression) == True

    # Check if the input has valid Roman numerals
    assert checkIfRoman(expression) == True

    # Ensure no back-to-back operators exist
    assert duplicateOperator(expression) == True

    # Ensure that the Roman numeral precedes the operator
    assert check_operator_by_roman(expression) == True

    # Test for the correct split of Roman numerals and operators
    separated = split_operators(expression)
    assert separated == ['IV', '+', 'II']

    # Test conversion from Roman to integer
    integerList = [roman2int(i) if i not in ['+', '-', '*', '/',"(",")","[","]"] else i for i in separated]
    assert integerList == [4, '+', 2]

    # Join list into a string and evaluate the expression
    combinedString = join_list(integerList)
    assert combinedString == "4 + 2"
    
    # Test evaluation of the expression
    result = eval_expr(combinedString)
    assert result == 6

    # Check if the result is a whole number
    assert IsWhole(result) == True

    # Convert result back to Roman numeral
    roman_result = int2roman(result)
    assert roman_result == "VI"
    
    # Ensure final output is correct
    assert roman_result == "VI"

def test_fractional_result(monkeypatch):
    # Mock an input that would result in a fractional number
    monkeypatch.setattr(sys, 'argv', ['main.py', 'VII/III'])

    expression = sys.argv[1:]
    expression = ' '.join(expression).upper().strip().replace(" ", "")

    # Check input
    InputCheck(expression)
    checkIfRoman(expression)
    duplicateOperator(expression)
    check_operator_by_roman(expression)

    separated = split_operators(expression)
    integerList = [roman2int(i) if i not in ['+', '-', '*', '/',"(",")","[","]"] else i for i in separated]
    combinedString = join_list(integerList)
    result = eval_expr(combinedString)

    # The result should be fractional
    with pytest.raises(ValueError, match="There is no concept of a fractional number in Roman numerals."):
        IsWhole(result)
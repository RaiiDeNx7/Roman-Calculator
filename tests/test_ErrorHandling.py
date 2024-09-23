import pytest
from src.Roman_Calculator.ErrorHandling import * 


#NOT FINISHED

###############################
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


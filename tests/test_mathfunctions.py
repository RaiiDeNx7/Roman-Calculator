import pytest
from src.Roman_Calculator.mathfunctions import *  

import ast
import operator as op

# Supported operators
operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
}

# Test cases for eval_expr function
def test_basic_arithmetic():
    # Test basic arithmetic operations
    assert eval_expr("1 + 1") == 2
    assert eval_expr("5 - 2") == 3
    assert eval_expr("3 * 4") == 12
    assert eval_expr("8 / 2") == 4.0

def test_exponentiation():
    # Test exponentiation
    assert eval_expr("2 ** 3") == 8

def test_modulo():
    # Test modulo operation
    assert eval_expr("10 % 3") == 1

def test_operator_precedence():
    # Test PEMDAS (order of operations)
    assert eval_expr("2 + 3 * 4") == 14  # Multiplication before addition
    assert eval_expr("(2 + 3) * 4") == 20  # Parentheses change the order

def test_nested_parentheses():
    # Test nested parentheses
    assert eval_expr("((2 + 3) * (5 - 1)) / 2") == 10.0

def test_division_by_zero():
    # Test division by zero should raise ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        eval_expr("10 / 0")

def test_unsupported_operator():
    # Test for unsupported operators
    with pytest.raises(ValueError, match="Unsupported operator: BitOr"):
        eval_expr("1 | 1")  # Bitwise OR is not supported

    with pytest.raises(ValueError, match="Unsupported operator: BitAnd"):
        eval_expr("1 & 1")  # Bitwise AND is not supported

def test_invalid_syntax():
    # Test for invalid syntax
    with pytest.raises(SyntaxError):
        eval_expr("1 +")  # Incomplete expression

    with pytest.raises(SyntaxError):
        eval_expr("2 **")  # Incomplete exponentiation

def test_large_numbers():
    # Test with large numbers
    assert eval_expr("1e10 + 1") == 1e10 + 1  # Scientific notation

def test_negative_numbers():
    # Test with negative numbers
    assert eval_expr("-5 + 3") == -2
    assert eval_expr("2 * -3") == -6

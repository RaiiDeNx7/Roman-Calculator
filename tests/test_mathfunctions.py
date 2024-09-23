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

def test_invalid_expression():
    # Test invalid or unsupported expressions should raise TypeError
    with pytest.raises(TypeError):
        eval_expr("10 + 'a'")  # Invalid operand
    with pytest.raises(TypeError):
        eval_expr("10 & 2")  # Unsupported operator
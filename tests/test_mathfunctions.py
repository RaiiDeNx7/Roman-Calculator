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
    assert eval_expr("1 + 2") == 3
    assert eval_expr("4 - 3") == 1
    assert eval_expr("2 * 5") == 10
    assert eval_expr("10 / 2") == 5
    assert eval_expr("2 ** 3") == 8  # Power
    assert eval_expr("10 % 3") == 1   # Modulo

def test_unary_operations():
    assert eval_expr("+5") == 5
    assert eval_expr("-10") == -10
    assert eval_expr("-(-5 + 3)") == 2

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
    assert eval_expr("((2 + 3) * (5 - 1)) / 2") == 10.0
    assert eval_expr("1 + 2 * 3") == 7       # Multiplication before addition
    assert eval_expr("(4 - 2) * 5") == 10     # Parenthesis
    assert eval_expr("2 + 3 * (7 - 5)") == 8  # Expression inside parentheses
    assert eval_expr("10 / 2 + 5") == 10      # Division before addition

def test_division_by_zero():
    # Test division by zero should raise ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        eval_expr("10 / 0")

def test_unsupported_operator():

    import pytest
    # Test for unsupported operators
    with pytest.raises(ValueError, match="Unsupported operator: BitOr"):
        eval_expr("1 | 1")  # Bitwise OR is not supported

    with pytest.raises(ValueError, match="Unsupported operator: BitAnd"):
        eval_expr("1 & 1")  # Bitwise AND is not supported
    
    with pytest.raises(ValueError):
        eval_expr("1 & 2")  # Bitwise AND is unsupported

    with pytest.raises(ValueError):
        eval_expr("1 | 2")  # Bitwise OR is unsupported

    with pytest.raises(ValueError):
        eval_expr("2 // 3")  # Floor division is unsupported

def test_invalid_syntax():
    import pytest
    # Test for invalid syntax
    with pytest.raises(SyntaxError):
        eval_expr("1 +")  # Incomplete expression

    with pytest.raises(SyntaxError):
        eval_expr("2 **")  # Incomplete exponentiation
    
    with pytest.raises(SyntaxError):
        eval_expr("x = 1 + 2")

    with pytest.raises(TypeError):
        eval_expr("a + b")  # Invalid variable names

def test_large_numbers():
    # Test with large numbers
    assert eval_expr("1e10 + 1") == 1e10 + 1  # Scientific notation

def test_negative_numbers():
    # Test with negative numbers
    assert eval_expr("-5 + 3") == -2
    assert eval_expr("2 * -3") == -6

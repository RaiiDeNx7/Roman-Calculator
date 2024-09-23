from src.Roman_Calculator.stringManipulation import *  

# Test cases for the split_operators function
def test_split_operators():
    # Test splitting of a typical Roman numeral expression with operators
    assert split_operators("IV+V-VI") == ["IV", "+", "V", "-", "VI"]
    
    # Test splitting when the expression starts and ends with Roman numerals
    assert split_operators("X*IX+III") == ["X", "*", "IX", "+", "III"]

    # Test expression with parentheses
    assert split_operators("(IV+X)/II") == ["(", "IV", "+", "X", ")", "/", "II"]
    
    # Test empty string (should return an empty list)
    assert split_operators("") == []
    
    # Test only Roman numerals (no operators)
    assert split_operators("IVXLCDM") == ["IVXLCDM"]
    
    # Test only operators
    assert split_operators("+-*/") == ["+", "-", "*", "/"]

# Test cases for the join_list function
def test_join_list():
    # Test joining a list of Roman numerals and operators
    assert join_list(["IV", "+", "V", "-", "VI"]) == "IV + V - VI"
    
    # Test joining a list of mixed integers and Roman numerals
    assert join_list([10, "X", "+", 5, "V"]) == "10 X + 5 V"
    
    # Test joining a list with parentheses
    assert join_list(["(", "IV", "+", "X", ")", "/", "II"]) == "( IV + X ) / II"
    
    # Test joining an empty list (should return an empty string)
    assert join_list([]) == ""
    
    # Test joining a list with a single element
    assert join_list(["IV"]) == "IV"
    
    # Test joining a list with a single integer
    assert join_list([42]) == "42"
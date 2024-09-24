import re

def is_invalid_expression(expression):
    # Allowed subtractive patterns
    valid_subtractive_patterns = ["IV", "IX", "XL", "XC", "CD", "CM"]

    # Invalid subtractive patterns: these should not exist in a valid expression numeral
    invalid_subtractive_patterns = [
        "IL", "IC", "ID", "IM",  # Invalid subtraction of I
        "VX", "VL", "VC", "VD", "VM",  # Invalid subtraction of V
        "XD", "XM",  # Invalid subtraction of X
        "LC", "LD", "LM",  # Invalid subtraction of L
        "DM",  # Invalid subtraction of D
    ]

    # Ensure that no numeral has more than three consecutive repetitions (except M)
    if re.search(r"(IIII|VV|XXXX|LL|CCCC|DD)", expression):
        raise ValueError("Invalid Numeral Repetition")  # Invalid repetition found
    
    # Check for invalid patterns
    for pattern in invalid_subtractive_patterns:
        if pattern in expression:
            raise ValueError("Invalid Numeral Pattern Found")  # Invalid numeral found
    
    
    
    # If no invalid pattern or repetition is found, it's valid
    return True
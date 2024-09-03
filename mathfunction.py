from romantoint import *

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

class RomanNumeralCalculator:
    # Define Roman numeral values
    ROMAN_NUMERAL_MAP = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

def add(self, roman1: str, roman2: str) -> str:
        """Add two Roman numerals."""
        int_sum = self.roman_to_int(roman1) + self.roman_to_int(roman2)
        return self.int_to_roman(int_sum)

def subtract(self, roman1: str, roman2: str) -> str:
        """Subtract the second Roman numeral from the first."""
        int_diff = self.roman_to_int(roman1) - self.roman_to_int(roman2)
        if int_diff < 1:
            raise ValueError("Resulting value is out of range (must be 1-3999).")
        return self.int_to_roman(int_diff)

def multiply(self, roman1: str, roman2: str) -> str:
        """Multiply two Roman numerals."""
        int_product = self.roman_to_int(roman1) * self.roman_to_int(roman2)
        return self.int_to_roman(int_product)

def divide(self, roman1: str, roman2: str) -> str:
        """Divide the first Roman numeral by the second."""
        int_dividend = self.roman_to_int(roman1)
        int_divisor = self.roman_to_int(roman2)
        if int_divisor == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        int_result = int_dividend // int_divisor
        if int_result < 1:
            raise ValueError("Resulting value is out of range (must be 1-3999).")
        return self.int_to_roman(int_result)
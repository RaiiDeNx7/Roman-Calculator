from mathfunction import *
from RomanNumeralValue import *
from romantoint import *

#Get input from user
numeral = input("\nEnter your equation: ")

#Strip white space at beginning and ends of string
numeral = numeral.strip()  

#Strip white space in between words
numeral = numeral.replace(" ","") 


print(numeral)

#initialize array
equation = []

#Fill array
for x in numeral:
    equation.append(x)

print(equation)

i=0
while i < len(equation):
    equation[i] = StringValue(equation[i])
    i += 1


print(equation)

class RomanNumeralCalculator:
    # Define Roman numeral values
    ROMAN_NUMERAL_MAP = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    def roman_to_int(self, roman: str) -> int:
        """Convert a Roman numeral to an integer."""
        total = 0
        prev_value = 0
        for char in reversed(roman):
            value = self.ROMAN_NUMERAL_MAP[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total

    def int_to_roman(self, num: int) -> str:
        """Convert an integer to a Roman numeral."""
        if not 1 <= num <= 3999:
            raise ValueError("Integer out of range (must be 1-3999).")

        value_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        roman = []
        for value, numeral in value_map:
            while num >= value:
                num -= value
                roman.append(numeral)
        return ''.join(roman)

    def add(self, *romans: str) -> str:
        """Add multiple Roman numerals."""
        int_sum = sum(self.roman_to_int(roman) for roman in romans)
        return self.int_to_roman(int_sum)

    def subtract(self, *romans: str) -> str:
        """Subtract multiple Roman numerals sequentially."""
        if not romans:
            raise ValueError("At least one Roman numeral is required.")
        int_diff = self.roman_to_int(romans[0])
        for roman in romans[1:]:
            int_diff -= self.roman_to_int(roman)
            if int_diff < 1:
                raise ValueError("Resulting value is out of range (must be 1-3999).")
        return self.int_to_roman(int_diff)

    def multiply(self, *romans: str) -> str:
        """Multiply multiple Roman numerals."""
        if not romans:
            raise ValueError("At least one Roman numeral is required.")
        int_product = 1
        for roman in romans:
            int_product *= self.roman_to_int(roman)
        return self.int_to_roman(int_product)

    def divide(self, *romans: str) -> str:
        """Divide multiple Roman numerals sequentially."""
        if len(romans) < 2:
            raise ValueError("At least two Roman numerals are required.")
        int_result = self.roman_to_int(romans[0])
        for roman in romans[1:]:
            int_divisor = self.roman_to_int(roman)
            if int_divisor == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            int_result //= int_divisor
            if int_result < 1:
                raise ValueError("Resulting value is out of range (must be 1-3999).")
        return self.int_to_roman(int_result)


# Example usage:
calculator = RomanNumeralCalculator()
print(calculator.add('X', 'V', 'III'))       # Output: XVIII
print(calculator.subtract('XX', 'V', 'III')) # Output: XII
print(calculator.multiply('II', 'V', 'III')) # Output: XXX
print(calculator.divide('C', 'V', 'II'))     # Output: X

# The num2roman function is meant for converting integer numbers received after calculating provess back to Roman Numerals.
# The function accepts the integer, result, as an argument. Once processing result and turning it into a Roman numeral, it returns the variable numeral.

from src.Roman_Calculator.ErrorHandling import *

"""
Function Name: 
    int2roman()

Function Description: 
    The int2roman function is meant for converting integer numbers received back to Roman Numerals.
        
Parameters:
    result (integer)

Returns:
    numeral (string)
    
Exceptions:
    None
"""

def int2roman(result):

    # Handle errors using error handling function
    int2romanErrorHandler(result)

    # Define Roman numeral mappings from highest to lowest
    number_symbol_pairs = zip(
        [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
        ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    )

    # Initialize the result string
    numeral = ""

    # Loop through the number-symbol pairs
    for number, symbol in number_symbol_pairs:
        # Determine how many times the number fits into result
        count = result // number

        # Append the Roman numeral symbol `count` times
        numeral += symbol * count

        # Decrease the result by the corresponding value
        result -= number * count

    #Return roman numeral string
    return numeral
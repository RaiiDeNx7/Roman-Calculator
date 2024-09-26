
def roman2int(expression: str) -> int:

    """
    Function Description: 
        Function meant to convert roman numerals into integers. The calculation is stored in result and returned to main. 
        
    Parameters: 
        expression (string).

    Return Types: 
        result (integer)
    """

    # Dictionary of Roman Numeral Values
    roman = { 
        "I" : 1, 
        "V" : 5, 
        "X" : 10, 
        "L" : 50, 
        "C" : 100, 
        "D" : 500, 
        "M" : 1000 
    }

    # variable to hold the sum of roman numerals
    result = 0

    # loop through the roman numeral string
    for i in range(len(expression)):

        # Checks the current roman numeral to the next one
        if i + 1 < len(expression) and roman[expression[i]] < roman[expression[i+1]]:

            # if the current roman numeral is smaller than the next, subtract from result
            result -= roman[expression[i]]

        else:

            # The number is bigger than the next, add to result
            result += roman[expression[i]]
    
    # return the result integer value
    return result
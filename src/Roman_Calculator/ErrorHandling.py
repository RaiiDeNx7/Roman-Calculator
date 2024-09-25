#This python file contains functinos meant to help with detecting and handling Errors.
from src.Roman_Calculator.romantoint import *

"""
Function Name: 
    InputCheck()

Function Description: 
    This function checks if any invald characters (ones not in set) are present. The function accepts an expression (the input from user) 
    and returns True if only valid characters are present. It returns False if invalid character appears.
        
Parameters:
    expression (string)

Returns:
    Boolean (True if valid, raise error if invalid)
    
Exceptions:
    ValueError: Invalid Characters Detected
"""
def InputCheck(expression):

    #set of characters which are allowed
    valid_chars = set("+-/*()[]IVXLCDM ")

    #looping through each character in the expression
    for char in expression:

        #if a character not in the set appears, return False
        if char not in valid_chars:
            raise ValueError("Invalid Character Detected!")
        
    #If no invalid character is found, return true
    return True


"""
Function Name: 
    check_parenthesis_balance()

Function Description: 
    Function to make sure there is no parenthesis that were not closed, or ones that closed without being opened. 
        
Parameters:
    expression (string)

Returns:
    bool (True if proper parenthesis, raise error if not)
    
Exceptions:
    ValueError: Improper use of Parenthesis!
"""

def check_parentheses_balance(expression):
    # Initialize a counter for open parentheses
    open_count = 0
    
    for char in expression:
        if char == '(':

            # Increment count when an open parenthesis is found
            open_count += 1  

        elif char == ')':
            if open_count == 0:

                # A closing parenthesis appeared without a matching opening one
                raise ValueError("Improper use of Parenthesis!")
            
            # Decrement count when a close parenthesis is found
            open_count -= 1  

    if open_count > 0:
        raise ValueError("Improper use of Parenthesis!")

    # If open_count is zero, all parentheses are balanced
    return True

"""
Function Name: 
    check_brackets_balance()

Function Description: 
    Function to make sure there is no brackets that were not closed, or ones that closed without being opened. 
        
Parameters:
    expression (string)

Returns:
    bool (True if proper brackets, raise error if not)
    
Exceptions:
    ValueError: Improper use of Brackets!
"""

def check_brackets_balance(expression):

    # Initialize a counter for open parentheses
    open_count = 0
    
    for char in expression:
        if char == '[':

            # Increment count when an open parenthesis is found
            open_count += 1  

        elif char == ']':
            if open_count == 0:

                # A closing parenthesis appeared without a matching opening one
                raise ValueError("Improper use of Brackets!")
            
            # Decrement count when a close parenthesis is found
            open_count -= 1  

    if open_count > 0:
        raise ValueError("Improper use of Brackets!")

    # If open_count is zero, all parentheses are balanced
    return True
    
"""
Function Name: 
    IsWhole()

Function Description: 
    This function checks if a number is a whole number. 
    The function accepts the result variable as an argument and 
    returns a True if the float is a whole number. it returns False if not.
        
Parameters:
    result (float or integer)

Returns:
    bool (True if whole, False or raise error if not)
    
Exceptions:
    ValueError: There is no concept of a fractional number in Roman numerals.
"""

def IsWhole(result):

    # Check if result is an integer
    if isinstance(result, int):  
        return True
    
    # Check if result is a float
    elif isinstance(result, float):  

        # Call is_integer() for floats
        if result.is_integer() == True: 
            return True
        else:
            raise ValueError("There is no concept of a fractional number in Roman numerals.")      

    # Handle other types if necessary   
    return False 
        

"""
Function Name: 
    checkIfRoman()

Function Description: 
    This function checks if no roman numerals are present in the expression. Every input should contain roman numerals. 
        
Parameters:
    expression (string)

Returns:
    bool (True if roman numeral present, raise error if not)
    
Exceptions:
    ValueError: No Roman Numeral Detected!
"""

def checkIfRoman(expression):

    #set of valid characters (roman numerals)
    valid_chars = set("IVXLCDM")

    #looping through each character in the expression
    for char in expression:
        #if a character the set appears, return True
        if char in valid_chars:
            return True
    #If no valid character appears, return False
    raise ValueError("No Roman Numeral Detected!")
    

"""
Function Name: 
    duplicateOperator()

Function Description: 
    This function checks if operators appears consecutively. 
        
Parameters:
    expression (string)

Returns:
    bool (True if no duplicate found, raise error if not)
    
Exceptions:
    ValueError: Repitive Operators Found!
"""

#The function accepts an expression (the input from user) and returns true if two in a row isn't found.
def duplicateOperator(expression):

    # Define the set of operators to check
    operators = set("+-*/")
    
    #Looping through the string, checking for consecutive operators
    for i in range(len(expression) - 1):

        #If the current character and the next character is an operator
        if expression[i] in operators and expression[i + 1] in operators:

            #Back to back operator were found, so return False
            raise ValueError("Repitive Operators Found!")
        
    #No consecutive operators found, so return True
    return True  

"""
Function Name: 
    check_operator_by_roman()

Function Description: 
    This function is meant to return an error if there is a roman numeral missing (Example "M*"" or "L/"" or "/D")
        
Parameters:
    expression (string)

Returns:
    bool (True if no duplicate found, raise error if not)
    
Exceptions:
    ValueError: Operator Found With Missing Roman Numeral!
"""

def check_operator_by_roman(expression: str) -> bool:

    #list of valid operators
    operators = {'+', '-', '*', '/'}

    #list of valid roman chars
    roman_chars = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}

    #Remove parenthesis and brackets which are not needed in this function.
    newExpression = expression.strip("()[]")  
    newExpression = expression.replace("(", "").replace(")", "").replace("[", "").replace("]", "")
    
    #Loop through the stripped expression
    for i, char in enumerate(newExpression):

        #if a valid operator appears
        if char in operators:

            # Check if there is a next character and if it is a Roman numeral. Return False if Roman numeral doesn't appear
            if i + 1 >= len(newExpression) or newExpression[i + 1] not in roman_chars:
                raise ValueError("Operator Found With Missing Roman Numeral!")
            
            # Check if there is a previous character and if it is a Roman numeral. Return False if Roman numeral doesn't appear
            if i == 0 or newExpression[i - 1] not in roman_chars:
                raise ValueError("Operator Found With Missing Roman Numeral!")
                
    #By default, return true if no error was found
    return True

"""
Function Name: 
    findOperator()

Function Description: 
    #Determines if the input contains an operator. If it does not, it will print the integer conversion of their roman numeral. 
        
Parameters:
    expression (string)

Returns:
    bool (True if operator found, print and exit if not)
    
Exceptions:
    None
"""

def findOperator(expression):

    #Valid list of operators
    operators = {'+', '-', '*', '/'}
    
    #If any operator in the list appears in the expression, return True
    if any(op in expression for op in operators):
        return True
    
    #No operator was found
    else:

        #Since no operator found, the string is stripped of unneeded parenthesis and brackets for easy conversion.
        expression = expression.strip("()[]")  

        #print integer of roman numeral input so the user can see.
        print(str(roman2int(expression)))

        #successful termination
        exit()

"""
Function Name: 
    int2romanErrorHandler()

Function Description: 
    Function Determines if the result of roman numeral calculation has an error. 
        
Parameters:
    result (integer or float)

Returns:
    bool (True if no errors, raise error if there is)
    
Exceptions:
    TypeError: Only integers can be converted to Roman numerals.
    ValueError: Negative numbers can't be represented in Roman numerals.
    ValueError: 0 does not exist in Roman numerals.
"""

def int2romanErrorHandler(result):

    if not isinstance(result, int):
        raise TypeError("Only integers can be converted to Roman numerals.")

    #Error handling if the number is negative
    if(result<0):
        raise ValueError("Negative numbers can't be represented in Roman numerals.")
    
    
    #Error Handling if number is zero
    if(result==0):
        raise ValueError("0 does not exist in Roman numerals.")
        
    
    #Error handling if the number is too big
    if(result>3999):
        raise ValueError("You're going to need a bigger calculator.")
    
    return True




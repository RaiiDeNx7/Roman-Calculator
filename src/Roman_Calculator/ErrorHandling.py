#This python file contains functinos meant to help with detecting and handling Errors.
from src.Roman_Calculator.romantoint import *

#This function checks if any invald characters (ones not in set) are present. The function accepts an expression (the input from user)
# and returns True if only valid characters are present. It returns False if invalid character appears
def InputCheck(expression):
    #set of characters which are allowed
    valid_chars = set("+-/*()[]IVXLCDM ")

    #looping through each character in the expression
    for char in expression:
        #if a character not in the set appears, return False
        if char not in valid_chars:
            raise ValueError("Error: Invalid Character Detected!")
        
    #If no invalid character is found, return true
    return True
    

#This function checks if a number is a whole number. The function accepts the result variable as an argument and returns a True if the float is a whole number. it returns False if not.
def IsWhole(result):
    if isinstance(result, int):  # Check if result is an integer
        return True
    elif isinstance(result, float):  # Check if result is a float
        if result.is_integer() == True: # Call is_integer() for floats
            return True
        else:
            raise ValueError("There is no concept of a fractional number in Roman numerals.")         
    return False # Handle other types if necessary
        
#This function checks if no roman numerals are present in the expression. Every input should contain roman numerals. 
#The function accepts an expression (the input from user) and returns true if there is a Roman Numeral Present. It returns False otherwise.
def checkIfRoman(expression):
    #set of valid characters (roman numerals)
    valid_chars = set("IVXLCDM")

    #looping through each character in the expression
    for char in expression:
        #if a character the set appears, return True
        if char in valid_chars:
            return True
    #If no valid character appears, return False
    print("Error: No Roman Numeral Detected!")
    exit(1)

#This function checks if operators appears twice in a row, or back to back. 
#The function accepts an expression (the input from user) and returns true if two in a row isn't found. It returns False if two in a row are found.
def duplicateOperator(expression):
    # Define the set of operators to check
    operators = set("+-*/")
    
    #Looping through the string, checking for consecutive operators
    for i in range(len(expression) - 1):
        #If the current character and the next character is an operator
        if expression[i] in operators and expression[i + 1] in operators:
            #Back to back operator were found, so return False
            print("Error: Repitive Operators Found!")
            exit(1)
        
    #No consecutive operators found, so return True
    return True  

#This function is meant to return an error if there is a roman numeral missing (Example "M*"" or "L/"" or "/D")
#The function accepts an expression (the input from user) and returns True if there is a roman numeral next to each operator. Returns False if a roman numeral is missing.
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
                print("Error: Operator Found With Missing Roman Numeral!")
                exit(1)
            # Check if there is a previous character and if it is a Roman numeral. Return False if Roman numeral doesn't appear
            if i == 0 or newExpression[i - 1] not in roman_chars:
                print("Error: Operator Found With Missing Roman Numeral!")
                exit(1)
            
    #By default, return true if no error was found
    return True

#Determines if the input contains an operator. If it does not, it will return the integer conversion of their roman numeral. 
#The function accepts an expression (the input from user) and prints the calculated integer to the user before successful termination.
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

#Function Determines if the result of roman numeral calculation has an error. The functions takes in the result as an argument. It prints an error and exits if an error occurs.
def num2romanErrorHandler(result):

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




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
            return False
    #If no invalid character is found, return true
    return True
    

#This function checks if a number is a whole number. The function accepts the result variable as an argument and returns a True if the float is a whole number. it returns False if not.
def IsWhole(result):
    #Checks if number is a whole number (Ex: 2.0, 3, 5.0 would be true)
    if ((result).is_integer() == True):
        #If whole number, return true
        return True
    else:
        #Not whole number
        return False
        
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
    return False

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
            return False 
        
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
    
    #Loop through the stripped expression
    for i, char in enumerate(newExpression):
        #if a valid operator appears
        if char in operators:
            # Check if there is a next character and if it is a Roman numeral. Return False if Roman numeral doesn't appear
            if i + 1 >= len(newExpression) or newExpression[i + 1] not in roman_chars:
                return False
            # Check if there is a previous character and if it is a Roman numeral. Return False if Roman numeral doesn't appear
            if i == 0 or newExpression[i - 1] not in roman_chars:
                return False
            
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
        print("The integer conversion of your roman numeral is: " + str(roman2int(expression)))

        #successful termination
        exit()

#Function Determines if the result of roman numeral calculation has an error. The functions takes in the result as an argument. It prints an error and exits if an error occurs.
def num2romanErrorHandler(result):

    #Error handling if the number is negative
    if(result<0):
        print("Negative numbers can’t be represented in Roman numerals.")
        exit(1)
    
    
    #Error Handling if number is zero
    if(result==0):
        print("0 does not exist in Roman numerals.")
        exit(1)
    
    #Error handling if the number is too big
    if(result>3999):
        print("You’re going to need a bigger calculator.")
        exit(1)




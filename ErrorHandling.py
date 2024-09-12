
#function to check if any invald characters (ones not in set) are present.
def InputCheck(expression):
    valid_chars = set("+-/*()[]IVXLCDM ")
    for char in expression:
        if char not in valid_chars:
            return False
    return True
    

#This function checks if a number is a whole number.
def IsWhole(n):
    #Checks if number is a whole number (Ex: 2.0, 3, 5.0 would be true)
    if ((n).is_integer() == True):
        return True
    else:
        return False
        
#This function is meant to check if no roman numerals are present. Every input should contain roman numerals.
def checkIfRoman(n):
    valid_chars = set("IiVvXxLlCcDdMm")
    for char in n:
        if char in valid_chars:
            return True
    return False

def duplicateOperator(n):
    # Define the set of operators to check
    operators = set("+-*/")
    
    # Iterate through the string, checking for consecutive operators
    for i in range(len(n) - 1):
        if n[i] in operators and n[i + 1] in operators:
            return False  # Found two operators beside each other
    return True  # No consecutive operators found

#This function is meant to return an error if there is a roman numeral missing (Examlpe "M* or L/")
def MissingNumeral(n):
    return True
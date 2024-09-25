
"""
    Function Name: 
        split_operators()

    Function Description: 
        This function is meant to splits operators from roman numerals and then group roman numerals together. 

    Parameters: 
        expression (string)

    Return Types: 
        newList (list)

    Exceptions: 
        None
""" 
def split_operators(expression):
    
    # list of roman numerals that we want to seperate from operators 
    numbers = "IVXLCDM"

    # initialize empty list
    newList = []

    # initialize empty string
    lastNumber = ""

    # Loop through characters in the string
    for char in expression:

        # If a roman numeral appears
        if char in numbers:

            # Add to the roman numeral to the string
            lastNumber += char

        
            # If a roman numeral doesn't appear
        else:
            
            # if lastNumber is not empty
            if lastNumber:

                # if lastNumber has a numeral, it appends to newList list
                newList.append(lastNumber)

                # LastNumber is reset to empty 
                lastNumber = ""

            # if character is non-empty, it is appended to the newList list
            if char:
                newList.append(char)

    # Checks if unappended lastNumber (expression ends in number)
    if lastNumber:

        # Append final number to newList
        newList.append(lastNumber)

    # return the list with seperated operators
    return newList




"""
Function Name: 
    join_list()

Function Description: 
    The Function meant to combine a list into one complete string

Parameters: 
    The function accepts the list variable (integerList). It joins the input list into a string.

Return Types: 
    String 

Exceptions: 
    None
"""
def join_list(integerList):

    # Convert all integerList to strings and joins them with spaces
    return ' '.join(map(str, integerList))
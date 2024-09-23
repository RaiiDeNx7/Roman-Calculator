
#The function takes in the expression (user input) as an arguement and returns the new formatted list


"""
#Function Description: This function is meant to splits operators from roman numerals and then group roman numerals together. 
#Parameters: 
#Return Types: 
"""
def split_operators(expression):
    #list of roman numerals that we want to seperate from operators"
    numbers = "IVXLCDM"

    #initialize empty array
    newList = []
    #initialize empty string
    lastNumber = ""
    #Loop through characters in the string
    for char in expression:
        #If a roman numeral appears
        if char in numbers:
            #Add to the roman numeral to the string
            lastNumber += char

        #If a roman numeral doesn't appear
        else:
            #if lastNumber is not empty
            if lastNumber:
                #if lastNumber has a numeral, it appends to newList array
                newList.append(lastNumber)
                #LastNumber is reset to empty
                lastNumber = ""
            #if character is non-empty, it is appended to the newList array
            if char:
                newList.append(char)
    #Checks if unappended lastNumber (expression ends in number)    
    if lastNumber:
        #Append final number to newList
        newList.append(lastNumber)
    #return the list with seperated operators
    return newList


#The Function meant to combine a list into one complete string
#The function accepts the integerList array. It joins the array into a string and returns to be stored in combinedString

def join_list(integerList):
    # Convert all integerList to strings and joins them with spaces
    return ' '.join(map(str, integerList))
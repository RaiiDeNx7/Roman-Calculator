from mathfunctions import *
from romantoint import *
from inttoroman import *
from NoOperator import *
from ValidInputCheck import *
from stringManipulation import *

#Initialize Numeral String
numeral = "1"

#Check user input for invalid characters
while InputCheck(numeral) == False:

    #Get input from user
    numeral = input("\nEnter your equation: ")

    #If incorrect input, print error
    if InputCheck(numeral) == False:
         print("Error: Incorrect input detected. Please try again!")

#Strip white space at beginning and ends of string
numeral = numeral.strip()  

#Strip white space in between words
numeral = numeral.replace(" ","") 

#print that shows stripped white space
print("The stripped equation is: " + numeral)


#Uses findOperator function to determine if the string has an operator. If it does not, it will convert the roman numeral to an integer and display to user
if findOperator(numeral) == False:
        numeral = numeral.strip("()[]")  
        print("The integer of your roman numeral is: " + str(roman2int(numeral)))
        exit(1)


#seperate operators from numerals
split = split_operators(numeral)

print("The comp is: " + str(split))

## Find a way to convert numeral to integer if no operator
## Find a way to loop through string and carry out operations

#runs the roman numeral string through function to turn all roman numerals into integers.
split = [roman2int(i) if i not in ['+', '-', '*', '/',"(",")","[","]"] else i for i in split]

print("List to evalutate: " + str(split))


def join_tokens(tokens):
    """ Join a list of tokens into a single string. """
    # Convert all tokens to strings and join them with spaces
    return ' '.join(map(str, tokens))


joined_string = join_tokens(split)
print(joined_string)  # Output: "20 + 10"



 

"""
# Example usage:
expression = split
result = calculate_expression(expression)
print("The calculation result is: " + str(result))

roman = num2roman(result)
print("The answer is: " + roman)
"""

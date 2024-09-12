import pytest
from mathfunctions import *
from romantoint import *
from inttoroman import *
from NoOperator import *
from ErrorHandling import *
from stringManipulation import *

#Initialize Numeral String
numeral = "1"

#Check user input for invalid characters. Keep asking for input until a correct input has been made.
while not (InputCheck(numeral) and checkIfRoman(numeral) and duplicateOperator(numeral)):

    #Get input from user
     numeral = input("\nEnter your equation: ")

     #Strip white space at beginning and ends of string
     numeral = numeral.strip()  

     #Strip white space in between words
     numeral = numeral.replace(" ","") 

     #turn string into upper case for easier computing
     numeral = numeral.upper() 


     #If incorrect input, print error
     if not (InputCheck(numeral)):
          print("Error: Invalid Character Detected!")
     if not (checkIfRoman(numeral)):
          print("Error: No Roman Numeral Detected!")
     if not (duplicateOperator(numeral)):
          print("Error: Repitive Operators Found!")



#Calls findOperator function to determine if the string has an operator. If it does not, it will convert the roman numeral to an integer and display to user
if findOperator(numeral) == False:
        #If no operator found, the string is stripped of unneeded parenthesis and brackets for easy conversion.
        numeral = numeral.strip("()[]")  

        #print test
        print("The integer conversion of your roman numeral is: " + str(roman2int(numeral)))

        #successful termination
        exit()


#seperation of operators from numerals
seperatedString = split_operators(numeral)

#runs the roman numeral string through function to turn all roman numerals into integers.
integerString = [roman2int(i) if i not in ['+', '-', '*', '/',"(",")","[","]"] else i for i in seperatedString]

#combining the list back into a string
combinedString = join_tokens(integerString)

# Example usage
expr = combinedString
result = eval_expr(expr)

#check if number is float or a valid input
if (IsWhole(result) == False):
     print("Error: Can't Calculate Decimals")
     exit()

#Remove float decimal by changing result to an int variable. This number ends in .0 as any decimal number would've returned an error prior.
result = int(result)

#Call num2roman function to turn evaluated integer back into a roman numeral
roman = num2roman(result)

#print out answer to user
print("The calculated roman numeral is: " + roman)


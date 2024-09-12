import pytest
from mathfunctions import *
from romantoint import *
from inttoroman import *
from ErrorHandling import *
from stringManipulation import *

#Initialize Numeral String
numeral = "1"

#Check user input for invalid characters. Keep asking for input until a correct input has been made.
while not (InputCheck(numeral) and checkIfRoman(numeral) and duplicateOperator(numeral) and check_operator_by_roman(numeral)):

    #Get input from user. The functions make the string uppercase, then strip the ends of spacing, then strips the middle of spacing.
     numeral = input("\nEnter your equation: ").upper().strip().replace(" ","")

     #If incorrect input, print error
     if not (InputCheck(numeral)):
          print("Error: Invalid Character Detected!")
     if not (checkIfRoman(numeral)):
          print("Error: No Roman Numeral Detected!")
     if not (duplicateOperator(numeral)):
          print("Error: Repitive Operators Found!")
     if not (check_operator_by_roman(numeral)):
          print("Error: Operator Found With Missing Roman Numeral!")


#Calls findOperator function to determine if the string has an operator. If it does not, it will convert the roman numeral to an integer and display to user
findOperator(numeral)


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


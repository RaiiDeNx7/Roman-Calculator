import pytest
from src.Roman_Calculator.mathfunctions import *
from src.Roman_Calculator.romantoint import *
from src.Roman_Calculator.inttoroman import *
from src.Roman_Calculator.ErrorHandling import *
from src.Roman_Calculator.stringManipulation import *

#Initialize Numeral String
expression = "None"

#Check user input for invalid characters. Keep asking for input until a correct input has been given.
while not (InputCheck(expression) and checkIfRoman(expression) and duplicateOperator(expression) and check_operator_by_roman(expression)):

    #Get input from user. The functions make the string uppercase, then strip the ends of spacing, and then strips the middle of spacing.
     expression = input("\nEnter your equation: ").upper().strip().replace(" ","")

     #Checks if an invalid character exists, print error found
     if not (InputCheck(expression)):
          print("Error: Invalid Character Detected!")
     #Checks if No Roman Numeral exists, print error found
     if not (checkIfRoman(expression)):
          print("Error: No Roman Numeral Detected!")
     #Checks if back to back operators occur, print error found
     if not (duplicateOperator(expression)):
          print("Error: Repitive Operators Found!")
     #Checks if a roman numeral comes before and operator, print error found
     if not (check_operator_by_roman(expression)):
          print("Error: Operator Found With Missing Roman Numeral!")


#Calls findOperator function to determine if the string has an operator. If it does not, it will convert the roman numeral to an integer and display to user
findOperator(expression)


#seperation of operators from numerals
seperatedString = split_operators(expression)

#runs the roman numeral string through function to turn all roman numerals into their respective integers.
integerList = [roman2int(i) if i not in ['+', '-', '*', '/',"(",")","[","]"] else i for i in seperatedString]

#combining the previous list back into a string using the join_tokens function which acceptes the integerList
combinedString = join_list(integerList)

#Calls the eval_expr function which accepted the combined string. This evaluates the mathematical equation in the string and stores the answer in the result variable.
result = eval_expr(combinedString)

#Error check if number is float or decimal number
if (IsWhole(result) == False):

     #Print error
     print("There is no concept of a fractional number in Roman numerals.") 

     #Failed Execution
     exit(1) 

#Remove float decimal by changing result to an int variable. This number ends in .0 as any decimal number would've returned an error prior.
result = int(result)

#Call num2roman function to turn evaluated integer back into a roman numeral. 
roman = num2roman(result)

#print out the final answer to user
print("The calculated roman numeral is: " + roman)


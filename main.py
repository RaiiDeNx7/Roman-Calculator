from mathfunctions import *
from RomanNumeralValue import *
from romantoint import *
from inttoroman import *
from NoOperator import *
from ValidInputCheck import *
from stringManipulation import *
import re 

#Initialize Numeral String
numeral=""

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
print("The roman numeral is: " + numeral)


#Uses findOperator function to determine if the string has an operator. If it does not, it will convert the roman numeral to an integer and display to user
if findOperator(numeral) == False:
        print(roman2int(numeral))
        exit(1)


#seperate operators from numerals
comp = split_operators(numeral)

print("The comp is: " + str(comp))

## Find a way to convert numeral to integer if no operator
## Find a way to loop through string and carry out operations

#initialize array
""""
equation = []

#Fill array
for x in numeral:
    equation.append(x)

print(equation)

i=0
while i < len(equation):
    equation[i] = StringValue(equation[i])
    i += 1


print(equation)

"""
from mathfunctions import *
from RomanNumeralValue import *
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
    numeral = input("\n\nEnter your equation: ")

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
        print(roman2int(numeral))
        exit(1)


#seperate operators from numerals
split = split_operators(numeral)

print("The comp is: " + str(split))

## Find a way to convert numeral to integer if no operator
## Find a way to loop through string and carry out operations


#for idx in range(len(split)):
#    split[idx] = roman2int(split[idx])

split = [roman2int(i) if i not in ['+', '-', '*', '/'] else i for i in split]

print(split)

from mathfunction import *
from RomanNumeralValue import *
from romantoint import *
from inttoroman import *
from NoOperator import *
import re 

#Get input from user
numeral = input("\nEnter your equation: ")

#Strip white space at beginning and ends of string
numeral = numeral.strip()  

#Strip white space in between words
numeral = numeral.replace(" ","") 

#print that shows stripped white space
print("The roman numeral is: " + numeral)

#Check user input for invalid characters

#Uses findOperator function to determine if the string has an operator. If it does not, it will convert the roman numeral to an integer and display to user
if findOperator(numeral) == False:
    print(roman2int(numeral))
    

s = numeral
numbers = "IVXLCDM"


#splits operators and groups roman numerals

def split_operators(s):
    l = []
    last_number = ""
    for c in s:
        if c in numbers:
            last_number += c
        else:
            if last_number:
                l.append(last_number)
                last_number = ""
            if c:
                l.append(c)
    if last_number:
        l.append(last_number)
    return l

comp = split_operators(s)

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
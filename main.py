from mathfunction import *
from RomanNumeralValue import *
from romantoint import *
from inttoroman import *
import re 

#Get input from user
numeral = input("\nEnter your equation: ")

#Strip white space at beginning and ends of string
numeral = numeral.strip()  

#Strip white space in between words
numeral = numeral.replace(" ","") 

print("The roman numeral is: " + numeral)

res = re.findall('[+-/*//()]+|\d+',numeral)

s = "(1-2+3)*5+10/2"
numbers = "0123456789."

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

print split_operators(s)

"""
res = re.split(r'(\D)', numeral)
"""
print("The result is: " + str(res))

## Find a way to convert numeral to integer if no operator
## Find a way to loop through string and carry out operations

#initialize array
equation = []
""""
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
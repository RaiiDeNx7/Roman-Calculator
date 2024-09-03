from mathfunction import *
from RomanNumeralValue import *

#Get input from user
numeral = input("\nEnter your equation: ")

#Strip white space at beginning and ends of string
numeral = numeral.strip()  

#Strip white space in between words
numeral = numeral.replace(" ","") 


print(numeral)

#initialize array
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


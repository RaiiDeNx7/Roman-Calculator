from mathfunction import *
from RomanNumeralValue import *

#Get input from user
numeral = input("\nEnter your equation: ")
print(len(numeral))

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



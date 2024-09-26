import sys
from src.Roman_Calculator.mathfunctions import *
from src.Roman_Calculator.romantoint import *
from src.Roman_Calculator.inttoroman import *
from src.Roman_Calculator.ErrorHandling import *
from src.Roman_Calculator.stringManipulation import *
from src.Roman_Calculator.invalidRomanSubtraction import *

#Initialize Numeral String
expression = sys.argv[1:]
expression = arguments_str = ' '.join(expression).upper().strip().replace(" ","")

#Checks if No Roman Numeral exists, print error found
checkIfRoman(expression)

#Checks for invalid subtraction pattern and repitive numerals
is_invalid_expression(expression)

#Checks if back to back operators occur, print error found
duplicateOperator(expression)

#Checks if a roman numeral comes before and operator, print error found
check_operator_by_roman(expression)

#Check if every open parenthesis is closed#
check_parentheses_balance(expression)

#Check if every open bracket is closed
check_brackets_balance(expression)

#Change brackets to parenthesis. This makes calculations simplified and can be done because error checks we're already handled
expression = expression.replace("[", "(").replace("]", ")")

#Calls findOperator function to determine if the string has an operator. If it does not, it will convert the roman numeral to an integer and display to user
findOperator(expression)



#seperation of operators from numerals
seperatedString = split_operators(expression)

#runs the roman numeral string through roman2int function to turn all roman numerals into their respective integers.
integerList = [roman2int(i) if i not in ['+', '-', '*', '/',"(",")","[","]"] else i for i in seperatedString]

#Combining the previous list back into a string using the join_tokens function which acceptes the integerList.
combinedString = join_list(integerList)

#Calls the eval_expr function which accepted the combined string. This evaluates the mathematical equation in the string and stores the answer in the result variable.
result = eval_expr(combinedString)

#Error check if number is float or decimal number
IsWhole(result)

#Remove float decimal by changing result to an int variable. This number ends in .0 as any decimal number would've returned an error prior.
result = int(result)

#Call num2roman function to turn evaluated integer back into a roman numeral. 
roman = int2roman(result)

#print out the final answer to user
print(roman)


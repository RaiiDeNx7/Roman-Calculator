from mathfunctions import *
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
    numeral = input("\nEnter your equation: ")

    #If incorrect input, print error
    if InputCheck(numeral) == False:
         print("Error: Incorrect input detected. Please try again!")

#Strip white space at beginning and ends of string
numeral = numeral.strip()  

#Strip white space in between words
numeral = numeral.replace(" ","") 

#print test
print("The stripped equation is: " + numeral)


#Uses findOperator function to determine if the string has an operator. If it does not, it will convert the roman numeral to an integer and display to user
if findOperator(numeral) == False:
        #If no operator found, the string is stripped of unneeded parenthesis and brackets for easy conversion.
        numeral = numeral.strip("()[]")  

        #print test
        print("The integer of your roman numeral is: " + str(roman2int(numeral)))

        #successful termination
        exit()


#seperation of operators from numerals
seperatedString = split_operators(numeral)

#print test
print("The comp is: " + str(seperatedString))

#runs the roman numeral string through function to turn all roman numerals into integers.
integerString = [roman2int(i) if i not in ['+', '-', '*', '/',"(",")","[","]"] else i for i in seperatedString]

#print test
print("List to evalutate: " + str(integerString))

#combining the list back into a string
combinedString = join_tokens(integerString)
print(combinedString)  # Output: "20 + 10"

# Example usage
expr = combinedString
result = eval_expr(expr)

#check if number is float or a valid input
if (IsWhole(result) == False):
     print("Error: Can't Calculate Decimals")
     exit()

result = int(result)
print("the evaluated integer is: " + str(result))


#Call num2roman function to turn evaluated integer back into a roman numeral
roman = num2roman(result)

#print out answer to user
print(roman)


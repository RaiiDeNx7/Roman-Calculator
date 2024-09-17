# The num2roman function is meant for converting integer numbers received after calculating provess back to Roman Numerals.
# The function accepts the integer, result, as an argument. Once processing result and turning it into a Roman numeral, it returns the variable numeral.

from src.Roman_Calculator.ErrorHandling import *

def num2roman(result):

    #Calls error handling function to return errors to User if present.
    num2romanErrorHandler(result)

    #Roman Numeral Number Cases
    number = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

    #Roman Numeral Symbols that represent number cases
    symbol = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

    #New numeral string to be returned later
    numeral = ""
    #sets default position
    pos = 0

    #Loop which converts the integers in result into the string numeral
    while result > 0:

        #If result is greater than 0, roman numerals need to be added.
        if result - number[pos] >= 0:

            #Add the Roman Numeral at position to the numeral string
            numeral += symbol[pos]
            #Remove the integer value of the previous Roman Numeral from the result (total)
            result -= number[pos]

        #change position to next roman numeral and number value
        else:
            pos+=1

    #returns the completed roman numeral string
    return numeral
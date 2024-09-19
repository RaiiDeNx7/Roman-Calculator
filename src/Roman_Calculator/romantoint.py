#Function meant to convert roman numerals into integers. The calulation is stored in result and then returned to main.
# The function accepts the string as an argument. Once processing result and turning it into an integer, it returns result.

def roman2int(s: str) -> int:
    #Dict of Roman Numeral Values
    roman = { 
        "I" : 1, 
        "V" : 5, 
        "X" : 10, 
        "L" : 50, 
        "C" : 100, 
        "D" : 500, 
        "M" : 1000 
    }

    #variable to hold the sum of roman numerals
    result = 0

    #loop through the roman numeral string
    for i in range(len(s)):

        #Checks the roman numeral to the next one
        if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            #if the current roman numeral is smaller than the next, subtract from result
            result -= roman[s[i]]

        else:
            #since the number is bigger than the next, add to result
            result += roman[s[i]]
    
    #return the calculation
    return result
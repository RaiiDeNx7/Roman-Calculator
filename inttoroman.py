#the num2roman function is meant for converting integer numbers received after calculating provess back to Roman Numerals.
def num2roman(n):

    #Error handling if number is negative
    if(n<0):
        return("No Negative Numbers Allowed")
    
    #Error Handling if number is zero
    if(n==0):
        return("No Zeros Allowed")
    
    #Error handling if the number is too big
    if(n>3999):
        return("You need a bigger calculator for this.")
    
    #Error handling if number is float

    #Roman Numeral Number Cases
    number = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

    #Roman Numeral Symbols that represent number cases
    symbol = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

    numeral = ""
    current_num = n
    pos = 0
    while current_num > 0:
        if current_num - number[pos] >= 0:
            numeral += symbol[pos]
            current_num -= number[pos]
        else:
            pos+=1
    return numeral
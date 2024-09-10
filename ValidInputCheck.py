def InputCheck(expression):
    valid_chars = set("+-/*()[]IiVvXxLlCcDdMm ")
    for char in expression:
        if char not in valid_chars:
            return False
    return True

def IsWhole(n):
    #Error handling if number is float
    if ((n).is_integer() == True):
        return True
    else:
        return False
        
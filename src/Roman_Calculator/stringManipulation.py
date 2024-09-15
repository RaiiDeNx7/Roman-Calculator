#splits operators and groups roman numerals
def split_operators(s):
    #list of roman numerals that we want to seperate from operators"
    numbers = "IVXLCDM"

    #empty array
    newList = []
    lastNumber = ""
    for char in s:
        if char in numbers:
            lastNumber += char
        else:
            if lastNumber:
                newList.append(lastNumber)
                lastNumber = ""
            if char:
                newList.append(char)
    if lastNumber:
        newList.append(lastNumber)
    return newList


#function meant to combine a list into one complete string
def join_tokens(tokens):
    # Convert all tokens to strings and join them with spaces
    return ' '.join(map(str, tokens))
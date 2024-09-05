def findOperator(n):
    phrase = n
    if ('+' in phrase) or ('-' in phrase) or ('/' in phrase) or ('*' in phrase):
        return True
    else:
        return False
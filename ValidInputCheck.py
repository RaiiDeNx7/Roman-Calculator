def InputCheck(s):
    phrase = s
    if ('+' in phrase) or ('-' in phrase) or ('/' in phrase) or ('*' in phrase) or ('I' in phrase) or ('V' in phrase) or ('X' in phrase) or ('L' in phrase) or ('C' in phrase) or ('D' in phrase) or ('M' in phrase):
        return True
    else:
        return False
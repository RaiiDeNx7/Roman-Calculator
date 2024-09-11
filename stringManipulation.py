#splits operators and groups roman numerals
def split_operators(s):
    numbers = "IVXLCDM"
    l = []
    last_number = ""
    for c in s:
        if c in numbers:
            last_number += c
        else:
            if last_number:
                l.append(last_number)
                last_number = ""
            if c:
                l.append(c)
    if last_number:
        l.append(last_number)
    return l


def join_tokens(tokens):
    """ Join a list of tokens into a single string. """
    # Convert all tokens to strings and join them with spaces
    return ' '.join(map(str, tokens))
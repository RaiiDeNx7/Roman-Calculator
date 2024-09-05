def InputCheck(expression):
    valid_chars = set("+-/*()[]IiVvXxLlCcDdMm ")
    for char in expression:
        if char not in valid_chars:
            return False
    return True
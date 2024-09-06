import operator

def calculate_expression(expression):
    total = expression[0]
    for i in range(1, len(expression), 2):
        operator = expression[i]
        number = expression[i + 1]
        if operator == '+':
            total += number
        elif operator == '-':
            total -= number
        elif operator == '*':
            total *= number
        elif operator == '/':
            total /= number
    return total
import ast
import operator as op

# Supported operators
operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
}

def eval_expr(expr):
    """
    Safely evaluate a mathematical expression using PEMDAS.
    """
    # Parse the expression into an Abstract Syntax Tree (AST)
    tree = ast.parse(expr, mode='eval')

    # Define a function to evaluate the AST nodes
    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        elif isinstance(node, ast.BinOp):
            left = _eval(node.left)
            right = _eval(node.right)
            op_type = type(node.op)
            if op_type in operators:
                return operators[op_type](left, right)
            raise TypeError(f"Unsupported operator: {op_type}")
        elif isinstance(node, ast.Num):
            return node.n
        else:
            raise TypeError(f"Unsupported AST node: {type(node)}")

    # Evaluate the expression
    return _eval(tree.body)

""""
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
"""
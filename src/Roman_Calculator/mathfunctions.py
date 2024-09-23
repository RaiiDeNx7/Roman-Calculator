import ast
import operator as op

# Supported operators
operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,  # Added support for modulo
}

def eval_expr(expr):
    """
    Safely evaluate a mathematical expression using PEMDAS.
    
    Args:
        expr (str): The mathematical expression as a string.

    Returns:
        The result of the evaluated expression.
    
    Raises:
        ValueError: If the expression contains unsupported operations.
        TypeError: If the expression contains invalid syntax.
    """
    # Parse the expression into an Abstract Syntax Tree (AST)
    tree = ast.parse(expr, mode='eval')

    def _eval(node):
        """Recursively evaluate the AST nodes."""
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        elif isinstance(node, ast.BinOp):
            left = _eval(node.left)
            right = _eval(node.right)
            op_type = type(node.op)
            if op_type in operators:
                return operators[op_type](left, right)
            raise ValueError(f"Unsupported operator: {op_type.__name__}")
        elif isinstance(node, ast.UnaryOp):
            operand = _eval(node.operand)
            if isinstance(node.op, ast.UAdd):  # Unary plus
                return +operand
            elif isinstance(node.op, ast.USub):  # Unary minus
                return -operand
            raise ValueError(f"Unsupported unary operator: {type(node.op).__name__}")
        elif isinstance(node, ast.Constant):
         return node.value
        else:
            raise TypeError(f"Unsupported AST node: {type(node).__name__}")


    # Evaluate the expression
    return _eval(tree.body)
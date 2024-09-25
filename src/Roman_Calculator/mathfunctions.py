import ast
import operator as op

"""Supported operators"""
operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,  
}


"""
Function Name: 
    eval_expr()

Function Description: 
    Evaluates mathematical expressions by using AST (Abstract Syntax Tree). It recursively evaluates the tree
        
Parameters:
    expression (string)

Returns:
    The result of the evaluated expression.
    
Exceptions:
    ValueError: If the expression contains unsupported operations.
    TypeError: If the expression contains invalid syntax.
"""

def eval_expr(expression):
    
    # Parse the expression into an Abstract Syntax Tree (AST)
    tree = ast.parse(expression, mode='eval')

    # Inner Function which recursively evaluates the nodes
    def _eval(node):

        # Recursively calls body 
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        
        # Checks for Binary Operation Symbol
        elif isinstance(node, ast.BinOp): 

            # Every Binary Operation contains a left and right node
            left = _eval(node.left)
            right = _eval(node.right)

            # Type of Binary Operation is stored and checked if valid. Returns that operation of left and right node
            op_type = type(node.op)
            if op_type in operators:
                return operators[op_type](left, right)
            
            # Exception if there is an Invalid Operator
            raise ValueError(f"Unsupported operator: {op_type.__name__}")
        
        # Checks for Unary Operation (Plus or Negative Sign)
        elif isinstance(node, ast.UnaryOp):

            # Recursively calls _eval() to evaluate
            operand = _eval(node.operand)

            # If the operation is + (plus)
            if isinstance(node.op, ast.UAdd):  

                # return operand as is
                return +operand
            
            # If the operation is - (negative)
            elif isinstance(node.op, ast.USub): 

                # return negated operand
                return -operand
            
            # Exception for Unsupported Unary Operator
            raise ValueError(f"Unsupported unary operator: {type(node.op).__name__}")
        
            # Checks if the node is a constant and returns itself
        elif isinstance(node, ast.Constant):
            return node.value
        
        # Unsupported AST node if Expression, BinOp, UnaryOp, or Constant don't appear
        else:
            raise TypeError(f"Unsupported AST node: {type(node).__name__}")


    # Calls _eval on the body and returns the final result of the input
    return _eval(tree.body)
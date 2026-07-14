"""
Calculator Tool - For basic math operations in the Agent.
Inspired by LangChain's tool design pattern.
"""

import re
import ast
import operator as op

class Calculator:
    """
    A simple calculator tool that can evaluate mathematical expressions safely.
    Supports +, -, *, /, ^, sqrt, etc.
    """
    
    def __init__(self):
        self.operators = {
            '+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv,
            '^': op.pow, '**': op.pow, 'sqrt': lambda x: x**0.5
        }
    
    def run(self, expression: str) -> str:
        """
        Evaluate a mathematical expression.
        Returns error message if invalid.
        """
        try:
            # Clean and parse
            expression = expression.replace(' ', '')
            # Basic safety: only allow numbers and operators
            if not re.match(r'^[\d+\-*/^().\s]+$', expression):
                return "Invalid characters in expression."
            
            # Evaluate safely using AST
            node = ast.parse(expression, mode='eval')
            result = self._eval(node.body)
            return str(result)
        except Exception as e:
            return f"Error: {str(e)}"
    
    def _eval(self, node):
        if isinstance(node, ast.Num):  # <number>
            return node.n
        elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
            return self.operators[type(node.op).__name__](self._eval(node.left), self._eval(node.right))
        elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
            return self.operators[type(node.op).__name__](self._eval(node.operand))
        else:
            raise TypeError(f"Unsupported type: {type(node)}")

# Example
if __name__ == "__main__":
    calc = Calculator()
    print(calc.run("2 + 3 * 4"))  # 14
    print(calc.run("sqrt(16)"))   # 4.0
    print(calc.run("10 / 0"))     # Error

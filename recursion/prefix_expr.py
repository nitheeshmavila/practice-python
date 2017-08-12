# handling tree-like structures

def eval(expr):
    if isinstance(expr, int):
        return expr
    else:
        if expr[0] == '+':
            return eval(expr[1]) + eval(expr[2])

print(eval(['+',5,7]))
print(eval(['+', ['+', 3, 4], 8]))

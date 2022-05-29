
import math
import operator as op


# The lamba for 'find' in Environment will call this function
def find(x, y):
    with open(y) as file:
        data = file.read()
        if x in data:
            return True
    return False


class Environment(dict):

    def __init__(self) -> None:
        self.initialize_default()

    def initialize_default(self):
        self.update(vars(math))  # sin, cos, sqrt, pi, ...
        self.update({

            # Standard Math operations (+,-,/,*, %)
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '%': lambda x, y: x % y,

            # Comparison Operators
            '>': lambda x, y: x > y,
            '<': lambda x, y: x < y,
            '>=': lambda x, y: x >= y,
            '<=': lambda x, y: x <= y,
            '=': lambda x,y: x==y,
            'equal?': lambda x,y: x==y,
            'eq?': lambda x,y : x is y,
             
            

            # Max and Min operations
            'max': lambda x, y: max(x, y),
            'min': lambda x, y: min(x, y),


            # Begin is necessary to implement functions
            'begin': lambda *x: x[-1],

            # Add ons:
            # (exp first second) ;  the exp will take the first given int and raise it to the power of the second
            'exp': lambda x, y: x**y,

            # (find, word, filename) ; find will look for a word in a given text file and evaluate to true if found, and false if not
            'find': lambda x, y: find(x, y),



            'length':  len,




            'not':     op.not_,
            'null?': lambda x: x == [],
            'number?': lambda x: isinstance(x, int),
            'print': print,
            'round':   round,
        })

import random
class Environment(dict):

    def __init__(self) -> None:
        self.initialize_default()

    def initialize_default(self):

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
    
    
            #Extra math operations
            'max': lambda x, y: max(x, y),
            'min': lambda x, y: min(x, y),
            'exp': lambda x, y: x**y,
            'pi' : 3.141592653589793,

            # Begin is necessary to implement functions
            'begin': lambda *x: x[-1],

            # Add ons:
            'find': lambda x, y: find(x, y),
            'counter': lambda x,y: countFile(x,y),
            'random': lambda x,y: generateRandom(x,y)
         
        })

# The lambda for 'find', 'count' and 'random' in Environment will call these function
def find(x, y):
    with open(y) as file:
        data = file.read()
        if x in data:
            return True
    return False


def countFile(x, y):
    count = 0
    with open(y) as file:
        data = file.read()
        for word in data.split():
            if word == x:
                count +=1

    return count


def generateRandom(x,y):
    num = random.randint(x,y)
    return num


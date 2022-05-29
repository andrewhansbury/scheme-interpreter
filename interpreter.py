from environment import Environment


class Interpreter:
    def __init__(self):
        self.global_env = Environment()

    def interpret(self, x, env=None):
        if env == None:
            env = self.global_env
        if isinstance(x, str):        # variable reference
            if x in env:
                return env[x]
            else:
                env[x] = x
                return env[x]

        elif isinstance(x, int):      # constant number
            return x
        elif x[0] == 'if':               # conditional
            (_, test, conseq, alt) = x
            exp = (conseq if self.interpret(test, env) else alt)
            return self.interpret(exp, env)
        elif x[0] == 'define':           # definition
            (_, symbol, exp) = x
            env[symbol] = self.interpret(exp, env)
        else:                            # procedure call
            proc = self.interpret(x[0], env)
            args = [self.interpret(arg, env) for arg in x[1:]]
            return proc(*args)

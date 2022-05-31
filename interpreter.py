from environment import Environment


class Interpreter:
    def __init__(self):
        self.global_env = Environment()


    def interpret(self, code, env=None):
        if env == None:
            env = self.global_env

        if isinstance(code, str):   
            if code in env:
                return env[code]
            else:
                env[code] = code
                return env[code]

        elif isinstance(code, int):  
            return code

        elif code[0] == 'if':        
            condition = code[1]
            truthy_res = code[2]
            falsy_res = code[3]

            if self.interpret(condition, env) == True:
                result = truthy_res
            else:
                result = falsy_res

            return self.interpret(result, env)

        elif code[0] == 'define':          
            symbol = code[1]
            val = code[2]
            env[symbol] = self.interpret(val, env)

        else:                          
            func = self.interpret(code[0], env)
            args = []
            for arg in code[1:]:
                args.append(self.interpret(arg, env))

            return func(*args)

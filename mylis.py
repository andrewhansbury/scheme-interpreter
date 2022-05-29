
from parser import Parser
from interpreter import Interpreter


if __name__ == "__main__":
    parser = Parser()
    code = parser.scanTokens("(begin (define r 10) (* pi (* r r)))")
    print(code)

    code2 = parser.scanTokens("(= 1 5)")

    code3 = parser.scanTokens("(find banana text.txt)")

    code4 = parser.scanTokens(
        "(begin (define x 11)(if (< x 10)x(if (> x 20)x(* x 2))))")

    interpreter = Interpreter()

    print(interpreter.interpret(code))

    print(interpreter.interpret(code2))

    print(interpreter.interpret(code3))

    print(interpreter.interpret(code4))

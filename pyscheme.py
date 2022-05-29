# interpretation of Lox from https://craftinginterpreters.com/
import sys
from scanner import Scanner
from parser import Parser
from interpreter import Interpreter


class Scheme:
    def __init__(self):
        pass

    def run(self, source: str):
        self.hadError = False
        scanner = Scanner(source, self)
        scanner.scanTokens()
        tokens = scanner.tokens

        parser: Parser = Parser(tokens, self)
        statements = parser.parse()

        # expression = parser.parse()

        if self.hadError:
            return
        self.interpreter.interpret(statements)

    def runPrompt(self):
        while True:
            try:
                line = input(">")
                self.run(line)
                self.hadError = False

            except (EOFError, KeyboardInterrupt) as e:
                print()
                break

    def main(self):
        if len(sys.argv) > 2:
            print("Too many arguments for pyscheme!!")
        elif len(sys.argv) == 2:
            # print(sys.argv[1])
            self.runFile(sys.argv[1])
        else:
            self.runPrompt()


if __name__ == "__main__":
    Scheme().main()

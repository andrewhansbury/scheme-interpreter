import sys
from parser import Parser
from interpreter import Interpreter


class Scheme:
    def __init__(self):
        self.interpreter = Interpreter()

    def run(self, source: str):
        self.hadError = False
        #parser will create scanner first before parsing
        parser: Parser = Parser()
        statements = parser.parseTokens(source)

        if self.hadError:
            return
        print(self.interpreter.interpret(statements))

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
 
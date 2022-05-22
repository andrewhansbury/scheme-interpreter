

class Parser:

    def __init__(self):
        self.tokens = []

    def scanTokens(self, scheme: str) -> None:

        tokens = self.separateTokens(scheme)

        if len(tokens == 0):
            raise SyntaxError("Error: Unexpected EOF")

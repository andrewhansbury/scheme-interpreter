

class Scanner:

    def __init__(self):
        self.tokens = []

    def separateTokens(self, code: str) -> None:
        # add spaces around parentheses so tokens are not read with them
        code = code.replace('(', ' ( ')
        code = code.replace(')', ' ) ')

        return code.split()

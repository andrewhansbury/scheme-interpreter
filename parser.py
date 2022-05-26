# Inspired by http://norvig.com/lispy.html
from toml import TomlEncoder
from scanner import Scanner
from collections import deque


class Parser:

    def __init__(self):
        self.tokens = []
        self.scanner = Scanner()

    def scanTokens(self, scheme: str) -> None:

        tokens: list = self.scanner.separateTokens(scheme)
        tokens: deque = deque(tokens)

        if len(tokens == 0):
            raise SyntaxError("Error: Unexpected EOF")
        token = tokens.popleft()

        if token == '(':
            s_expression = []
            while tokens[0] != ')':
                s_expression.append(self.scanTokens(tokens))
            tokens.popleft()
            return s_expression
        elif token == ')':
            raise SyntaxError('Unexpected )')
        else:
            return self.addToken(token)

    def addToken(self, token: str):
        if token.isnumeric():
            return int(token)
        elif '.' in token:
            return float(token)
        else:
            return token

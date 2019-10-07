from sly import Lexer

class CalcLexer(Lexer):
    """Basic Lexer.

    Basically just a copy paste from the doc:
    https://sly.readthedocs.io/en/latest/sly.html
    """
    # Set tokens names
    tokens = { ID, NUMBER, PLUS, MINUS, TIMES,
               DIVIDE, ASSIGN, LPAREN, RPAREN,
               MODULO, EQ, IF, ELSE, WHILE,
               PRINT }

    # Inline characters to ignore
    ignore = ' \t'

    # others ignored patterns
    ignore_comment = r'\#.*'
    ignore_newline = r'\n+'

    # Regex for tokens
    # Identifiers & keywords
    ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['if'] = IF
    ID['else'] = ELSE
    ID['while'] = WHILE
    ID['print'] = PRINT

    # Other Regex
    NUMBER  = r'\d+'
    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    EQ      = r'==' # LONGER => MUST APPEARS FIRST !!
    ASSIGN  = r'='
    LPAREN  = r'\('
    RPAREN  = r'\)'
    MODULO  = r'%'

    def NUMBER(self, token):
        """Casting when received token type is NUMBER."""
        token.value = int(token.value)
        return token

    @_(r'\n+')
    def ignore_newline(self, token):
        """Counting line number."""
        self.lineno += len(t.value)


if __name__ == '__main__':
    lexer = CalcLexer()

    while True:
        data = input('>>>')

        for token in lexer.tokenize(data):
            print('type={token_type}, value={token_value}'.format(
                token_type=token.type,
                token_value=repr(token.value),
            ))

        print('')

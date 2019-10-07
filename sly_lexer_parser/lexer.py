from sly import Lexer

class CalcLexer(Lexer):
    """Basic Lexer.

    Basically just a copy paste from the doc:
    https://sly.readthedocs.io/en/latest/sly.html
    """
    # Set tokens names
    tokens = { ID, NUMBER, PLUS, MINUS, TIMES,
               DIVIDE, ASSIGN, LPAREN, RPAREN,
               MODULO }

    # Characters to ignore
    ignore = ' \t'

    # Regex for tokens
    ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER  = r'\d+'
    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    ASSIGN  = r'='
    LPAREN  = r'\('
    RPAREN  = r'\)'
    MODULO  = r'%'

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

from sly import Lexer

class FrenchCalcLexer(Lexer):
    tokens = { ID, NOMBRE, PLUS, MOINS, MULTIPLIER,
               DIVISER, ASSIGNER, GPAREN, RPAREN }

    ignore = ' \t'

    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NOMBRE = r'\d+'
    PLUS = r'\+'
    MOINS = r'-'
    MULTIPLIER = r'\*'
    DIVISER = r'/'
    ASSIGNER = r'='
    GPAREN = r'\('
    RPAREN = r'\)'

if __name__ == '__main__':
    lexer = FrenchCalcLexer()

    while True:
        data = input('>>> ')

        for token in lexer.tokenize(data):
            print('type={t_type}, value={t_val}'.format(
                t_type=token.type,
                t_val=repr(token.value),
            ))

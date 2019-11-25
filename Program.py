import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprListener import ExprListener
from ConcreteExprListener import ConcreteExprListener


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    parser.buildParseTrees = True
    parser_tree = parser.prog()
    expressoes = ConcreteExprListener()
    ParseTreeWalker.DEFAULT.walk(expressoes, parser_tree)
    for expressao in expressoes.values:
        print('{} = {}'.format(expressao['expr'], expressao['value']))


if __name__ == '__main__':
    main(sys.argv)

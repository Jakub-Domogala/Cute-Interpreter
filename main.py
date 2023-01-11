
from sys import argv
from antlr4 import *
from cutiev2Lexer import cutiev2Lexer
from cutiev2Parser import cutiev2Parser
from klasa import klasa


input_stream = FileStream(argv[1])
lexer = cutiev2Lexer(input_stream)
stream = CommonTokenStream(lexer)
parser = cutiev2Parser(stream)
tree = parser.block()
k = klasa()
walker = ParseTreeWalker()
walker.walk(k, tree)

from sys import argv
from antlr4 import *
from dist.cutiev2Lexer import cutiev2Lexer
from dist.cutiev2Parser import cutiev2Parser
from dist.ourVisitor import ourVisitor
from dist.cutiev2Visitor import cutiev2Visitor


input_stream = FileStream(argv[1])
lexer = cutiev2Lexer(input_stream)
stream = CommonTokenStream(lexer)
parser = cutiev2Parser(stream)
tree = parser.block()
visitor = ourVisitor()
visitor.visit(tree)
# walker = ParseTreeWalker()
# walker.walk(visitor, tree)
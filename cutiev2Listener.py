# Generated from cutiev2.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cutiev2Parser import cutiev2Parser
else:
    from cutiev2Parser import cutiev2Parser

# This class defines a complete listener for a parse tree produced by cutiev2Parser.
class cutiev2Listener(ParseTreeListener):

    # Enter a parse tree produced by cutiev2Parser#block.
    def enterBlock(self, ctx:cutiev2Parser.BlockContext):
        pass

    # Exit a parse tree produced by cutiev2Parser#block.
    def exitBlock(self, ctx:cutiev2Parser.BlockContext):
        pass


    # Enter a parse tree produced by cutiev2Parser#stat.
    def enterStat(self, ctx:cutiev2Parser.StatContext):
        pass

    # Exit a parse tree produced by cutiev2Parser#stat.
    def exitStat(self, ctx:cutiev2Parser.StatContext):
        pass


    # Enter a parse tree produced by cutiev2Parser#define_stat.
    def enterDefine_stat(self, ctx:cutiev2Parser.Define_statContext):
        pass

    # Exit a parse tree produced by cutiev2Parser#define_stat.
    def exitDefine_stat(self, ctx:cutiev2Parser.Define_statContext):
        pass


    # Enter a parse tree produced by cutiev2Parser#assign_stat.
    def enterAssign_stat(self, ctx:cutiev2Parser.Assign_statContext):
        pass

    # Exit a parse tree produced by cutiev2Parser#assign_stat.
    def exitAssign_stat(self, ctx:cutiev2Parser.Assign_statContext):
        pass


    # Enter a parse tree produced by cutiev2Parser#print_stat.
    def enterPrint_stat(self, ctx:cutiev2Parser.Print_statContext):
        pass

    # Exit a parse tree produced by cutiev2Parser#print_stat.
    def exitPrint_stat(self, ctx:cutiev2Parser.Print_statContext):
        pass


    # Enter a parse tree produced by cutiev2Parser#if_stat.
    def enterIf_stat(self, ctx:cutiev2Parser.If_statContext):
        pass

    # Exit a parse tree produced by cutiev2Parser#if_stat.
    def exitIf_stat(self, ctx:cutiev2Parser.If_statContext):
        pass


    # Enter a parse tree produced by cutiev2Parser#while_stat.
    def enterWhile_stat(self, ctx:cutiev2Parser.While_statContext):
        pass

    # Exit a parse tree produced by cutiev2Parser#while_stat.
    def exitWhile_stat(self, ctx:cutiev2Parser.While_statContext):
        pass


    # Enter a parse tree produced by cutiev2Parser#expr.
    def enterExpr(self, ctx:cutiev2Parser.ExprContext):
        pass

    # Exit a parse tree produced by cutiev2Parser#expr.
    def exitExpr(self, ctx:cutiev2Parser.ExprContext):
        pass


    # Enter a parse tree produced by cutiev2Parser#term.
    def enterTerm(self, ctx:cutiev2Parser.TermContext):
        pass

    # Exit a parse tree produced by cutiev2Parser#term.
    def exitTerm(self, ctx:cutiev2Parser.TermContext):
        pass


    # Enter a parse tree produced by cutiev2Parser#type.
    def enterType(self, ctx:cutiev2Parser.TypeContext):
        pass

    # Exit a parse tree produced by cutiev2Parser#type.
    def exitType(self, ctx:cutiev2Parser.TypeContext):
        pass



del cutiev2Parser
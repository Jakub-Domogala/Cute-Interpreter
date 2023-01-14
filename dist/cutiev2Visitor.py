# Generated from cutiev2.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cutiev2Parser import cutiev2Parser
else:
    from cutiev2Parser import cutiev2Parser

# This class defines a complete generic visitor for a parse tree produced by cutiev2Parser.

class cutiev2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by cutiev2Parser#block.
    def visitBlock(self, ctx:cutiev2Parser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cutiev2Parser#stat.
    def visitStat(self, ctx:cutiev2Parser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cutiev2Parser#define_stat.
    def visitDefine_stat(self, ctx:cutiev2Parser.Define_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cutiev2Parser#assign_stat.
    def visitAssign_stat(self, ctx:cutiev2Parser.Assign_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cutiev2Parser#print_stat.
    def visitPrint_stat(self, ctx:cutiev2Parser.Print_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cutiev2Parser#if_stat.
    def visitIf_stat(self, ctx:cutiev2Parser.If_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cutiev2Parser#while_stat.
    def visitWhile_stat(self, ctx:cutiev2Parser.While_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cutiev2Parser#operat.
    def visitOperat(self, ctx:cutiev2Parser.OperatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cutiev2Parser#parentise.
    def visitParentise(self, ctx:cutiev2Parser.ParentiseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cutiev2Parser#terminal.
    def visitTerminal(self, ctx:cutiev2Parser.TerminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cutiev2Parser#term.
    def visitTerm(self, ctx:cutiev2Parser.TermContext):
        return self.visitChildren(ctx)



del cutiev2Parser
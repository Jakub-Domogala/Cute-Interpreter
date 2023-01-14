# Generated from cutiev2.g4 by ANTLR 4.11.1
from antlr4 import *

from .cutiev2Parser import cutiev2Parser

from .cutiev2Visitor import cutiev2Visitor

# This class defines a complete generic visitor for a parse tree produced by cutiev2Parser.

class ourVisitor(cutiev2Visitor):
    variables = []

    # Visit a parse tree produced by cutiev2Parser#block.
    def visitBlock(self, ctx:cutiev2Parser.BlockContext):
        global variables
        variables.append({})
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
        l = ctx.left.accept(self)
        r = ctx.right.accept(self)
        print(l, r)
        if ctx.Operator_sign().getText() == '+':
            return l + r
        if ctx.Operator_sign().getText() == '-':
            return l - r
        
        print("nie przeszlo", ctx.Operator_sign())
        return l + r

        return self.visitChildren(ctx)


    # Visit a parse tree produced by cutiev2Parser#parentise.
    def visitParentise(self, ctx:cutiev2Parser.ParentiseContext):
        return ctx.mid.accept(self)


    # Visit a parse tree produced by cutiev2Parser#terminal.
    def visitTerminal(self, ctx:cutiev2Parser.TerminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cutiev2Parser#term.
    def visitTerm(self, ctx:cutiev2Parser.TermContext):
        if ctx.Int() is not None:
            print(ctx.Int(), "visitTerm")
            return int(ctx.Int().getText())

        return self.visitChildren(ctx)

    def aggregateResult(self, aggregate, nextResult):
        if aggregate is None:
            return nextResult
        return aggregate, nextResult





del cutiev2Parser
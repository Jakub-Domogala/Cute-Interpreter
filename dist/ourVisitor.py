# Generated from cutiev2.g4 by ANTLR 4.11.1
from antlr4 import *

from .cutiev2Parser import cutiev2Parser

from .cutiev2Visitor import cutiev2Visitor

# This class defines a complete generic visitor for a parse tree produced by cutiev2Parser.

class ourVisitor(cutiev2Visitor):

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
        result = self.visitChildren(ctx)
        thing = self.visitChildren(ctx)
        print(thing, "wydrukowane")
        return result


    # Visit a parse tree produced by cutiev2Parser#if_stat.
    def visitIf_stat(self, ctx:cutiev2Parser.If_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cutiev2Parser#while_stat.
    def visitWhile_stat(self, ctx:cutiev2Parser.While_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cutiev2Parser#expr.
    def visitExpr(self, ctx:cutiev2Parser.ExprContext):
        
        print(ctx.Open_Parenthesis(), "nawiasy", ctx.Operator_sign())
        # result = self.visitChildren(ctx) 
        # l = self.visit(ctx.left)
        # r = self.visitChildren(ctx.right)
        # print(r, l)
        # print(result, "aa")
        print(ctx.mid, "ctxmid")
        if ctx.Operator_sign() is not None:
            l = self.visitChildren(ctx.left)
            r = self.visitChildren(ctx.right)
            print(l, r)
            if type(l) is not type(int(1)):
                print(l)
                l = l.getText()
            if type(r) is not type(int(1)):
                print(r)
                r = r.getText()
            print(l,ctx.children[1], r, "aaaaaaaaaa", type(r))
            l = int(l)
            r = int(r)
            # print(type(l.getText))
            print(l + r)
            return l + r
        elif ctx.Open_Parenthesis() is not None:
            print("open")
            oldctx = ctx
            m = self.visitChildren(ctx.mid)
            print(m, "mid=================")
            return int(m.getText())
        print("END")
        # result = self.visitChildren(ctx)
        # print(result)
        # print(self.visitChildren(ctx.mid))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cutiev2Parser#term.
    def visitTerm(self, ctx:cutiev2Parser.TermContext):
        if ctx.Int() is not None:
            print(ctx.Int(), "visitTerm")
            return ctx.Int()

        return self.visitChildren(ctx)



del cutiev2Parser
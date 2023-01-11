

from cutiev2Listener import cutiev2Listener
from cutiev2Parser import cutiev2Parser


class klasa(cutiev2Listener):

# Enter a parse tree produced by cutiev2Parser#block.
    def enterBlock(self, ctx:cutiev2Parser.BlockContext):
        print("enterBlock")

    # Exit a parse tree produced by cutiev2Parser#block.
    def exitBlock(self, ctx:cutiev2Parser.BlockContext):
        print("exitBlock")


    # Enter a parse tree produced by cutiev2Parser#stat.
    def enterStat(self, ctx:cutiev2Parser.StatContext):
        print("enterStat")

    # Exit a parse tree produced by cutiev2Parser#stat.
    def exitStat(self, ctx:cutiev2Parser.StatContext):
        print("exitStat")


    # Enter a parse tree produced by cutiev2Parser#define_stat.
    def enterDefine_stat(self, ctx:cutiev2Parser.Define_statContext):
        print(cutiev2Parser.Define_statContext.Identifier(ctx))
        print(cutiev2Parser.Define_statContext.type_(ctx))
        print("enterDefine_stat")

    # Exit a parse tree produced by cutiev2Parser#define_stat.
    def exitDefine_stat(self, ctx:cutiev2Parser.Define_statContext):
        print("exitDefine_stat")


    # Enter a parse tree produced by cutiev2Parser#assign_stat.
    def enterAssign_stat(self, ctx:cutiev2Parser.Assign_statContext):
        print("enterAssign_stat")

    # Exit a parse tree produced by cutiev2Parser#assign_stat.
    def exitAssign_stat(self, ctx:cutiev2Parser.Assign_statContext):
        print("exitAssign_stat")


    # Enter a parse tree produced by cutiev2Parser#print_stat.
    def enterPrint_stat(self, ctx:cutiev2Parser.Print_statContext):
        print("enterPrint_stat")

    # Exit a parse tree produced by cutiev2Parser#print_stat.
    def exitPrint_stat(self, ctx:cutiev2Parser.Print_statContext):
        print("exitPrint_stat")


    # Enter a parse tree produced by cutiev2Parser#if_stat.
    def enterIf_stat(self, ctx:cutiev2Parser.If_statContext):
        print("enterIf_stat")

    # Exit a parse tree produced by cutiev2Parser#if_stat.
    def exitIf_stat(self, ctx:cutiev2Parser.If_statContext):
        print("exitIf_stat")


    # Enter a parse tree produced by cutiev2Parser#while_stat.
    def enterWhile_stat(self, ctx:cutiev2Parser.While_statContext):
        print("enterWhile_stat")

    # Exit a parse tree produced by cutiev2Parser#while_stat.
    def exitWhile_stat(self, ctx:cutiev2Parser.While_statContext):
        print("exitWhile_stat")


    # Enter a parse tree produced by cutiev2Parser#expr.
    def enterExpr(self, ctx:cutiev2Parser.ExprContext):
        print("enterExpr")

    # Exit a parse tree produced by cutiev2Parser#expr.
    def exitExpr(self, ctx:cutiev2Parser.ExprContext):
        print("exitExpr")


    # Enter a parse tree produced by cutiev2Parser#term.
    def enterTerm(self, ctx:cutiev2Parser.TermContext):
        print("enterTerm")

    # Exit a parse tree produced by cutiev2Parser#term.
    def exitTerm(self, ctx:cutiev2Parser.TermContext):
        print("exitTerm")
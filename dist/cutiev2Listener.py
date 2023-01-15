# Generated from cutiev2.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cutiev2Parser import cutiev2Parser
else:
    from cutiev2Parser import cutiev2Parser

# This class defines a complete listener for a parse tree produced by cutiev2Parser.
class cutiev2Listener(ParseTreeListener):

    # Enter a parse tree produced by cutiev2Parser#program.
    def enterProgram(self, ctx:cutiev2Parser.ProgramContext):
        pass

    # Exit a parse tree produced by cutiev2Parser#program.
    def exitProgram(self, ctx:cutiev2Parser.ProgramContext):
        pass


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


    # Enter a parse tree produced by cutiev2Parser#defonly.
    def enterDefonly(self, ctx:cutiev2Parser.DefonlyContext):
        pass

    # Exit a parse tree produced by cutiev2Parser#defonly.
    def exitDefonly(self, ctx:cutiev2Parser.DefonlyContext):
        pass


    # Enter a parse tree produced by cutiev2Parser#defandasign.
    def enterDefandasign(self, ctx:cutiev2Parser.DefandasignContext):
        pass

    # Exit a parse tree produced by cutiev2Parser#defandasign.
    def exitDefandasign(self, ctx:cutiev2Parser.DefandasignContext):
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


    # Enter a parse tree produced by cutiev2Parser#operat.
    def enterOperat(self, ctx:cutiev2Parser.OperatContext):
        pass

    # Exit a parse tree produced by cutiev2Parser#operat.
    def exitOperat(self, ctx:cutiev2Parser.OperatContext):
        pass


    # Enter a parse tree produced by cutiev2Parser#negate.
    def enterNegate(self, ctx:cutiev2Parser.NegateContext):
        pass

    # Exit a parse tree produced by cutiev2Parser#negate.
    def exitNegate(self, ctx:cutiev2Parser.NegateContext):
        pass


    # Enter a parse tree produced by cutiev2Parser#parentise.
    def enterParentise(self, ctx:cutiev2Parser.ParentiseContext):
        pass

    # Exit a parse tree produced by cutiev2Parser#parentise.
    def exitParentise(self, ctx:cutiev2Parser.ParentiseContext):
        pass


    # Enter a parse tree produced by cutiev2Parser#terminal.
    def enterTerminal(self, ctx:cutiev2Parser.TerminalContext):
        pass

    # Exit a parse tree produced by cutiev2Parser#terminal.
    def exitTerminal(self, ctx:cutiev2Parser.TerminalContext):
        pass


    # Enter a parse tree produced by cutiev2Parser#TermName.
    def enterTermName(self, ctx:cutiev2Parser.TermNameContext):
        pass

    # Exit a parse tree produced by cutiev2Parser#TermName.
    def exitTermName(self, ctx:cutiev2Parser.TermNameContext):
        pass


    # Enter a parse tree produced by cutiev2Parser#TermInt.
    def enterTermInt(self, ctx:cutiev2Parser.TermIntContext):
        pass

    # Exit a parse tree produced by cutiev2Parser#TermInt.
    def exitTermInt(self, ctx:cutiev2Parser.TermIntContext):
        pass


    # Enter a parse tree produced by cutiev2Parser#TermDouble.
    def enterTermDouble(self, ctx:cutiev2Parser.TermDoubleContext):
        pass

    # Exit a parse tree produced by cutiev2Parser#TermDouble.
    def exitTermDouble(self, ctx:cutiev2Parser.TermDoubleContext):
        pass


    # Enter a parse tree produced by cutiev2Parser#TermBool.
    def enterTermBool(self, ctx:cutiev2Parser.TermBoolContext):
        pass

    # Exit a parse tree produced by cutiev2Parser#TermBool.
    def exitTermBool(self, ctx:cutiev2Parser.TermBoolContext):
        pass



del cutiev2Parser
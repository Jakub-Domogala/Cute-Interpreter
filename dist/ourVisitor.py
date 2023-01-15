# Generated from cutiev2.g4 by ANTLR 4.11.1
from antlr4 import *

from .cutiev2Parser import cutiev2Parser

from .cutiev2Visitor import cutiev2Visitor

# This class defines a complete generic visitor for a parse tree produced by cutiev2Parser.

def get_type(name):
    if name == 'bezprzecinek':
        return 'INT'
    if name == 'zprzecinek':
        return 'DOUBLE'
    if name == 'zerojedynek':
        return 'BOOL'
    return "Coś ewidetnie poszło nie tak"

class ourVisitor(cutiev2Visitor):
    def __init__(self) -> None:
        super().__init__()
        self.variables = [{}]
        # Form of dicts
        # {key-name : (type, value)}

    def enterScope(self):
        self.variables.append({})
    
    def exitScope(self):
        self.variables.pop()

    def new_variable(self, name, type, value = None):
        for d in self.variables:
            if name in d:
                return False # GO FOR ERROR
        if value is None:
            if type == 'INT':
                value = 69
            elif type == 'DOUBLE':
                value = 21.37
            elif type == 'BOOL':
                value = 'prawda'
        self.variables[-1][name] = (type, value)
    
    def variable_new_value(self, name, type, value):
        for d in self.variables:
            if name in d:
                if d[name][0] != type:
                    return False
                d[name] = (type, value)
                return True

    # Visit a parse tree produced by cutiev2Parser#block.
    def visitBlock(self, ctx:cutiev2Parser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cutiev2Parser#stat.
    def visitStat(self, ctx:cutiev2Parser.StatContext):
        return self.visitChildren(ctx)

    # For DEFINE
    # Visit a parse tree produced by cutiev2Parser#defonly.
    def visitDefonly(self, ctx:cutiev2Parser.DefonlyContext):
        self.new_variable(ctx.NAME().getText(), get_type(ctx.TYPE().getText()))
        print(self.variables)
        return self.visitChildren(ctx)

    # For DEFINE
    # Visit a parse tree produced by cutiev2Parser#defandasign.
    def visitDefandasign(self, ctx:cutiev2Parser.DefandasignContext):
        value = ctx.value.accept(self)
        self.new_variable(ctx.NAME().getText(), value[1], value[0])
        print(self.variables)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cutiev2Parser#assign_stat.
    def visitAssign_stat(self, ctx:cutiev2Parser.Assign_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cutiev2Parser#print_stat.
    def visitPrint_stat(self, ctx:cutiev2Parser.Print_statContext):
        print(ctx.valorname.accept(self)[0])
        print(self.variables[ctx.valorname.accept(self)[0]])
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cutiev2Parser#if_stat.
    def visitIf_stat(self, ctx:cutiev2Parser.If_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cutiev2Parser#while_stat.
    def visitWhile_stat(self, ctx:cutiev2Parser.While_statContext):
            
        return self.visitChildren(ctx)

    # For EXPRESIONS
    # Visit a parse tree produced by cutiev2Parser#operat.
    def visitOperat(self, ctx:cutiev2Parser.OperatContext):
        l = ctx.left.accept(self)
        r = ctx.right.accept(self)
        if l[1] != r[1]:
            raise Exception(f"Złe typy gamoniu... {l} nie ma takiego samego typu jak {r}")
        if l[1] != "BOOL":
            if ctx.Operator_sign().getText() == '+':
                return l[0] + r[0], l[1]
            if ctx.Operator_sign().getText() == '-':
                return l[0] - r[0], l[1]
            if ctx.Operator_sign().getText() == '/':
                return l[0] / r[0], l[1]
            if ctx.Operator_sign().getText() == '*':
                return l[0] * r[0], l[1]
            if ctx.Operator_sign().getText() == '%':
                return l[0] % r[0], l[1]
            if ctx.Operator_sign().getText() == '|/|':  # nudny symbol....
                return l[0] // r[0], l[1]
            if ctx.Operator_sign().getText() == '|^|':
                return max(l[0], r[0]), l[1]
            if ctx.Operator_sign().getText() == '|v|':
                return min(l[0], r[0]), l[1]
            if ctx.Operator_sign().getText() == '|*|':
                return l[0] ** r[0], l[1]
            if ctx.Operator_sign().getText() == 'mniejszyod':
                return 'prawda' if l[0] < r[0] else 'nieprawda', 'BOOL'
            if ctx.Operator_sign().getText() == 'wiekszyod':
                return 'prawda' if l[0] > r[0] else 'nieprawda', 'BOOL'

        if ctx.Operator_sign().getText() == 'kropkawkropke':
            return 'prawda' if l[0] == r[0] else 'nieprawda', 'BOOL'
        if ctx.Operator_sign().getText() == 'innyod':
            return 'prawda' if l[0] != r[0] else 'nieprawda', 'BOOL'

        raise Exception("Nie ma takiej operacji :( ")

        # return self.visitChildren(ctx)

    # For EXPRESIONS
    # Visit a parse tree produced by cutiev2Parser#parentise.
    def visitParentise(self, ctx:cutiev2Parser.ParentiseContext):
        return ctx.mid.accept(self)

    # For EXPRESIONS
    # Visit a parse tree produced by cutiev2Parser#terminal.
    def visitTerminal(self, ctx:cutiev2Parser.TerminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cutiev2Parser#term.
    def visitTerm(self, ctx:cutiev2Parser.TermContext):
        if ctx.Int() is not None:
            print(ctx.Int(), "visitTerm")
            return int(ctx.Int().getText())

        return self.visitChildren(ctx)

    # Visit a parse tree produced by cutiev2Parser#TermName.
    def visitTermName(self, ctx:cutiev2Parser.TermNameContext):
        name = ctx.NAME().getText()
        for d in self.variables:
            if name in d:
                return d[name]
        return None, None


    # Visit a parse tree produced by cutiev2Parser#TermInt.
    def visitTermInt(self, ctx:cutiev2Parser.TermIntContext):
        return int(ctx.Int().getText()), 'INT'


    # Visit a parse tree produced by cutiev2Parser#TermDouble.
    def visitTermDouble(self, ctx:cutiev2Parser.TermDoubleContext):
        return float(ctx.Double().getText()), 'DOUBLE'


    # Visit a parse tree produced by cutiev2Parser#TermBool.
    def visitTermBool(self, ctx:cutiev2Parser.TermBoolContext):
        return ctx.Bool().getText(), 'BOOL'


    def aggregateResult(self, aggregate, nextResult):
        if aggregate is None:
            return nextResult
        return aggregate, nextResult


del cutiev2Parser
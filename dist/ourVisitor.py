from antlr4 import *
from .cutiev2Parser import cutiev2Parser
from .cutiev2Visitor import cutiev2Visitor
from random import randint

# This class defines a complete generic visitor for a parse tree produced by cutiev2Parser.
emotes_happy = ['😀', '😁', '🤣', '😃', '😄', '😅', '😆', '😉', '😊', '😋', '😎', '😍', '😘', '😗']
emotes_sad = ['😒', '🤐', '😠', '😭', '😒']


# Emotes Functions
def get_emote_happy():
    global emotes_happy
    return emotes_happy[randint(0, len(emotes_happy) - 1)]


def get_emote_sad():
    global emotes_sad
    return emotes_sad[randint(0, len(emotes_sad) - 1)]


# Translation Functions
def bool_name_to_real(val):
    return True if val == "prawda" else False


def bool_real_to_name(val):
    return "prawda" if val is True else "nieprawda"


def get_type(name):
    if name == 'bezprzecinek':
        return 'INT'
    if name == 'zprzecinek':
        return 'DOUBLE'
    if name == 'zerojedynek':
        return 'BOOL'
    return "Coś ewidetnie poszło nie tak"


def reverse_get_type(name):
    if name == 'INT':
        return 'bezprzecinek'
    if name == 'DOUBLE':
        return 'zprzecinek'
    if name == 'BOOL':
        return 'zerojedynek'
    return "Coś ewidetnie poszło nie tak"


class ourVisitor(cutiev2Visitor):
    # Init Function
    def __init__(self) -> None:
        super().__init__()
        # Define list of dicts to remember variables
        self.variables = [{}]
        # Form of dicts
        # {key-name : (type, value)}

    # Functions to move up or down in scopes of variables

    def enterScope(self):
        self.variables.append({})

    def exitScope(self):
        self.variables.pop()

    # Functions to handle defining variables and making operations on them

    # Function to define new variable
    def new_variable(self, name, type, value=None):
        for d in self.variables:
            if name in d:
                raise Exception(f"No niestety ale zmienna {name} już istnieje", get_emote_sad())
        if value is None:
            if type == 'INT':
                value = 69
            elif type == 'DOUBLE':
                value = 21.37
            elif type == 'BOOL':
                value = 'prawda'
        self.variables[-1][name] = (value, type)

    # Function to change value of variable
    def variable_new_value(self, name, type, value):
        for d in self.variables:
            if name in d:
                if d[name][1] != type:
                    return False
                d[name] = (value, type)
                return True

    # Function to get value and type of variable with given name
    def get_variable(self, name):
        for d in self.variables:
            if name in d:
                return d[name]
        return None, None

    # OVERRIDE Functions from cutiev2Visitor

    # Visit a parse tree produced by cutiev2Parser#program.
    def visitProgram(self, ctx: cutiev2Parser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cutiev2Parser#block.
    def visitBlock(self, ctx: cutiev2Parser.BlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cutiev2Parser#stat.
    def visitStat(self, ctx: cutiev2Parser.StatContext):
        return self.visitChildren(ctx)

    # For DEFINE
    # Visit a parse tree produced by cutiev2Parser#defonly.
    def visitDefonly(self, ctx: cutiev2Parser.DefonlyContext):
        self.new_variable(ctx.NAME().getText(), get_type(ctx.TYPE().getText()))
        # print(self.variables)
        return self.visitChildren(ctx)

    # For DEFINE
    # Visit a parse tree produced by cutiev2Parser#defandasign.
    def visitDefandasign(self, ctx: cutiev2Parser.DefandasignContext):
        value = ctx.value.accept(self)
        self.new_variable(ctx.NAME().getText(), value[1], value[0])
        # print(self.variables)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cutiev2Parser#assign_stat.
    def visitAssign_stat(self, ctx: cutiev2Parser.Assign_statContext):
        vtype, vval = self.get_variable(ctx.NAME().getText())
        if vtype is None:
            raise Exception(f"No szkoda, ale nie mamy zmiennej [{ctx.NAME().getText()}] {get_emote_sad()}")
        newval = ctx.value.accept(self)
        self.variable_new_value(ctx.NAME().getText(), newval[1], newval[0])

    # Visit a parse tree produced by cutiev2Parser#print_stat.
    def visitPrint_stat(self, ctx: cutiev2Parser.Print_statContext):
        try:
            if ctx.valorname.NAME():
                var = self.get_variable(ctx.valorname.NAME().getText())
                print(get_emote_happy(), ctx.valorname.NAME().getText(), 'ma wartość',
                      "{:<{width}}".format(var[0], width=10), 'i jest typu', reverse_get_type(var[1]),
                      get_emote_happy())
                return
        except:
            if ctx.valorname.accept(self)[0] is None:
                raise Exception(
                    f"No szkoda, ale nie mamy zmiennej [{ctx.valorname.NAME().getText()}] {get_emote_sad()}")
            print(get_emote_happy(), ctx.valorname.accept(self)[0], get_emote_happy())

    # Visit a parse tree produced by cutiev2Parser#if_stat.
    def visitIf_stat(self, ctx: cutiev2Parser.If_statContext):
        var = ctx.valorname.accept(self)
        print(var)
        if var[0] is None:
            return
        if var[1] != "BOOL":
            if var[0] != 0:
                ctx.block().accept(self)
                return
        if var[0] == "prawda":
            return ctx.block().accept(self)
        return None

    # Visit a parse tree produced by cutiev2Parser#while_stat.
    def visitWhile_stat(self, ctx: cutiev2Parser.While_statContext):
        self.enterScope()
        while (ctx.valorname.accept(self)[0] is not None
               and (ctx.valorname.accept(self)[1] == "BOOL"
                    and ctx.valorname.accept(self)[0] == "prawda")
               or (ctx.valorname.accept(self)[1] != "BOOL"
                   and ctx.valorname.accept(self)[0] != 0)):
            # print(ctx.valorname.accept(self))
            ctx.block().accept(self)
        self.exitScope()
        return
        return self.visitChildren(ctx)

    # For EXPRESIONS
    # Visit a parse tree produced by cutiev2Parser#operat.
    def visitOperat(self, ctx: cutiev2Parser.OperatContext):
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
                if l[1] == "INT":  # if we operate on int we want to keep in int
                    return l[0] // r[0], l[1]
                return l[0] / r[0], l[1]
            if ctx.Operator_sign().getText() == '*':
                return l[0] * r[0], l[1]
            if ctx.Operator_sign().getText() == '%':
                return l[0] % r[0], l[1]
            if ctx.Operator_sign().getText() == '|/|':
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

        if l[1] == "BOOL":
            lv = bool_name_to_real(l[0])
            rv = bool_name_to_real(r[0])
            if ctx.Operator_sign().getText() == 'lub':
                return bool_real_to_name(lv or rv), "BOOL"
            if ctx.Operator_sign().getText() == 'oraz':
                return bool_real_to_name(lv and rv), "BOOL"

        raise Exception("Nie ma takiej operacji", get_emote_sad())

    # For EXPRESIONS
    # Visit a parse tree produced by cutiev2Parser#negate.
    def visitNegate(self, ctx: cutiev2Parser.NegateContext):
        vval, vtype = ctx.mid.accept(self)
        if vtype == "BOOL" and ctx.Operator_sign().getText() == "nie":
            return ("prawda", "BOOL") if vval == "nieprawda" else ("nieprawda", "BOOL")
        if ctx.Operator_sign().getText() == "-":
            return (-vval, vtype)
        raise Exception(f"Nawet tak nie żartuj, co {ctx.Operator_sign().getText()} {ctx.expr().getText()} ")

    # For EXPRESIONS
    # Visit a parse tree produced by cutiev2Parser#parentise.
    def visitParentise(self, ctx: cutiev2Parser.ParentiseContext):
        return ctx.mid.accept(self)

    # For EXPRESIONS
    # Visit a parse tree produced by cutiev2Parser#terminal.
    def visitTerminal(self, ctx: cutiev2Parser.TerminalContext):
        return self.visitChildren(ctx)

    # For TERM
    # Visit a parse tree produced by cutiev2Parser#TermName.
    def visitTermName(self, ctx: cutiev2Parser.TermNameContext):
        name = ctx.NAME().getText()
        for d in self.variables:
            if name in d:
                return d[name]
        return None, None

    # For TERM
    # Visit a parse tree produced by cutiev2Parser#TermInt.
    def visitTermInt(self, ctx: cutiev2Parser.TermIntContext):
        return int(ctx.Int().getText()), 'INT'

    # For TERM
    # Visit a parse tree produced by cutiev2Parser#TermDouble.
    def visitTermDouble(self, ctx: cutiev2Parser.TermDoubleContext):
        return float(ctx.Double().getText()), 'DOUBLE'

    # For TERM
    # Visit a parse tree produced by cutiev2Parser#TermBool.
    def visitTermBool(self, ctx: cutiev2Parser.TermBoolContext):
        return ctx.Bool().getText(), 'BOOL'

    # OVERRIDE Function to Tree Class from Tree.py
    def aggregateResult(self, aggregate, nextResult):
        if aggregate is None:
            return nextResult
        return aggregate, nextResult


del cutiev2Parser

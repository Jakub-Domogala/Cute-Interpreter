# Generated from cutiev2.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,99,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,1,4,1,24,8,1,11,1,12,1,25,1,
        2,1,2,1,2,1,2,1,2,3,2,33,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,3,3,46,8,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,83,8,8,1,8,1,8,1,8,5,8,88,8,8,
        10,8,12,8,91,9,8,1,9,1,9,1,9,1,9,3,9,97,8,9,1,9,0,1,16,10,0,2,4,
        6,8,10,12,14,16,18,0,0,100,0,20,1,0,0,0,2,23,1,0,0,0,4,32,1,0,0,
        0,6,45,1,0,0,0,8,47,1,0,0,0,10,52,1,0,0,0,12,58,1,0,0,0,14,66,1,
        0,0,0,16,82,1,0,0,0,18,96,1,0,0,0,20,21,3,2,1,0,21,1,1,0,0,0,22,
        24,3,4,2,0,23,22,1,0,0,0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,
        0,26,3,1,0,0,0,27,33,3,6,3,0,28,33,3,8,4,0,29,33,3,10,5,0,30,33,
        3,12,6,0,31,33,3,14,7,0,32,27,1,0,0,0,32,28,1,0,0,0,32,29,1,0,0,
        0,32,30,1,0,0,0,32,31,1,0,0,0,33,5,1,0,0,0,34,35,5,17,0,0,35,36,
        5,11,0,0,36,37,5,23,0,0,37,46,5,9,0,0,38,39,5,17,0,0,39,40,5,11,
        0,0,40,41,5,23,0,0,41,42,5,12,0,0,42,43,3,16,8,0,43,44,5,9,0,0,44,
        46,1,0,0,0,45,34,1,0,0,0,45,38,1,0,0,0,46,7,1,0,0,0,47,48,5,23,0,
        0,48,49,5,12,0,0,49,50,3,16,8,0,50,51,5,9,0,0,51,9,1,0,0,0,52,53,
        5,13,0,0,53,54,5,1,0,0,54,55,3,18,9,0,55,56,5,2,0,0,56,57,5,9,0,
        0,57,11,1,0,0,0,58,59,5,14,0,0,59,60,5,1,0,0,60,61,3,16,8,0,61,62,
        5,2,0,0,62,63,5,3,0,0,63,64,3,2,1,0,64,65,5,4,0,0,65,13,1,0,0,0,
        66,67,5,15,0,0,67,68,5,1,0,0,68,69,3,16,8,0,69,70,5,2,0,0,70,71,
        5,3,0,0,71,72,3,2,1,0,72,73,5,4,0,0,73,15,1,0,0,0,74,75,6,8,-1,0,
        75,76,5,1,0,0,76,77,3,16,8,0,77,78,5,2,0,0,78,83,1,0,0,0,79,83,3,
        18,9,0,80,81,5,10,0,0,81,83,3,16,8,1,82,74,1,0,0,0,82,79,1,0,0,0,
        82,80,1,0,0,0,83,89,1,0,0,0,84,85,10,4,0,0,85,86,5,10,0,0,86,88,
        3,16,8,5,87,84,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,
        90,17,1,0,0,0,91,89,1,0,0,0,92,97,5,23,0,0,93,97,5,19,0,0,94,97,
        5,20,0,0,95,97,5,22,0,0,96,92,1,0,0,0,96,93,1,0,0,0,96,94,1,0,0,
        0,96,95,1,0,0,0,97,19,1,0,0,0,6,25,32,45,82,89,96
    ]

class cutiev2Parser ( Parser ):

    grammarFileName = "cutiev2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "'.'", "','", "'|<3|'", "<INVALID>", "'->'", "'<-'", 
                     "'drukareczka'", "'waruneczek'", "'powielanko'", "'zwrocik'" ]

    symbolicNames = [ "<INVALID>", "Open_Parenthesis", "Close_Parenthesis", 
                      "Open_Bracket", "Close_Bracket", "Open_Square_Bracket", 
                      "Close_Square_Bracket", "Dot", "Comma", "Semicolon", 
                      "Operator_sign", "Var_define", "Val_assign", "Print", 
                      "If", "While", "Return", "TYPE", "White_Sign", "Int", 
                      "Double", "Number", "Bool", "NAME", "COMMENT" ]

    RULE_program = 0
    RULE_block = 1
    RULE_stat = 2
    RULE_define_stat = 3
    RULE_assign_stat = 4
    RULE_print_stat = 5
    RULE_if_stat = 6
    RULE_while_stat = 7
    RULE_expr = 8
    RULE_term = 9

    ruleNames =  [ "program", "block", "stat", "define_stat", "assign_stat", 
                   "print_stat", "if_stat", "while_stat", "expr", "term" ]

    EOF = Token.EOF
    Open_Parenthesis=1
    Close_Parenthesis=2
    Open_Bracket=3
    Close_Bracket=4
    Open_Square_Bracket=5
    Close_Square_Bracket=6
    Dot=7
    Comma=8
    Semicolon=9
    Operator_sign=10
    Var_define=11
    Val_assign=12
    Print=13
    If=14
    While=15
    Return=16
    TYPE=17
    White_Sign=18
    Int=19
    Double=20
    Number=21
    Bool=22
    NAME=23
    COMMENT=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(cutiev2Parser.BlockContext,0)


        def getRuleIndex(self):
            return cutiev2Parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = cutiev2Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cutiev2Parser.StatContext)
            else:
                return self.getTypedRuleContext(cutiev2Parser.StatContext,i)


        def getRuleIndex(self):
            return cutiev2Parser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = cutiev2Parser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.stat()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 8577024) != 0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def define_stat(self):
            return self.getTypedRuleContext(cutiev2Parser.Define_statContext,0)


        def assign_stat(self):
            return self.getTypedRuleContext(cutiev2Parser.Assign_statContext,0)


        def print_stat(self):
            return self.getTypedRuleContext(cutiev2Parser.Print_statContext,0)


        def if_stat(self):
            return self.getTypedRuleContext(cutiev2Parser.If_statContext,0)


        def while_stat(self):
            return self.getTypedRuleContext(cutiev2Parser.While_statContext,0)


        def getRuleIndex(self):
            return cutiev2Parser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = cutiev2Parser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stat)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.define_stat()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.assign_stat()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.print_stat()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.if_stat()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 5)
                self.state = 31
                self.while_stat()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Define_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cutiev2Parser.RULE_define_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DefandasignContext(Define_statContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cutiev2Parser.Define_statContext
            super().__init__(parser)
            self.value = None # ExprContext
            self.copyFrom(ctx)

        def TYPE(self):
            return self.getToken(cutiev2Parser.TYPE, 0)
        def Var_define(self):
            return self.getToken(cutiev2Parser.Var_define, 0)
        def NAME(self):
            return self.getToken(cutiev2Parser.NAME, 0)
        def Val_assign(self):
            return self.getToken(cutiev2Parser.Val_assign, 0)
        def Semicolon(self):
            return self.getToken(cutiev2Parser.Semicolon, 0)
        def expr(self):
            return self.getTypedRuleContext(cutiev2Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefandasign" ):
                listener.enterDefandasign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefandasign" ):
                listener.exitDefandasign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefandasign" ):
                return visitor.visitDefandasign(self)
            else:
                return visitor.visitChildren(self)


    class DefonlyContext(Define_statContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cutiev2Parser.Define_statContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TYPE(self):
            return self.getToken(cutiev2Parser.TYPE, 0)
        def Var_define(self):
            return self.getToken(cutiev2Parser.Var_define, 0)
        def NAME(self):
            return self.getToken(cutiev2Parser.NAME, 0)
        def Semicolon(self):
            return self.getToken(cutiev2Parser.Semicolon, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefonly" ):
                listener.enterDefonly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefonly" ):
                listener.exitDefonly(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefonly" ):
                return visitor.visitDefonly(self)
            else:
                return visitor.visitChildren(self)



    def define_stat(self):

        localctx = cutiev2Parser.Define_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_define_stat)
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = cutiev2Parser.DefonlyContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(cutiev2Parser.TYPE)
                self.state = 35
                self.match(cutiev2Parser.Var_define)
                self.state = 36
                self.match(cutiev2Parser.NAME)
                self.state = 37
                self.match(cutiev2Parser.Semicolon)
                pass

            elif la_ == 2:
                localctx = cutiev2Parser.DefandasignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.match(cutiev2Parser.TYPE)
                self.state = 39
                self.match(cutiev2Parser.Var_define)
                self.state = 40
                self.match(cutiev2Parser.NAME)
                self.state = 41
                self.match(cutiev2Parser.Val_assign)
                self.state = 42
                localctx.value = self.expr(0)
                self.state = 43
                self.match(cutiev2Parser.Semicolon)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None # ExprContext

        def NAME(self):
            return self.getToken(cutiev2Parser.NAME, 0)

        def Val_assign(self):
            return self.getToken(cutiev2Parser.Val_assign, 0)

        def Semicolon(self):
            return self.getToken(cutiev2Parser.Semicolon, 0)

        def expr(self):
            return self.getTypedRuleContext(cutiev2Parser.ExprContext,0)


        def getRuleIndex(self):
            return cutiev2Parser.RULE_assign_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_stat" ):
                listener.enterAssign_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_stat" ):
                listener.exitAssign_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stat" ):
                return visitor.visitAssign_stat(self)
            else:
                return visitor.visitChildren(self)




    def assign_stat(self):

        localctx = cutiev2Parser.Assign_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assign_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(cutiev2Parser.NAME)
            self.state = 48
            self.match(cutiev2Parser.Val_assign)
            self.state = 49
            localctx.value = self.expr(0)
            self.state = 50
            self.match(cutiev2Parser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.valorname = None # TermContext

        def Print(self):
            return self.getToken(cutiev2Parser.Print, 0)

        def Open_Parenthesis(self):
            return self.getToken(cutiev2Parser.Open_Parenthesis, 0)

        def Close_Parenthesis(self):
            return self.getToken(cutiev2Parser.Close_Parenthesis, 0)

        def Semicolon(self):
            return self.getToken(cutiev2Parser.Semicolon, 0)

        def term(self):
            return self.getTypedRuleContext(cutiev2Parser.TermContext,0)


        def getRuleIndex(self):
            return cutiev2Parser.RULE_print_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_stat" ):
                listener.enterPrint_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_stat" ):
                listener.exitPrint_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_stat" ):
                return visitor.visitPrint_stat(self)
            else:
                return visitor.visitChildren(self)




    def print_stat(self):

        localctx = cutiev2Parser.Print_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_print_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(cutiev2Parser.Print)
            self.state = 53
            self.match(cutiev2Parser.Open_Parenthesis)
            self.state = 54
            localctx.valorname = self.term()
            self.state = 55
            self.match(cutiev2Parser.Close_Parenthesis)
            self.state = 56
            self.match(cutiev2Parser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.valorname = None # ExprContext

        def If(self):
            return self.getToken(cutiev2Parser.If, 0)

        def Open_Parenthesis(self):
            return self.getToken(cutiev2Parser.Open_Parenthesis, 0)

        def Close_Parenthesis(self):
            return self.getToken(cutiev2Parser.Close_Parenthesis, 0)

        def expr(self):
            return self.getTypedRuleContext(cutiev2Parser.ExprContext,0)


        def Open_Bracket(self):
            return self.getToken(cutiev2Parser.Open_Bracket, 0)

        def block(self):
            return self.getTypedRuleContext(cutiev2Parser.BlockContext,0)


        def Close_Bracket(self):
            return self.getToken(cutiev2Parser.Close_Bracket, 0)

        def getRuleIndex(self):
            return cutiev2Parser.RULE_if_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stat" ):
                listener.enterIf_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stat" ):
                listener.exitIf_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stat" ):
                return visitor.visitIf_stat(self)
            else:
                return visitor.visitChildren(self)




    def if_stat(self):

        localctx = cutiev2Parser.If_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_if_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(cutiev2Parser.If)
            self.state = 59
            self.match(cutiev2Parser.Open_Parenthesis)
            self.state = 60
            localctx.valorname = self.expr(0)
            self.state = 61
            self.match(cutiev2Parser.Close_Parenthesis)

            self.state = 62
            self.match(cutiev2Parser.Open_Bracket)
            self.state = 63
            self.block()
            self.state = 64
            self.match(cutiev2Parser.Close_Bracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.valorname = None # ExprContext

        def While(self):
            return self.getToken(cutiev2Parser.While, 0)

        def Open_Parenthesis(self):
            return self.getToken(cutiev2Parser.Open_Parenthesis, 0)

        def Close_Parenthesis(self):
            return self.getToken(cutiev2Parser.Close_Parenthesis, 0)

        def expr(self):
            return self.getTypedRuleContext(cutiev2Parser.ExprContext,0)


        def Open_Bracket(self):
            return self.getToken(cutiev2Parser.Open_Bracket, 0)

        def block(self):
            return self.getTypedRuleContext(cutiev2Parser.BlockContext,0)


        def Close_Bracket(self):
            return self.getToken(cutiev2Parser.Close_Bracket, 0)

        def getRuleIndex(self):
            return cutiev2Parser.RULE_while_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stat" ):
                listener.enterWhile_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stat" ):
                listener.exitWhile_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stat" ):
                return visitor.visitWhile_stat(self)
            else:
                return visitor.visitChildren(self)




    def while_stat(self):

        localctx = cutiev2Parser.While_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_while_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(cutiev2Parser.While)
            self.state = 67
            self.match(cutiev2Parser.Open_Parenthesis)
            self.state = 68
            localctx.valorname = self.expr(0)
            self.state = 69
            self.match(cutiev2Parser.Close_Parenthesis)

            self.state = 70
            self.match(cutiev2Parser.Open_Bracket)
            self.state = 71
            self.block()
            self.state = 72
            self.match(cutiev2Parser.Close_Bracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cutiev2Parser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class OperatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cutiev2Parser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Operator_sign(self):
            return self.getToken(cutiev2Parser.Operator_sign, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cutiev2Parser.ExprContext)
            else:
                return self.getTypedRuleContext(cutiev2Parser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperat" ):
                listener.enterOperat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperat" ):
                listener.exitOperat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperat" ):
                return visitor.visitOperat(self)
            else:
                return visitor.visitChildren(self)


    class NegateContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cutiev2Parser.ExprContext
            super().__init__(parser)
            self.mid = None # ExprContext
            self.copyFrom(ctx)

        def Operator_sign(self):
            return self.getToken(cutiev2Parser.Operator_sign, 0)
        def expr(self):
            return self.getTypedRuleContext(cutiev2Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegate" ):
                listener.enterNegate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegate" ):
                listener.exitNegate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegate" ):
                return visitor.visitNegate(self)
            else:
                return visitor.visitChildren(self)


    class ParentiseContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cutiev2Parser.ExprContext
            super().__init__(parser)
            self.mid = None # ExprContext
            self.copyFrom(ctx)

        def Open_Parenthesis(self):
            return self.getToken(cutiev2Parser.Open_Parenthesis, 0)
        def Close_Parenthesis(self):
            return self.getToken(cutiev2Parser.Close_Parenthesis, 0)
        def expr(self):
            return self.getTypedRuleContext(cutiev2Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentise" ):
                listener.enterParentise(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentise" ):
                listener.exitParentise(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentise" ):
                return visitor.visitParentise(self)
            else:
                return visitor.visitChildren(self)


    class TerminalContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cutiev2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(cutiev2Parser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerminal" ):
                listener.enterTerminal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerminal" ):
                listener.exitTerminal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminal" ):
                return visitor.visitTerminal(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cutiev2Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = cutiev2Parser.ParentiseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 75
                self.match(cutiev2Parser.Open_Parenthesis)
                self.state = 76
                localctx.mid = self.expr(0)
                self.state = 77
                self.match(cutiev2Parser.Close_Parenthesis)
                pass
            elif token in [19, 20, 22, 23]:
                localctx = cutiev2Parser.TerminalContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 79
                self.term()
                pass
            elif token in [10]:
                localctx = cutiev2Parser.NegateContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 80
                self.match(cutiev2Parser.Operator_sign)
                self.state = 81
                localctx.mid = self.expr(1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = cutiev2Parser.OperatContext(self, cutiev2Parser.ExprContext(self, _parentctx, _parentState))
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 84
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 85
                    self.match(cutiev2Parser.Operator_sign)
                    self.state = 86
                    localctx.right = self.expr(5) 
                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cutiev2Parser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TermNameContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cutiev2Parser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self):
            return self.getToken(cutiev2Parser.NAME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermName" ):
                listener.enterTermName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermName" ):
                listener.exitTermName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermName" ):
                return visitor.visitTermName(self)
            else:
                return visitor.visitChildren(self)


    class TermBoolContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cutiev2Parser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Bool(self):
            return self.getToken(cutiev2Parser.Bool, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermBool" ):
                listener.enterTermBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermBool" ):
                listener.exitTermBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermBool" ):
                return visitor.visitTermBool(self)
            else:
                return visitor.visitChildren(self)


    class TermIntContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cutiev2Parser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Int(self):
            return self.getToken(cutiev2Parser.Int, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermInt" ):
                listener.enterTermInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermInt" ):
                listener.exitTermInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermInt" ):
                return visitor.visitTermInt(self)
            else:
                return visitor.visitChildren(self)


    class TermDoubleContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cutiev2Parser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Double(self):
            return self.getToken(cutiev2Parser.Double, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermDouble" ):
                listener.enterTermDouble(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermDouble" ):
                listener.exitTermDouble(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermDouble" ):
                return visitor.visitTermDouble(self)
            else:
                return visitor.visitChildren(self)



    def term(self):

        localctx = cutiev2Parser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_term)
        try:
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                localctx = cutiev2Parser.TermNameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(cutiev2Parser.NAME)
                pass
            elif token in [19]:
                localctx = cutiev2Parser.TermIntContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.match(cutiev2Parser.Int)
                pass
            elif token in [20]:
                localctx = cutiev2Parser.TermDoubleContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.match(cutiev2Parser.Double)
                pass
            elif token in [22]:
                localctx = cutiev2Parser.TermBoolContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 95
                self.match(cutiev2Parser.Bool)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         





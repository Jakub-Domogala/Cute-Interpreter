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
        4,1,24,98,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,1,1,1,1,1,1,1,1,
        1,3,1,29,8,1,1,2,1,2,1,2,1,2,1,2,3,2,36,8,2,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,4,5,56,8,5,11,
        5,12,5,57,1,5,1,5,1,5,3,5,63,8,5,1,6,1,6,1,6,1,6,1,6,1,6,4,6,71,
        8,6,11,6,12,6,72,1,6,1,6,1,6,3,6,78,8,6,1,7,1,7,1,7,1,7,1,7,1,7,
        3,7,86,8,7,1,7,1,7,1,7,5,7,91,8,7,10,7,12,7,94,9,7,1,8,1,8,1,8,0,
        1,14,9,0,2,4,6,8,10,12,14,16,0,1,2,0,20,21,23,24,100,0,19,1,0,0,
        0,2,28,1,0,0,0,4,30,1,0,0,0,6,39,1,0,0,0,8,44,1,0,0,0,10,49,1,0,
        0,0,12,64,1,0,0,0,14,85,1,0,0,0,16,95,1,0,0,0,18,20,3,2,1,0,19,18,
        1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,1,1,0,0,0,23,
        29,3,4,2,0,24,29,3,6,3,0,25,29,3,8,4,0,26,29,3,10,5,0,27,29,3,12,
        6,0,28,23,1,0,0,0,28,24,1,0,0,0,28,25,1,0,0,0,28,26,1,0,0,0,28,27,
        1,0,0,0,29,3,1,0,0,0,30,31,5,18,0,0,31,32,5,12,0,0,32,35,5,24,0,
        0,33,34,5,13,0,0,34,36,3,14,7,0,35,33,1,0,0,0,35,36,1,0,0,0,36,37,
        1,0,0,0,37,38,5,9,0,0,38,5,1,0,0,0,39,40,5,24,0,0,40,41,5,13,0,0,
        41,42,3,14,7,0,42,43,5,9,0,0,43,7,1,0,0,0,44,45,5,14,0,0,45,46,5,
        1,0,0,46,47,3,16,8,0,47,48,5,2,0,0,48,9,1,0,0,0,49,50,5,15,0,0,50,
        51,5,1,0,0,51,52,3,14,7,0,52,62,5,2,0,0,53,55,5,3,0,0,54,56,3,2,
        1,0,55,54,1,0,0,0,56,57,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,59,
        1,0,0,0,59,60,5,4,0,0,60,63,1,0,0,0,61,63,3,2,1,0,62,53,1,0,0,0,
        62,61,1,0,0,0,63,11,1,0,0,0,64,65,5,16,0,0,65,66,5,1,0,0,66,67,3,
        14,7,0,67,77,5,2,0,0,68,70,5,3,0,0,69,71,3,2,1,0,70,69,1,0,0,0,71,
        72,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,75,5,4,0,
        0,75,78,1,0,0,0,76,78,3,2,1,0,77,68,1,0,0,0,77,76,1,0,0,0,78,13,
        1,0,0,0,79,80,6,7,-1,0,80,81,5,1,0,0,81,82,3,14,7,0,82,83,5,2,0,
        0,83,86,1,0,0,0,84,86,3,16,8,0,85,79,1,0,0,0,85,84,1,0,0,0,86,92,
        1,0,0,0,87,88,10,3,0,0,88,89,5,10,0,0,89,91,3,14,7,4,90,87,1,0,0,
        0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,15,1,0,0,0,94,92,
        1,0,0,0,95,96,7,0,0,0,96,17,1,0,0,0,9,21,28,35,57,62,72,77,85,92
    ]

class cutiev2Parser ( Parser ):

    grammarFileName = "cutiev2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "'.'", "','", "'|<3|'", "<INVALID>", "'nie'", "'->'", 
                     "'<-'", "'drukareczka'", "'waruneczek'", "'powielanko'", 
                     "'zwrocik'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'0'" ]

    symbolicNames = [ "<INVALID>", "Open_Parenthesis", "Close_Parenthesis", 
                      "Open_Bracket", "Close_Bracket", "Open_Square_Bracket", 
                      "Close_Square_Bracket", "Dot", "Comma", "Semicolon", 
                      "Operator_sign", "Not", "Var_define", "Val_assign", 
                      "Print", "If", "While", "Return", "TYPE", "White_Sign", 
                      "Int", "Double", "Number", "Bool", "NAME" ]

    RULE_block = 0
    RULE_stat = 1
    RULE_define_stat = 2
    RULE_assign_stat = 3
    RULE_print_stat = 4
    RULE_if_stat = 5
    RULE_while_stat = 6
    RULE_expr = 7
    RULE_term = 8

    ruleNames =  [ "block", "stat", "define_stat", "assign_stat", "print_stat", 
                   "if_stat", "while_stat", "expr", "term" ]

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
    Not=11
    Var_define=12
    Val_assign=13
    Print=14
    If=15
    While=16
    Return=17
    TYPE=18
    White_Sign=19
    Int=20
    Double=21
    Number=22
    Bool=23
    NAME=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




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
        self.enterRule(localctx, 0, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.stat()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 17154048) != 0):
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
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.define_stat()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.assign_stat()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.print_stat()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.if_stat()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 5)
                self.state = 27
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

        def TYPE(self):
            return self.getToken(cutiev2Parser.TYPE, 0)

        def Var_define(self):
            return self.getToken(cutiev2Parser.Var_define, 0)

        def NAME(self):
            return self.getToken(cutiev2Parser.NAME, 0)

        def Semicolon(self):
            return self.getToken(cutiev2Parser.Semicolon, 0)

        def Val_assign(self):
            return self.getToken(cutiev2Parser.Val_assign, 0)

        def expr(self):
            return self.getTypedRuleContext(cutiev2Parser.ExprContext,0)


        def getRuleIndex(self):
            return cutiev2Parser.RULE_define_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefine_stat" ):
                listener.enterDefine_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefine_stat" ):
                listener.exitDefine_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefine_stat" ):
                return visitor.visitDefine_stat(self)
            else:
                return visitor.visitChildren(self)




    def define_stat(self):

        localctx = cutiev2Parser.Define_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_define_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(cutiev2Parser.TYPE)
            self.state = 31
            self.match(cutiev2Parser.Var_define)
            self.state = 32
            self.match(cutiev2Parser.NAME)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 33
                self.match(cutiev2Parser.Val_assign)
                self.state = 34
                self.expr(0)


            self.state = 37
            self.match(cutiev2Parser.Semicolon)
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

        def NAME(self):
            return self.getToken(cutiev2Parser.NAME, 0)

        def Val_assign(self):
            return self.getToken(cutiev2Parser.Val_assign, 0)

        def expr(self):
            return self.getTypedRuleContext(cutiev2Parser.ExprContext,0)


        def Semicolon(self):
            return self.getToken(cutiev2Parser.Semicolon, 0)

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
        self.enterRule(localctx, 6, self.RULE_assign_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(cutiev2Parser.NAME)
            self.state = 40
            self.match(cutiev2Parser.Val_assign)
            self.state = 41
            self.expr(0)
            self.state = 42
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
        self.enterRule(localctx, 8, self.RULE_print_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(cutiev2Parser.Print)
            self.state = 45
            self.match(cutiev2Parser.Open_Parenthesis)
            self.state = 46
            localctx.valorname = self.term()
            self.state = 47
            self.match(cutiev2Parser.Close_Parenthesis)
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

        def If(self):
            return self.getToken(cutiev2Parser.If, 0)

        def Open_Parenthesis(self):
            return self.getToken(cutiev2Parser.Open_Parenthesis, 0)

        def expr(self):
            return self.getTypedRuleContext(cutiev2Parser.ExprContext,0)


        def Close_Parenthesis(self):
            return self.getToken(cutiev2Parser.Close_Parenthesis, 0)

        def Open_Bracket(self):
            return self.getToken(cutiev2Parser.Open_Bracket, 0)

        def Close_Bracket(self):
            return self.getToken(cutiev2Parser.Close_Bracket, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cutiev2Parser.StatContext)
            else:
                return self.getTypedRuleContext(cutiev2Parser.StatContext,i)


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
        self.enterRule(localctx, 10, self.RULE_if_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(cutiev2Parser.If)
            self.state = 50
            self.match(cutiev2Parser.Open_Parenthesis)
            self.state = 51
            self.expr(0)
            self.state = 52
            self.match(cutiev2Parser.Close_Parenthesis)
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 53
                self.match(cutiev2Parser.Open_Bracket)
                self.state = 55 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 54
                    self.stat()
                    self.state = 57 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 17154048) != 0):
                        break

                self.state = 59
                self.match(cutiev2Parser.Close_Bracket)
                pass
            elif token in [14, 15, 16, 18, 24]:
                self.state = 61
                self.stat()
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


    class While_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def While(self):
            return self.getToken(cutiev2Parser.While, 0)

        def Open_Parenthesis(self):
            return self.getToken(cutiev2Parser.Open_Parenthesis, 0)

        def expr(self):
            return self.getTypedRuleContext(cutiev2Parser.ExprContext,0)


        def Close_Parenthesis(self):
            return self.getToken(cutiev2Parser.Close_Parenthesis, 0)

        def Open_Bracket(self):
            return self.getToken(cutiev2Parser.Open_Bracket, 0)

        def Close_Bracket(self):
            return self.getToken(cutiev2Parser.Close_Bracket, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cutiev2Parser.StatContext)
            else:
                return self.getTypedRuleContext(cutiev2Parser.StatContext,i)


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
        self.enterRule(localctx, 12, self.RULE_while_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(cutiev2Parser.While)
            self.state = 65
            self.match(cutiev2Parser.Open_Parenthesis)
            self.state = 66
            self.expr(0)
            self.state = 67
            self.match(cutiev2Parser.Close_Parenthesis)
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 68
                self.match(cutiev2Parser.Open_Bracket)
                self.state = 70 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 69
                    self.stat()
                    self.state = 72 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 17154048) != 0):
                        break

                self.state = 74
                self.match(cutiev2Parser.Close_Bracket)
                pass
            elif token in [14, 15, 16, 18, 24]:
                self.state = 76
                self.stat()
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
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = cutiev2Parser.ParentiseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 80
                self.match(cutiev2Parser.Open_Parenthesis)
                self.state = 81
                localctx.mid = self.expr(0)
                self.state = 82
                self.match(cutiev2Parser.Close_Parenthesis)
                pass
            elif token in [20, 21, 23, 24]:
                localctx = cutiev2Parser.TerminalContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 84
                self.term()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 92
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = cutiev2Parser.OperatContext(self, cutiev2Parser.ExprContext(self, _parentctx, _parentState))
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 87
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 88
                    self.match(cutiev2Parser.Operator_sign)
                    self.state = 89
                    localctx.right = self.expr(4) 
                self.state = 94
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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

        def NAME(self):
            return self.getToken(cutiev2Parser.NAME, 0)

        def Int(self):
            return self.getToken(cutiev2Parser.Int, 0)

        def Double(self):
            return self.getToken(cutiev2Parser.Double, 0)

        def Bool(self):
            return self.getToken(cutiev2Parser.Bool, 0)

        def getRuleIndex(self):
            return cutiev2Parser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = cutiev2Parser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 28311552) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         





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
        4,1,28,102,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,1,1,1,1,
        1,1,1,1,1,3,1,31,8,1,1,2,1,2,1,2,1,2,1,2,3,2,38,8,2,1,2,1,2,1,3,
        1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,4,5,
        58,8,5,11,5,12,5,59,1,5,1,5,1,5,3,5,65,8,5,1,6,1,6,1,6,1,6,1,6,1,
        6,4,6,73,8,6,11,6,12,6,74,1,6,1,6,1,6,3,6,80,8,6,1,7,1,7,1,7,1,7,
        1,7,1,7,3,7,88,8,7,1,7,1,7,1,7,5,7,93,8,7,10,7,12,7,96,9,7,1,8,1,
        8,1,9,1,9,1,9,0,1,14,10,0,2,4,6,8,10,12,14,16,18,0,2,3,0,5,5,24,
        25,27,27,1,0,1,4,103,0,21,1,0,0,0,2,30,1,0,0,0,4,32,1,0,0,0,6,41,
        1,0,0,0,8,46,1,0,0,0,10,51,1,0,0,0,12,66,1,0,0,0,14,87,1,0,0,0,16,
        97,1,0,0,0,18,99,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,23,1,0,0,
        0,23,21,1,0,0,0,23,24,1,0,0,0,24,1,1,0,0,0,25,31,3,4,2,0,26,31,3,
        6,3,0,27,31,3,8,4,0,28,31,3,10,5,0,29,31,3,12,6,0,30,25,1,0,0,0,
        30,26,1,0,0,0,30,27,1,0,0,0,30,28,1,0,0,0,30,29,1,0,0,0,31,3,1,0,
        0,0,32,33,3,18,9,0,33,34,5,17,0,0,34,37,5,5,0,0,35,36,5,18,0,0,36,
        38,3,14,7,0,37,35,1,0,0,0,37,38,1,0,0,0,38,39,1,0,0,0,39,40,5,14,
        0,0,40,5,1,0,0,0,41,42,5,5,0,0,42,43,5,18,0,0,43,44,3,14,7,0,44,
        45,5,14,0,0,45,7,1,0,0,0,46,47,5,19,0,0,47,48,5,6,0,0,48,49,3,16,
        8,0,49,50,5,7,0,0,50,9,1,0,0,0,51,52,5,20,0,0,52,53,5,6,0,0,53,54,
        3,14,7,0,54,64,5,7,0,0,55,57,5,8,0,0,56,58,3,2,1,0,57,56,1,0,0,0,
        58,59,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,61,1,0,0,0,61,62,5,
        9,0,0,62,65,1,0,0,0,63,65,3,2,1,0,64,55,1,0,0,0,64,63,1,0,0,0,65,
        11,1,0,0,0,66,67,5,21,0,0,67,68,5,6,0,0,68,69,3,14,7,0,69,79,5,7,
        0,0,70,72,5,8,0,0,71,73,3,2,1,0,72,71,1,0,0,0,73,74,1,0,0,0,74,72,
        1,0,0,0,74,75,1,0,0,0,75,76,1,0,0,0,76,77,5,9,0,0,77,80,1,0,0,0,
        78,80,3,2,1,0,79,70,1,0,0,0,79,78,1,0,0,0,80,13,1,0,0,0,81,82,6,
        7,-1,0,82,83,5,6,0,0,83,84,3,14,7,0,84,85,5,7,0,0,85,88,1,0,0,0,
        86,88,3,16,8,0,87,81,1,0,0,0,87,86,1,0,0,0,88,94,1,0,0,0,89,90,10,
        3,0,0,90,91,5,15,0,0,91,93,3,14,7,4,92,89,1,0,0,0,93,96,1,0,0,0,
        94,92,1,0,0,0,94,95,1,0,0,0,95,15,1,0,0,0,96,94,1,0,0,0,97,98,7,
        0,0,0,98,17,1,0,0,0,99,100,7,1,0,0,100,19,1,0,0,0,9,23,30,37,59,
        64,74,79,87,94
    ]

class cutiev2Parser ( Parser ):

    grammarFileName = "cutiev2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'bezprzecinek'", "'zerojedynek'", "'napisik'", 
                     "'zprzecinek'", "<INVALID>", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "'.'", "','", "'|<3|'", "<INVALID>", 
                     "'nie'", "'->'", "'<-'", "'drukareczka'", "'waruneczek'", 
                     "'powielanko'", "'zwrocik'", "<INVALID>", "<INVALID>", 
                     "'0'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "Identifier", "Open_Parenthesis", "Close_Parenthesis", 
                      "Open_Bracket", "Close_Bracket", "Open_Square_Bracket", 
                      "Close_Square_Bracket", "Dot", "Comma", "Semicolon", 
                      "Operator_sign", "Not", "Var_define", "Val_assign", 
                      "Print", "If", "While", "Return", "White_Sign", "Int", 
                      "Double", "Number", "Bool", "NAME" ]

    RULE_block = 0
    RULE_stat = 1
    RULE_define_stat = 2
    RULE_assign_stat = 3
    RULE_print_stat = 4
    RULE_if_stat = 5
    RULE_while_stat = 6
    RULE_expr = 7
    RULE_term = 8
    RULE_type = 9

    ruleNames =  [ "block", "stat", "define_stat", "assign_stat", "print_stat", 
                   "if_stat", "while_stat", "expr", "term", "type" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    Identifier=5
    Open_Parenthesis=6
    Close_Parenthesis=7
    Open_Bracket=8
    Close_Bracket=9
    Open_Square_Bracket=10
    Close_Square_Bracket=11
    Dot=12
    Comma=13
    Semicolon=14
    Operator_sign=15
    Not=16
    Var_define=17
    Val_assign=18
    Print=19
    If=20
    While=21
    Return=22
    White_Sign=23
    Int=24
    Double=25
    Number=26
    Bool=27
    NAME=28

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
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.stat()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 3670078) != 0):
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
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.define_stat()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.assign_stat()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.print_stat()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.if_stat()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 5)
                self.state = 29
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

        def type_(self):
            return self.getTypedRuleContext(cutiev2Parser.TypeContext,0)


        def Var_define(self):
            return self.getToken(cutiev2Parser.Var_define, 0)

        def Identifier(self):
            return self.getToken(cutiev2Parser.Identifier, 0)

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
            self.state = 32
            self.type_()
            self.state = 33
            self.match(cutiev2Parser.Var_define)
            self.state = 34
            self.match(cutiev2Parser.Identifier)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 35
                self.match(cutiev2Parser.Val_assign)
                self.state = 36
                self.expr(0)


            self.state = 39
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

        def Identifier(self):
            return self.getToken(cutiev2Parser.Identifier, 0)

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
            self.state = 41
            self.match(cutiev2Parser.Identifier)
            self.state = 42
            self.match(cutiev2Parser.Val_assign)
            self.state = 43
            self.expr(0)
            self.state = 44
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

        def Print(self):
            return self.getToken(cutiev2Parser.Print, 0)

        def Open_Parenthesis(self):
            return self.getToken(cutiev2Parser.Open_Parenthesis, 0)

        def term(self):
            return self.getTypedRuleContext(cutiev2Parser.TermContext,0)


        def Close_Parenthesis(self):
            return self.getToken(cutiev2Parser.Close_Parenthesis, 0)

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
            self.state = 46
            self.match(cutiev2Parser.Print)
            self.state = 47
            self.match(cutiev2Parser.Open_Parenthesis)
            self.state = 48
            self.term()
            self.state = 49
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
            self.state = 51
            self.match(cutiev2Parser.If)
            self.state = 52
            self.match(cutiev2Parser.Open_Parenthesis)
            self.state = 53
            self.expr(0)
            self.state = 54
            self.match(cutiev2Parser.Close_Parenthesis)
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.state = 55
                self.match(cutiev2Parser.Open_Bracket)
                self.state = 57 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 56
                    self.stat()
                    self.state = 59 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 3670078) != 0):
                        break

                self.state = 61
                self.match(cutiev2Parser.Close_Bracket)
                pass
            elif token in [1, 2, 3, 4, 5, 19, 20, 21]:
                self.state = 63
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
            self.state = 66
            self.match(cutiev2Parser.While)
            self.state = 67
            self.match(cutiev2Parser.Open_Parenthesis)
            self.state = 68
            self.expr(0)
            self.state = 69
            self.match(cutiev2Parser.Close_Parenthesis)
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.state = 70
                self.match(cutiev2Parser.Open_Bracket)
                self.state = 72 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 71
                    self.stat()
                    self.state = 74 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 3670078) != 0):
                        break

                self.state = 76
                self.match(cutiev2Parser.Close_Bracket)
                pass
            elif token in [1, 2, 3, 4, 5, 19, 20, 21]:
                self.state = 78
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

        def Open_Parenthesis(self):
            return self.getToken(cutiev2Parser.Open_Parenthesis, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cutiev2Parser.ExprContext)
            else:
                return self.getTypedRuleContext(cutiev2Parser.ExprContext,i)


        def Close_Parenthesis(self):
            return self.getToken(cutiev2Parser.Close_Parenthesis, 0)

        def term(self):
            return self.getTypedRuleContext(cutiev2Parser.TermContext,0)


        def Operator_sign(self):
            return self.getToken(cutiev2Parser.Operator_sign, 0)

        def getRuleIndex(self):
            return cutiev2Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
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
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 82
                self.match(cutiev2Parser.Open_Parenthesis)
                self.state = 83
                self.expr(0)
                self.state = 84
                self.match(cutiev2Parser.Close_Parenthesis)
                pass
            elif token in [5, 24, 25, 27]:
                self.state = 86
                self.term()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = cutiev2Parser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 89
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 90
                    self.match(cutiev2Parser.Operator_sign)
                    self.state = 91
                    self.expr(4) 
                self.state = 96
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

        def Identifier(self):
            return self.getToken(cutiev2Parser.Identifier, 0)

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
            self.state = 97
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 184549408) != 0):
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


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cutiev2Parser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = cutiev2Parser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0):
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
         





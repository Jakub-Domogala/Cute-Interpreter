// Generated from cutiev2.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class cutiev2Parser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, Open_Parenthesis=3, Close_Parenthesis=4, Open_Bracket=5, 
		Close_Bracket=6, Open_Square_Bracket=7, Close_Square_Bracket=8, Dot=9, 
		Comma=10, Semicolon=11, Operator_sign_equality=12, Operator_sign_comparison=13, 
		Minus=14, Operator_sign_numerical=15, Operator_sign_boolean=16, Operator_sign=17, 
		Not=18, If=19, While=20, Return=21, Def=22, Type=23, White_Sign=24, Int=25, 
		Double=26, Number=27, Bool=28, NAME=29;
	public static final int
		RULE_program = 0, RULE_stat = 1, RULE_define_stat = 2, RULE_assign_stat = 3, 
		RULE_if_stat = 4, RULE_while_stat = 5, RULE_expr = 6, RULE_term = 7, RULE_identifier = 8, 
		RULE_var_define = 9, RULE_val_assign = 10;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "stat", "define_stat", "assign_stat", "if_stat", "while_stat", 
			"expr", "term", "identifier", "var_define", "val_assign"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'->'", "'<-'", "'('", "')'", "'{'", "'}'", "'['", "']'", "'.'", 
			"','", "'|<3|'", null, null, "'-'", null, null, null, "'nie'", "'waruneczek'", 
			"'powielanko'", "'zwrocik'", "'metodka'", null, null, null, "'0'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, "Open_Parenthesis", "Close_Parenthesis", "Open_Bracket", 
			"Close_Bracket", "Open_Square_Bracket", "Close_Square_Bracket", "Dot", 
			"Comma", "Semicolon", "Operator_sign_equality", "Operator_sign_comparison", 
			"Minus", "Operator_sign_numerical", "Operator_sign_boolean", "Operator_sign", 
			"Not", "If", "While", "Return", "Def", "Type", "White_Sign", "Int", "Double", 
			"Number", "Bool", "NAME"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "cutiev2.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public cutiev2Parser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ProgramContext extends ParserRuleContext {
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof cutiev2Listener ) ((cutiev2Listener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof cutiev2Listener ) ((cutiev2Listener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(23); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(22);
				stat();
				}
				}
				setState(25); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << If) | (1L << While) | (1L << Type) | (1L << NAME))) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatContext extends ParserRuleContext {
		public Define_statContext define_stat() {
			return getRuleContext(Define_statContext.class,0);
		}
		public Assign_statContext assign_stat() {
			return getRuleContext(Assign_statContext.class,0);
		}
		public If_statContext if_stat() {
			return getRuleContext(If_statContext.class,0);
		}
		public While_statContext while_stat() {
			return getRuleContext(While_statContext.class,0);
		}
		public StatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof cutiev2Listener ) ((cutiev2Listener)listener).enterStat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof cutiev2Listener ) ((cutiev2Listener)listener).exitStat(this);
		}
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_stat);
		try {
			setState(31);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Type:
				enterOuterAlt(_localctx, 1);
				{
				setState(27);
				define_stat();
				}
				break;
			case NAME:
				enterOuterAlt(_localctx, 2);
				{
				setState(28);
				assign_stat();
				}
				break;
			case If:
				enterOuterAlt(_localctx, 3);
				{
				setState(29);
				if_stat();
				}
				break;
			case While:
				enterOuterAlt(_localctx, 4);
				{
				setState(30);
				while_stat();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Define_statContext extends ParserRuleContext {
		public TerminalNode Type() { return getToken(cutiev2Parser.Type, 0); }
		public Var_defineContext var_define() {
			return getRuleContext(Var_defineContext.class,0);
		}
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode Semicolon() { return getToken(cutiev2Parser.Semicolon, 0); }
		public Val_assignContext val_assign() {
			return getRuleContext(Val_assignContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Define_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_define_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof cutiev2Listener ) ((cutiev2Listener)listener).enterDefine_stat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof cutiev2Listener ) ((cutiev2Listener)listener).exitDefine_stat(this);
		}
	}

	public final Define_statContext define_stat() throws RecognitionException {
		Define_statContext _localctx = new Define_statContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_define_stat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(33);
			match(Type);
			setState(34);
			var_define();
			setState(35);
			identifier();
			setState(39);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(36);
				val_assign();
				setState(37);
				expr(0);
				}
			}

			setState(41);
			match(Semicolon);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assign_statContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public Val_assignContext val_assign() {
			return getRuleContext(Val_assignContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode Semicolon() { return getToken(cutiev2Parser.Semicolon, 0); }
		public Assign_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof cutiev2Listener ) ((cutiev2Listener)listener).enterAssign_stat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof cutiev2Listener ) ((cutiev2Listener)listener).exitAssign_stat(this);
		}
	}

	public final Assign_statContext assign_stat() throws RecognitionException {
		Assign_statContext _localctx = new Assign_statContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_assign_stat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(43);
			identifier();
			setState(44);
			val_assign();
			setState(45);
			expr(0);
			setState(46);
			match(Semicolon);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_statContext extends ParserRuleContext {
		public TerminalNode If() { return getToken(cutiev2Parser.If, 0); }
		public TerminalNode Open_Parenthesis() { return getToken(cutiev2Parser.Open_Parenthesis, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode Close_Parenthesis() { return getToken(cutiev2Parser.Close_Parenthesis, 0); }
		public TerminalNode Open_Bracket() { return getToken(cutiev2Parser.Open_Bracket, 0); }
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public TerminalNode Close_Bracket() { return getToken(cutiev2Parser.Close_Bracket, 0); }
		public If_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof cutiev2Listener ) ((cutiev2Listener)listener).enterIf_stat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof cutiev2Listener ) ((cutiev2Listener)listener).exitIf_stat(this);
		}
	}

	public final If_statContext if_stat() throws RecognitionException {
		If_statContext _localctx = new If_statContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_if_stat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			match(If);
			setState(49);
			match(Open_Parenthesis);
			setState(50);
			expr(0);
			setState(51);
			match(Close_Parenthesis);
			setState(57);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Open_Bracket:
				{
				setState(52);
				match(Open_Bracket);
				setState(53);
				stat();
				setState(54);
				match(Close_Bracket);
				}
				break;
			case If:
			case While:
			case Type:
			case NAME:
				{
				setState(56);
				stat();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class While_statContext extends ParserRuleContext {
		public TerminalNode While() { return getToken(cutiev2Parser.While, 0); }
		public TerminalNode Open_Parenthesis() { return getToken(cutiev2Parser.Open_Parenthesis, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode Close_Parenthesis() { return getToken(cutiev2Parser.Close_Parenthesis, 0); }
		public TerminalNode Open_Bracket() { return getToken(cutiev2Parser.Open_Bracket, 0); }
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public TerminalNode Close_Bracket() { return getToken(cutiev2Parser.Close_Bracket, 0); }
		public While_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof cutiev2Listener ) ((cutiev2Listener)listener).enterWhile_stat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof cutiev2Listener ) ((cutiev2Listener)listener).exitWhile_stat(this);
		}
	}

	public final While_statContext while_stat() throws RecognitionException {
		While_statContext _localctx = new While_statContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_while_stat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			match(While);
			setState(60);
			match(Open_Parenthesis);
			setState(61);
			expr(0);
			setState(62);
			match(Close_Parenthesis);
			setState(68);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Open_Bracket:
				{
				setState(63);
				match(Open_Bracket);
				setState(64);
				stat();
				setState(65);
				match(Close_Bracket);
				}
				break;
			case If:
			case While:
			case Type:
			case NAME:
				{
				setState(67);
				stat();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> Minus() { return getTokens(cutiev2Parser.Minus); }
		public TerminalNode Minus(int i) {
			return getToken(cutiev2Parser.Minus, i);
		}
		public List<TerminalNode> Not() { return getTokens(cutiev2Parser.Not); }
		public TerminalNode Not(int i) {
			return getToken(cutiev2Parser.Not, i);
		}
		public TerminalNode Open_Parenthesis() { return getToken(cutiev2Parser.Open_Parenthesis, 0); }
		public TerminalNode Close_Parenthesis() { return getToken(cutiev2Parser.Close_Parenthesis, 0); }
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public TerminalNode Operator_sign() { return getToken(cutiev2Parser.Operator_sign, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof cutiev2Listener ) ((cutiev2Listener)listener).enterExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof cutiev2Listener ) ((cutiev2Listener)listener).exitExpr(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 12;
		enterRecursionRule(_localctx, 12, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Minus:
				{
				setState(72); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(71);
						match(Minus);
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(74); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				setState(76);
				expr(4);
				}
				break;
			case Not:
				{
				setState(78); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(77);
						match(Not);
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(80); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				setState(82);
				expr(3);
				}
				break;
			case Open_Parenthesis:
				{
				setState(83);
				match(Open_Parenthesis);
				setState(84);
				expr(0);
				setState(85);
				match(Close_Parenthesis);
				}
				break;
			case Int:
			case Double:
			case Bool:
			case NAME:
				{
				setState(87);
				term();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(95);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr);
					setState(90);
					if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
					setState(91);
					match(Operator_sign);
					setState(92);
					expr(6);
					}
					} 
				}
				setState(97);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class TermContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode Int() { return getToken(cutiev2Parser.Int, 0); }
		public TerminalNode Double() { return getToken(cutiev2Parser.Double, 0); }
		public TerminalNode Bool() { return getToken(cutiev2Parser.Bool, 0); }
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof cutiev2Listener ) ((cutiev2Listener)listener).enterTerm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof cutiev2Listener ) ((cutiev2Listener)listener).exitTerm(this);
		}
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_term);
		try {
			setState(102);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NAME:
				enterOuterAlt(_localctx, 1);
				{
				setState(98);
				identifier();
				}
				break;
			case Int:
				enterOuterAlt(_localctx, 2);
				{
				setState(99);
				match(Int);
				}
				break;
			case Double:
				enterOuterAlt(_localctx, 3);
				{
				setState(100);
				match(Double);
				}
				break;
			case Bool:
				enterOuterAlt(_localctx, 4);
				{
				setState(101);
				match(Bool);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdentifierContext extends ParserRuleContext {
		public TerminalNode NAME() { return getToken(cutiev2Parser.NAME, 0); }
		public IdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifier; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof cutiev2Listener ) ((cutiev2Listener)listener).enterIdentifier(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof cutiev2Listener ) ((cutiev2Listener)listener).exitIdentifier(this);
		}
	}

	public final IdentifierContext identifier() throws RecognitionException {
		IdentifierContext _localctx = new IdentifierContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_identifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			match(NAME);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_defineContext extends ParserRuleContext {
		public Var_defineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_define; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof cutiev2Listener ) ((cutiev2Listener)listener).enterVar_define(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof cutiev2Listener ) ((cutiev2Listener)listener).exitVar_define(this);
		}
	}

	public final Var_defineContext var_define() throws RecognitionException {
		Var_defineContext _localctx = new Var_defineContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_var_define);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Val_assignContext extends ParserRuleContext {
		public Val_assignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_val_assign; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof cutiev2Listener ) ((cutiev2Listener)listener).enterVal_assign(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof cutiev2Listener ) ((cutiev2Listener)listener).exitVal_assign(this);
		}
	}

	public final Val_assignContext val_assign() throws RecognitionException {
		Val_assignContext _localctx = new Val_assignContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_val_assign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 6:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\37q\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4"+
		"\f\t\f\3\2\6\2\32\n\2\r\2\16\2\33\3\3\3\3\3\3\3\3\5\3\"\n\3\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\5\4*\n\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\5\6<\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7G\n"+
		"\7\3\b\3\b\6\bK\n\b\r\b\16\bL\3\b\3\b\6\bQ\n\b\r\b\16\bR\3\b\3\b\3\b\3"+
		"\b\3\b\3\b\5\b[\n\b\3\b\3\b\3\b\7\b`\n\b\f\b\16\bc\13\b\3\t\3\t\3\t\3"+
		"\t\5\ti\n\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\2\3\16\r\2\4\6\b\n\f\16\20\22"+
		"\24\26\2\2\2u\2\31\3\2\2\2\4!\3\2\2\2\6#\3\2\2\2\b-\3\2\2\2\n\62\3\2\2"+
		"\2\f=\3\2\2\2\16Z\3\2\2\2\20h\3\2\2\2\22j\3\2\2\2\24l\3\2\2\2\26n\3\2"+
		"\2\2\30\32\5\4\3\2\31\30\3\2\2\2\32\33\3\2\2\2\33\31\3\2\2\2\33\34\3\2"+
		"\2\2\34\3\3\2\2\2\35\"\5\6\4\2\36\"\5\b\5\2\37\"\5\n\6\2 \"\5\f\7\2!\35"+
		"\3\2\2\2!\36\3\2\2\2!\37\3\2\2\2! \3\2\2\2\"\5\3\2\2\2#$\7\31\2\2$%\5"+
		"\24\13\2%)\5\22\n\2&\'\5\26\f\2\'(\5\16\b\2(*\3\2\2\2)&\3\2\2\2)*\3\2"+
		"\2\2*+\3\2\2\2+,\7\r\2\2,\7\3\2\2\2-.\5\22\n\2./\5\26\f\2/\60\5\16\b\2"+
		"\60\61\7\r\2\2\61\t\3\2\2\2\62\63\7\25\2\2\63\64\7\5\2\2\64\65\5\16\b"+
		"\2\65;\7\6\2\2\66\67\7\7\2\2\678\5\4\3\289\7\b\2\29<\3\2\2\2:<\5\4\3\2"+
		";\66\3\2\2\2;:\3\2\2\2<\13\3\2\2\2=>\7\26\2\2>?\7\5\2\2?@\5\16\b\2@F\7"+
		"\6\2\2AB\7\7\2\2BC\5\4\3\2CD\7\b\2\2DG\3\2\2\2EG\5\4\3\2FA\3\2\2\2FE\3"+
		"\2\2\2G\r\3\2\2\2HJ\b\b\1\2IK\7\20\2\2JI\3\2\2\2KL\3\2\2\2LJ\3\2\2\2L"+
		"M\3\2\2\2MN\3\2\2\2N[\5\16\b\6OQ\7\24\2\2PO\3\2\2\2QR\3\2\2\2RP\3\2\2"+
		"\2RS\3\2\2\2ST\3\2\2\2T[\5\16\b\5UV\7\5\2\2VW\5\16\b\2WX\7\6\2\2X[\3\2"+
		"\2\2Y[\5\20\t\2ZH\3\2\2\2ZP\3\2\2\2ZU\3\2\2\2ZY\3\2\2\2[a\3\2\2\2\\]\f"+
		"\7\2\2]^\7\23\2\2^`\5\16\b\b_\\\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2"+
		"b\17\3\2\2\2ca\3\2\2\2di\5\22\n\2ei\7\33\2\2fi\7\34\2\2gi\7\36\2\2hd\3"+
		"\2\2\2he\3\2\2\2hf\3\2\2\2hg\3\2\2\2i\21\3\2\2\2jk\7\37\2\2k\23\3\2\2"+
		"\2lm\7\3\2\2m\25\3\2\2\2no\7\4\2\2o\27\3\2\2\2\f\33!);FLRZah";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
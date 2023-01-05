// Generated from cutiev2.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class cutiev2Lexer extends Lexer {
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
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "Open_Parenthesis", "Close_Parenthesis", "Open_Bracket", 
			"Close_Bracket", "Open_Square_Bracket", "Close_Square_Bracket", "Dot", 
			"Comma", "Semicolon", "Equals", "UnEquals", "Operator_sign_equality", 
			"Lesser", "Greater", "Operator_sign_comparison", "Plus", "Minus", "Multiplication", 
			"Division", "Operator_sign_numerical", "And", "Or", "Operator_sign_boolean", 
			"Operator_sign", "Not", "If", "While", "Return", "Def", "Type", "White_Sign", 
			"Int", "Double", "Number", "Bool", "NAME"
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


	public cutiev2Lexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "cutiev2.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\37\u0135\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\3\2\3\2\3\2\3\3\3\3\3"+
		"\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3"+
		"\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r"+
		"\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\5\17\u0082\n\17\3\20"+
		"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21"+
		"\3\21\3\21\3\22\3\22\3\22\5\22\u0098\n\22\3\23\3\23\3\24\3\24\3\25\3\25"+
		"\3\26\3\26\3\27\3\27\3\27\3\27\5\27\u00a6\n\27\3\30\3\30\3\30\3\30\3\30"+
		"\3\31\3\31\3\31\3\31\3\32\3\32\5\32\u00b3\n\32\3\33\3\33\3\33\3\33\5\33"+
		"\u00b9\n\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35"+
		"\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36"+
		"\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3!\3"+
		"!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3"+
		"!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u010d\n!\3\"\6\"\u0110"+
		"\n\"\r\"\16\"\u0111\3\"\3\"\3#\5#\u0117\n#\3#\3#\7#\u011b\n#\f#\16#\u011e"+
		"\13#\3$\3$\3%\3%\5%\u0124\n%\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u012f\n&\3"+
		"\'\6\'\u0132\n\'\r\'\16\'\u0133\2\2(\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21"+
		"\n\23\13\25\f\27\r\31\2\33\2\35\16\37\2!\2#\17%\2\'\20)\2+\2-\21/\2\61"+
		"\2\63\22\65\23\67\249\25;\26=\27?\30A\31C\32E\33G\34I\35K\36M\37\3\2\5"+
		"\5\2\13\f\17\17\"\"\3\2\62;\3\2c|\2\u013e\2\3\3\2\2\2\2\5\3\2\2\2\2\7"+
		"\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2"+
		"\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\35\3\2\2\2\2#\3\2\2\2\2\'"+
		"\3\2\2\2\2-\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2"+
		"\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G"+
		"\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\3O\3\2\2\2\5R\3\2\2\2\7U\3\2"+
		"\2\2\tW\3\2\2\2\13Y\3\2\2\2\r[\3\2\2\2\17]\3\2\2\2\21_\3\2\2\2\23a\3\2"+
		"\2\2\25c\3\2\2\2\27e\3\2\2\2\31j\3\2\2\2\33x\3\2\2\2\35\u0081\3\2\2\2"+
		"\37\u0083\3\2\2\2!\u008c\3\2\2\2#\u0097\3\2\2\2%\u0099\3\2\2\2\'\u009b"+
		"\3\2\2\2)\u009d\3\2\2\2+\u009f\3\2\2\2-\u00a5\3\2\2\2/\u00a7\3\2\2\2\61"+
		"\u00ac\3\2\2\2\63\u00b2\3\2\2\2\65\u00b8\3\2\2\2\67\u00ba\3\2\2\29\u00be"+
		"\3\2\2\2;\u00c9\3\2\2\2=\u00d4\3\2\2\2?\u00dc\3\2\2\2A\u010c\3\2\2\2C"+
		"\u010f\3\2\2\2E\u0116\3\2\2\2G\u011f\3\2\2\2I\u0123\3\2\2\2K\u012e\3\2"+
		"\2\2M\u0131\3\2\2\2OP\7/\2\2PQ\7@\2\2Q\4\3\2\2\2RS\7>\2\2ST\7/\2\2T\6"+
		"\3\2\2\2UV\7*\2\2V\b\3\2\2\2WX\7+\2\2X\n\3\2\2\2YZ\7}\2\2Z\f\3\2\2\2["+
		"\\\7\177\2\2\\\16\3\2\2\2]^\7]\2\2^\20\3\2\2\2_`\7_\2\2`\22\3\2\2\2ab"+
		"\7\60\2\2b\24\3\2\2\2cd\7.\2\2d\26\3\2\2\2ef\7~\2\2fg\7>\2\2gh\7\65\2"+
		"\2hi\7~\2\2i\30\3\2\2\2jk\7m\2\2kl\7t\2\2lm\7q\2\2mn\7r\2\2no\7m\2\2o"+
		"p\7c\2\2pq\7y\2\2qr\7m\2\2rs\7t\2\2st\7q\2\2tu\7r\2\2uv\7m\2\2vw\7g\2"+
		"\2w\32\3\2\2\2xy\7k\2\2yz\7p\2\2z{\7p\2\2{|\7{\2\2|}\7q\2\2}~\7f\2\2~"+
		"\34\3\2\2\2\177\u0082\5\31\r\2\u0080\u0082\5\33\16\2\u0081\177\3\2\2\2"+
		"\u0081\u0080\3\2\2\2\u0082\36\3\2\2\2\u0083\u0084\7o\2\2\u0084\u0085\7"+
		"p\2\2\u0085\u0086\7k\2\2\u0086\u0087\7g\2\2\u0087\u0088\7l\2\2\u0088\u0089"+
		"\7u\2\2\u0089\u008a\7|\2\2\u008a\u008b\7{\2\2\u008b \3\2\2\2\u008c\u008d"+
		"\7y\2\2\u008d\u008e\7k\2\2\u008e\u008f\7g\2\2\u008f\u0090\7m\2\2\u0090"+
		"\u0091\7u\2\2\u0091\u0092\7|\2\2\u0092\u0093\7{\2\2\u0093\"\3\2\2\2\u0094"+
		"\u0098\5\37\20\2\u0095\u0098\5!\21\2\u0096\u0098\5\35\17\2\u0097\u0094"+
		"\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0096\3\2\2\2\u0098$\3\2\2\2\u0099"+
		"\u009a\7-\2\2\u009a&\3\2\2\2\u009b\u009c\7/\2\2\u009c(\3\2\2\2\u009d\u009e"+
		"\7,\2\2\u009e*\3\2\2\2\u009f\u00a0\7\61\2\2\u00a0,\3\2\2\2\u00a1\u00a6"+
		"\5%\23\2\u00a2\u00a6\5\'\24\2\u00a3\u00a6\5)\25\2\u00a4\u00a6\5+\26\2"+
		"\u00a5\u00a1\3\2\2\2\u00a5\u00a2\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a4"+
		"\3\2\2\2\u00a6.\3\2\2\2\u00a7\u00a8\7q\2\2\u00a8\u00a9\7t\2\2\u00a9\u00aa"+
		"\7c\2\2\u00aa\u00ab\7|\2\2\u00ab\60\3\2\2\2\u00ac\u00ad\7n\2\2\u00ad\u00ae"+
		"\7w\2\2\u00ae\u00af\7d\2\2\u00af\62\3\2\2\2\u00b0\u00b3\5/\30\2\u00b1"+
		"\u00b3\5\61\31\2\u00b2\u00b0\3\2\2\2\u00b2\u00b1\3\2\2\2\u00b3\64\3\2"+
		"\2\2\u00b4\u00b9\5\63\32\2\u00b5\u00b9\5#\22\2\u00b6\u00b9\5\35\17\2\u00b7"+
		"\u00b9\5-\27\2\u00b8\u00b4\3\2\2\2\u00b8\u00b5\3\2\2\2\u00b8\u00b6\3\2"+
		"\2\2\u00b8\u00b7\3\2\2\2\u00b9\66\3\2\2\2\u00ba\u00bb\7p\2\2\u00bb\u00bc"+
		"\7k\2\2\u00bc\u00bd\7g\2\2\u00bd8\3\2\2\2\u00be\u00bf\7y\2\2\u00bf\u00c0"+
		"\7c\2\2\u00c0\u00c1\7t\2\2\u00c1\u00c2\7w\2\2\u00c2\u00c3\7p\2\2\u00c3"+
		"\u00c4\7g\2\2\u00c4\u00c5\7e\2\2\u00c5\u00c6\7|\2\2\u00c6\u00c7\7g\2\2"+
		"\u00c7\u00c8\7m\2\2\u00c8:\3\2\2\2\u00c9\u00ca\7r\2\2\u00ca\u00cb\7q\2"+
		"\2\u00cb\u00cc\7y\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce\7g\2\2\u00ce\u00cf"+
		"\7n\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2\7m\2\2\u00d2"+
		"\u00d3\7q\2\2\u00d3<\3\2\2\2\u00d4\u00d5\7|\2\2\u00d5\u00d6\7y\2\2\u00d6"+
		"\u00d7\7t\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9\7e\2\2\u00d9\u00da\7k\2\2"+
		"\u00da\u00db\7m\2\2\u00db>\3\2\2\2\u00dc\u00dd\7o\2\2\u00dd\u00de\7g\2"+
		"\2\u00de\u00df\7v\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1\7f\2\2\u00e1\u00e2"+
		"\7m\2\2\u00e2\u00e3\7c\2\2\u00e3@\3\2\2\2\u00e4\u00e5\7d\2\2\u00e5\u00e6"+
		"\7g\2\2\u00e6\u00e7\7|\2\2\u00e7\u00e8\7r\2\2\u00e8\u00e9\7t\2\2\u00e9"+
		"\u00ea\7|\2\2\u00ea\u00eb\7g\2\2\u00eb\u00ec\7e\2\2\u00ec\u00ed\7k\2\2"+
		"\u00ed\u00ee\7p\2\2\u00ee\u00ef\7g\2\2\u00ef\u010d\7m\2\2\u00f0\u00f1"+
		"\7|\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3\7t\2\2\u00f3\u00f4\7q\2\2\u00f4"+
		"\u00f5\7l\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7\7f\2\2\u00f7\u00f8\7{\2\2"+
		"\u00f8\u00f9\7p\2\2\u00f9\u00fa\7g\2\2\u00fa\u010d\7m\2\2\u00fb\u00fc"+
		"\7p\2\2\u00fc\u00fd\7c\2\2\u00fd\u00fe\7r\2\2\u00fe\u00ff\7k\2\2\u00ff"+
		"\u0100\7u\2\2\u0100\u0101\7k\2\2\u0101\u010d\7m\2\2\u0102\u0103\7|\2\2"+
		"\u0103\u0104\7r\2\2\u0104\u0105\7t\2\2\u0105\u0106\7|\2\2\u0106\u0107"+
		"\7g\2\2\u0107\u0108\7e\2\2\u0108\u0109\7k\2\2\u0109\u010a\7p\2\2\u010a"+
		"\u010b\7g\2\2\u010b\u010d\7m\2\2\u010c\u00e4\3\2\2\2\u010c\u00f0\3\2\2"+
		"\2\u010c\u00fb\3\2\2\2\u010c\u0102\3\2\2\2\u010dB\3\2\2\2\u010e\u0110"+
		"\t\2\2\2\u010f\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u010f\3\2\2\2\u0111"+
		"\u0112\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0114\b\"\2\2\u0114D\3\2\2\2"+
		"\u0115\u0117\7/\2\2\u0116\u0115\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118"+
		"\3\2\2\2\u0118\u011c\t\3\2\2\u0119\u011b\t\3\2\2\u011a\u0119\3\2\2\2\u011b"+
		"\u011e\3\2\2\2\u011c\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011dF\3\2\2\2"+
		"\u011e\u011c\3\2\2\2\u011f\u0120\7\62\2\2\u0120H\3\2\2\2\u0121\u0124\5"+
		"E#\2\u0122\u0124\5G$\2\u0123\u0121\3\2\2\2\u0123\u0122\3\2\2\2\u0124J"+
		"\3\2\2\2\u0125\u0126\7H\2\2\u0126\u0127\7c\2\2\u0127\u0128\7n\2\2\u0128"+
		"\u0129\7u\2\2\u0129\u012f\7g\2\2\u012a\u012b\7V\2\2\u012b\u012c\7t\2\2"+
		"\u012c\u012d\7w\2\2\u012d\u012f\7g\2\2\u012e\u0125\3\2\2\2\u012e\u012a"+
		"\3\2\2\2\u012fL\3\2\2\2\u0130\u0132\t\4\2\2\u0131\u0130\3\2\2\2\u0132"+
		"\u0133\3\2\2\2\u0133\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134N\3\2\2\2"+
		"\17\2\u0081\u0097\u00a5\u00b2\u00b8\u010c\u0111\u0116\u011c\u0123\u012e"+
		"\u0133\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
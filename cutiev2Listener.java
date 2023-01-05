// Generated from cutiev2.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link cutiev2Parser}.
 */
public interface cutiev2Listener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link cutiev2Parser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(cutiev2Parser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link cutiev2Parser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(cutiev2Parser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link cutiev2Parser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStat(cutiev2Parser.StatContext ctx);
	/**
	 * Exit a parse tree produced by {@link cutiev2Parser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStat(cutiev2Parser.StatContext ctx);
	/**
	 * Enter a parse tree produced by {@link cutiev2Parser#define_stat}.
	 * @param ctx the parse tree
	 */
	void enterDefine_stat(cutiev2Parser.Define_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link cutiev2Parser#define_stat}.
	 * @param ctx the parse tree
	 */
	void exitDefine_stat(cutiev2Parser.Define_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link cutiev2Parser#assign_stat}.
	 * @param ctx the parse tree
	 */
	void enterAssign_stat(cutiev2Parser.Assign_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link cutiev2Parser#assign_stat}.
	 * @param ctx the parse tree
	 */
	void exitAssign_stat(cutiev2Parser.Assign_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link cutiev2Parser#if_stat}.
	 * @param ctx the parse tree
	 */
	void enterIf_stat(cutiev2Parser.If_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link cutiev2Parser#if_stat}.
	 * @param ctx the parse tree
	 */
	void exitIf_stat(cutiev2Parser.If_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link cutiev2Parser#while_stat}.
	 * @param ctx the parse tree
	 */
	void enterWhile_stat(cutiev2Parser.While_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link cutiev2Parser#while_stat}.
	 * @param ctx the parse tree
	 */
	void exitWhile_stat(cutiev2Parser.While_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link cutiev2Parser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(cutiev2Parser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link cutiev2Parser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(cutiev2Parser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link cutiev2Parser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(cutiev2Parser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link cutiev2Parser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(cutiev2Parser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link cutiev2Parser#identifier}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(cutiev2Parser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link cutiev2Parser#identifier}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(cutiev2Parser.IdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link cutiev2Parser#var_define}.
	 * @param ctx the parse tree
	 */
	void enterVar_define(cutiev2Parser.Var_defineContext ctx);
	/**
	 * Exit a parse tree produced by {@link cutiev2Parser#var_define}.
	 * @param ctx the parse tree
	 */
	void exitVar_define(cutiev2Parser.Var_defineContext ctx);
	/**
	 * Enter a parse tree produced by {@link cutiev2Parser#val_assign}.
	 * @param ctx the parse tree
	 */
	void enterVal_assign(cutiev2Parser.Val_assignContext ctx);
	/**
	 * Exit a parse tree produced by {@link cutiev2Parser#val_assign}.
	 * @param ctx the parse tree
	 */
	void exitVal_assign(cutiev2Parser.Val_assignContext ctx);
}
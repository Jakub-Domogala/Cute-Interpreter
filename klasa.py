

# from cutiev2Listener import cutiev2Listener
# from cutiev2Parser import cutiev2Parser


# class klasa(cutiev2Listener):

# # Enter a parse tree produced by cutiev2Parser#block.
#     def enterBlock(self, ctx:cutiev2Parser.BlockContext):
#         print("enterBlock")

#     # Exit a parse tree produced by cutiev2Parser#block.
#     def exitBlock(self, ctx:cutiev2Parser.BlockContext):
#         print("exitBlock")


#     # Enter a parse tree produced by cutiev2Parser#stat.
#     def enterStat(self, ctx:cutiev2Parser.StatContext):
#         # print("-------------------")
#         # print(cutiev2Parser.StatContext.define_stat(ctx))
#         # print(cutiev2Parser.StatContext.assign_stat(ctx))
#         # print(cutiev2Parser.StatContext.print_stat(ctx))
#         # print(cutiev2Parser.StatContext.if_stat(ctx))
#         # print(cutiev2Parser.StatContext.while_stat(ctx))
#         # print(cutiev2Parser.StatContext.getRuleIndex(ctx))
#         # print(cutiev2Parser.Define_statContext.TYPE(ctx))
#         # print("-------------------")
#         print("enterStat")

#     # Exit a parse tree produced by cutiev2Parser#stat.
#     def exitStat(self, ctx:cutiev2Parser.StatContext):
#         print("exitStat")


#     # Enter a parse tree produced by cutiev2Parser#define_stat.
#     def enterDefine_stat(self, ctx:cutiev2Parser.Define_statContext):
#         print("enterDefine_stat")
#         print('==============')
#         print(cutiev2Parser.Define_statContext.TYPE(ctx))
#         print(cutiev2Parser.Define_statContext.Var_define(ctx))
#         print(cutiev2Parser.Define_statContext.NAME(ctx))
#         print(cutiev2Parser.Define_statContext.Semicolon(ctx))
#         print(cutiev2Parser.Define_statContext.Val_assign(ctx))
#         print(cutiev2Parser.Define_statContext.expr(ctx))
#         print(cutiev2Parser.Define_statContext.getRuleIndex(ctx))
#         print('==============')

#     # Exit a parse tree produced by cutiev2Parser#define_stat.
#     def exitDefine_stat(self, ctx:cutiev2Parser.Define_statContext):
#         print("exitDefine_stat")


#     # Enter a parse tree produced by cutiev2Parser#assign_stat.
#     def enterAssign_stat(self, ctx:cutiev2Parser.Assign_statContext):
#         print("enterAssign_stat")

#     # Exit a parse tree produced by cutiev2Parser#assign_stat.
#     def exitAssign_stat(self, ctx:cutiev2Parser.Assign_statContext):
#         print("exitAssign_stat")


#     # Enter a parse tree produced by cutiev2Parser#print_stat.
#     def enterPrint_stat(self, ctx:cutiev2Parser.Print_statContext):
#         print("enterPrint_stat")

#     # Exit a parse tree produced by cutiev2Parser#print_stat.
#     def exitPrint_stat(self, ctx:cutiev2Parser.Print_statContext):
#         print("exitPrint_stat")


#     # Enter a parse tree produced by cutiev2Parser#if_stat.
#     def enterIf_stat(self, ctx:cutiev2Parser.If_statContext):
#         print("enterIf_stat")

#     # Exit a parse tree produced by cutiev2Parser#if_stat.
#     def exitIf_stat(self, ctx:cutiev2Parser.If_statContext):
#         print("exitIf_stat")


#     # Enter a parse tree produced by cutiev2Parser#while_stat.
#     def enterWhile_stat(self, ctx:cutiev2Parser.While_statContext):
#         print("enterWhile_stat")

#     # Exit a parse tree produced by cutiev2Parser#while_stat.
#     def exitWhile_stat(self, ctx:cutiev2Parser.While_statContext):
#         print("exitWhile_stat")


#     # Enter a parse tree produced by cutiev2Parser#expr.
#     def enterExpr(self, ctx:cutiev2Parser.ExprContext):
#         print("enterExpr")
#         print(cutiev2Parser.ExprContext.Operator_sign(ctx))

#     # Exit a parse tree produced by cutiev2Parser#expr.
#     def exitExpr(self, ctx:cutiev2Parser.ExprContext):
#         # if (cutiev2Parser.ExprContext.Operator_sign(ctx)):
#             # print(ctx.children[0],  cutiev2Parser.ExprContext.Operator_sign(ctx), ctx.children[2])
#         # exlif ( OpenBrackets)
#         #         return result, type
#         # else ()
#         #     return term.value, type
#         print("exitExpr")


#     # Enter a parse tree produced by cutiev2Parser#term.
#     def enterTerm(self, ctx:cutiev2Parser.TermContext):
#         print("enterTerm")
#         print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
#         print(cutiev2Parser.TermContext.NAME(ctx), "NAME")
#         print(cutiev2Parser.TermContext.Int(ctx), "Int")
#         print(cutiev2Parser.TermContext.Double(ctx), "Double")
#         print(cutiev2Parser.TermContext.Bool(ctx), "Bool")
#         print(cutiev2Parser.TermContext.getRuleIndex(ctx), "getRuleIndex")
#         print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

#     # Exit a parse tree produced by cutiev2Parser#term.
#     def exitTerm(self, ctx:cutiev2Parser.TermContext):
#         print("exitTerm")
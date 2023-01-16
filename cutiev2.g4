grammar cutiev2;

/*
 * Parser Rules
 */

program                   : block;

block                     : (stat)+;

// All Statements
stat                        : define_stat
                            | assign_stat
                            | print_stat
                            | if_stat
                            | while_stat;
                            

// Create new Variable statement
define_stat                 : TYPE Var_define NAME Semicolon                      #defonly
                            | TYPE Var_define NAME Val_assign value=expr Semicolon   #defandasign
                            ;

// Assign value to Variable
assign_stat                 : NAME Val_assign value=expr Semicolon;

// Print variable or sth
print_stat                  : Print Open_Parenthesis valorname=term Close_Parenthesis Semicolon;

// If statement
if_stat                     : If Open_Parenthesis valorname=expr Close_Parenthesis (Open_Bracket block Close_Bracket);

// While statement
while_stat                  : While Open_Parenthesis valorname=expr Close_Parenthesis (Open_Bracket block Close_Bracket);

// All expressions
expr                        : left=expr Operator_sign right=expr            # operat
                            | Open_Parenthesis mid=expr Close_Parenthesis   # parentise
                            | term                                          # terminal
                            | Operator_sign mid=expr                        # negate
                            ;

// All terms ( identifiers and s )
term                        : NAME      #TermName
                            | Int       #TermInt
                            | Double    #TermDouble
                            | Bool      #TermBool
                            ;

// atom                        : id | Int | Double | Bool;

/*
 * Lexer Rules
 */

Open_Parenthesis            : '(';
Close_Parenthesis           : ')';

Open_Bracket                : '{';
Close_Bracket               : '}';

Open_Square_Bracket         : '[';
Close_Square_Bracket        : ']';

Dot                         : '.';
Comma                       : ',';
Semicolon                   : '|<3|';

fragment Equals             : 'kropkawkropke';
fragment UnEquals           : 'innyod';
fragment Operator_sign_equality      : Equals | UnEquals;

fragment Lesser             : 'mniejszyod';
fragment Greater            : 'wiekszyod';
fragment Operator_sign_comparison    : Lesser | Greater | Operator_sign_equality;

fragment Plus               : '+';
fragment Minus              : '-';
fragment Multiplication     : '*';
fragment Division           : '/';
fragment Modulo             : '%';
fragment FloorDivision      : '|/|';
fragment Max                : '|^|';
fragment Min                : '|v|';
fragment Power              : '|*|';
fragment Operator_sign_numerical      : Plus 
                                      | Minus 
                                      | Multiplication 
                                      | Division
                                      | Modulo
                                      | FloorDivision
                                      | Max
                                      | Min
                                      | Power
                                      ;

fragment And                : 'oraz';
fragment Or                 : 'lub';
fragment Not                : 'nie';

fragment Operator_sign_boolean       : And | Or | Not;

Operator_sign               : Operator_sign_boolean
                            | Operator_sign_comparison
                            | Operator_sign_equality
                            | Operator_sign_numerical;

Method_sign                 : 'metodka';

Return                      : 'zwrocik';



Var_define                  : '->'; // def

Val_assign                  : '<-'; // asignVal

Print                       : 'drukareczka';

If                          : 'waruneczek';

While                       : 'powielanko';

TYPE                      : 'bezprzecinek'
                          | 'zerojedynek'
                          | 'napisik'
                          | 'zprzecinek';
White_Sign                  : 
                          ( ' ' 
                          | '\n' 
                          | '\r' 
                          | '\t'
                          )+ -> skip
                            ;

Int                         : (Minus)?[1-9][0-9]+ 
                            | (Minus)?[0-9];

Double                      : (Minus)?[1-9][0-9]+Dot[0-9]*
                            | (Minus)?[0-9]Dot[0-9]*;

Number                      : 
                            Int 
                          | Double
                            ;

Bool                        : 
                            'nieprawda'
                          | 'prawda'
                            ;

NAME                        : [a-zA-Z][a-zA-Z0-9_-_]* ;

COMMENT
    :   '|<3|' ~[\r\n]* -> skip
    ;
// TODO
// We forgot about the fact that in any kind of calculations we can use variable
// names and not only given values so we have to remake like everything xdddd
// it's going great
// lot of work to do 



grammar cutie;

/*
 * Parser Rules
 */

atom : id | Int | Double | Bool;

block                       :
                            declaration*
                            statement*
                            operation*
                            ;

operation                   :
                            operation_double
                          | operation_integer
                          | operation_boolean
                            ;

operation_boolean           : (Not)? Bool
                            | (Not)? Open_Parenthesis operation_boolean Close_Parenthesis
                            | (Not)? comparison_expresion
                            | operation_boolean Operator_sign_boolean operation_boolean
                            ;

comparison_expresion        : operation_integer Operator_sign_comparison operation_integer
                            | operation_double Operator_sign_comparison operation_double
                            | operation_boolean Operator_sign_equality operation_boolean
                            ;

// operation_integer           : Int (Operator_sign_numerical Int)* ;
operation_integer           : (Minus)* Int

operation_double            : Double (Operator_sign_numerical Double)* ;


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
Operator_sign_equality      : Equals | UnEquals;

fragment Lesser             : 'mniejszy';
fragment Greater            : 'wiekszy';
Operator_sign_comparison    : Lesser | Greater | Operator_sign_equality;


fragment Plus               : '+';
fragment Minus              : '-';
fragment Multiplication     : '*';
fragment Division           : '/';
Operator_sign_numerical     : Plus | Minus | Multiplication | Division;



fragment And                : 'oraz';
fragment Or                 : 'lub';
Operator_sign_boolean       : And | Or;

Not                         : 'nie';

var_assing                  : '->'; // defType

val_assign                  : '<-'; // asignVal

If                          : 'waruneczek';

While                       : 'powielanko';

Return                      : 'zwrocik';


Def                         : 'metodka';

Type
                            : 
                            'bezprzecinek' 
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

Int                         : ('-')[0-9][0-9]* ;

Double                      : ('-')[1-9][0-9]*'.'[0-9]* 
                            | ('-')'0.'[0-9]*
                            ;

Number                      : 
                            Int 
                          | Double
                            ;

Bool                        : 
                            False 
                          | True
                            ;

NAME                        : [a-z]+ ;
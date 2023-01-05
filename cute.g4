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

operation_boolean           : Bool (Operator_sign_boolean Bool)

operation_integer           : Int (Operator_sign_numerical Int)* ;

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




fragment Lesser             : 'mniejszy';
fragment Greater            : 'wiekszy';
fragment Equals             : 'kropkawkropke';
ComparationToken            : Lesser | Greater | Equals;


fragment Plus               : '+';
fragment Minus              : '-';
fragment Multiplication     : '*';
fragment Division           : '/';
Operator_sign_numerical     : Plus | Minus | Multiplication | Division;



fragment And                : 'oraz';
fragment Or                 : 'lub';
Operator_sign_boolean       : And | Or;

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
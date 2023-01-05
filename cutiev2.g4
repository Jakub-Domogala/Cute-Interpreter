grammar cutie;

/*
 * Parser Rules
 */

program                     : (stat)+;


// All Statements
stat                        : define_stat
                            | assign_stat
                            | if_stat
                            | while_stat;

// Create new Variable statement
define_stat                 : Type var_define identifier (val_assign expr)? Semicolon;

// Assign value to Variable
assign_stat                 : identifier val_assign expr Semicolon;

// If statement
if_stat                     : If Open_Parenthesis expr Close_Parenthesis (Open_Bracket stat Close_Bracket | stat);

// While statement
while_stat                  : While Open_Parenthesis expr Close_Parenthesis (Open_Bracket stat Close_Bracket | stat);

// All expressions
expr                        : expr Operator_sign expr
                            | (Minus)? expr
                            | (Not)? expr
                            | Open_Parenthesis expr Close_Parenthesis
                            | term;

// All terms ( identifiers and types )
term                        : identifier
                            | Int
                            | Double
                            | Bool;

// atom                        : id | Int | Double | Bool;

// identifier
identifier                  : NAME;


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

Operator_sign               : Operator_sign_boolean
                            | Operator_sign_comparison
                            | Operator_sign_equality
                            | Operator_sign_numerical;

Not                         : 'nie';

var_define                  : '->'; // defType

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
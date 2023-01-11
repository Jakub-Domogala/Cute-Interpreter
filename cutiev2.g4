grammar cutiev2;

/*
 * Parser Rules
 */

block                     : (stat)+;

// All Statements
stat                        : define_stat
                            | assign_stat
                            | print_stat
                            | if_stat
                            | while_stat;

// Create new Variable statement
define_stat                 : type Var_define Identifier (Val_assign expr)? Semicolon;

// Assign value to Variable
assign_stat                 : Identifier Val_assign expr Semicolon;

// Print variable or sth
print_stat                  : Print Open_Parenthesis term Close_Parenthesis;

// If statement
if_stat                     : If Open_Parenthesis expr Close_Parenthesis (Open_Bracket (stat)+ Close_Bracket | stat);

// While statement
while_stat                  : While Open_Parenthesis expr Close_Parenthesis (Open_Bracket (stat)+ Close_Bracket | stat);

// All expressions
// expr                        : expr operator_sign expr
//                             | (Minus)+ expr
//                             | (Not)+ expr
//                             | Open_Parenthesis expr Close_Parenthesis
//                             | term;
expr                        : expr Operator_sign expr
                            | Open_Parenthesis expr Close_Parenthesis
                            | term;

// All terms ( identifiers and s )
term                        : Identifier
                            | Int
                            | Double
                            | Bool;

// atom                        : id | Int | Double | Bool;

// identifier
Identifier                  : NAME;


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

fragment Lesser             : 'mniejszy';
fragment Greater            : 'wiekszy';
fragment Operator_sign_comparison    : Lesser | Greater | Operator_sign_equality;

fragment Plus               : '+';
fragment Minus                       : '-';
fragment Multiplication     : '*';
fragment Division           : '/';
fragment Operator_sign_numerical     : Plus | Minus | Multiplication | Division;

fragment And                : 'oraz';
fragment Or                 : 'lub';
fragment Operator_sign_boolean       : And | Or;

Operator_sign               : Operator_sign_boolean
                            | Operator_sign_comparison
                            | Operator_sign_equality
                            | Operator_sign_numerical;

Not                         : 'nie';

Var_define                  : '->'; // def

Val_assign                  : '<-'; // asignVal

Print                       : 'drukareczka';

If                          : 'waruneczek';

While                       : 'powielanko';

Return                      : 'zwrocik';


// Def                         : 'metodka';


// Int_name                  : 'bezprzecinek' ;
// Double_name               : 'zprzecinek' ;
// Bool_name                 : 'zerojedynek' ;
// String_name               : 'napisik' ;

// type                      : (
//                            Int_name
//                           | Double_name
//                           | Bool_name
//                           | String_name );

type                      : ('bezprzecinek' 
                          | 'zerojedynek' 
                          | 'napisik' 
                          | 'zprzecinek');

White_Sign                  : 
                          ( ' ' 
                          | '\n' 
                          | '\r' 
                          | '\t'
                          )+ -> skip
                            ;

Int                         : ('-')?[0-9][0-9]* ;

Double                         : '0';
// Double                      : ('-')?[1-9][0-9]*'.'[0-9]* 
//                             | ('-')?'0.'[0-9]*
//                             ;

Number                      : 
                            Int 
                          | Double
                            ;

Bool                        : 
                            'nieprawda'
                          | 'prawda'
                            ;

NAME                        : [a-zA-Z_-_][a-zA-Z0-9_-_]* ;
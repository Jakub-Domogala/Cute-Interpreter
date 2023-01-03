grammar cutie;

/*
 * Parser Rules
 */

atom : id | Int | Double | Bool;
// bulshit

// statement while return if 
// declaration int a
// operation c = a + b



program                 :
                        declaration*
                        statement*
                        operation*
                        ;

declaration             : Type rightArr NAME (leftArr operation) Semicolon;
operation               : 
                        Int (Operator_sign Int)* 
                      | Double (Operator_sign Double)*
                      | logical_expression
                        ;

statement               :
                        if_stat
                      | while_stat
                      | return_stat
                      | def_stat
                        ;


// bulshit








if_stat                 : If Open_Parenthesis logical_expression Close_Parenthesis Open_Bracket Close_Bracket

comparison_expresion    : Int LogicSign Int | Double LogicSign Double

logical_expression      : comparison_expresion (LogicSign comparison_expresion)*


/*
 * Lexer Rules
 */

fragment Lowercase
    : [a-z]
    ;
fragment Uppercase
    : [A-Z]
    ;

Open_Parenthesis        : '(';
Close_Parenthesis       : ')';

Open_Bracket            : '{';
Close_Bracket           : '}';

Open_Square_Bracket     : '[';
Close_Square_Bracket    : ']';

Dot                     : '.';
Comma                   : ',';
Semicolon               : '|<3|'; // ;

TypeSeparator           : '::';

fragment True           : 'prawda';
fragment False          : 'nieprawda';

fragment Lesser         : 'mniejszy';
fragment Greater        : 'wiekszy';
fragment Equals         : 'kropkawkropke';
ComparationToken        : Lesser | Greater | Equals;


fragment Plus           : '+';
fragment Minus          : '-';
fragment Multiplication : '*';
fragment Division       : '/';
Operator_sign           : Plus | Minus | Multiplication | Division;



fragment And            : 'oraz';
fragment Or             : 'lub';
LogicSign               : And | Or;

If                      : 'waruneczek';

While                   : 'powielanko';

// Outer                   : 'outer'; nie wiemy co to

Return                  : 'zwrocik';


Def                     : 'metodka';

Type
    : 'bezprzecinek' | 'zerojedynek' | 'napisik' | 'zprzecinek';

White_Sign
    : (' ' | '\n' | '\r' | '\t')+ -> skip
    ;

Int
    : ('-')[0-9][0-9]*
    ;
Double
    : ('-')[1-9][0-9]*'.'[0-9]* | ('-')'0.'[0-9]*
    ;
Number
    : Int | Double
    ;
Bool
    : False | True
    ;

NAME: [a-z]+;

rightArr : '->'; // defType

leftArr  : '<-'; // asignVal
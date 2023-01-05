grammar SimpleCalculator;

// Parser Rules

prog:   (func | stmt) ('\n' (func | stmt))* EOF;

func:   'def' ID '(' (ID ',')* ID? ')' '{' '\n' (stmt '\n')* '}';

stmt:   expr
    |   ID '=' expr #assign
    |   ID '(' (expr (',' expr)*)? ')' #call;

expr:   expr ('+'|'-') expr
    |   expr ('*'|'/') expr
    |   '-' expr
    |   '(' expr ')'
    |   INT
    |   DOUBLE
    |   ID
    |   'true'
    |   'false'
    |   expr ('and'|'or') expr
    |   'not' expr
    |   expr ('=='|'!=') expr
    |   expr ('<'|'<='|'>'|'>=') expr;

// Lexer Rules

ID  :   [a-zA-Z][a-zA-Z0-9]*;
INT :   [0-9]+;
DOUBLE  :   [0-9]+ '.' [0-9]+;
WS  :   [ \t\r\n]+ -> skip;
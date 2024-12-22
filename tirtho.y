%{
#include <stdio.h>
#include <stdlib.h>

void yyerror(const char *s);
int yylex(void);

%}

%token NUMBER

%%
input:  /* empty */
    | input line
    ;

line: '\n'
    | exp '\n' { printf("Result: %d\n", $1); }
    ;

exp: NUMBER
    | exp exp '+' { $$ = $1 + $2; }
    | exp exp '-' { $$ = $1 - $2; }
    | exp exp '*' { $$ = $1 * $2; }
    | exp exp '/' { $$ = $1 / $2; }
    ;
%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main(void) {
    return yyparse();
}
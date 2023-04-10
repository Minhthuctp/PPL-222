/// ID: 2053486

grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decl+ EOF ;
decl: vardecl | funcdecl;

vardecl: vardecl_ | vardeclass;

vardecl_: ID idlist* COLON typ SEMI;
vardeclass: ID varlist exp SEMI;
varlist: COMMA ID varlist exp COMMA | COLON typ ASSIGN;
automic: BOOLEAN | INTEGER | FLOAT | STRING;
typ: automic | arrtype | Auto;

idlist: COMMA ID;

arrtype: Array LS INTLIT (COMMA INTLIT)* RS Of automic;

funcdecl: ID COLON Function (typ | Void) LB paramlist? RB (Inherit ID)? blockstate;
paramlist: paramdecl (COMMA paramdecl)*;
paramdecl: Inherit? Out? ID COLON typ;


/* Statements */
blockstate: LP blockstmt? RP;

stmt: assignstmt 
    | ifstmt
	| forstmt
	| whiledostmt
	| dowhilestmt
	| breakstmt
	| continuestmt
	| returnstmt
	| callstmt
	| blockstate;

/* Assign statement*/
assignstmt: assign_cont SEMI;
assign_cont: assign_lhs ASSIGN exp;
assign_lhs: scalar_var;

scalar_var: ID | elem_exp | LB (ID | elem_exp) RB;

/* If statement*/
ifstmt: If LB exp RB stmt (Else stmt)?;

/* For statement */
forstmt: For LB assign_cont COMMA exp COMMA exp RB stmt; 

/* While statement */
whiledostmt: While LB exp RB stmt;

/* Do-while statement */
dowhilestmt: Do blockstate While LB exp RB SEMI;

/* Break statement */
breakstmt: Break SEMI;

/* Continue statement */
continuestmt: Continue SEMI;

/* Return statement */
returnstmt: Return exp? SEMI;

/* Call statement */
callstmt: func_call SEMI;

/* Block statement - Not fix */
statement: stmt | vardecl;
blockstmt: statement+;

/* Integer literal */
fragment DIGIT: [0-9];
fragment NoZeroDIGIT: [1-9];
INTLIT: '0' | NoZeroDIGIT DIGIT* ('_' DIGIT+)* {self.text = self.text.replace("_","")};

/* Float literal */
fragment INTR: '0' | NoZeroDIGIT DIGIT* ('_' DIGIT+)*;
fragment DECR: '.' DIGIT*;
fragment EXPR: [eE] [+-]? DIGIT+;

FLOATLIT: INTR DECR? EXPR {self.text = self.text.replace("_","")}
		| INTR DECR {self.text = self.text.replace("_","")}
		| DECR EXPR {self.text = self.text.replace("_","")}; 

/* Boolean literal */
BOOLIT: TRUE | FALSE;

/* String literal */
STRLIT: '"' STR_CHAR* '"' 
{
    self.text = self.text[1:-1]
}; 
// '"' (STR_CHAR | ESC_SEQ)* '"'
// {
// 	cont = str(self.text) 
// 	self.text = cont[1:-1]
// };

literal: INTLIT | FLOATLIT | BOOLIT | STRLIT | arraylit;

/* Array literal */
arraylit: LP explist? RP;

func_call: ID LB explist? RB;
explist: exp (COMMA exp)*;

/* Expression */
exp: exp1 STRCONCAT exp1 | exp1;
exp1: exp2 (EQUAL | NOTEQUAL | SMALLER | SMALLEREQUAL | GREATER | GREATEREQUAL) exp2 | exp2;
exp2: exp2 (LOGICALAND | LOGICALOR) exp3 | exp3;
exp3: exp3 (ADDOP | SUBSTROP) exp4 | exp4;
exp4: exp4 (MULOP | DIVOP | MODOP) exp5 | exp5;
exp5: LOGICALNOT exp5 | exp6;
exp6: SUBSTROP exp6| exp7;
exp7: func_call | elem_exp | operands | LB exp RB;

operands: literal | ID;

/* Indexed array */
elem_exp: ID LS explist RS;

/* Function call */


/* Key words */
Auto: 'auto';
Break: 'break';
Do: 'do';
Else: 'else';
FALSE: 'false';
For: 'for';
Function: 'function';
If: 'if';
Return: 'return';
TRUE: 'true';
While: 'while';
Void: 'void';
Out: 'out';
Continue: 'continue';
Of : 'of';
Inherit: 'inherit';
Array: 'array';

/* Operators */
ADDOP: '+';
SUBSTROP: '-';
MULOP: '*';
DIVOP: '/';
MODOP: '%';
LOGICALNOT: '!';
LOGICALAND: '&&';
LOGICALOR: '||';
EQUAL: '==';
NOTEQUAL: '!=';
ASSIGN: '=';
SMALLER: '<';
SMALLEREQUAL: '<=';
GREATER: '>';
GREATEREQUAL: '>=';
STRCONCAT: '::';

/* Seperators */
LB: '(';
RB: ')';
LS: '[';
RS: ']';
LP: '{';
RP: '}';
SEMI: ';';
COLON: ':';
COMMA: ',';
DOT: '.';

/* Type */
BOOLEAN: 'boolean';
FLOAT: 'float';
INTEGER: 'integer';
STRING: 'string';

/* ID */
ID: [_a-zA-Z][_a-zA-Z0-9]*;

// fragment STR_CHAR: ~[\\"\n];
// fragment ESC_SEQ: '\\b'
//        			| '\\f'
// 				| '\\r'
// 	   			| '\\n'
// 	   			| '\\t'
// 	   			| '\\\''
// 	   			| '\\\\'
// 	   			| '\\"';
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

Line_cmt: '//' ~[\r\n]*-> skip;
Block_cmt: '/*' .*? '*/'-> skip;

fragment STR_CHAR: ~[\r\\"\n] | ESC_SEQ;

fragment ESC_SEQ: '\\' [btnfr'"\\];
fragment ESC_ILLEGAL: '\\' ~[btnfr'"\\] | '\\';
UNCLOSE_STRING: '"' STR_CHAR* 
{
    raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL 
{
    raise IllegalEscape(self.text[1:])
};


ERROR_CHAR: .{raise ErrorToken(self.text)};
// UNCLOSE_STRING: '"' (STR_CHAR | ESC_SEQ)* ('\n' | EOF)
// {
// 	cont = str(self.text)
// 	esc = '\n'
// 	if (cont[-1] in esc):
// 		raise UncloseString(cont[1:-1])
// 	else:
// 		raise UncloseString(cont[1:])
// };
// fragment ESC_SEQ_ERR: '\\' ~[bfrnt'\\] | '\\' ~'"' ;
// ILLEGAL_ESCAPE: '"' (STR_CHAR | ESC_SEQ)* ESC_SEQ_ERR {
// 	cont = str(self.text) 
// 	raise IllegalEscape(cont[1:])
// };
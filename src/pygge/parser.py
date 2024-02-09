import sys
from lark import Lark

hygge_grammar = r'''
expression : "type" variable "=" pretype
| "let" variable "=" expression ";" expression
| "let" variable ":" pretype "=" expression ";" expression
| expression ";" expression
| "{" expression "}"
| "if" expression "then" expression "else" expression
| expression "or" expression
| expression "and" expression
| expression "=" expression
| expression "<" expression
| expression "+" expression
| expression "*" expression
| "not" expression
| "readInt" "(" ")"
| "readFloat" "(" ")"
| "print" "(" expression ")"
| "println" "(" expression ")"
| "assert" "(" expression ")"
| expression ":" pretype
| "(" expression ")"
| variable
| value


value : INT
| ESCAPED_STRING
| "true" -> true
| "false" -> false
| "()"

variable : CNAME

pretype : CNAME

COMMENT: "//" /[^\n]*/ NEWLINE
NEWLINE: "\n"

%import common.CNAME
%import common.ESCAPED_STRING
%import common.INT
%import common.WS

%ignore WS
%ignore COMMENT
%ignore NEWLINE
'''

hygge_parser = Lark(hygge_grammar, start="expression", lexer="basic")


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        print(hygge_parser.parse(f.read()).pretty())

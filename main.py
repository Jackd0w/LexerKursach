'''Вариант  222222'''

from multiprocessing.sharedctypes import Value
import sys
import re
from typing import List
from unicodedata import name

RESERVED = 'RESERVED'
INT      = 'INT'
ID       = 'ID'


class TokenTables:
    def _init__(self):
        self.__keywords : List[str] = ["readln", "writeln", "while", "next", "if",
        "true", "false", "dim", "begin", "end", "integer", "real", "boolean", "step",
        "else", "for", "to", "next"]
        self.__separators : List[str] = ['(', ')', ',',';','-', '+', '*', '/', '!=',
        '<=', '=>', '{', '}', '[', ']', ':=', '<', '>', '/*', '*/', '==', '||', '&&', '!']
        self.__ids : List[str] = []
        self.__numbers : List[str] = []

    @property
    def keywords(self):
        return self.__keywords

    @property
    def separators(self):
        return self.__separators

    @property
    def ids(self):
        return self.__ids

    @property
    def numbers(self):
        return self.__numbers

        
token_exprs = {
    1: "readln",
    2: "writeln",
    3: "while",
    4: "next",
    5: "if",
    6: "true",
    7: "false",
    8: "dim",
    9: "begin",
    10: "end",
    11: "integer",
    12: "real",
    13: "boolean",
    14: "step",
    15: "else", 
    16: "for",
    17: "to",
    18: "next",
    19: '(',
    20: ')',
    21: ',',
    22: ';',
    23: '-',
    24: '+',
    25: '*',
    26: '/',
    27: '!=',
    28: '<=',
    29: '=>',
    30: '{',
    31: '}',
    32: '[',
    33: ']',
    34: ':=',
    35: '<',
    36: '>',
    37: '/*',
    38: '*/',
    39: '==',
    40: '||',
    41: '&&',
    42: '!',
}

class Lex:
    
    lex_type = token_exprs.values()
    value = token_exprs.keys()

    def __init__(self, lex_type, value):
        self.lex_type = lex_type
        self.int_value = value

    def get_type(self):
        return self.lex_type

    def get_value(self):
        return self.int_value

    def pretty_output(L):
        print("(" + L.type_ + "," + L.int_value + ")")


class Identificator:
    def __init__(self, name, lex_type, value, declared, assigned):
        self.name = name
        self.declared = False
        self.assigned = False

    @property
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_type(self):
        return self.lex_type

    def set_type(self, lex_type):
        self.lex_type = lex_type

    def is_declared(self) -> bool:
        return self.declared

    def is_assigned(self) -> bool:
        return self.assigned

    def get_value(self):
        return self.value


class TableID:

    p = List[str]
    top = 1


    def __init__(self, max_size : int, top : int):
        self.size = max_size



def lex(characters, token_exprs):
	pos = 0
	tokens = []
	while pos < len(characters):
		match = None
		for token_expr in token_exprs:
			pattern, tag = token_expr
			regex = re.compile(pattern)
			match = regex.match(characters, pos)
			if match:
				text = match.group(0)
				if tag:
					token = (text, tag)
					tokens.append(token)
				break
		if not match:
			sys.stderr.write('Illegal character: %s\n' % characters[pos])
			sys.exit(1)
		else:
			pos = match.end(0)
	return tokens


def imp_lex(characters):
    return lex(characters, token_exprs)

if __name__ == "__main__":
    filename = "token_file.txt"   #sys.argv[1]
    file = open(filename)
    characters = file.read()
    file.close()
    tokens = imp_lex(characters)
    for token in tokens:
        print(token)

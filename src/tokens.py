from collections import namedtuple
from enum import Enum

class NewEnum(Enum):
    """ I want enum class to automatically compare name 
    between two Enum or comparing string to the Enum. 
    But once __eq__ is defined in an object it requres 
    __hash__(self) to be implemented to make the Enum 
    usuable as items in hash collections. """   
    def __eq__(self, b) -> bool:
        """ When I do == between the Enum I want to check the name"""
        if isinstance(b, str):
            print(2)
            return self.name == b 
        else:
            return  self.name == b.name

    def __hash__(self):
        return id(self.name)

TokenInfo = namedtuple('TokenInfo', ["name", "value"])

EOF = "EOF"
ILLEGAL = "ILLEGAL"

Token = NewEnum("Token", [
    "ASSIGN",    # "="
##############
# Arthemetic operators 
##############
    "PLUS",      # "+"
    "MINUS",     # "-"
    "DIVIDE",    # "/"
    "TIMES",     # "*"
    "MODULUS",   # "%"  Не нужен
    "POWER",     # "^"  Нк нужен
##############
# Logical operators LOOK HERE
#############
    "AND",       # "&" !!!!!!!  "&&"
    "OR",        # "|" !!!!!!! " ||" 
    "NOT",       # "!"
##############
# Comparisions   lEAVE AS IT BE
##############
    "EQUAL",     # "=="
    "NOTEQ",     # "!="
    "SMALL",     # "<"
    "LARGE",     # ">"
    "SMALLEQ",   # "<="
    "LARGEEQ",   # ">="
##############
# Brackets
##############
    "COMMA",     # ","
    "SEMICOLON", # ";"
    "LPAREN",    # "("
    "RPAREN",    # ")"
    "LBRACE",    # "{"
    "RBRACE",    # "}"
    "LSQUARE",   # "["
    "RSQUARE",   # "]"
##############
# EXTRA
##############
    "ID",        #  Variables
##############
# Datatypes
##############  
    "INTEGER",       
    "REAL",
    "BOOLEAN",     
    "TRUE",      
    "FALSE",     
##############
# Keywords
##############
    "BEGIN",  
    "END",
    "FOR",
    "TO",
    "NEXT",
    "WHILE",
    "DIM",
    "READLN",       
    "IF",        
    "ELSE",      
    "RETURN",    
    "WRITELN"
])

keywords = {
    "begin"  : Token.BEGIN.name,
    "end"   : Token.END.name,
    "for"   : Token.FOR.name,
    "to"    : Token.TO.name,
    "next"  : Token.NEXT.name,
    "while" : Token.WHILE.name,
    "dim"   : Token.DIM.name,
    "readln": Token.READLN.name,
    "if"    : Token.IF.name,
    "else"  : Token.ELSE.name,
    "true"  : Token.TRUE.name,
    "false" : Token.FALSE.name,
    "return": Token.RETURN.name,
    "writeln" : Token.WRITELN.name,
    "integer" : Token.INTEGER.name,
    "real" : Token.REAL.name,
    "boolean" : Token.BOOLEAN.name
}

def get_token(data: str) -> Token:
    # checks if the given string is keyword or not
    # if its a keyword return the respective Token
    # or by default return Token.Id 
    return keywords.get(data, Token.ID.name)
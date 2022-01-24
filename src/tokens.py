from enum import Enum
import re
from collections import namedtuple


TokenInfo = namedtuple("Tokens", ["name", "value"])


class NewEnum(Enum):
    """Изначально планировалось, чтобы класс автоматически проверял имена двух лексем.
    Но как только метод __eq__ был объявлен, его необходимо захешировать с помощью метода __hash__.
    Тогда эти элементы можно будет ичпользовать в хэш коллекции """
    def __eq__(self, b) -> bool:
        if isinstance(b, str):
            return self.name == b 
        else:
            return  self.name == b.name

    def __hash__(self):
        return id(self.name)



ILLEGAL = 'ILLEGAL'
EOF     = 'EOF'



#Все нелбходимые токены, реализованные с помощью регулярных выражений
class Token(NewEnum):
    # типы данных
    STRING  = re.compile(r'(\".*\")|(\'.*\')')
    FLOAT   = re.compile(r'\d+\.\d+')
    INT     = re.compile(r'\d+')
    # скобки
    LPAREN  = re.compile(r'\(')
    RPAREN  = re.compile(r'\)')
    LBRACE  = re.compile(r'\{')
    RBRACE  = re.compile(r'\}')
    LSQUARE = re.compile(r'\[')
    RSQUARE = re.compile(r'\]')
    # операторф
    ASSIGN  = re.compile(r':=')
    # арифметические операторы
    PLUS    = re.compile(r'\+')
    MINUS   = re.compile(r'\-')
    TIMES   = re.compile(r'\*')
    DIVIDE  = re.compile(r'/')
    
    # Логические операторы
    AND     = re.compile(r'&&')
    OR      = re.compile(r'\|\|')
    NOT     = re.compile(r'!')
    # операции группы отношения
    EQUAL   = re.compile(r'\=\=')
    SMALL   = re.compile(r'<')
    SMALLEQ = re.compile(r'<\=')
    LARGE   = re.compile(r'>')
    LARGEEQ = re.compile(r'>\=')
    NOTEQ   = re.compile(r'!\=')
    # ключевые слова
    IF      = re.compile(r'if')
    WHILE   = re.compile(r'while')
    TRUE    = re.compile(r'true')
    FALSE   = re.compile(r'false')
    BEGIN   = re.compile(r'begin')
    END     = re.compile(r'end')
    FOR     = re.compile(r'for')
    TO      = re.compile(r'to')
    NEXT    = re.compile(r'next')
    ELSE    = re.compile(r'else')
    STEP    = re.compile(r'step')
    NAN     = re.compile(r'nan')
    DIM     = re.compile(r'dim')
    READLN  = re.compile(r'readln')
    WRITELN = re.compile(r'writeln')

    #переменные
    ID      = re.compile(r'[_a-zA-Z][_a-zA-Z0-9]*')
    # комментарии
    COMMENT = re.compile(r'\*\/.*\/\*')
    # разделители
    COMMA   = re.compile(r',')
    SEMICOLON  = re.compile(r';')
    WHITESPACE = re.compile(r'(\t|\n|\s|\r)+')

#Реализация приоритетов операций через перечисление
Priority = NewEnum("priority", [
    "LOWEST",
    "LOWER",
    "LOW",
    "HIGH",
    "HIGHER",
    "HIGHEST",
])

# Токены приоритетов
precedence =  {
    Token.EQUAL.name : Priority.LOWER,       # ==
    Token.NOTEQ.name : Priority.LOWER,       # !=
    Token.SMALL.name : Priority.LOW,         # <  
    Token.LARGE.name : Priority.LOW,         # >
    Token.PLUS.name  : Priority.HIGH,        # +
    Token.MINUS.name : Priority.HIGH,        # -
    Token.TIMES.name : Priority.HIGHER,      # *
    Token.DIVIDE.name: Priority.HIGHER,      # /
    Token.LPAREN.name: Priority.HIGHEST,     # ()  
}


#Функция для вычисления приоритета токена. По умолчанию возвращает наименьший
def get_precedence(token: Token) -> Priority:
    return precedence.get(token.name, Priority.LOWEST)
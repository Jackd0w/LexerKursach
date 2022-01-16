import sys
import re


MODEL_QUOTE = ' '
MODEL_WHITESPACE = [' ', '\t', '\b', '\n', '\r']

LIST_KEYWORDS = {
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
    18: "next"
}


LIST_SEPARATORS = {
    1: '(',
    2: ')',
    3: ',',
    4: ';',
    5: '-',
    6: '+',
    7: '*',
    8: '/',
    9: '!=',
    10: '<=',
    11: '=>',
    12: '{',
    13: '}',
    14: '[',
    15: ']',
    16: ':=',
    17: '<',
    18: '>',
    19: '/*',
    20: '*/',
    21: '==',
    22: '||',
    23: '&&',
    24: '!',
}

FALSE_LEN = len('false')
TRUE_LEN = len('true')
NULL_LEN = len('null')
 
'''Нужно добавить проверку на входной символ для модельного языка. Посмотри еще раз в таблице'''
def lex_string(string):
    model_string = ''
 
    '''
    if string[0] == MODEL_QUOTE:
        string = string[1:]
    else:
        return None, string
    '''
 
    for c in string:
        if c == MODEL_QUOTE:
            return model_string, string[len(model_string)+1:]
        else:
            model_string += c
 
    raise Exception('Expected end-of-string quote')
 
 
def lex_number(string):
    json_number = ''
 
    number_characters = [str(d) for d in range(0, 10)] + ['-', 'e', '.']
 
    for c in string:
        if c in number_characters:
            json_number += c
        else:
            break
 
    rest = string[len(json_number):]
 
    if not len(json_number):
        return None, string
 
    if '.' in json_number:
        return float(json_number), rest
 
    return int(json_number), rest
 
 
def lex_bool(string):
    string_len = len(string)
 
    if string_len >= TRUE_LEN and \
         string[:TRUE_LEN] == 'true':
        return True, string[TRUE_LEN:]
    elif string_len >= FALSE_LEN and \
         string[:FALSE_LEN] == 'false':
        return False, string[FALSE_LEN:]
 
    return None, string
 
 
def lex_null(string):
    string_len = len(string)
 
    if string_len >= NULL_LEN and \
         string[:NULL_LEN] == 'null':
        return True, string[NULL_LEN]
 
    return None, string
 
 
def lex(string):
    tokens = []
 
    while len(string):
        model_string, string = lex_string(string)
        if model_string is not None:
            tokens.append(model_string)
            continue
 
        json_number, string = lex_number(string)
        if json_number is not None:
            tokens.append(json_number)
            continue
 
        json_bool, string = lex_bool(string)
        if json_bool is not None:
            tokens.append(json_bool)
            continue
 
        json_null, string = lex_null(string)
        if json_null is not None:
            tokens.append(None)
            continue
 
        c = string[0]
 
        if c in MODEL_WHITESPACE:
            string = string[1:]
        elif c in JSON_SYNTAX:
            tokens.append(c)
            string = string[1:]
        else:
            raise Exception('Unexpected character: {}'.format(c))
 
    return tokens
 
if __name__ == "__main__":
    filename = "token_file.txt"          #sys.argv[1]
    file = open(filename)
    characters = file.read()
    file.close()
    tokens = lex(characters)
    for token in tokens:
        print(token)
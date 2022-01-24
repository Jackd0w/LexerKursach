from new_lexer import Lexer
from new_parser import Parser
from tokens import *

import sys
from os.path import exists

def interpretor(data: str):
    lex = Lexer(data)
    parse = Parser(lex)
    
    for p in parse:
        if p == EOF:
            break
        p.eval()


def repl():
    i = 0
    while True:
        try:
            data: str = input(f"[{i}]: ")
            interpretor(data)
        except EOFError:           
            print("EOF Error")
        except KeyboardInterrupt:  
            print("Keyboard Interruption")
            break
        except Exception as msg:
            print(msg)
        finally:  
                i += 1   


if __name__ == "__main__":

    file_name = "src/token_file.txt"
    if not exists(file_name):
        print(f"{file_name} not found")
        sys.exit(0)
    with open(file_name) as f:
        data = f.read()
        interpretor(data) 
        print("Ok")
    
from tokens import *
    
___all__ = ["Lexer"]

def Lexer(data: str) -> TokenInfo:
    pos = 0 
    while pos < len(data):
        for tokenId in Token:
            if match := tokenId.value.match(data, pos):
                pos = match.end(0)
                if tokenId == Token.WHITESPACE or tokenId == Token.COMMENT:
                    # Игнорируем комменты и пробелы
                    break
                yield TokenInfo(tokenId.name, match.group(0))
                break
        else:
            # если паттерн не совпадает, выдаем ошибку
            yield TokenInfo(ILLEGAL, data[pos])
            pos += 1
    else:
        yield TokenInfo(EOF, '\x00') 
        yield TokenInfo(EOF, '\x00') 
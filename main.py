'''Вариант  222222'''

a = ['*', '-', '/', '=', '>', '<', '>=', '=', '<=', '+','<>']
b = ['(', ')', '"', ';', '!']
c = ['long','float','static',
   'char','short','switch','int',
   'const','if','then','else','for'
   ,'while','break']

def isLetter(Char):
    if ((Char >= 'a' and Char <= 'z') or (Char >= 'A' and Char <= 'Z')):
        return True
    else:
        return False


def isDigit(Char):
    if (Char <= '9' and Char >= '0'):
        return True
    else:
        return False


def IsSpace(Char):
    if (Char == ' '):
        return True
    else:
        return False


def fenli(List):
    ResultList = []
    for String in List:
        Letter = ''
        letter = ''
        index = 0
        for Char in String:
            if (index < len(String) - 1):
                index += 1
            if (IsLetter(Char) or IsDigit(Char)):
                if (IsLetter(String[index]) or IsDigit(String[index])):
                    Letter += Char
                elif (IsSpace(String[index]) or (String[index] in b) or (
                        String[index] in a) or (String[index:index + 2] in a)):
                    Letter += Char
                    ResultList.append(Letter)
                    Letter = ''
            elif Char in b:
                        ResultList.append(Char)
            elif Char in a:
                        letter += Char
                        if (String[index] in a):
                            letter += String[index]
                            ResultList.append(letter)
                            letter = ''
                        else:
                            ResultList.append(letter)
                            letter = ''
            elif IsSpace(Char):
                            pass
    return ResultList

if __name__ == "__main__":
    pass
'''Вариант  222222'''

a = ['*', '-', '/', '=', '>', '<', '>=', '=', '<=', '+','<>']
b = ['(', ')', '"', ';', '!']
c = ['long','float','static',
   'char','short','switch','int',
   'const','if','then','else','for'
   ,'while','break']

def is_letter(Char):
    if ((Char >= 'a' and Char <= 'z') or (Char >= 'A' and Char <= 'Z')):
        return True
    else:
        return False


def is_digit(Char):
    if (Char <= '9' and Char >= '0'):
        return True
    else:
        return False


def is_space(Char):
    if (Char == ' '):
        return True
    else:
        return False


def lexer(List):
    ResultList = []
    for String in List:
        Letter = ''
        letter = ''
        index = 0
        for Char in String:
            if (index < len(String) - 1):
                index += 1
            if (is_letter(Char) or is_digit(Char)):
                if (is_letter(String[index]) or is_digit(String[index])):
                    Letter += Char
                elif (is_space(String[index]) or (String[index] in b) or (
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
            elif is_space(Char):
                            pass
    return ResultList

def pretty_printer(char):
    for i in char:
        if i in a:
            print("Оператор"+i+">")
        elif i in b:
            print("<Defense",+i+">")
        elif i in c:
            print("<Ключевое слово", +i+">")
        elif i.isdigit():
            print("Постоянный,"+i+">")
        elif i.isalnum():
            print("<Идентификатор," + i + ">")


if __name__ == "__main__":
    p=[]
    with open("token_file.txt",'r') as f:
        m=f.readlines()
        for i in m:
            n=i.strip()
            p.append(n)
        y=lexer(p)
        pretty_printer(y)

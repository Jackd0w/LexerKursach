from tokens import TokenInfo

class Node:  ...
class Statement(Node): ...
class Expression(Node): ...
storage = {}

from tokens import *


class Identifier(Expression):
    def __init__(self, name): 
        self.name  = name    

    def __repr__(self) -> str:
        return self.name

    def eval(self):
        if self.name in storage:
            return storage[self.name]
        else:
            raise NameError(f"'{self.name}' is not defined")


class Literal(Expression):
    def __init__(self, typ: str, value: str):
        self.type = typ
        self.value = value

    def __repr__(self) -> str:
        return str(self.value)
    
    #Возвращает тип данных
    def get_type(self) -> str:
        
        if self.type == Token.FALSE or self.type == Token.TRUE:
            return "bool" 
        return self.type.lower()

    def type_casting(self):
        #Здесь происходит конверсия в типы значений
        if self.type == Token.INT:
            return int(self.value)
        elif self.type == Token.FLOAT:
            return float(self.value)
        elif self.type ==  Token.STRING:
            return str(self.value)
        elif self.type == Token.TRUE :
            return True 
        elif self.type == Token.FALSE:
            return False
        else:
            return None

    def eval(self):
        try:
            out = self.type_casting()
        except ValueError:
            raise ValueError(f"Error converting {self.value} to {self.type}")
        return out


class DimStatement(Statement):
    def __init__(self, name: Identifier, expr: Expression):   
        self.name = name
        self.expr = expr

    def __repr__(self) -> str:
        return f"(let {self.name} {self.expr})"

    def eval(self):
        if self.name in storage:
            print(f'"{self.name}" already defined')
            raise NameError(f'"{self.name}" already defined')
        storage[self.name] = self.expr.eval()


class AssignStatement(Statement):
    def __init__(self, name: str, expr: Expression):   
        self.name = name
        self.expr = expr

    def __repr__(self) -> str:
        return f"(set {self.name} {self.expr})"

    def eval(self):
        if self.name not in storage:
            print(f'"{self.name}" not defined')
            raise NameError(f'"{self.name}" not defined')
        storage[self.name] = self.expr.eval()


class IfStatement(Statement):
    def __init__(self, condition, true_stmt: Statement, flase_stmt: Statement):
        self.condition = condition
        self.true_stmt = true_stmt
        self.flase_stmt = flase_stmt

    def __repr__(self) -> str:
        return f"(if ({self.condition}) ({self.true_stmt}) ({self.flase_stmt}))"

    def eval(self):
        if self.condition.eval():
            self.true_stmt.eval()  
        else:
            self.flase_stmt.eval()


class WhileStatement(Statement):
    def __init__(self, condition: Expression, stmt: Statement):
        self.condition = condition
        self.stmt = stmt
   
    def __repr__(self) -> str:
        return f"(while ({self.condition}) ({self.stmt}))"

    def eval(self):
        while self.condition.eval():
            self.stmt.eval() 


class ForStatement(Statement):
    def __init__(self, condition: Expression, stmt: Statement):
        self.condition = condition
        self.stmt = stmt
    
    def __repr__(self) -> str:
        return f"(for (set {self.name} {self.expr}) to ({self.condition}) step ({self.condition}) next ({self.condition}))"

    def eval(self):
        while self.condition.eval():
            self.stmt.eval() 


class InfixExpression(Expression):
    def __init__(self, left: Expression, operator: Statement, right: Expression):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self) -> str:
        return f"({self.left} {self. operator} {self.right})"

    def eval(self):
        operator =  {
            "+" : lambda a,b: a+b,
            "-" : lambda a,b: a-b,
            "*" : lambda a,b: a*b,
            "/" : lambda a,b: a//b,
            "&&" : lambda a,b: a and b,
            "||" : lambda a,b: a or b,
        }
        try:
            return operator[self.operator](self.left.eval(), self.right.eval()) 
        except TypeError:
            raise TypeError(f"can't perform {self.operator} between {self.left_type()} and  {self.left_type()}")


class PrefixExpression(Expression):
    def __init__(self, operator: Statement, right: Expression):
        self.operator = operator
        self.right = right

    def get_type(self) -> str:
        # returns data type
        return self.type.right

    def __repr__(self) -> str:
        return f"({self. operator}{self.right})"

    def eval(self):
        operator =  {
            "!" : lambda a: not a,
            "-" : lambda a: -a,
        }
        try:
            return operator[self.operator](self.right.eval())  
        except TypeError:
            raise TypeError(f"can't perform {self.operator} between {self.left_type()} and  {self.left_type()}")
 

class WriteStatement(Statement):
    def __init__(self, state, value: Expression):
        self.state = state
        self.value = value

    def __repr__(self) -> str:
        return f"({self.state.lower()} {self.value})"

    def eval(self):
        if self.state == "writeln":
            print(self.value.eval())
        else:
            print(self.value.eval(), end="")
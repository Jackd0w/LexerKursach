from new_parser import *
from src.new_lexer import *
from src.tokens import *
import pytest

@pytest.mark.parametrize("data, expected", [
    ("2+3*4", "(2 + (3 * 4))"),
    ("-1 +3/4 - 4", "((-1) + ((3 / 4) - 4))"),
    ("(1^  3)%3/3.0", "((1 ^ 3) % (3 / 3.0))")
])
def test_parser(data, expected):
    output = next(Parser(Lexer(data)))
    assert  output.__repr__() == expected


def test_assignment():
    data = """
    let a = 100;
    a = 10/20;
    """
    for i in Parser(Lexer(data)):
        if i == EOF:
            break
        print(data)
        data = i.eval()
    assert data == 50.0
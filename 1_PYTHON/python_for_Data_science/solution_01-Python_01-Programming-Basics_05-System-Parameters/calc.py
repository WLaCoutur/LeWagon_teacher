# pylint: disable=missing-module-docstring,missing-function-docstring,eval-used
import sys
# $DELETE_BEGIN
import operator
# $DELETE_END

def main():
    """Implement the calculator"""
    # $CHALLENGIFY_BEGIN
    left_operand = int(sys.argv[1])
    op_name = sys.argv[2]
    right_operand = int(sys.argv[3])
    if op_name == '+':
        return left_operand + right_operand
    if op_name == '-':
        return left_operand - right_operand
    if op_name == '*':
        return left_operand * right_operand
    if op_name == '/':
        return left_operand / right_operand
    return 'usage: '
    # $CHALLENGIFY_END

# $DELETE_BEGIN
def main2():
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }
    return ops[sys.argv[2]](int(sys.argv[1]), int(sys.argv[3]))

def main3():
    return {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }[sys.argv[2]](int(sys.argv[1]), int(sys.argv[3]))

def main4():
    #getattr(1,'__add__',2)
    return getattr(int(sys.argv[1]), {
        '+': '__add__',
        '-': '__sub__',
        '*': '__mul__',
        '/': '__truediv__'
    }[sys.argv[2]])(int(sys.argv[3]))

def main5():
    # style is not happy with eval :'(
    return eval(f'{sys.argv[1]} {sys.argv[2]} {sys.argv[3]}')
# $DELETE_END
if __name__ == "__main__":
    print(main())
    # $DELETE_BEGIN
    # print(main2())
    # print(main3())
    # print(main4())
    # print(main5())
    # $DELETE_END

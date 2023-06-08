#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]

    if op == '+':
        value = add(a, b)
    elif op == '-':
        value = sub(a, b)
    elif op == '*':
        value = mul(a, b)
    elif op == '/':
        value = div(a, b)

    print(f"{a} {op} {b} = {value}")

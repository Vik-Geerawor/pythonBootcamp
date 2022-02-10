def addition(a, b):
    print("\n *** OPERATORS ***\n")
    print(str(a) + " + " + str(b) + " = " + str(a + b))


def subtraction(a, b):
    print(str(a) + " - " + str(b) + " = " + str(a - b))


def comparison_operators():
    a = 3
    b = 4

    print(f"{a} == {b}: {a == b}")
    print(f"{a} != {b}: {a != b}")
    print(f"{a} > {b}: {a > b}")
    print(f"{a} < {b}: {a < b}")
    print(f"{a} >= {b}: {a >= b}")
    print(f"{a} <= {b}: {a <= b}")


def logical_operators():
    a = 3
    b = 4

    print(f"{a} == {b} and {a} != {b}: {a == b and a != b}")
    print(f"{a} == {b} or {a} != {b}: {a == b or a != b}")


if __name__ == '__main__':
    # addition(1, 2)
    # comparison_operators()
    logical_operators()

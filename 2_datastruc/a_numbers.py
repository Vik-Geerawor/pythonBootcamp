def addition():
    # Variable declaration and initialisation
    a: int = 2      # declare and initialise
    b: int = 3
    c: int          # declared but not init
    c = a + b       # simple addition operation
    print(c)


def subtraction():
    a: int = 2
    b: int = 3
    c: int = b - a
    print("3 - 2 = " + str(c))  # cast int value c to str


def multiplication():
    a: int = 2
    b: int = 3
    c: int

    c = a * b
    print(str(a) + " * " + str(b) + " = " + str(c))


def division():
    a: int = 2
    b: int = 3
    c: int
    c = b / a
    print(str(b) + " / " + str(a) + " = " + str(c))
    # although c is of type int, it's now holding a float value
    # this is called dynamic typing, a var can hold different types

    # Floor Division
    c = b // a
    print(str(b) + " // " + str(a) + " = " + str(c))


def remainder():
    a: int = 2
    b: int = 3
    c: int
    c = b % a
    print(str(b) + " % " + str(a) + " = " + str(c))


def modulus():
    a: int = 2
    b: int = 3
    c: int
    c = b ** a
    print(str(b) + " ** " + str(a) + " = " + str(c))


def exponent():
    a: int = 2
    b: int = 3
    c: int
    c = b ** a
    print(str(b) + " ** " + str(a) + " = " + str(c))


if __name__ == '__main__':
    print("\n*** NUMBERS ***")
    exponent()


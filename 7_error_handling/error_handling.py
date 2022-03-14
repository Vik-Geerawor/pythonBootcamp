def try_except():
    try:
        for i in ['a', 'b', 'c']:
            print(i ** 2)
    except TypeError:
        print("Incorrect data type")


def try_except_finally():
    try:
        x = 5
        y = 0
        z = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("All done")


def try_except_else():
    i = 0
    while True:
        try:
            number = int(input("Enter a number: "))
        except:
            print("Incorrect input")
            i += 1
            continue
        else:
            print(f"{number} ^ 2 = {number ** 2}")
            break


if __name__ == '__main__':
    # try_except()
    # try_except_finally()
    try_except_else()

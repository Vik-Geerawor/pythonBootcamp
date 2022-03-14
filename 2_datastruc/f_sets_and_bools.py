def sets():
    # declare and init
    myset = {1, 3, 2, 4}

    # display the elements of a set
    print(f"My set: {myset}")

    # add an element
    myset.add(8)
    print(f"My set after adding 8: {myset}")


def set_ops():
    myset = {1, 3, 2, 4}

    # another way of declaring a set
    yourset = set()
    yourset.add(4)
    yourset.add(2)
    print(f"You set: {yourset}")

    print(f"Difference between myset and yourset: {myset.difference(yourset)}")


def boolean():
    # declare and init
    flag: bool = False

    print(f"Flag: {flag}")

    if 1 < 2:
        flag = True
        print(f"Flag: {flag}")


if __name__ == '__main__':
    print("\n*** SETS AND BOOLS ***")
    # sets()
    boolean()

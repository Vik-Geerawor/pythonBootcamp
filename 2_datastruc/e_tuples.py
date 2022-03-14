def basics():
    # declare and init
    mytuple = (1, 'two', 3, 'two')

    # display the elements
    print(f"My tuple: {mytuple}")
    print(f"Element number 2: {mytuple[1]}")

    # count no. of occurrences of an element
    print(f"Count of 'two': {mytuple.count('two')}")

    # find the index of an element
    print(f"Index of 'two': {mytuple.index('two')}")


if __name__ == '__main__':
    print("\n*** TUPLES ***")
    basics()

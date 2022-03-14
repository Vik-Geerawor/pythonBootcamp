def for_loop():
    print("Simple for loop")
    mylist1 = [1, 2, 3]
    for item in mylist1:
        print(item)

    print("\nTuple unpacking")
    mylist2 = [(1, 2), (3, 4), (5, 6)]
    for a, b in mylist2:
        print(a)

    print("\nLoop through a dictionary")
    mydictionary = {'k1': 'apple', 'k2': 'banana', 'k3': 'eggs'}
    for key, value in mydictionary.items():
        print(value)


def while_loop():
    mylist1 = [1, 2, 3, 4, 5]
    i = 0
    while i < len(mylist1):
        if mylist1[i] == 4:     # exit condition
            break
        print(f"{mylist1[i]}")

        if mylist1[i] == 1:
            pass                # TODO: avoids exception

        i += 1

        if mylist1[i] % 2 == 0:     # skip condition
            continue
        print("Even number printed ^")


if __name__ == '__main__':
    # for_loop()
    while_loop()

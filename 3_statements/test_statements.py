def test1():
    st = 'Print only the words that start with s in this sentence'
    print(f"\nWords starting with 's':")
    for word in st.split():
        if word[0] == 's':
            print(word)

    print(f"\nWords with even number of letters:")
    for word in st.split():
        if len(word) % 2 == 0:
            print(word)


def test2():
    for i in range(0, 11):
        if i % 2 == 0:
            print(i)


def test3():
    mylist = [x for x in range(1, 51) if x % 3 == 0]
    print(mylist)


def test4():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"FizzBuzz")
        elif i % 3 == 0:
            print(f"Fizz")
        elif i % 5 == 0:
            print(f"Buzz")
        else:
            print(i)


def test5():
    st = 'Create a list of the first letters of every word in this string'
    mylist = [word[:3] for word in st.split()]
    print(mylist)


if __name__ == '__main__':
    print(f"\n*** Statements Test ***")
    test5()

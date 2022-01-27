def test_strings():
    print("\n *** STRINGS ***\n")
    print(r"C:\User\Vik")

    word = "Python"
    print(word[-2])  # returns "o"
    print(word[:2])  # returns "Py"
    print(word[4:])  # returns "on"
    print(len(word))  # returns 6

    print("""\
    \nUsage: thingy [OPTIONS]
        -h		Display this usage message
        -H hostname	Hostname to connect to
    """)


if __name__ == '__main__':
    test_strings()
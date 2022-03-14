def test_numbers():
    a = 10 ** 3 / 100 * 10 + 1 - 0.75
    print(f"Result: {a}")

    print(f"44 : {4 * (6 + 5)}")
    print(f"29 : {4 * 6 + 5}")
    print(f"34 : {4 + 6 * 5}")

    print(f"Double: {3 + 1.5 + 4}")

    print(f"Root of 9: {9 ** (1/2)}")
    print(f"Sq root of 3: {3 ** 2}")


def test_strings():
    s = 'hello'
    print(f"'e' in 'hello': {s[1]}")
    print(f"Reverse: {s[::-1]}")
    print(f"One way of getting 'o': {s[-1]}")
    print(f"Another way is: {s[4]}")


def test_lists():
    list1 = [0, 0, 0]
    print(f"List 1: {list1}")

    list2 = [0] * 3
    print(f"List 2: {list2}")

    list3 = [1, 2, [3, 4, 'hello']]
    list3[2][2] = 'goodbye'
    print(f"List 3: {list3}")

    list4 = [5, 3, 4, 6, 1]
    list4.sort()
    print(f"List 4 sort: {list4}")


def test_dictionaries():
    d = {'simple_key': 'hello'}
    print(f"Value: {d['simple_key']}")

    d = {'k1': {'k2': 'hello'}}
    print(f"Value: {d['k1']['k2']}")

    d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
    print(f"Value: {d['k1'][0]['nest_key'][1][0]}")

    d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
    print(f"Value: {d['k1'][2]['k2'][1]['tough'][2][0]}")


def test_tuples():
    list5 = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
    set1 = set(list5)
    print(f"List 5: {list5}")
    print(f"Set 1: {set1}")


def test_bool():
    print(f"2 > 3: False - {2 > 3}")
    print(f"3 <= 2: False - {3 <= 2}")
    print(f"3 == 2.0: False - {3 == 2.0}")
    print(f"3.0 == 3: False - {3.0 == 3}")          # TODO: incorrect
    print(f"4 ** 0.5 != 2: False - {4 ** 0.5 != 2}")    # TODO: incorrect


if __name__ == '__main__':
    print("\n*** Data Structures Test ***")

    # test_numbers()
    # test_strings()
    # test_lists()
    # test_dictionaries()
    # test_tuples()
    test_bool()

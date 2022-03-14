def basics():
    # declare and init
    mydict = {'k1': 'v1', 2: 'v2', 'k3': 3}

    # display dictionary
    print(f"My dictionary: {mydict}")

    # display the value of a key
    print(f"Value at key k1 = {mydict['k1']}")

    # format element in a nested dictionary
    print(f"Value of k1 in uppercase: {mydict['k1'].upper()}")

    # add new pair
    mydict['k4'] = 'apple'
    print(f"My dictionary after adding apple: {mydict}")

    # update the value of a key
    mydict['k3'] = 'v3'
    print(f"Updated value of k3: {mydict['k3']}")

    # list all the keys of a dict
    print(f"All the keys: {mydict.keys()}")

    # list all values
    print(f"All the values: {mydict.values()}")

    # list the pairs
    print(f"All the pairs: {mydict.items()}")


def nested_dict():
    # nested list
    mydict = {1: 'apple', 2: 'banana', 3: ['grapes', 'cherries']}
    print(f"My dictionary: {mydict}")
    print(f"First element in nested list: {mydict[3][0]}")

    # nested dictionary
    mydict[4] = {'name': 'Vik', 'age': 40}
    print(f"My dictionary with a nested dictionary: {mydict}")
    print(f"Age in the nested dictionary: {mydict[4]['age']}")


if __name__ == '__main__':
    print("\n*** DICTIONARIES ***")
    # basics()
    nested_dict()

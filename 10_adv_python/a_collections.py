from collections import Counter
from collections import defaultdict
from collections import namedtuple


def counter_demo():
    mylist = [1, 2, 3, 1, 5, 4, 7, 2, 9, 8, 5, 2, 0, 2]

    # solution 1 - long
    uniq_list = []
    for item in mylist:
        if item not in uniq_list:
            uniq_list.append(item)
    print(uniq_list)

    # solution 2 - quick
    new_dict = Counter(mylist)      # item: count
    # print(new_dict)
    new_list = list(new_dict)
    print(new_list)


def defaultdict_demo():
    mydict = {'a': 1, 'b': 2, 'c': 3}

    # printing a value of a key
    value = mydict['b']
    print(value)

    # printing a value of a non-existent key -> leads to 'KeyError'
    # value = mydict['d']
    # print(value)

    # assigning a default value to a non-existent key
    mydict = defaultdict(lambda: 0)         # default value is 0
    value = mydict['d']
    print(value)


def namedtype_demo():
    mytuple = (103, 'Vik', '15-Oct-1981')       # perceived as a DB record

    # printing the second item in a tuple
    print(mytuple[1])                           # kinda hard with indexes

    # a better way
    myrec = namedtuple('emp', ['id', 'name', 'dob'])    # 'emp' is the int class name
    emprec1 = myrec(104, 'Neli', '15-Oct-1981')
    print(emprec1.name)


if __name__ == '__main__':
    counter_demo()
    defaultdict_demo()
    namedtype_demo()

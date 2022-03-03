# used for map_demo
def square(num):
    return num ** 2


def map_demo():
    my_list = [1, 2, 3]
    for item in map(square, my_list):       # TODO: function name without ()
        print(item)

    sq_list = list(map(square, my_list))
    print(sq_list)


# used for filter_demo
def is_even(num):
    return num % 2 == 0     # True if even


def filter_demo():
    my_list = [1, 2, 3, 4, 5]

    even_list = list(filter(is_even, my_list))
    print(even_list)


def lambda_demo():
    my_list = [1, 2, 3, 4, 5]
    # another version of map_demo
    # the square function has been replaced by a lambda
    # which is then passed to map function
    # then cast to a list and printed
    print(list(map(lambda num: num ** 2, my_list)))

    # another version of filter_demo using lambda
    print(list(filter(lambda num: num % 2 == 0, my_list)))


if __name__ == '__main__':
    print(f"\n*** Advance Functions ***")
    # map_demo()
    # filter_demo()
    lambda_demo()

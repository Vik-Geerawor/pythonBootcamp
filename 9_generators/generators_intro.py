import random


def gensquares(n):
    for i in range(n):
        yield i ** 2


def gen_random(n, low, high):
    for i in range(n):
        yield random.randint(low, high)


def itr_str(my_string):
    my_string = iter(my_string)
    for letter in my_string:
        yield letter


if __name__ == '__main__':
    print(f"*** Generators ***")

    for x in gensquares(10):
        print(x)

    for num in gen_random(12, 1, 10):
        print(num)

    for letter in itr_str('hello'):
        print(letter)

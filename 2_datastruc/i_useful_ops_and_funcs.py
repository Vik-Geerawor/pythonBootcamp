import datetime
from random import shuffle, randint


def range_demo():
    for i in range(0, 10, 2):
        print(i)


def enumerate_demo():
    shopping_list = ['tea', 'sugar', 'milk', 'eggs', 'bread', 'butter', 'cheese']
    for i, j in enumerate(shopping_list):
        print(f"Index {i}: Item: {j}")


def zip_demo():
    shopping_list = ['tea', 'sugar', 'milk', 'eggs', 'bread', 'butter', 'cheese']
    quantity = [2, 1, 1, 12, 1, 1, 2]
    unit = ['bag', 'bag', 'bottle', 'unit', 'loaf', 'box', 'brick']
    for i, j, k in zip(quantity, unit, shopping_list):
        print(f"{i} {j}(s) of {k}")


def in_demo():
    shopping_list = ['tea', 'sugar', 'milk', 'eggs', 'bread', 'butter', 'cheese']
    if 'sugar' in shopping_list:
        print("Sugar is in shopping list")


def min_demo():
    quantity = [2, 1, 1, 12, 1, 1, 2]
    print(f"Min. value in list: {min(quantity)}")


def max_demo():
    quantity = [2, 1, 1, 12, 1, 1, 2]
    print(f"Max. value in list: {max(quantity)}")


def shuffle_demo():
    quantity = [2, 1, 1, 12, 1, 1, 2]
    shuffle(quantity)           # shuffles the list itself
    print(quantity)


def randint_demo():
    main = []
    star = []
    for i in range(1, 6):
        number = randint(1, 49)
        main.append(number)
    for i in range(1, 3):
        number = randint(1, 11)
        star.append(number)
    print(f"Main: {main}")
    print(f"Star: {star}")

    result = main + star
    print(f"Result: {result}")


def input_demo():
    name = input("Enter your name: ")
    dob = input("Enter your date of birth (dd/mm/yyyy): ")  # all inputs are str
    dob = datetime.datetime.strptime(dob, '%d/%m/%Y')
    print(
        f"Your name is {name.title()} and you were born on "
        f"the {dob.day}th of {dob.strftime('%B')}, {dob.year}"
    )


def list_comprehension_demo():
    odd_num = [x for x in range(1, 10) if x % 2 == 1]
    print(f"{odd_num}")


if __name__ == '__main__':
    print(f"*** USEFUL OPERATORS AND FUNCTIONS ***")
    # range_demo()
    # enumerate_demo()
    # zip_demo()
    # in_demo()
    # min_demo()
    # max_demo()
    # shuffle_demo()
    # randint_demo()
    # input_demo()
    list_comprehension_demo()


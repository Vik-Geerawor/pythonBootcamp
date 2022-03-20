import math
import random


def rounding_demo():
    value = 4.63
    print(f"Value = {value}")
    print(f"\tmath.floor: {math.floor(value)}")
    print(f"\tmath.ceil: {math.ceil(value)}")


def math_constants_demo():
    print(f"pi = {math.pi}")
    print(f"Euler's number e = {math.e}")
    print(f"tau = {math.tau}")      # ration between circumference and radius


def logarithm_demo():
    print(f"Log base e = {math.log(math.e)}")
    print(f"Log base 10 = {math.log(100, 10)}")


def trigonometry_demo():
    print(f"sin 10: {math.sin(10)}")
    print(f"pi/2 in deg: {math.degrees(math.pi/2)}")
    print(f"radians of 180: {math.radians(180)}")


def random_demo():
    print(f"A random no. between 0 and 100: {random.randint(0, 100)}")

    print(f"Setting a seed of 100")
    {random.seed(100)}
    print(f"\tA seeded random number: {random.randint(0, 100)}")
    print(f"\tA seeded random number: {random.randint(0, 100)}")
    print(f"\tA seeded random number: {random.randint(0, 100)}")

    print(f"Setting a seed of 100")
    {random.seed(100)}          # change this to see the diff
    print(f"\tA seeded random number: {random.randint(0, 100)}")
    print(f"\tA seeded random number: {random.randint(0, 100)}")
    print(f"\tA seeded random number: {random.randint(0, 100)}")

    # Comment out the seeding before proceeding
    print(f"Playing Lotto")
    my_list = list(range(1, 49))
    print(f"\tChoose 5 with replacement: {random.choices(my_list, k=5)}")
    print(f"\tChoose 5 without replacement: {random.sample(my_list, 5)}")

    print(f"Shuffling a list")
    print(f"\tA list: {my_list}")
    random.shuffle(my_list)             # in place
    print(f"\tAfter shuffle: {my_list}")

    print(f"Continuous Random Variable if a uniform distribution")
    print(f"\tx = {random.uniform(0, 100)}")

    print(f"Normal/Gaussian Distribution")
    print(f"\tRandom num - mu=0 & var=1: {random.gauss(0, 1)}")


if __name__ == '__main__':
    print(f"*** Math and Random ***")
    # help(math)
    # rounding_demo()
    # math_constants_demo()
    # logarithm_demo()
    # trigonometry_demo()
    random_demo()


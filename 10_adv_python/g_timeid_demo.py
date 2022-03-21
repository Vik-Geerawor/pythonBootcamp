import time
import timeit
import inspect


def func_one(n):
    # for each num in range, convert to str and add to list
    # return list
    return [str(num) for num in range(n)]


def func_two(n):
    # for each num in range, apply str()
    # add to list and return the list
    return list(map(str, range(n)))


def large_block(func_name, n):
    # current time before
    start_time = time.time()

    # run code
    func_name(n)

    # current time after
    end_time = time.time()

    # elapsed time
    elapsed_time = end_time - start_time
    print(f"{func_name.__name__} took: {elapsed_time} to run")


def timeit_demo(func_name):
    func_def = inspect.getsource(func_name)

    stmt = f"""{func_name.__name__}(100)"""
    setup = f"""{func_def}"""

    return timeit.timeit(stmt=stmt, setup=setup, number=100000)


if __name__ == '__main__':
    print(f"*** Performance Measurement ***")
    # large_block(func_one, 100000)
    # large_block(func_two, 100000)

    func_name = func_one
    print(f"{func_name.__name__}: {timeit_demo(func_name)}")
    func_name = func_two
    print(f"{func_name.__name__}: {timeit_demo(func_two)}")



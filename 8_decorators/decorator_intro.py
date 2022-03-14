def decorate_func(func):
    def wrap_it():
        print(f"*** Beautiful Function ***")
        print(f"{func()}")
        print(f"*** End of Decoration ***")

    return wrap_it


@decorate_func            # toggle comment to see difference
def a_func():
    return 'A Function'


if __name__ == '__main__':
    print(f"*** Decorators ***")
    print(f"{a_func()}")

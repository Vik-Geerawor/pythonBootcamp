def args_demo(*args):
    return list(args)


def myfunc(my_string):
    result = []
    counter = 1
    for letter in my_string:
        if counter % 2 == 0:     # even
            result.append(letter.upper())
        else:
            result.append(letter.lower())
        counter += 1
    return ''.join(result)      # list to string


if __name__ == '__main__':
    print(f"\n*** Functions ***")

    snake_string = myfunc('Anthropomorphism')
    print(snake_string)

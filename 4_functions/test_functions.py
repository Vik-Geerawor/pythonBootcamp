def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:        # even numbers
        if a < b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b


def animal_crackers(my_string):
    new_string = my_string.split(' ')
    print(new_string)
    if new_string[0][0] == new_string[1][0]:
        return True
    else:
        return False


def makes_twenty(a, b):
    if a == 20 or b == 20 or a + b == 20:
        return True
    else:
        return False


def old_macdonald(name):
    my_list = []
    counter = 1
    for letter in name:
        if counter == 1 or counter == 4:
            my_list.append(letter.upper())
        else:
            my_list.append(letter)
        counter += 1
    return ''.join(my_list)


def master_yoga(sentence):
    return sentence[::-1]


def almost_there(a):
    if 90 <= a <= 110 or 190 <= a <= 210:
        return True
    else:
        return False


def find33(list_int):
    previous_int = ''
    for n in list_int:
        if n == previous_int:
            return True
        previous_int = n
    return False


def paper_roll(string):
    result = []
    for letter in string:
        result.append(letter * 3)
    return ''.join(result)


def black_jack(a, b, c):
    sum = a + b + c
    if sum <= 21:
        return sum
    elif sum > 21 and (a == 11 or b == 11 or c == 11):
        return sum - 10
    elif sum > 21:
        return 'BUST'


def summer_69(list_of_int):
    six_nine_flag = False
    result = 0
    temp = 0

    for n in list_of_int:
        # check if n is a 6
        if n == 6:
            six_nine_flag = True
        # while we don't have a 6, add to result
        while not six_nine_flag:
            result += n
            break
        # until we find a 9, add to temp
        while six_nine_flag:
            temp += n
            if n == 9:
                six_nine_flag = False
                temp = 0
            break
    result = result + temp
    return result


def spy_game(my_list):
    a = False
    b = False

    for n in my_list:
        if not a and not b and n == 0:
            a = True        # first 0
        elif a and not b and n == 0:
            b = True        # second 0
        elif a and b and n == 7:
            return True     # found 007
        else:
            a = b = False   # restart from 0

    return False            # 007 not found and end of list


def count_primes(number):
    div_by_two = div_by_three = div_by_five = div_by_seven = False

    n = 2
    i = 0
    while n <= number:
        # check if n is a prime number
        if n != 2 and n % 2 == 0:
            div_by_two = True
        elif n != 3 and n % 3 == 0:
            div_by_three = True
        elif n != 5 and n % 5 == 0:
            div_by_five = True
        elif n != 7 and n % 7 == 0:
            div_by_seven = True

        if not (div_by_two or div_by_three or div_by_five or div_by_seven):
            # print(f"{n} is a prime number")
            i += 1
        # else:
            # print(f"{n} is not a prime number")
        n += 1
        div_by_two = div_by_three = div_by_five = div_by_seven = False
    print(f"Count of prime numbers upto {number}: {i}")


def print_big(letter):
    pattern_dict = {
        'a': '  *  \n * * \n*****\n*   *\n*   *',
        'b': '*****\n*   *\n*****\n*   *\n*****',
        'c': '*****\n*\n*\n*\n*****'
    }
    if letter == 'a':
        return pattern_dict['a']
    elif letter == 'b':
        return pattern_dict['b']
    elif letter == 'c':
        return pattern_dict['c']


if __name__ == '__main__':
    print(f"\n*** Function Test ***")
    # print(lesser_of_two_evens(2, 5))
    # print(animal_crackers('hello horld'))
    # print(makes_twenty(2, 8))
    # print(old_macdonald('world'))
    # print(master_yoga('downward facing dog'))
    # print(almost_there(104))
    # print(find33([ 3, 1, 3]))
    # print(paper_roll('abc'))
    # print(black_jack(9, 9, 9))
    # print(summer_69([1, 2, 6, 3, 9, 1, 2, 6, 1, 2, 9, 1, 2]))
    # print(spy_game([1, 2, 4, 0, 0, 7, 5]))
    # count_primes(100)
    print(print_big('c'))

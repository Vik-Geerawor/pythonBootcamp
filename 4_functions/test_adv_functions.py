import string


def vol(rad):
    PI = 3.14
    return 4 / 3 * PI * rad ** 3


def ran_check(num, low, high):
    return low <= num <= high


def up_low(s):
    up_counter = 0
    low_counter = 0

    for letter in s:
        if letter.isupper():
            up_counter += 1
        elif letter.islower():
            low_counter += 1

    print(f"String: {s}")
    print(f"No. of upper case letters: {up_counter}")
    print(f"No. of lower case letters: {low_counter}")


def unique_list(lst):
    uniq_list = []

    for item in lst:
        if item not in uniq_list:
            uniq_list.append(item)

    return uniq_list


def multiply(numbers):
    result = 0
    i = 1

    for item in numbers:
        i *= item

    result += i
    return result


def palindrome(s):
    return s == s[::-1]


def ispangram(str1, alphabet=string.ascii_lowercase):
    s = list(str1.replace(" ", "").lower())
    s.sort()

    my_alphabet = list(alphabet)
    print(my_alphabet)
    print(s)
    flag = False
    for letter in my_alphabet:
        if letter in s:
            flag = True
        else:
            flag = False
            break
    return flag


if __name__ == "__main__":
    print(f"\n*** Advanced Functions ***")
    # print(f"Volume of r = 2: {vol(2)}")
    # print(f"5 <= 2 <= 10?: {ran_check(2, 5, 10)}")
    # up_low("Hello Mr. Rogers, how are you this fine Tuesday?")
    # print(unique_list([1, 1, 2, 3, 4, 4, 6, 7, 8, 8, 8, 8, 9]))
    # print(multiply([1, 2, 3, -4]))
    # print(palindrome("ollo"))
    print(ispangram("The quick brown fox jumps over the lazy do"))

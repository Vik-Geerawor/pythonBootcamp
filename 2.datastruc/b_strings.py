import datetime


def simple():
    print("hello world")
    print(r"C:\User\Vik")   # raw string, i.e. ignore escape char


def slicing():
    word = "Python"
    print(word[2:4])    # return "th"
    # N.B. the char at the end index is excluded

    print(word[-2])  # returns "o", -1 index is the last char
    print(word[:2])  # returns "Py", start ind defaults to 0
    print(word[4:])  # returns "on", end ind defaults to length of string
    print(word[0::2])  # returns "Pto"

    print(len(word))  # returns 6


def multi_line():
    print("""\
    Usage: thingy [OPTIONS]
        -h		Display this usage message
        -H hostname	Hostname to connect to
    """)


def methods():
    word = "Python"
    print(word.upper())
    sentence = "Hi, my name is Vik"
    print(sentence.split())     # split using white space
    print(sentence.split(","))  # split using ","


def f_string():
    name = 'Vik'
    print(f"\nMy name is {name}")
    print(f"My name is {name:2.1s}")

    num = 12345.123
    print(f"Number = {num}")
    print(f"Number = {num:{10}.{2}f}")      # nested expr eval to the one below
    print(f"Number = {num:10.2f}")

    today = datetime.date.today()
    date_time = datetime.datetime.now()
    print(f"\n{today:%b %d, %Y}")
    print(f"{date_time:%b %d, %Y %Hh%M}")


if __name__ == '__main__':
    print("\n*** STRINGS ***")

    f_string()

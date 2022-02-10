def if_statement():
    score = 64

    if score < 50:
        print(f"Fail")
    elif 50 <= score < 60:
        print(f"Pass")
    elif 60 <= score < 70:
        print(f"Merit")
    elif score >= 70:
        print(f"Distinction")
    else:
        print(f"Undefined")


if __name__ == '__main__':
    print(f"\n*** Conditionals ***")
    if_statement()

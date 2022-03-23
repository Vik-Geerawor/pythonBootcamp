import sys

if __name__ == '__main__':
    print(f"*** sys argv ***")
    print(f"No. of args: {len(sys.argv)}")
    print(f"Args: {sys.argv}")

    # forcing user to provide a filename as an argument
    if len(sys.argv) < 2:
        print(f"Please provide a filename to process")
    else:
        for arg in sys.argv:
            print(f"{arg}")

# create a file and write a line
def create_file():
    with open('myfile.txt', mode='w') as file:
        print(f"File {file.name} created")
        file.write('This is the first line\n')


# append to an existing file
def write_file():
    with open('myfile.txt', mode='a') as file:
        file.write('This is the second line\n')


# read from an existing file
def read_file():
    with open('myfile.txt', mode='r') as file:
        contents = file.read()
        print(f"\nContents of {file.name} is as follows:\n{contents}")


# read one line at a time from an existing file
def readlines_file():
    with open('myfile.txt', mode='r') as file:
        contents = file.readlines()         # returns a list of strings
        print(f"\nContents of {file.name} is as follows:")
        # each element is processed/printed in its own line in for loop
        for line in contents:
            # strip '\n' from the RHS of the string
            print(line.rstrip('\n'))


if __name__ == '__main__':
    print("\n*** Basic IO ***")
    create_file()
    write_file()
    read_file()
    readlines_file()

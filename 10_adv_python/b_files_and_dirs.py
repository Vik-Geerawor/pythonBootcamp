import os
import shutil


def file_exists(path):
    if os.path.isfile(path):
        return True
    else:
        return False

def write_file(text):
    with open('test_file.txt', 'a') as file:
        file.write(text)


def list_files(path):
    print(f"Current dir: {os.getcwd()}")
    print(f"Files in {path}:")
    for file in os.listdir(path):
        print(file)


def move_file(source, destination):
    shutil.move(source, destination)                       # TODO


def traverse_dir(path):
    for a, b, c in os.walk(path):
        print(f"Directory: {a}")
        if len(b) > 0:
            print(f"\tSub Directories:")
            for dir in b:
                print(f"\t\t{dir}")
        if len(c) > 0:
            print(f"\tFiles:")
            for file in c:
                print(f"\t\t{file}")


def delete_file(path, option):
    if option == 'f':
        os.unlink(path)         # deletes a file
    elif option == 'd':
        os.rmdir(path)          # deletes a non-empty directory
    elif option == 'p':
        shutil.rmtree(path)     # permanently deletes a non-empty directory
    else:
        print(f"Please specify an option: f for file, d for directory or " +
              f"p for permanent delete")


if __name__ == '__main__':
    print(f"*** Files and Directories ***")

    file = '/tmp/file1.txt'
    print(f"{file} is a file: {file_exists(file)}")
    # write_file('A line of text\n')
    # list_files('/home/vik/Documents')
    # move_file('/tmp/test1/file1.txt', '/tmp/test3/sub1/file2.txt')
    # delete_file('/tmp/test3/sub1/file2.txt', 'f')
    # traverse_dir('/tmp/test1')

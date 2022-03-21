import shutil
import os
import re
import b_files_and_dirs as fd


def unzip_file(a_path):
    a_path = 'unzip_me_for_instructions.zip'
    shutil.unpack_archive(a_path, os.getcwd(), 'zip')


def get_files(file_path):
    my_files = []
    for a, b, c in os.walk(file_path):
        relative_path = a
        if len(c) > 0:
            for a_file in c:
                relative_path = a + '/' + a_file
                my_files.append(relative_path)
    return my_files


def find_tel(a_file):
    with open(a_file, 'r') as my_file:
        tels = re.findall(r'\d{3}-\d{3}-\d{4}', my_file.read())

    if len(tels) > 0:
        # print(f"{a_file}:")
        # for tel in tels:
            # print(f"\t{tel}")
        return [a_file, tels]
    else:
        return -1


if __name__ == '__main__':
    print(f"*** Advance Python Module Test ***")

    # unzip the files
    # path = 'unzip_me_for_instructions.zip'
    # unzip_file(path)

    # get the list of files
    path = 'extracted_content'
    files = get_files(path)

    # search each file and save successful result in a list
    result = []
    print(f"No. of files: {len(files)}")
    for file in files:
        if not os.path.isfile(file):
            print(f"{file} is not a valid file")
        else:
            output = find_tel(file)
            if output != -1:
                print(f"{output[0]}:")
                for tel in output[1]:
                    print(f"\t{tel}")



import shutil
import os

def unzip_file(path):
    path = 'unzip_me_for_instructions.zip'
    shutil.unpack_archive(path, os.getcwd(), 'zip')


if __name__ == '__main__':
    print(f"*** Advance Python Module Test ***")

    file = 'unzip_me_for_instructions.zip'
    shutil.unpack_archive(file, os.getcwd(), 'zip')

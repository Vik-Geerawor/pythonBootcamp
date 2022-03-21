import os
import zipfile
import shutil


def zip_compress(a_file, z_file):
    if os.path.isfile(z_file):
        try:
            z_file = zipfile.ZipFile(z_file, 'a')
            z_file.open()
        except:
            print(f"{z_file.filename} already open")
    else:
        # create the file and open for writing
        z_file = zipfile.ZipFile(z_file, 'w')

    # compress files into the zipped file
    z_file.write(a_file, compress_type=zipfile.ZIP_DEFLATED)

    print(f"{a_file} compressed to {z_file.filename}")

    # close the zipped file
    z_file.close()


def zip_extractall(z_file, path):
    # open zipped file in read mode
    z_file = zipfile.ZipFile(z_file, 'r')

    # extract all to the path specified
    z_file.extractall(path)


if __name__ == '__main__':
    print(f"*** Zip and Unzip ***")

    # specify the zipped filename
    zipped_file = 'zipped_file.zip'

    # add a file to the zipped file
    zip_compress('file1.txt', zipped_file)
    zip_compress('file2.txt', zipped_file)

    # extract all contents
    zip_extractall(zipped_file, "unzipped_files")

    # compress a folder and decompress it using shutil
    shutil.make_archive(base_name='compressed', format='tar', root_dir='unzipped_files')
    shutil.unpack_archive('compressed.tar', 'untarred', format='tar')

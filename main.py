import os
import math
import shutil


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    folder_paths = input('What all the complete folder paths? (comma separated)')
    output_folder_path = input('What is the output folder path?')

    paths = folder_paths.split(',')

    # Verify the provided paths
    path_exists = True
    for path in paths:
        path_exists &= os.path.isdir(path)
    path_exists &= os.path.isdir(output_folder_path)

    if not path_exists:
        print('Non existing path')
        exit(1)

    # Calculate the number of zeros for the new file names creation
    total_number_of_files = 0
    for path in paths:
        files = os.listdir(path)
        total_number_of_files += len(files)
    number_of_zeros = math.ceil(math.log(total_number_of_files, 10)) + 1

    # Rename and copy all the files
    current_file_index = 1
    for path in paths:
        files = os.listdir(path)
        file_name_size_dict = dict()

        # Inside each folder separate the files by their original name size
        for file in files:
            if len(file) in file_name_size_dict:
                file_name_size_dict[len(file)].append(file)
            else:
                file_name_size_dict[len(file)] = [file]

        file_size_keys = list(file_name_size_dict.keys())
        file_size_keys.sort()

        for key in file_size_keys:
            for file in file_name_size_dict[key]:
                extension = file.split('.')[-1]
                new_file_name = 'IMG' + ('{:0' + str(number_of_zeros) + 'd}').format(current_file_index) + '.' + extension
                new_file_path = os.path.join(path, new_file_name)
                old_file_path = os.path.join(path, file)

                # copy file to new location
                shutil.copyfile(old_file_path, new_file_path)







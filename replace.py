import os
import shutil


sequences_dir_name = 'download/brasiliense/others'
list_of_files = os.listdir(sequences_dir_name)

for file_name in list_of_files:
    path_to_file = ('download/brasiliense/others/' + file_name)
    if 'BF45' in open(path_to_file).read():
        print('yes')
        # shutil.move(path_to_file, 'download/brasiliense/pectobacterium_brasiliense')


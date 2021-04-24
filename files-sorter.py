#! /usr/bin/python3

import os
import shutil
from posix import listdir

intro_message = 'This is a script that sorts your files and places them in folders depending   on their extension'

dir_names = ['Documents', 'Pictures', 'Music', 'Coding', 'Videos', 'Design Files', 'Archives']
dir_ext = [
        ('.txt', '.pdf', '.odt'), ('.jpg', '.jpeg', '.tiff', '.png'), 
        ('.wav', '.mp3'), ('.py', '.css', '.html', '.js'), ('.avi', '.mov', '.mkv'),
        ('.cdr', '.psd', '.ai', '.indd'), ('.rar', '.zip', '.tar', '.7z')]

def sortFiles(source_path, dir_name, *types):
    for filename in listdir(source_path):
        for type in types:
            if filename.endswith(type):
                if os.path.isdir(f'{dest_path}/{dir_name}') == False:
                    os.mkdir(f'{dest_path}/{dir_name}')
                dest_dir = f'{dest_path}/{dir_name}'
                src_file = f'{source_path}/{filename}'
                shutil.move(src_file, dest_dir)

print(intro_message)

source_path = input("Source path: ")
dest_path = input("Destination path: ")


if os.path.isdir(dest_path) == False:
    os.mkdir(dest_path)

i = 0
for i in range(len(dir_names)):
    sortFiles(source_path, dir_names[i], dir_ext[i])
    i += 1


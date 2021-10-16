import os
import pathlib


#get folder path
directory = input('Enter Folder Path:\n')
tag = input('Enter File Tag:')
os.chdir(directory)
count = 0
#iterate through folder

for num, file in enumerate(os.listdir()):
    # rename files based on count and criteria and maintain extention
    file_extension = pathlib.Path(file).suffix
    print(f'FILE EXTENSION >> {file_extension}')
    os.rename(file, f'{count}_{tag}{file_extension}')
    count = count+1


print(f'{count} Files Renamed')
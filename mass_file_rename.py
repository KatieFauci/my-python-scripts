import os


#get folder path
directory = input('Enter Folder Path:\n')
tag = input('Enter File Tag:')
os.chdir(directory)
count = 0
#iterate through folder

for num, file in enumerate(os.listdir()):
    #rename files based on counta nd criteria
    os.rename(file, f'{count}_{tag}.jpg')
    count = count+1


print(f'{count} Files Renamed')
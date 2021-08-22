import os


#get folder path
directory = input('Enter Folder Path:\n')
os.chdir(directory)
count = 0
#iterate through folder

for num, file in enumerate(os.listdir()):
    #rename files based on counta nd criteria
    os.rename(file, f'{count}_namtiddies.jpg')
    count = count+1


print(f'{count} Files Renamed')
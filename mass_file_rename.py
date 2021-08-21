import os


#get folder path
directory = input('Enter Folder Path:\n')
os.chdir(directory)

#iterate through folder
for count, file in enumerate(os.listdir()):
    #rename files based on counta nd criteria
    os.rename(file, f'{count}_suga.jpg')
    


print(f'{count} Files Renamed')
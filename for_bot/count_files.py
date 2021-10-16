import os


#get folder path
directory = input('Enter Folder Path:\n')
os.chdir(directory)
count = 0
#iterate through folder

for file in enumerate(os.listdir()):
    count += 1

print(f'NUM FILES >> {count}')
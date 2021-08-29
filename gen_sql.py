import csv


with open('OUTPUT/raw_output_data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        val = row[1]
        val_cut = val[2:len(val)-1]
        #print(bytes(val_cut, encoding='ascii').decode('utf-8'))
        #print(val_cut.encode('utf-8').decode('utf-8'))
        print(b'\xec\x95\xbd\xec\x86\x8d (Promise)'.decode('utf-8'))
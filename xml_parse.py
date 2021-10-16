import csv
import requests
import xml.etree.ElementTree as ET
import xlsxwriter


def clean_data(file):
    # remove blank lines
    with open('OUTPUT/raw_output_data.csv') as raw_file:
        with open('OUTPUT/clean_output_data.csv', 'w') as clean_file:
            writer = csv.writer(clean_file)
            for row in csv.reader(raw_file):
                for col in row:
                    print()



def pull_data(root):
    data = []
    this_id = ''
    mv_id = 1
    for album in root.findall('album'):
        for a_album in album:
            if a_album.tag == 'album_id':
                rel_id = a_album.text
                mv_id = 1
        for child in album.findall('mv'):
            row = []
            #print(this_id)
            row.append(rel_id)
            row.append(mv_id)
            for field in fields:
                if child.tag == field:
                    row.append(child.text)
                if child.tag == 'mv':
                    for sub in child:
                        if sub.tag == field:
                            row.append(sub.text)  

            row.append(f'tn_{rel_id}_{mv_id}.jpg')
            print(row)
            data.append(row)
            mv_id+=1
        
    return data


def save_csv(data, fields):
    #print(data)
    with open('OUTPUT/raw_output_data.csv', 'w', newline= '') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        writer.writerows(data)


def save_xlsx(data, fields):
    workbook = xlsxwriter.Workbook("OUTPUT/data_pull.xlsx")
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    # write header
    for item in fields:
        worksheet.write(row, col, item)
        col+=1
    col = 0
    row+=1
    # iterate over the data and write it out row by row
    for d_row in data:
        col = 0
        #print(d_row)
        for d_item in d_row:
            #print(d_item)
            worksheet.write(row, col, d_item)
            col+=1
        row+=1

    workbook.close()

# Get file path for xml
path = input('File Path: \n')

# fields to collect
fields = ['album_id',
          'mv_id',
          'mv_title', 
          'mv_url',
          'mv_image',]



tree = ET.parse(path)
root = tree.getroot()

save_xlsx(pull_data(root), fields)
#save_csv(pull_data(root),fields)
#clean_data('OUTPUT/raw_output_data.csv')




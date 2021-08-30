import xlsxwriter

def save_xlsx(data):
    workbook = xlsxwriter.Workbook("OUTPUT/data_pull.xlsx")
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    # iterate over the data and write it out row by row
    print(data)
    for d_row in data:
        col = 0
        #print(d_row)
        for d_item in d_row:
            #print(d_item)
            worksheet.write(row, col, d_item)
            col+=1
        row+=1
    workbook.close()



lines = []
file_path = 'INPUT/albumStand.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()


start_val = 'INSERT INTO version VALUES ('
data = []
for line in lines:
    if start_val in line:
        row = []
        raw = line[len(start_val): len(line)-2]
        
        while raw.find(',') > 0:
            #pull Data
            row.append(raw[0:raw.find(',')])
            raw = raw[raw.find(',')+1:len(raw)]
            #print(raw)
        
        data.append(row)

#print(data)
save_xlsx(data)


print(data)
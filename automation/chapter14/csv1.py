import csv

infile = open('example.csv')
infile_reader = csv.reader(infile)
datas = list(infile_reader)
for line in datas:
    for cell in line:
        print(cell)

infile.close()
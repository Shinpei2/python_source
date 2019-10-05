import csv

# outfile = open('output.csv', 'w', newline='')
# outfile_writer = csv.writer(outfile)
# outfile_writer.writerow(['a', 'b', 'c', 'd'])
# outfile_writer.writerow(['Hello World!!', 'becon', 'cider', 'date'])
# outfile_writer.writerow([13, 5, 5, 4])
# outfile.close()

csv_file = open('delim.tsv', 'w', newline='')
csv_writer = csv.writer(csv_file, delimiter='\t', lineterminator='\n\n')
csv_writer.writerow(['a', 'b', 'c', 'd'])
csv_writer.writerow(['Hello World!!', 'becon', 'cider', 'date'])
csv_writer.writerow([13, 5, 5, 4])
csv_file.close()

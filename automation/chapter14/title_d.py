# title_d.py : CSVファイルから1行目を削除する
import os, csv

os.makedirs('headerRemoved', exist_ok=True)


# カレントディレクトリの全てのCSVファイルをループ
dir_list = os.listdir()
print(dir_list)

for filename in dir_list:
    if not filename.endswith('.csv'):
        continue # CSVファイルでないので飛ばす
    print("見出し削除中 " + filename + '...')

    # TODO: CSVファイルを読み込み
    lines = []
    infile =open(filename)
    reader = csv.reader(infile)
    for row in reader:
        # print('ROW #' + str(reader.line_num) + str(row))
        if reader.line_num == 1:
            continue
        lines.append(row)
    infile.close()
    print(lines)

    # TODO: 新規ファイルへの書き込み
    outfile = open(os.path.join('headerRemoved', filename), 'w', newline='')    # パスを設定し、その中で書き込みファイルを作成
    writer = csv.writer(outfile)
    for item in lines:
        writer.writerow(item)
    outfile.close()
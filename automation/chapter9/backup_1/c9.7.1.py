import os, re, shutil

# TODO(1) - 新規フォルダの作成
number = 1
while True:
    folder_name = 'backup_' + str(number)
    # CDに既存のファイルが存在しなければループを抜ける
    if not os.path.exists(folder_name):
        print(folder_name)
        break
    number += 1
os.makedirs(folder_name)
# folder_pass = os.path.abspath('.') + '\\' + folder_name
# print(folder_pass)


# TODO(2) - 「.txt」ファイルの探索
rg = re.compile(r"(.+\.txt)|(.+\.pdf)|(.+\.py)")
for filename in os.listdir('.'):
    mo = rg.search(filename)

    # txt,pdfファイルでなければスキップ
    if mo == None:
        continue

    # ファイルを新規フォルダにコピー
    shutil.copy(filename, folder_name)
    print(f"{filename}を{folder_name}へコピーしました。")

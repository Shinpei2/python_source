import re, os, shutil

rg = re.compile(r"^(.*?)(\d)(\d)(\d)(.*?)$")    # 3桁の連番

# 現在のフォルダ内の全てのファイルを探索
ser_num = 1
for filename in os.listdir('.'):
    mo = rg.search(filename)

    # 正規表現と一致しなければスキップ
    if mo == None:
        continue

    before_part = mo.group(1)
    after_part = mo.group(5)
    # ファイル名が一致しなければスキップ
    if not(filename.startswith(before_part) and filename.endswith(after_part)):
        continue

    dig1 = int(mo.group(4))
    dig2 = int(mo.group(3))
    dig = -1
    new_name = ''
    # 連番が1桁の場合
    if 1 <= ser_num <= 9:
        if dig1 != ser_num:
            dig = ser_num
            new_name = before_part + '00' + str(ser_num) + after_part
            # print(new_name)
    # 連番が2桁の場合
    elif 10 <= ser_num <= 99:
        dig = str(dig2) + str(dig1)
        print(dig)
        if int(dig) != ser_num:
            dig = ser_num
            new_name = before_part + '0' + str(ser_num) + after_part
            # print(new_name)

    ser_num += 1
    # ファイルネームを更新
    if dig != -1:
        # print(f"ファイル名を{filename}から{new_name}に変更します。")
        shutil.move(filename, new_name)

import os, zipfile

os.chdir('C:\\Users\\tskak\\python\\automation\\chapter9')

zip = zipfile.ZipFile('example.zip')
print(zip.namelist())

spam_info = zip.getinfo('spam.txt')
size1 = spam_info.file_size
size2 = spam_info.compress_size
print(size1)
print(size2)
print(f'圧縮ファイルは{round(size1/size2,2)}倍小さい')
'''
while True:
    print('Zipファイルを展開しますか？')
    num = int(input('展開する場合：1  転回しない場合：2\n>>>'))
    if num == 1:
        # print('break')
        break
    elif num == 2:
        exit()
    else:
        print('入力が不正です。')
        continue

zip.extractall()
'''

new_zip = zipfile.ZipFile('new.zip', 'w')
new_zip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)

list1 = os.listdir('C:\\Users\\tskak\\python\\automation\\chapter9\\cats')
pass1 = 'cats'

for item in list1:
    pass_name = pass1 +'\\'+ item
    new_zip.write(pass_name, compress_type=zipfile.ZIP_DEFLATED)
    # print(pass_name)
new_zip.close()

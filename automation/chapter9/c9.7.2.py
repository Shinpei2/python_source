import os

big = 100  # 出力するファイルのサイズ(MB)

# TODO(1) - C:\から全てのディレクトリツリーを渡り歩く
print(f'{big}MB以上のファイルを表示'.center(50,'='))

for folder, subfolders, files in os.walk('C:\\'):
    os.chdir(folder)
    # print('CALLENT DIR: ' + folder)

    # TODO(2) - 100MB以上のファイルを全て表示
    for file in files:
        file_size = os.path.getsize(file)
        # print('FILE OF ' + folder + ': ' + file)
        # print(f'ファイルサイズ: {file_size}バイト)')

        if file_size > big * 10**6:
            print(folder + '\\' + file)

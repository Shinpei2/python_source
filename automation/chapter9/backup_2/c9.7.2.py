import os

max_size = 0
max_file = ''
# C:\から全てのディレクトリツリーを渡り歩く
for folder, subfolders, files in os.walk('C:\\Users\\tskak\\python\\automation\\chapter9'):
    print('CALLENT DIR: ' + folder)

    '''
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folder + ': ' + subfolder)
    '''

    for file in files:
        print('FILE OF ' + folder + ': ' + file)
        print(f'ファイルサイズ: {os.path.getsize(file)}バイト)')

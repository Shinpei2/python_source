import os

### ファイルのパスを調べるための諸関数 ###
'''
# パスを返す関数os.path.join()
my_file = ['accounts.text', 'details.csv', 'invite.docx']
for item in my_file:
    print(os.path.join('C:\\Users\\tskak\\python', item))

# カレントディレクトリの取得、更新
print(os.getcwd())
os.chdir('C:\\Users\\tskak\\python')
print(os.getcwd())
'''


print(os.path.relpath('C:\\Users\\tskak\\python', 'C:\\Users'))
base = os.path.basename('C:\\Users\\tskak\\python\\automation\\chapter8\\file01.py')
dir = os.path.dirname('C:\\Users\\tskak\\python\\automation\\chapter8\\file01.py')
print(base)
print(dir)

# baseとdirを分割してタプルに格納する関数os.path.split(), パス.split(os.sep)
path = 'C:\\Users\\tskak\\python\\automation\\chapter8\\file01.py'
tuple = os.path.split(path)
print(tuple)
tup = list(tuple)
print(tup)

abs_path = 'C:\\Users\\tskak\\python\\automation\\chapter8\\file01.py'
spl = abs_path.split(os.sep)
print(spl)

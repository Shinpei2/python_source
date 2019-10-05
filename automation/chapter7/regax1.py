import re



'''
text = input("テキストを入力\n>>>")
numrg = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
mo = numrg.search(text)
print('電話番号が探索されました: '+mo.group())

text = '090-1111-2222, 090-12223-3445'
numrg = re.compile(r'(\d\d\d)-(\d\d\d\d)-(\d\d\d\d)')
mo = numrg.findall(text)
print(mo.group(0)) # group(0)は正規表現全体を指す
print('電話番号が探索されました: '+mo.group(1) + mo.group(2) + mo.group(3))

reg = re.compile(r'(wo){1,3}?')
text ='I am Batwowowoman'
mo = reg.search(text)
print(mo.group())

text = '090-1111-2222, 090-1223-3445'
numrg = re.compile(r'(\d\d\d)-(\d\d\d\d)-(\d\d\d\d)')
mo = numrg.findall(text)
print(mo) # group(0)は正規表現全体を指す
# print('電話番号が探索されました: '+mo.group(1) + mo.group(2) + mo.group(3)
# moの内側タプルをリストに変換
for i in range(len(mo)):
    mo[i] = list(mo[i])
print(mo)

text = 'a spam is spam and spam'
reg = re.compile(r'[^aiueo]')
mo = reg.findall(text)
print(mo)

text = 'RoboCop is robocop and roBOcop and roboCOP and ROBCOP '
rc = re.compile(r'robocop', re.I)  # 大文字、小文字区別なしで'robocop'を正規表現として格納
mo = rc.findall(text)
print(mo)
mo = rc.sub('***' ,text)
print(mo)

text = 'Agent Alice is a reporter and Agent Bob is a secretary'
regax = re.compile(r'Agent (\w)\w*')
mo = regax.sub(r'\1****', text)
print(mo)

'''

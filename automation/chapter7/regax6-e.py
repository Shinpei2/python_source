import re

def pw_check(text):
    reg = re.compile(r'[a-zA-Z0-9]{8,}')
    mo = reg.search(text)
    if mo == None:
        return print('不正なパスワードです。')
    # print(mo.group())

    # テキスト内の大文字の個数をカウント
    up_count  = 0
    for i in range(len(text)):
        if text[i].isupper():
            up_count += 1

    # テキスト内の小文字の個数をカウント
    low_count = 0
    for i in range(len(text)):
        if text[i].islower():
            low_count += 1

    # テキスト内の数字の個数をカウント
    num_count = 0
    for i in range(len(text)):
        if text[i].isdecimal():
            num_count += 1

    # テキスト内に大文字・小文字・数字をすべて含む場合のみ、強いパスワード表示
    if (up_count > 0) and (low_count > 0) and (num_count > 0):
        print('強いパスワードです。')
    else:
        print('弱いパスワードです。')


print('パスワードの強さチェック'.center(20,'='))
password = input("パスワードを入力してください:\n>>>")
pw_check(password)

#! python3
# phoneAndEmail.py - 電話番号と電子メールアドレスの抽出
import pyperclip, re

"""
▼疑似コード
1． クリップボードからテキストを取得する。
2. テキストから電話番号とメールアドレスを探索する。
3. クリップボードに張り付ける

"""

# 1． クリップボードからテキストを取得する。
text = pyperclip.paste()
# 1. 正規表現の用意
# 電話番号を表す正規表現
phone_reg = re.compile(r'''(
    (\d{1,4}|\(\d{1,4}\))              # 市外局番: 1～4桁
    (\s|-|\.)?                            # 区切り(' 'or'-')
    (\d{1,4})                           # 市内局番: 1～4桁
    (\s|-)                              # 区切り(' 'or'-')
    (\d{3,4})                           # 加入者番号　: 3～4桁
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      # 内線番号
)''', re.VERBOSE)
# print(phone_reg.findall(text))

# メールアドレスを表す正規表現
mail_reg = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           # ユーザー名
    @                           # @
    [a-zA-Z0-9._]+              # ドメイン名
    (\.[a-zA-Z]{2,4})           # .anything
)''', re.VERBOSE)
# print(mail_reg.findall(text))

# 1． クリップボードからテキストを取得する。
text = str(pyperclip.paste())

# 2. テキストから電話番号とメールアドレスを探索する。
# テキストから全ての電話番号を探索し、リストmatchesへ格納
matches = []
for item in phone_reg.findall(text):
    phone_num = '-'.join([item[1], item[3], item[5]])
    if item[8] != '':
        phone_num += ' x' + item[8]
    matches.append(phone_num)
for item in mail_reg.findall(text):
    matches.append(item[0])
# print(matches)


# 3. クリップボードに張り付ける
emalis =  []
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('電話番号とメールアドレスをクリップボードにコピーしました。')
    print('\n'.join(matches))
else:
    print('電話番号とメールアドレスが見つかりませんでした。')

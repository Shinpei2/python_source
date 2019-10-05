#! python3
# bulletPointAdder.py : クリップボードのテキストを各行に

# 1. 点を打って、wikipediaの箇条書きにする
import pyperclip
text = pyperclip.paste()

# 2. TODO: 行を分割して、'*'を追加して、リストlinesに格納
lines = text.split("\r\n")
# print(lines)
for i in range(len(lines)):
    lines[i] = '・' + lines[i]
# print(lines)

# 3. テキストへlinesの要素を連結
text = '\n'.join(lines)
print(text)
pyperclip.copy(text)

import re

def strip2(text):
    reg = re.compile(r'\S+(\s+\S+)*')

    mo = reg.search(text)
    if mo == None:
        return print('不正な入力です。')
    return mo.group()


text = '    HELLO WORLD k  o  ko  ko   sroi   '
print(strip2(text))

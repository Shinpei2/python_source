import re

text = 'carol eats cats.'
reg = re.compile(r'''
    (alice|bob|carol)
    \s
    (eats|pets|throws)
    \s
    (apples|cats|baseballs)
    .$

''', re.I | re.VERBOSE)

mo = reg.search(text)
if mo == None:
    print('None')
else:
    print(mo.group(0))

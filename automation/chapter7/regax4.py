# 7-21
import re

text = 'Satoshi Nakamoto'
reg = re.compile(r'''
    ^([A-Z][a-z]*)
    \s
    (Nakamoto)$
''', re.VERBOSE)

mo = reg.search(text)
if mo == None:
    print('None')
else:
    print(mo.group(0))

import re

text = '123,123,123,123,123'
reg = re.compile(r'''
^([1-9]{1}\d{0,2})
(,\d{3})*$
''', re.VERBOSE)

mo = reg.search(text)
if mo == None:
    print('None')
else:
    print(mo.group(0))

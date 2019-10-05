import os
import shelve

'''
outfile = open('test.txt', 'a')
outfile.write('Hello world!\n')

lis = ['Hello,world!1\n', 'Hello,world!2\n', 'Hello,world!3\n']
for item in lis:
    outfile.write(item)

outfile.close()
'''

s_file = shelve.open('catdata')
cat_list = ['zophie', 'tama', 'mike']
s_file['cats'] = cat_list
s_file.close()

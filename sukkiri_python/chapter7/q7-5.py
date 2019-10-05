'''
intext = input("コピー元のファイル名を入力して下さい。(***.txt) >>>")
infile = open(intext, 'r')
outtext = input("コピー先のファイル名を入力して下さい。(***.txt) >>>")
outfile = open(outtext, 'w')

for line in infile:
    text = line # infileの1行相当をtextへ格納
    outfile.write(text) # textをoutfileへ書き込み＋自動改行
print("コピー完了！")
infile.close()
'''

py = 'python'
li = list(py)
oi = ''.join(li)
print(oi)

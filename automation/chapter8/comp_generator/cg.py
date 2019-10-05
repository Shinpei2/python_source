#! python3
# cg.py : テキストファイル内の4品詞を書き換えるプログラム
# CL引数にテキストファイルの絶対パスを指定
# 未達事項：①'.'と','の処理　②改行の処理

import sys, os, re

argv = sys.argv

# 読み込みファイルのチェック(CL引数：ファイル名)
if len(argv) != 2:
    print('コマンドライン引数の数が異なります。')
    exit()

if open(argv[1]) == None:       # open()の戻り値：Fileオブジェクト
    print('テキストファイルが見つかりません')
    exit()

# 読み込みファイル、書込みファイルを開く
infile = open(argv[1], 'r')
outfile = open('gen_text.txt', 'w')
origin_text = re.split(" |\.|,|\n",infile.read())
print(origin_text)


# ADJECTIVE, NOUN, VERB, ADVERBを表す正規表現の作成 ※正規表現を書くとき、スペース空けちゃだめ
rg = re.compile(r'ADJECTIVE|NOUN|VERB(\.|,)?|ADVERB(\.|,)?')
# rg_adj = re.compile(r'ADJECTIVE')
# rg_noun = re.compile(r'NOUN')
# rg_verb = re.compile(r'VERB')
# rg_adv = re.compile(r'ADVERB')

# 正規表現と一致する文字列を探索
convert_list = []
for item in origin_text:
    print(item)
    mo = rg.search(item)
    if mo == None:
        print('None')
        continue
    else:
        convert_list.append(mo.group())
print(convert_list)
# 変換する文字列の入力を受け付け
convert_count = 0
while convert_count < len(convert_list):
    # 全文字列を探索
    for i in range(len(origin_text)):
        if origin_text[i] == convert_list[convert_count]:
            # 文字列の変換
            word = convert_list[convert_count].lower()
            print(f'Enter an {word}:')
            origin_text[i] = input('')
    convert_count += 1
new_text = ' '.join(origin_text)
print(new_text)

# 文字列の結合&変換後のテキストをファイルに出力
outfile.write(new_text)

# ファイルを閉じる
infile.close()
outfile.close()

#! python3
# mcb.pyw クリップボードの保存・復元
# Usage:
# py.exe mcb.pyw save <keyword> - クリップボードをキーワードに紐づけて保存
# py.exe mcb.pyw <keyword> - キーワードに紐づけられたテキストをクリップボードにコピー
# py.exe mcb pyw list - 全キーワードをクリップボードにコピー

import sys, pyperclip, shelve

mcbs = shelve.open('mcb') # バイナリファイルmcbsの作成
argv = sys.argv

# クリップからmcbsへの書き込み
if len(argv) == 3 and argv[1].lower() == 'save':
    # read  from clip_board and write it in mcbs
    mcbs[sys.argv[2]] = pyperclip.paste()

# CL引数が2であれば
elif len(argv) == 2:
    # キーワード一覧コピー
    if argv[1] == 'list':
        pyperclip.copy(str(list(mcbs.keys())))
    # 特定のキーワードのコピー
    elif argv[1] in mcbs:
        pyperclip.copy(mcbs[argv[1]])

mcbs.close()

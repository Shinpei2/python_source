#! python3
# パスワード管理プログラム（脆弱性あり）

PASSWORD = {'email': 'F7minBDDuvMjuESSKHFhTxFtjVB6',
            'blog': 'VmAlvQyKAxiVH5G8v01if1MLZF3sdt',
            'luggage': '12345'}

import sys
import pyperclip
if len(sys.argv) < 2:
    print('使い方: python pw.py [アカウント名]')
    print('パスワードをクリップボードにコピーします')
    sys.exit()

account = sys.argv[1] # 第1のコマンドライン引数がアカウント名


if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print(account + 'のパスワードをクリップボードにコピーします。')
else:
    print(account + 'というアカウント名は存在しません。')

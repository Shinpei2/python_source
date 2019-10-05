import re, os, shutil


# 米国式日付用の正規表現
rgx = re.compile(r"""
    ^(.*?)              # 全テキスト
    ((0|1)?\d)-         # 月を表す1,2桁の数字
    ((0|1|2|3)?\d)-     # 日を表す1,2桁の数字
    ((19|20)\d\d)       # 年を表す4桁の数字
    (.*?)$              # 日付後の全テキスト
""", re.VERBOSE)

""" ※groupの番号
    ^(1)              # 全テキスト
    ((2)3)-         # 月を表す1,2桁の数字
    ((4)5)-     # 日を表す1,2桁の数字
    ((6)7)       # 年を表す4桁の数字
    (8)$              # 日付後の全テキスト
"""


# TODO(1) - CDの全ファイルをループ
for amer_ver in os.listdir('.'):
    mo = rgx.search(amer_ver)

    # TODO(2) - 日付の無いファイルをスキップ
    if mo == None:
        continue

    # TODO(3) - ファイル名を部分分解
    before = mo.group(1)
    month = mo.group(2)
    day = mo.group(4)
    year = mo.group(6)
    after = mo.group(8)

    # TODO(4) - 欧州式の日付ファイルを作成
    euro_ver = before + day + '-' + month + '-' + year + after

    # TODO(5) - ファイル名を変更 shutil.move()
    # print(f"ファイル名を「{amer_ver}」から「{euro_ver}」に変更します。")
    shutil.move(amer_ver, euro_ver)

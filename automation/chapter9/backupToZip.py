#! python3
# backupToZip.py

import zipfile, os

def backup_to_zip(folder):
    # フォルダ全体をZIPファイルにバックアップ

    folder = os.path.abspath(folder)    # folderを絶対パスに

    # TODO(1) - 既存のファイル名からファイル名の連番を決定
    number = 1
    while True:
        zip_name = os.path.basename(folder) + '_' + str(number) + '.zip'
        # CDに既存のファイルが存在しなければループを抜ける
        if not os.path.exists(zip_name):
            break
        number += 1

    # TODO(2) - ZIPファイルの作成
    print(zip_name)
    backup_zip = zipfile.ZipFile(zip_name, 'w')

    # folder内の全てのファイルを渡り歩いてファイルを全て圧縮
    for folder, subfolders, files in os.walk(folder):
        print(f"ZIPファイルに{folder}内のファイルを追加します。")
        # 現在のフォルダを追加
        backup_zip.write(folder)
        # 現在のフォルダ内の全ファイルをZIPファイルに追加
        for item in files:
            # ZIPファイル('ファイル名_….zip')はバックアップしない
            new_base = os.path.basename(folder) + '_'
            if item.startswith(new_base) and item.endswith('.zip'):
                continue
            backup_zip.write(os.path.join(folder, item))

    backup_zip.close()
    print('Done')

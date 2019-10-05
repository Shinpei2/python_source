import subprocess, sys, os

# editor_pass = 'C:\\Users\\tskak\\C_lang\\c_study\\editor\\editor.exe'
# subprocess.Popen(editor_pass, executable=editor_pass)     # 記述は、この形式で！

# 現状では、pythonでpythonファイルを開くと上手くいかない
# filename = input('ファイル名を入力して下さい>>> ')
# filePath = os.path.join(os.getcwd(), filename)    # CDのファイルパスを格納
# subprocess.Popen([sys.executable, filename])

ff_pass = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
subprocess.Popen(ff_pass, executable=ff_pass)

ALIVE案
1. ALIVEの通常出勤画面まで自動遷移するPG　→　タスクスケジューラでPC起動時に開くように設定
2. 17:30になったら、ALIVEの退勤画面に自動遷移するPG　→タスクスケジューラで、17:30にプログラムを実行するように設定
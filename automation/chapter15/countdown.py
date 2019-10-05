#! python3
# countdown.py - シンプルなカウントダウンスクリプト

import time, subprocess

# カウントダウン
time_left = 10
while time_left > 0:
    print(time_left)
    time.sleep(1)
    time_left -= 1

subprocess.Popen(['start', 'Love Saver Undercover.mp3'], shell=True)



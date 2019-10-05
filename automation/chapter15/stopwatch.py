#! python
# stopwatch.py - the simple stop watch program

import time

# print the description of the program
print('------------ストップウォッチ------------')
print('Enterを押すと開始します。')
print('その後、Enterを押すと経過時間を表示します。')
print('Ctrl+Cで強制終了します。')
print('----------------------------------------')


input()
print('スタート')
start_time = time.time()
last_time = time.time()
lap_num = 1

#! ラップタイムの計測
try:
    while True:
        input()
        now = time.time()
        lap_time = round(now - last_time, 2)
        total_time = round(now - start_time, 2)
        print(f'ラップ数：{lap_num} ラップタイム：{lap_time}  (総タイム:{total_time}))', end='')
        lap_num += 1
        last_time = now
except KeyboardInterrupt:
    # Ctrl-C : 例外処理して、エラーメッセージを表示しないようにする
    print('\n終了')
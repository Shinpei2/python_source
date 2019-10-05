import time

# 注意点：time.sleepは途中で強制終了が出来ない
# 時間指定する場合は、for文で回すようにする
# for i in range(3):
#     print('Tick')
#     time.sleep(1)
#     print('Tock')
#     time.sleep(1)

now = time.time()
print(now)
print(round(now,2))
print(round(now,4))
print(round(now))

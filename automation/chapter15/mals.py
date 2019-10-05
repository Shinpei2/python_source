import time, datetime, threading

# start_time = datetime.datetime(2029, 10, 31, 0, 0, 0)

# while datetime.datetime.now() < start_time:
#     time.sleep()

# print('当プログラムは2029年のHelloweenに開始しました')

# ----------------------------------------------------------------------- #
# マルチスレッド：コード内の異なる行を同時に実行可能　→threadingモジュール
# ※スレッド間での変数書き換えに注意　☆呼び出し関数内では、ローカル変数のみを用いるようにする
# print('プログラム開始')

# def nap():
#     time.sleep(5)
#     print('起きた！')

# thread_obj = threading.Thread(target=nap)   # ()着けない点に注意：関数そのものを呼び出すわけではないため
# thread_obj.start()  # Threadオブジェクトは別スレッド内で実行される

# print('プログラム終了')     # 「起きた」よりも早く表示される

# ----------------------------------------------------------------------- #

thr = threading.Thread(target=print, args=['Cat', 'Dog', 'Frogs'], kwargs={'sep':' & '})

thr.start()
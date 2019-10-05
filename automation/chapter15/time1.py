import time

def calc_prd():
    product = 1
    for i in range(1,100000):
        product = product * i
    return product

# calc_prd()の呼び出し前後の時間を取得し、その差異で計算時間を計算する
start_time = time.time()
prod = calc_prd()
end_time = time.time()
print(f'計算結果は{len(str(prod))}桁です。')
print('計算時間は{}秒でした。'.format(end_time - start_time))

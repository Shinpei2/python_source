count = 1
print("カレーを召し上がれ")
while True:
    print(f"{count}皿のカレーを食べました。")
    while True:
        key = input("おかわりはいかがですか？(y/n)>>")
        if key in ["y","n"]:
            break
        else:
            print("yかnを入力して下さい。")
    if key == 'y':
        count += 1
    else:
        break
print("ごちそうさまでした。")

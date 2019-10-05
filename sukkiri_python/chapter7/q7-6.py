from random import randint

print("数当てゲームを始めます。3桁の数を当ててください１")

answer = list()
for i in range(3):
    answer.append(randint(0,9))
print(answer)

while True:
    prediction = list()
    for i in range(3):
        prediction.append(int(input(f"{3-i}桁目の予想を入力(0~9)>>>")))
    print(prediction)

    pos = 0
    num = 0

    # coressponding check
    for i in range(3):
        # position check
        if answer[i] == prediction[i]:
            pos += 1
            continue
        else:
            # number check
            for j in range(3):
                if answer[i] == prediction[j]:
                    num += 1
                    break

    print("{}ヒット！{}ボール！".format(pos,num))
    if  pos == 3:
        print("正解です！")
        break

    while True:
        cont = int(input("続けますか？ 1: 続ける　2: 終了"))
        if cont == 1:
            break
        elif cont == 2:
            ans = ''.join(str(answer))
            print(f"正解は{ans}でした。")
            exit(0)
        else:
            print("不正な値です。")

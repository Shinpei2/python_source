subject = []
score = []

# 1科目目の受付
subject.append(input("1科目目の科目名を入力して下さい :"))
score.append(input("1科目目の点数を入力して下さい :"))
sub_num = 1

# 追加強化の受付
while True:
    print("追加する教科はありますか？")
    # prompt inputting until user inputs 1 or 0
    while True:
        next = int(input("ある場合：1    ない場合：2"))
        if  next == 1 or next == 2:
            break
        else:
            print("1または2を入力して下さい。")

    # nextが1の場合は科目と点数をリストに追加、それ以外の場合はループを抜ける
    if next == 1:
        sub_num += 1
        subject.append(input(f"{sub_num}科目目の科目名を入力して下さい :"))
        score.append(input(f"{sub_num}科目目の点数を入力して下さい :"))
    else:
        break

 # 点数の表示
sum = 0
avg = 0
for i in range(len(subject)):
    print(f"教科: {subject[i]}  点数:{score[i]}")
    sum += int(score[i])
avg = sum / len(subject)
print(f"合計: {sum}  平均:{avg: 1f}")

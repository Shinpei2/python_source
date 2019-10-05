score = []
score.append(int(input("国語の点数を入力して下さい: )")))
score.append(int(input("数学の点数を入力して下さい: )")))
score.append(int(input("理科の点数を入力して下さい: )")))
score.append(int(input("社会の点数を入力して下さい: )")))
score.append(int(input("英語の点数を入力して下さい: )")))

print(f"合計：{sum(score)}  平均点：{sum(score) / len(score)}")

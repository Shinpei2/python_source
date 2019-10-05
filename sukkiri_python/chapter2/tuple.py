scores = (100,90,80,70,60,50)

print(f"タプル：{scores}")

sum = 0
for i in range(len(scores)):
    print(f"タプルの{i}番目の要素の値：{scores[i]}")
    sum += scores[i]

print(f"要素数は{len(scores)}個")
print(f"合計：{sum}")
print("平均:{}".format(sum/len(scores)))

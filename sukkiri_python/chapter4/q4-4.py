print("##### 九九の全表示 #####")
for i in range(1,10,1):
    for j in range(1,10,1):
        print(f"{i}×{j} = {i * j}")
    print("\n")

print("##### 九九の奇数段のみ表示 #####")
for i in range(1,10,1):
    if i % 2 == 0:
        continue    # 奇数であれば、表示せず次の段へ進む。
    for j in range(1,10,1):
        print(f"{i}×{j} = {i * j}")
    print("\n")

print("##### 九九(50未満の数のみ) #####")
for i in range(1,10,1):
    if i % 2 == 0:
        continue    # 奇数であれば、表示せず次の段へ進む。
    for j in range(1,10,1):
        if i * j > 50:
            break
        print(f"{i}×{j} = {i * j}")
    print("\n")

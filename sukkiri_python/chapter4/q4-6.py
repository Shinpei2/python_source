# (1)
numbers = [1,1]
pointer = 0     # 追加要素のうち、若い番号を指す変数pointer
while True:
    add = numbers[pointer] + numbers[pointer +1]
    if add > 1000:
        break
    numbers.append(add)
    pointer += 1
print(numbers)

# (2)
ratios = []
for i in range(len(numbers) -1):
    add = numbers[i+1] / numbers[i]
    ratios.append(add)
print(ratios)

# (3)   1000倍して、int型に変換後、1000で割る
for i in range(len(ratios)):
    ratios[i] = int(ratios[i] * 1000) / 1000
print(ratios)

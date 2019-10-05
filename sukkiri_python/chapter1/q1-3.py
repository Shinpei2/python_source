height = int(input("身長を入力して下さい: ")) / 100
weight = int(input("体重を入力して下さい: "))
bmi = weight / (height ** 2)
print(f"あなたのBMIは{bmi:.1f}です", end="")

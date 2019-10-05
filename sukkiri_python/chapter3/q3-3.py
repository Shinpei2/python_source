""" (1) """
isError = False
n = 100
if isError == False and n < 100:
    print("表示")
else:
    pass


""" (2) """
num = int(input("値を入力: "))
if num % 2 == 0:
    print("偶数")
else:
    print("奇数")

""" (3) """
greet = input("挨拶を入力： ")

if greet == "こんにちは":
    print("ようこそ！")
elif greet == "景気は?":
    print("ぼちぼちです")
elif greet == "さようなら":
    print("お元気で！")
else:
    print("どうしました?")    

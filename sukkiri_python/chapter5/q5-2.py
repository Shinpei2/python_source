def is_leapyear(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

# Main
year = ""
while True:
    year = input("西暦を数字で入力して下さい。")
    if year.isnumeric():
        year = int(year)
        break
check = is_leapyear(year)
if check:
    print('西暦' + str(year) + '年は、うるう年です。')
else:
    print('西暦' + str(year) + '年は、うるう年ではありません。')

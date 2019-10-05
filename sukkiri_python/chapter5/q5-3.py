def int_input(prompt):
    print(prompt)
    sum = int(input("合計金額を入力して下さい。>>>"))
    number = int(input("参加人数を入力して下さい。>>>"))
    return sum,number

def calc_payment(sum, number=2):
    split_bill = sum / number
    mod = (split_bill) % 100
    if mod == 0:
        person_pay, secretary_pay = int(split_bill), int(split_bill)
    else:
        person_pay = int(split_bill + (100- mod))
        secretary_pay = int(sum - person_pay * (number - 1))
    return person_pay, secretary_pay

def show_payment(person_pay, secretary_pay, number=2):
    print("***** 支払額 *****")
    print(f"1人あたり{person_pay}円({number}人)、幹事は{secretary_pay}円です。")

# Main
prompt = "合計金額と参加人数を入力して下さい"
sum, number = int_input(prompt)
person_pay, secretary_pay = calc_payment(sum,number)
show_payment(person_pay, secretary_pay, number)
print(f"合計金額検算: {secretary_pay +  person_pay* (number - 1)}円")

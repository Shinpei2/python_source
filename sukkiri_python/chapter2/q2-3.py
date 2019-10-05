# 1人目の趣味をセットhobbiesに格納
print("一人目の方")
first_person = {input("1番目の趣味を入力して下さい: ")}
for i in range(4):
    hobby = input(f"{i+2}番目の趣味を入力して下さい: ")
    first_person.add(hobby);
# print(first_person)

# 2人目の趣味をセットhobbiesに格納
print("二人目の方")
second_person = {input("1番目の趣味を入力して下さい: ")}
for i in range(4):
    hobby = input(f"{i+2}番目の趣味を入力して下さい: ")
    second_person.add(hobby);
# print(second_person)

# リストへの格納
hobbies = {
    '一人目': first_person,
    '二人目': second_person
}

# 相性の表示
input("心の準備ができたらEnterキーを押してください")
common = len(hobbies['一人目'] & hobbies['二人目'])
total = len(hobbies['一人目'] | hobbies['二人目'])
print(f"二人の趣味の相性は{int(common / total * 100)}%です。")

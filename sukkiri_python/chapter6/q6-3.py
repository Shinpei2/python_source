def welcome(u):
    print(f"ようこそ{u['age']}さん")
    u['age'] = u['age'] + 1
    print(f"あなたは来年{u['age']}歳だから大吉です！")



user_name = input("name: >>>")
user_age = int(input("age: >>>"))
user = {'name': user_name, 'age': user_age}
user_copy = user.copy()
welcome(user_copy)
print(f"{user['age']}歳の{user['name']}さん、またプレイしてくださいね")

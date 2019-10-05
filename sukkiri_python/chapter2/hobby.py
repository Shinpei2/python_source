member_hobby = {
    '増田': {'筋トレ', 'python', '忍者ごっこ', 'カイジの真似'},
    '高橋':  {'トレラン', '筋トレ', 'python', '読書', 'ヒトカラ'},
    '宮本': {'料理', 'プール'}
}

common_hobbies = member_hobby['増田'] | member_hobby['高橋'] | member_hobby['宮本']
print(common_hobbies)

import random


guess = ''
while guess not in ('表', '裏'):
    print('コインの表裏を当ててください。表か裏を入力して下さい:')
    # guess = input('>>>')
    guess = '表'
    
toss = random.randint(0,1) # 0:裏, 1:表
if toss == 1:
    toss = '表'
else:
    toss = '裏'
    
if toss == guess:
    print('当たり')
else:
    print('はずれ。もう一回当てて！')
    toss = random.randint(0,1) # 0:裏, 1:表
    if toss == 1:
        toss = '表'
    else:
        toss = '裏'
    guess  = input('>>>')
    if toss == guess:
        print('当たり')
    else:
        print('はずれ。このゲームは苦手ですね。')

class Myclass():
    def __init__(self, message):
        self.value = message

class Member():
    count = 0   # Memberクラスのインスタンス数を計測するための変数

    # 第2引数以降が、インスタンス生成時に書く必要があるもの
    # 初期化メソッド
    def __init__(self):
        self.name = ''
        self.possition = ''
        Member.count += 1

    # 関数定義
    def setName(self, name):
        self.name = name
    
    def setPossition(self, possition):
        self.possition = possition
    
    def swimming(self):
        print('{}は泳いでいます。'.format(self.name))
    
    
    
    


if __name__ == "__main__":
    m1 = Member()
    m1.setName('有長')
    m1.setPossition('裸の王様')
    print(m1.name)
    print(m1.possition)
    m1.swimming()
    print(Member.count)


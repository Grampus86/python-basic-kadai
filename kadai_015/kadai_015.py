class Human:
    def __init__(self, name, age):
        """
        属性を定義
        :param name:名前
        :param age:年齢
        """
        self.name = name
        self.age = age

    def printinfo(self):
        """
        名前と年齢を出力
        """
        print(f'名前は{self.name}です。')
        print(f'年齢は{self.age}歳です。')


age = 28  # 年齢
name = 'Kota'  # 名前

# インスタンス化
human = Human(name, age)
human.printinfo()

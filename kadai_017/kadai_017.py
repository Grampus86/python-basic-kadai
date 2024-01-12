class Human:
    def __init__(self, name: str, age: int):
        """
        属性を定義
        :param name:名前
        :param age:年齢
        """
        self.name = name
        self.age = age

    def check_adult(self):
        """
        大人か否かを判定
        """
        if self.age >= 20:
            print('あなたは、大人です。')
        elif 0 <= self.age < 20:
            print('あなたは、大人ではありません。')
        else:
            print('年齢の入力に不備があります。')


taro_age = 20  # 年齢
taro_name = 'Taro'  # 名前

hanako_age = 18  # 年齢
hanako_name = 'Hanako'  # 名前

ichiro_age = 5  # 年齢
ichiro_name = 'Ichiro'  # 名前

kota_age = 28  # 年齢
kota_name = 'Kota'  # 名前

# インスタンス化
taro = Human(taro_name, taro_age)
hanako = Human(hanako_name, hanako_age)
ichiro = Human(ichiro_name, ichiro_age)
kota = Human(kota_name, kota_age)

# インスタンスをリストに格納
human_info_list = [taro, hanako, ichiro, kota]

# `check_adult`メゾットを呼び出し、大人かどうかを判定
for human_info in human_info_list:
    human_info.check_adult()

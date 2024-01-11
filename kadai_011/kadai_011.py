list = ["水", "金", "地", "火", "木", "土", "天", "海", "冥"]

"""
forを使ったループ
"""

for element in list:
    print(element)

"""
whileを使ったループ
"""

# ループ用変数
num = 0

# リストの要素数の数を取得
list_length = len(list)

# num=0から1ループ毎にnumを1ずつ加算
# リストをインデックスが(リストの要素数の数-1)以下ならループ
while num <= list_length - 1:
    print(list[num])
    num += 1

price1 = 100
price2 = 200
tax = 1.1  # グローバル変数に修正


def total():
    # tax = 1.1 #ローカル変数になっている
    return price1 + price2


print(total() * tax)

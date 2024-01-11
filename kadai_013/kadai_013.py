def calc_tax_included_price(item_price, tax):
    """
    消費税込みの価格を計算
    :param item_price:商品の価格(円)
    :param tax: 消費税率(%)
    :return: 税込価格(円)
    """
    tax_included_price = item_price + item_price * (tax / 100)
    return tax_included_price


item_price = 200  # 商品の価格(円)
tax = 10  # 消費税率(%)
tax_included_price = calc_tax_included_price(item_price, tax)  # 税込価格を計算
print(f'税込価格は{tax_included_price}円です')

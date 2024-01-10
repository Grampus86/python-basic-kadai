var = 6  # 3の倍数
# var = 10 # 5の倍数
# var = 30 # 3の倍数と5の倍数の両方に該当
# var = 11 # 上記のどの場合にも該当しない

if (var % 15 == 0) and (var % 5 == 0):
    print('FizzBuzz')
elif var % 3 == 0:
    print('Fizz')
elif var % 5 == 0:
    print('Buzz')
else:
    print(var)

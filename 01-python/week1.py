# week1.py  用 while 记 7 天营业额
day = 1
total = 0
while day <= 7:
    money = float(input("今天营业额多少？ "))
    total = total + money
    day = day + 1
print("7 天总营业额:", round(total, 2))
print("7 天平均每天:", round(total / 7, 2))

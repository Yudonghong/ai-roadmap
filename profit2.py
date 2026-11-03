# profit2.py - 每天输入数字，自动算账
item = input("今天卖的是什么？ ")
box_cost = float(input("一箱进货价（元）？ "))
box_count = int(input("一箱多少个？ "))
price = float(input("每个售价（元）？ "))
sold = int(input("今天卖了几个？ "))
other_cost = float(input("炭/调料/摊位费合计（元）？ "))

cost = box_cost / box_count
gross = (price - cost) * sold
net = gross - other_cost

print("-" * 24)
print("商品:", item)
print("每个成本:", round(cost, 2))
print("每个毛利:", round(price - cost, 2))
print("当天毛利:", round(gross, 2))
print("当天净赚:", round(net, 2))

if net < 0:
    print("!! 今天亏了", round(-net, 2), "元")
elif net < 50:
    print("今天一般，明天多卖点")
else:
    print("今天不错")

break_even = other_cost / (price - cost)
print("保本要卖:", round(break_even), "个")
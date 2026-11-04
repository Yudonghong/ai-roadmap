print("程序开始")
item = input("今天卖的是什么？")
box_cost = float(input("一箱多少钱？"))
box_count = int(input("一箱有多少个？"))
print(item,box_cost, box_count)
cost = float(box_cost) / float(box_count)
print("每个成本:", cost)
price = float(input("售价是多少？"))
sold = int(input("卖了多少个？"))
other_cost = float(input("其他开销是多少？"))
print("售价", price, "卖了", sold, "个, 其他开销", other_cost, "元")
gross = (price - cost) * sold
net = gross - other_cost

print("当天毛利:", round(gross, 2))
print("当天净利:", round(net, 2))


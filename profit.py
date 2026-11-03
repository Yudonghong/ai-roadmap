

# profit .py-我的一天
item = "生蚝"
box_cost = 124
box_count = 400
price = 1
sold = 400
other_cost = 40


cost = box_cost / box_count
gross = (price - cost) * sold
net = gross - other_cost


print("商品:",item)
print("每个成本:", round(cost, 2))
print("每个毛利:", round(price - cost, 2))
print("当天毛利:", round(gross, 2))
print("每天净赚:", round(net, 2))
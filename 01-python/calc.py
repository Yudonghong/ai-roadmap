print("程序开始")
time="生蚝"
box_cost= 124
box_count= 400
print(time,box_cost, box_count)
cost =box_cost / box_count
print("每个成本:", cost)
price = 1
sold = 325
other_cost = 40
print("售价", price, "卖了", sold, "个, 其他开销", other_cost, "元")
gross = (price - cost) * sold
net = gross - other_cost

print("当天毛利:", round(gross, 2))
print("当天净利:", round(net, 2))
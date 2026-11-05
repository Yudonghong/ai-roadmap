# week2.py  一周营业报告（for + list）
sales = [325, 325, 720, 500, 532, 613, 413]

total = 0
for m in sales:
    total = total + m

print("7 天总营业:", round(total, 2))
print("平均每天:", round(total / len(sales), 2))
print("最高的一天:", max(sales))
print("最低的一天:", min(sales))

for i, m in enumerate(sales):
    print("第", i + 1, "天:", m)

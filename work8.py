num = 100
count = 0
for x in range(1,100):
    if x % 2 == 0:
        count += 1
print(f"1到100（不含100本身）范围内，有{count}个偶数")
# i = 1
# for i in range(1,101):
#     print(f"今天是向思嵛表白的第{i}天，坚持！")
#     j = 1
#     while j <= 10:
#         print(f"送给思嵛的第{j}朵玫瑰花")
#         j += 1
#     print(f"思嵛，我喜欢你(第{i}天的表白结束)")
#
# print(f"第{i}天，表白成功！")

i = 1
while i <= 100:
    print(f"今天是向思嵛表白的第{i}天，坚持！")
    for j in range(1,11):
        print(f"送给思嵛的第{j}朵玫瑰花")
    print(f"思嵛，我喜欢你(第{i}天的表白结束)")
    i += 1
print(f"第{i - 1}天，表白成功！")
print("欢迎来到黑马儿童游乐场，儿童免费，成人收费")
age = input("请输入你的年龄：")
age = int(age)
if age >= 18:
    print("您已成年，游戏需补票10元")
else:
    print("未成年人免费游玩")

print("祝您游玩愉快！")
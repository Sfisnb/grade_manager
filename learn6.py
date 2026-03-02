print("欢迎来到黑马动物园！")

if int(input("请输入你的身高（cm）：")) < 120:
    print("您的身高小于120cm，可以免费游玩。")
elif int(input("请输入你的vip级别(1~5):")) > 3:
    print("您的级别大于3，可以免费游玩。")
elif int(input("请告诉我今天几号：")) == 1:
    print("今天是1号免费日，可以免费")

print("祝您游玩愉快。")
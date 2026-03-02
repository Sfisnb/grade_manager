"""
演示python的input语句
获取键盘的输入信息
"""
name = input("请告诉我你是谁？")
print("你是：%s" % name)

num = input("请告诉我你的银行卡密码是：")
num = int(num)
print("你的银行卡类型是：", type(num))
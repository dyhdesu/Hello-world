# 通过用户输入计算阶乘

num = int(input("请输入一个整数："))
factorial = 1

# 查看数字是负数，0 或 正数
if num < 0:
    print("负数没有阶乘")
elif num == 0:
    print("0的阶乘是1")
else:
    for i in range(2,num+1):
        factorial = factorial * i
    print("{0} 的阶乘数为 {1}".format(num, factorial))
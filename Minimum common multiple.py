# 寻找最小公倍数
# 定义一个函数
def mcm(x, y):
    if x > y:
        greater = x
    elif x < y:
        greater = y
    else:
        print("请输入两个不一样的数！")
        return
    while(True):
        if (greater % x ==0) and (greater % y == 0):
            break
        greater += 1
    print(x, "和", y, "的最小公倍数为", greater)
    return

# 用户输入
num_1 = int(input("请输入第一个数："))
num_2 = int(input("请输入第二个数："))

mcm(num_1, num_2)
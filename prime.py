# 获得输入范围

lower = int(input("请输入下限："))
upper = int(input("请输入上限："))

# 寻找素数
for num in range(lower, upper+1):
    # 素数大于1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
        else:
            print(num)
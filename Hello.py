# 用户输入一个数字
num = int(input("请输入一个数字："))

# 判断是否有因子
if num > 1:

    for i in range(2,num):
        if (num % i) == 0:
            print("{0}".format(num),"不是质数")
            print("{0} 乘 {1} 等于 {2}".format(i,num//i,num))
            break
    else:
        print("{0}".format(num),"是质数")

else:
    print("{0}".format(num),"不是质数")

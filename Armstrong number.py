# 检测一个数是否为阿姆斯特朗数

# 获得一个输入
num = int(input("请输入一个正整数："))

# 获得数字的长度
N = len(str(num))

# 记录总数
sum = 0
t_num = num
for i in range(1,N+1):
    site_num = t_num %10
    sum += site_num ** N
    t_num = t_num//10

if sum == num:
    print(num,'是阿姆斯特朗数')
else:
    print(num,"不是阿姆斯特朗数")
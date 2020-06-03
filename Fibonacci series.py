# 实现斐波那契数列

# 用户输入数列项数
N = int(input("请输入数列的项数："))
# 初始化
list_fibo = [0]
# 如果只有一项
if N == 1:
    print("斐波那契数列：")
    print(list_fibo)
else:
    # 如果 > 1项
    i = 1
    list_fibo.append(1)
    i += 1
    fibo_front = 0
    fibo_behind = 1
    while i < N:
        next_num = fibo_front + fibo_behind
        fibo_front = fibo_behind
        fibo_behind = next_num
        list_fibo.append(next_num)
        i += 1
    print("斐波那契数列：")
    print(list_fibo)
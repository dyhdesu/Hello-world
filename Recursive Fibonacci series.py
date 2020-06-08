def fibos(n):
    '''递归函数，求第n项的值'''
    if n <= 1:
        return n
    else:
        return fibos(n-1) + fibos(n-2)

# 获取用户输入
nterms = int(input("您要输出几项? "))

# 检查输入的数字是否正确
if nterms <= 0:
    print("输入正数")
else:
    print("斐波那契数列:")
    for i in range(nterms):
        print(fibos(i))
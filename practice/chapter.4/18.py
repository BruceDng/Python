# 编写函数，实现根据输入的参数t输出斐波那契数列中大于t的第一个数
def fibo(t):
    a, b = 1, 1
    while b < t:
        a, b = b, a + b
    else:
        return b


def main():
    t = input("请输入t的值：")
    t = int(t)
    s = fibo(t)
    print("斐波那契数列中大于%d的第一个数为%d" % (t, s))


if __name__ == '__main__':
    main()

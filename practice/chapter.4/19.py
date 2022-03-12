# 编写函数，接收两个正整数为参数，返回一个数组，数组中第一个元素为最大公约数，第二个元素为最小公倍数
def comdm(a, b):
    if a > b:
        a, b = b, a
    p = a * b
    while a != 0:
        r = b % a
        b = a
        a = r
    return (int(p / b), b)


def main():
    t1 = input("请输入第一个数的值：")
    t2 = input("请输入第二个数的值：")
    t1 = int(t1)
    t2 = int(t2)
    print("两个正整数%d和%d的最大公约数和最小公倍数分别为" % (t1, t2), comdm(t1, t2))


if __name__ == '__main__':
    main()

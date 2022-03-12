# 编写函数实现求取给定的两个正整数的最大公约数，并在主调函数中输出这两个数的最大公约数
# 方法1：定义法
"""
def comd(a, b):
    if a > b:
        a, b = b, a
    for i in range(a, 0, -1):
        if (a % i == 0 and b % i == 0):
            d = i
            break
    return(d)


def main():
    t1 = input("请输入第一个数的值：")
    t2 = input("请输入第二个数的值：")
    t1 = int(t1)
    t2 = int(t2)
    print("两个正整数%d和%d的最大公约数为" % (t1, t2), comd(t1, t2))


if __name__ == ' __main__':
    main()
"""


# 辗转相除法
def comd(a, b):
    if a > b:
        a, b = b, a
    while a != 0:
        r = b % a
        b = a
        a = r
    return (b)


def main():
    t1 = input("请输入第一个数的值：")
    t2 = input("请输入第二个数的值：")
    t1 = int(t1)
    t2 = int(t2)
    print("两个正整数%d和%d的最大公约数为" % (t1, t2), comd(t1, t2))


if __name__ == '__main__':
    main()

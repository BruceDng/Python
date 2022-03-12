# 利用递归函数计算两个数的最大公约数
def demo(p, q):
    if q == 0:
        return p
    return demo(q, p % q)


def main():
    x = int(input("请输入第一个数："))
    y = int(input("请输入第二个数："))
    z = demo(x, y)
    print("%d和%d的最大公约数是%d" % (x, y, z))


if __name__ == '__main__':
    main()

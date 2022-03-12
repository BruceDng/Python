# 构造一个函数，判断一个数是否为素数，调用该函数判断从键盘中输入的数是否为素数
import math


def su(n):
    m = math.ceil(math.sqrt(n) + 1)
    for i in range(2, m):
        if n % i == 0 and i < n:
            print("%d不是素数" % n)
            break
    else:
        print("%d不是素数" % n)


def main():
    su(7)


if __name__ == '__main__':
    main()

# 编写函数，判断由键盘输入的正整数是否为素数
def isprime(n):
    if n < 2:
        return 0
    else:
        i = 2
        while i**2 <= n:
            if n % i == 0:
                return 0
            i += 1
        return 1


def main():
    x = int(input("请输入一个正整数："))
    y = isprime(x)
    if y == 1:
        print(x, "是素数")
    if y == 0:
        print(x, "不是素数")


if __name__ == '__main__':
    main()
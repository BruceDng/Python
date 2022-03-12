# 输入一个大于3的整数n,判断该数是否为素数
def main():
    n = int(input("请输入整数n:"))
    for i in range(2, n):
        if n % i ==0 and i < n:
            print("%d不是素数"%n)
            break
        else:
            print("%d是素数"%n)


if __name__ == '__main__':
    main()
# 输入两个正整数m和n,求其最大公约数和最小公倍数
def main():
    m = int(input("请输入第一个正整数m:"))
    n = int(input("请输入第二个正整数n:"))
    if n < m:
        n, m = m, n
    p = m * n
    while m != 0:
        r = n % m
        n = m
        m = r
    print("它们的最大公约数为：", n)
    print("它们的最小公倍数为：", p // n)


if __name__ == '__main__':
    main()

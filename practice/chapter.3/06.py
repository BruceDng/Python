# 利用while循环计算1~100中所有奇数的和及偶数的和
def main():
    sum_odd = 0
    sum_even = 0
    i = 1
    while (i <= 100):
        if (i % 2 != 0):
            sum_odd = sum_odd + i
        else:
            sum_even = sum_even + i
        i = i + 1
    print("奇数的和为：%d\n 偶数的和为：%d" % (sum_odd, sum_even))


if __name__ == '__main__':
    main()

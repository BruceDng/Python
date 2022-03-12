# 利用for循环计算1-100中所有奇数的和及偶数的和
def main():
    sum_odd = 0
    sum_even = 0
    for i in range(1, 101):
        if i % 2 != 0:
            sum_odd = sum_odd + i
        else:
            sum_even = sum_even + i
    # print("sum_even=", sum_even)
    # print("sum_odd=", sum_odd)
    print("奇数的和为：%d\n偶数的和为：%d" % (sum_odd, sum_even))


if __name__ == '__main__':
    main()

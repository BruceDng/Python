# 根据输入参数的个数计算各参数的平方和并输出
def func(*args):
    sum = 0
    for n in args:
        sum = sum + n * n
    print("输入的%d个数的平方和为："%len(args), sum)


def main():
    func(1, 2, 3, 4)
    func(2, 3, 4, 5, 6)
    func(3, 4, 5, 6, 7, 8)


if __name__ == '__main__':
    main()
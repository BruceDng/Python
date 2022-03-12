def main():
    x = int(input("请输入x的值："))
    if x >= 0:
        y = 3 * x + 1
    else:
        y = 2 * x / (x - 2)
    print("输入的x的值为：", x)
    print("y的值为：", y)


if __name__ == '__main__':
    main()

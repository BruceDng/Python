# 输出水仙花数
def main():
    for i in range(100, 1000):
        i1 = i // 100
        i2 = i // 10 % 10
        i3 = i % 10
        if i1 ** 3 + i2 ** 3 + i3 ** 3 == i:
            print("%d 是水仙花数" % i)


if __name__ == '__main__':
    main()

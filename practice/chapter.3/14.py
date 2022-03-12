# 九九乘法表
def main():
    for i in range(1, 10):
        for j in range(1, 10):
            print(i, '*', j, '=', i * j, '\t', end="")
        print("")


if __name__ == '__main__':
    main()

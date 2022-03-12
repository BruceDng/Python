# 编写函数，求多个数的最大值
def max(a, b, *c):
    maxvalue = a
    if maxvalue < b:
        maxvalue = b
    for i in c:
        if maxvalue < i:
            maxvalue = i
    return(maxvalue)


def main():
    print(max(3, 2, 5, 8, 1))
    print(max(4, 2, 3, 5))


if __name__ == '__main__':
    main()

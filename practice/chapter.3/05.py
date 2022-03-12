# 利用while循环计算1+2+。。+100
def main():
    sum = 0
    i = 1
    while i < 101:
        sum = sum + i
        i = i + 1
    print("1+2+3+...+100的值为：", sum)


if __name__ == '__main__':
    main()

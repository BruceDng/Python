# 定义函数，输出不同字符串。
def printMess(x='Hello', y='Python!'):
    print(x+y)


def main():
    printMess()
    printMess(y='World!')
    printMess(x='Thanks')
    printMess('World!')


if __name__ == '__main__':
    main()
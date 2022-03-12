# 定义函数，利用关键字参数实现在屏幕上输出多行字符串
def printMess(mess, n):
    for i in range(1, n+1):
        print(mess)


def main():
    printMess(n=5, mess='Hello World!')


if __name__ == '__main__':
    main()
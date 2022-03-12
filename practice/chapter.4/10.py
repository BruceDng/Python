# 定义函数，实现在屏幕上输出多行字符串。
def printMess(mess, n):
    for i in range(1, n+1):
        print(mess)

        
def main():
    printMess('Hello World!', 5)


if __name__ == '__main__':
    main()
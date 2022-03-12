# 循环输出0到9
# for i in range(0,10):
#   print(i,end=",")
# print("")
# if语句
"""def main():
    x = int(input("请输入x的值:"))
    if x > 10:
        print("输入x的值大于10")
    if __name__=='__main__':
        main()"""


def main():
    x = int(input("请输入x的值："))
    y = int(input("请输入y的值："))
    if x > y:
        x, y = y, x
        print("输入的2个数从小到大排序为：", x, y)


if __name__ == '__main__':
    main()

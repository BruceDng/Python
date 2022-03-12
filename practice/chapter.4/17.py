# 编写函数，根据输入的半径值r计算圆的面积
import math


def area(r):
    return math.pi*r*r


def main():
    r = input("请输入圆的半径：")
    r = int(r)
    s = area(r)
    print("半径为%d的圆的面积为%d"%(r, s))


if __name__ == '__main__':
    main()
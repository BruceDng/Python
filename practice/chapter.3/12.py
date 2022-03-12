# 计算半径为整数1-20的圆的面积，直到圆的面积大于200
def main():
    import math
    for r in range(1, 21):
        area = math.pi * r * r
        if (area > 200):
            break
        print("半径为%d的圆的面积为：%f""%(r,area)")


if __name__ == '__main__':
    main()

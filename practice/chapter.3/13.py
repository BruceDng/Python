# 输出50-80中不能被五整除的整数，要求每行输出4个数
def main():
    for x in range(50, 81):
        if x%5 ==0:
            print("")
            continue
        print(x,end=",")


if __name__ == '__main__':
    main()
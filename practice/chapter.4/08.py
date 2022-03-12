# 编写函数，生成一个随机列表，并在主程序中输出该随机列表
import random
def randlist(n):
    a = []
    for i in range(n):
        a.append(random.random())
    return a


def main():
    x = randlist(6)
    for i in x:
        print(i)


if __name__ == '__main__':
    main()
# 有一个分数列：2/1, 3/2,5/3,8/5,13/8,21/13,....求出该数列前20项的和
def main():
    a = 2
    b = 1
    s = 0
    for i in range(1, 21):
        s = s + a / b
        t = a
        b = t
    print("该数列前20项的和为：%f" % s)


if __name__ == '__main__':
    main()

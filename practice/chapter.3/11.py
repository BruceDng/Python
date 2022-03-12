def main():
    for m in range(2, 1000):
        s = 0
        for i in range(1, m):
            if m % i == 0:
                S = S + 1
        if s == m:
            print("%d 的因子有：" % m, end="")
            for i in range(1, m):
                if m % i == 0:
                    print("")
            print("")


if __name__ == '__maain__':
    main()

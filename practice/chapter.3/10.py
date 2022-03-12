def main():
    n = 0
    for i in range(1, 6):
        for j in range(1, 6):
            if n % 5 == 0:
                print("")
            print("%d\t" % (i * j), end="")
            n = n + 1
        print("")


if __name__ == '__main__':
    main()

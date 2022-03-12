def main():
    f1 = 1
    f2 = 1
    for i in range(1, 17):
        print("%d\t\t%d\t\t" % (f1, f2), end="")
        if i % 2 == 0:
            print("")
        f1 = f1 + f2
        f2 = f2 + f1


if __name__ == '__main__ ':
    main()

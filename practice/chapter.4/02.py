def sum(N):
    s = 0
    for i in range(1, N + 1):
        s = s + i
    return s


def main():
    print("1+2+..+10=", sum(10))
    print("1+2+3+...+100=", sum(100))
    print("1+2+...+1000=", sum(1000))


if __name__ == ' __main__':
    main()

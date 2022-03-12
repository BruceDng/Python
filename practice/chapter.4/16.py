def math(n):
    if n == 1:
        return lambda x, y: x + y
    if n == 2:
        return lambda x, y: x - y
    if n == 3:
        return lambda x, y: x * y
    if n == 4:
        return lambda x, y: x / y


def main():
    result = math(1)
    print(result(3, 2))
    result = math(2)
    print(result(3, 2))
    result = math(3)
    print(result(3, 2))
    result = math(4)
    print(result(3, 2))


if __name__ == '__main__':
    main()

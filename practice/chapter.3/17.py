# 利用while循环遍历字符串
def main():
    str = input("请输入字符串：")
    i = 0
    while i < len(str):
        print(str[i], end="")
        i += 1


if __name__ == '__main__':
    main()

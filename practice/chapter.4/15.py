# 对于一个列表，要求大于3的元素，分别使用程式编程、函数式编程和匿名函数实现
def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = []
    for i in list1:
        if i > 3:
            list2.append(i)
    print(list2)


if __name__ == '__main__':
    main()
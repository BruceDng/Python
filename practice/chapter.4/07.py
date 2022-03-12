# 编写函数实现统计字符串中大、小写字母的个数
def comuda(str):
    result1 = 0
    result2 = 0
    for ch in str:
        if ch >='a' and ch <= 'z':
            result1 += 1
        elif ch >='A' and ch <='Z':
            result2 +=1
    return(result1,result2)


def main():
    print(comuda('AaBbCcDd123'))


if __name__ == '__main__':
    main()
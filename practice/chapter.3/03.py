def main():
    score = int(input("请输入成绩："))
    if score < 90:
        if score < 80:
            if score < 70:
                if score < 60:
                    print("不及格")
                else:
                    print("及格")
            else:
                print("中")
        else:
            print("良")
    else:
        print("优秀")


if __name__ == '__main__':
    main()

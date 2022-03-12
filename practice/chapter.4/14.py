# 字典变长参数的综合示例
def foo(positional_arg, keyword_arg = 'default', **dict_arg):
    print("positional_arg:", positional_arg)
    print("keyword_arg:", keyword_arg)
    for each_dict_arg in dict_arg.keys():
        print("dict_arg:%s=>%s"%(each_dict_arg, str(dict_arg[each_dict_arg])))


def main():
    foo(1, 2, a = "b")


if __name__ == '__main__':
    main()
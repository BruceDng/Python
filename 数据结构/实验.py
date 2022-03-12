# 基础实验1.实现顺序表的基本操作
class list(object):
    # 初始化顺序表
    def __init__(self):
        self.SL = []

    # 判断SL顺序表是否为空
    def IsEmpty(self):
        if self.GetLength() == 0:
            print("此顺序表为空！")
        else:
            print("此顺序表不为空。")

    # 创建顺序表函数（将2,5,16,55,8元素依次存入SL中）
    def Create(self):
        Element = input("请输入元素：")
        while Element != "#":
            self.SL.append(int(Element))
            Element = input("请输入元素：")

    # 输出SL中元素的个数
    def GetLength(self):
        length = len(self.SL)
        return length

    def GetLength1(self):
        print("顺序表长度为:", len(self.SL))

    # 获取SL中元素5的位置
    def Find(self):
        key = int(input("输入你要查找的元素"))
        if key in self.SL:
            Pos = self.SL.index(key)
            print(self.SL[Pos], "元素在第", Pos + 1, "位置上")
        else:
            print(key, "元素不在该顺序表中")

    # 在指定元素（5）后插入元素（11）
    def Insert(self):
        key = int(input("输入你要插入元素前一个的元素："))
        if key in self.SL:
            Pos = self.SL.index(key)
        else:
            print(key, "元素不在该顺序表中")
        Element = int(input("输入要插入的元素"))
        self.SL.insert(Pos + 1, Element)

    # 删除指定元素（16）
    def Delete(self):
        key = int(input("请输入你要删除的元素"))
        if key in self.SL:
            print("正在删除", key, "元素")
            self.SL.remove(key)
        else:
            print("该元素不在顺序表中")

    # 遍历元素函数
    def Traverse(self):
        for i in range(self.GetLength()):
            print(self.SL[i])





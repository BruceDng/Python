# 定义一个car类并调用方法
class Car:
    def getCarInfor(self):
        print("车轮子个数：%d, 颜色%s" % (self.wheelNum, self.color))

    def move(self):
        print("车在移动。。。")

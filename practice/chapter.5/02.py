# 创建demo对象，给对象添加属性并调用对象的方法。


class Car:
    def move(self):
        print("车在移动......")

    def toot(self):
        print("车在鸣笛...嘟嘟嘟")


BMW = Car()
BMW.color = "黑色"
BMW.wheelNum = 4
BMW.move()
BMW.toot()
print(BMW.color)
print(BMW.wheelNum)

import datetime
import random


# 定义汽车类
class Car(object):
    def __init__(self, num, owner, color, type, connect, money, entime):
        # 汽车属性
        self.num = num
        self.color = color
        self.type = type
        self.owner = owner
        self.connect = connect
        self.money = money
        self.entime = entime

    def __str__(self):
        print('车牌号：<%s> 车主：<%s> 颜色:<%s> 车型:<%s> 联系方式：<%s> 余额：<%s> 进入停车场时间：<%s> '
              % (self.num, self.owner, self.color, self.type, self.connect, self.money, self.entime))


# 定义汽车管理类
class Park(object):
    def init(self):  # 对停车场初始化车辆

        self.cars.append(Car('1001', 'python', '红色', '大卡', '21212121', 340, datetime.datetime.now()))
        self.cars.append(
            Car('1002', 'hello', '蓝色', '小汽车', '28343434', 87, datetime.datetime.now() - datetime.timedelta(minutes=1)))
        self.cars.append(
            Car('1003', 'java', '白色', '小汽车', '15434212', 160, datetime.datetime.now() - datetime.timedelta(minutes=2)))
        self.cars.append(
            Car('1004', 'westos', '黑色', '小卡', '5432121', 500, datetime.datetime.now() - datetime.timedelta(minutes=3)))
        self.cars.append(
            Car('1005', 'root', '白色', '中卡', '9087921', 240, datetime.datetime.now() - datetime.timedelta(minutes=4)))

    def __init__(self):
        # 停车场属性
        self.max_car = 200
        self.cars = []
        self.cur_car = len(self.cars)

    def Menu(self):
        self.init()
        while 1:
            print('''
                    停车管理系统
                  1）停车                                    
                  2）显示                  
                  3）取车                  
                  4）退出
            ''')
            choice = int(input('Choice:'))
            if choice == 1:
                self.park()
            elif choice == 2:
                for i in self.cars:
                    Car.__str__(i)
            elif choice == 3:
                self.exit()
            elif choice == 4:
                exit(0)
            else:
                print('Error!没有该选项。。。')

    # 定义停车方法
    def park(self):
        car_num = input('车牌号：')
        res = self.check(car_num)  # 判断该车牌是否有停车记录
        if res is None:
            if self.cur_car < self.max_car:  # 判断停车场是否满负荷
                self.cars.append(Car(car_num, input('车主：'), input('颜色：'), input('车型：'),
                                     input('联系方式：'), int(input('余额')), datetime.datetime.now()))
                print('停车成功！')
            else:
                print('停车场已满！暂时不能停车。。。')
        else:
            print('车牌为%s车辆已停在停车场' % car_num)

    # 定义取车方法
    def exit(self):
        car_num = input('车牌号：')
        res = self.check(car_num)  # 判断该车牌是否有停车记录
        if res is not None:
            self.pay(res)
            self.cars.remove(res)

            print('成功取车，祝您一路顺风。。。')
        else:
            print('警报警报！！！车牌：%s车辆非法进入停车场。。。' % car_num)

    # 定义检查车辆是否有记录的方法
    def check(self, car_num):
        for i in self.cars:
            if car_num == i.num:
                return i
        else:
            return None

    # 定义付款方法
    def pay(self, car):
        money = (datetime.datetime.now() - car.entime).seconds / 20  # 收费方法：一分钟3块钱
        time=(datetime.datetime.now() - car.entime).seconds
        while 1:
            if car.money >= money:  # 判断余额是否足够支付
                car.money -= money
                print('自动付款%s成功' % (money))
                print("停车时间(s)",time)
                break
            else:
                print('余额不足请充值')
                car.money += int(input('充值金额：'))
                print('充值成功')


par = Park()
par.Menu()
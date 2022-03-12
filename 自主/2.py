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
                  2）查询                  
                  3）显示                  
                  4）编辑
                  5）取车                  
                  6）统计
                  7）退出
            ''')
            choice = int(input('Choice:'))
            if choice == 1:
                self.park()
            elif choice == 2:
                self.find()
            elif choice == 3:
                for i in self.cars:
                    Car.__str__(i)
            elif choice == 4:
                self.edit()
            elif choice == 5:
                self.exit()
            elif choice == 6:
                self.sta()
            elif choice == 7:
                exit(0)
            else:
                print('Error!没有该选项。。。')

    # 1.定义停车方法
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

    # 5.定义取车方法
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
        while 1:
            if car.money >= money:  # 判断余额是否足够支付
                car.money -= money
                print('自动付款%s成功' % (money))
                break
            else:
                print('余额不足请充值')
                car.money += int(input('充值金额：'))
                print('充值成功')

    # 定义查询方法
    def find(self):
        while 1:
            print('''
                    1)依据车牌查询
                    2)依据车型查询
                    3)退出查询

                    ''')
            choice = int(input('Choice:'))
            if choice == 1:  # 依据车牌查询
                num = input('车牌号：')
                res = self.check(num)  # 判断该车牌号是否有停车记录
                if res is not None:
                    Car.__str__(res)

                else:
                    print('车牌%s停车记录为空...' % num)
            elif choice == 2:  # 依据车型查询
                type = input('车型：(小汽车,小卡,中卡,大卡)')
                if type in ['小汽车', '小卡', '中卡', '大卡']:
                    for i in self.cars:
                        if i.type == type:
                            Car.__str__(i)

                else:
                    print('不存在%s车型' % type)
            elif choice == 3:
                break
            else:
                print('请输入正确选择...')

    # 定义修改修改信息方法
    def edit(self):
        num = input('车牌号：')
        res = self.check(num)  # 判断该车牌号是否有停车记录
        if res is not None:
            Car.__str__(res)
            print('信息修改：\n车牌号：%s' % num)
            res.owner = input('车主：')
            res.clor = input('颜色：')
            res.type = input('车型(小汽车,小卡,中卡,大卡)：')
            res.connect = input('联系方式：')
            res.money = int(input('余额：'))
            res.entime = datetime.datetime.strptime(input('进入停车场时间(eg:2018-05-21 11:14:10)：'),
                                                    '%Y-%m-%d %H:%M:%S')
            print('信息修改成功...')

        else:
            print('车牌%s停车记录为空...' % num)

    # 定义信息统计方法
    def sta(self):
        while 1:
            print('''
                    1）按车型统计
                    2）按时间统计
                    3）退出统计
                    ''')
            choice = int(input('Choice:'))
            if choice == 1:  # 按车型统计
                type1 = type2 = type3 = type4 = 0
                for i in self.cars:
                    if i.type == '小汽车':
                        type1 += 1
                    elif i.type == '小卡':
                        type2 += 1
                    elif i.type == '中卡':
                        type3 += 1
                    else:
                        type4 += 1

                print('总数：%s辆\n小汽车：%s辆\n小卡：%s辆\n中卡;%s辆\n大卡：%s辆'
                      % (len(self.cars), type1, type2, type3, type4))
            elif choice == 2:  # 按时间统计
                # 查找最早停车时间
                base1time = random.choice(self.cars, ).entime
                for i in self.cars:
                    if i.entime < base1time:
                        base1time = i.entime
                # 查找最晚停车时间
                base2time = random.choice(self.cars).entime
                for i in self.cars:
                    if i.entime > base2time:
                        base2time = i.entime
                print('车辆总数：%s' % (len(self.cars)))
                while 1:
                    count = 0
                    for i in self.cars:
                        if base1time <= i.entime < base1time + datetime.timedelta(minutes=1):  # 定义每分钟为一个时间段
                            count += 1
                    print('%s至%s时间段有%s辆车停车' % (base1time,
                                               base1time + datetime.timedelta(minutes=1), count))
                    if base1time + datetime.timedelta(minutes=1) > base2time:
                        break
                    else:
                        base1time = base1time + datetime.timedelta(minutes=1)


            elif choice == 3:
                break
            else:
                print('Error 输入错误...')


par = Park()
par.Menu()
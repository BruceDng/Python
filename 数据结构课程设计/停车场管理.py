import time
from setting_Manage import ParkManage

class Car(ParkManage):
    """一个关于车的类"""
    def __init__(self,car_number,car_owner,contact_way,car_color,car_model):
        super(Car,self).__init__()
        self.car_number=car_number
        self.car_owner=car_owner
        self.contact_way=contact_way
        self.car_color=car_color
        self.car_model=car_model
        self.balance=200
        self.entrance_time = 0
        self.exit_time = 0

    def __setitem__(self, key, value):
        self.__dict__[key]=value


def slot_card(self):
    """根据时间计费"""
    park_time = time.mktime(time.strptime(self.exit_time)) - time.mktime(
        time.strptime(self.entrance_time))
    h = park_time // 3600
    m = (park_time - h * 3600) // 60
    s = park_time - h * 3600 - m * 60
    P_time = "%.0f时%.0f分%.0f秒" % (h, m, s)
    consumption = ((park_time) / 3600) * 5
    self.balance -= consumption
    print("车牌号为:%s\n停车时长:%s\n本次消费:%.2f元\n卡里余额:%.2f元\n" % (self.car_number, P_time, consumption, self.balance))


def __str__(self):
    if self.car_model == '0':
        self.car_model = "小汽车"
    elif self.car_model == '1':
        self.car_model = "小卡"
    elif self.car_model == '2':
        self.car_model = "中卡"
    elif self.car_model == '3':
        self.car_model = "大卡"
    return "%s %s %s %s %s %s" % (self.car_number, self.car_owner, self.contact_way,
                                  self.car_color, self.car_model, self.entrance_time)
import time

class ParkManage(object):
    """创建一个关于停车的类"""
    def __init__(self,max_car=100,):  #定义最大停车辆数
        self.max_car=max_car
        self.car_list = []
        self.cur_car=len(self.car_list)


    def info(self):
        """ #显示系统功能信息"""
        print("""
        —————————————————————————
        |***欢迎进入车辆管理系统***|
        —————————————————————————    
{1}                                    
{2}           1)添加车辆信息{3}{2}
{0}                                  
{2}           2)查询车辆信息{3}{2}
{0}
{2}           3)显示车辆信息{3}{2}
{0}
{2}           4)编辑车辆信息{3}{2}
{0}
{2}           5)删除车辆信息{3}{2}
{0}
{2}           6)统计车辆信息{3}{2}
{0}
{2}              7)退出系统{3}{2}
{1}
        """.format("-"*40,"="*40,"|"," "*16))

    def add_car(self,car):
        """#添加车辆信息"""
        entrance_time = time.ctime()
        car["entrance_time"]=entrance_time
        for Car in self.car_list:
            if Car.car_number == car.car_number:
                print("车牌号信息有误，重新输入")
                break
        else:
            self.car_list.append(car)
            print("车牌号为%s的车入库成功" %car.car_number)

    def search_By_Number(self):
        """#按车牌号查询"""
        car_number=input("请输入你您要查找的车牌号：")
        for car in self.car_list:
            if car.car_number==car_number:
                print(car)
                break
        else:
            print("未找到车牌号为%s的车辆" %car_number)

    def search_By_Model(self):
        """#按车型查询"""
        car_model=int(input("(小汽车:0,小卡：1，中卡：2，大卡：3)\n请输入您要查找的车型："))
        if car_model in [0,1,2,3]:
            for car in self.car_list:
                if car_model==int(car.car_model):
                    print(car)
            else:
                print("未找到相关车辆信息")
        else:
            print("输入有误，请重新输入")

    def searchCar(self):
        """#查找车辆信息"""
        print("""
            1)按车牌号查找
            2)按车型查找
        """)
        search_chioce=input("输入您要查找的方式：")
        if search_chioce == '1':
            self.search_By_Number()
        elif search_chioce=='2':
            self.search_By_Model()
        else:
            print("输入有误，请重新输入")


    def display(self):
        """#显示车车辆信息"""
        if len(self.car_list)!=0:
            for car in self.car_list:
                print(car)
        else:
            print("车库为空")

    def change_Carinfo(self):
        """#修改车辆信息"""
        car_number = input("请输入你您要查找的车牌号：")
        for car in self.car_list:
            if car.car_number == car_number:
                index=self.car_list.index(car)
                change=int(input("(修改信息的序号:\n车主0,\n联系方式1,\n车颜色2,\n车型3)\n输入你要修改的信息序号："))
                if change==0:
                    new_info=input("输入新的信息：")
                    self.car_list[index].car_owner=new_info
                    print("车主名修改成功")
                    break
                elif change==1:
                    new_info=input("输入新的信息：")
                    self.car_list[index].contact_way=new_info
                    print("联系方式修改成功")
                    break
                elif change==2:
                    new_info=input("输入新的信息：")
                    self.car_list[index].car_color=new_info
                    print("车颜色修改成功")
                    break
                elif change==3:
                    new_info=input("输入新的信息：")
                    self.car_list[index].car_model=new_info
                    print("车型修改成功")
                    break
        else:
            print("未找到车牌号为%s的车辆" % car_number)

    def delete_car(self,car):
        """删除车辆信息"""
        exit_time=time.ctime()
        car["exit_time"]=exit_time
        car.slot_card()
        self.car_list.remove(car)
        print("车牌号为%s的车两成功删除"%car.car_number)


    def statistics(self):
        """统计车辆信息"""
        sedan_car_number=0
        pickup_truck_number=0
        middle_truck_number=0
        super_truck_number=0
        for car in self.car_list:
            if car.car_model=='0':
                sedan_car_number+=1
            elif car.car_model=='1':
                pickup_truck_number+=1
            elif car.car_model=='2':
                middle_truck_number+=1
            elif car.car_model=='3':
                super_truck_number+=1
        else:
            print("小汽车：%s\n"
                  "小  卡：%s\n"
                  "中  卡：%s\n"
                  "大  卡：%s\n"
                  %(sedan_car_number,pickup_truck_number,middle_truck_number,super_truck_number))
import re
from  setting_Car import Car
from setting_Manage import ParkManage


def check_car_number(car_number):    #判断车牌号是否合法
    pattern = re.compile(u'[\u4e00-\u9fa5]?')
    pattern1 = re.compile(u'[A-Z]+')
    pattern2 = re.compile(u'[0-9]+')

    match = pattern.search(car_number)
    match1 = pattern1.search(car_number)
    match2 = pattern2.search(car_number)
    if match and match1 and match2:
        return True
    else:
        return False

def check_contact_way(contact_way):   #判断手机号是否合法
    pattern = re.compile(u'1[3|4|5|6|7|8|9]\d{9}$')

    match = pattern.search(contact_way)
    if match:
        return True
    else:
        return False


def main():
    parkmanage=ParkManage()
    while True:
        parkmanage.info()
        choice=input("请输入你要的功能:")
        if choice=='1':
            check_error_list=[]
            car_number=input("请输入车牌号:")
            if check_car_number(car_number):
                car_owner=input("请输入车主姓名:")
                contact_way=input("请输入车主联系方式:")
                if check_contact_way(contact_way):
                    car_color=input("请输入车颜色:")
                    car_model=input("请输入车型(小汽车:0,小卡：1，中卡：2，大卡：3):")
                    check_error_list=[car_number,car_owner,contact_way,car_color,car_model]
                    for info in check_error_list:    #判断输入信息的完整性
                        if info=='':
                            print("输入信息不全")
                            break
                    else:
                        car = Car(car_number, car_owner, contact_way, car_color, car_model)
                        parkmanage.add_car(car)
                else:
                    print("手机号无效")
            else:
                print("车牌号不合法")

        elif choice=='2':
            parkmanage.searchCar()
        elif choice =='3':
            parkmanage.display()
        elif choice=='4':
            parkmanage.change_Carinfo()
        elif choice=='5':
            car_number = input("输入您要删除的车辆的车牌号：")
            for car in parkmanage.car_list:
                if car.car_number == car_number:
                    parkmanage.delete_car(car)
                    break
            else:
                print("未找到车牌号为%s的车辆" % (car_number))

        elif choice=='6':
            parkmanage.statistics()
        elif choice=='7':
            print("欢迎下次使用！！！")
            exit()
        else:
            print("请输入正确的选项")


if __name__ == '__main__':
    main()





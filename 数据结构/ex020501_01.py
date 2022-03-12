#实现顺序表的基本操作
class SequenceList(object):
   #初始化一个顺序表SL
   def __init__(self):
       self.SL=[]
   #判断SL是否为空
   def IsEmpty(self):
       if self.GetLength()==0:
           print("SL为空")
       else:
           print("SL不为空")
   #将元素2、5、16、55、8依次存入SL中
   def CreateSequenceList(self):
       print("请输入数据后按回车键确认，若想结束请输入“#”。")
       Element=input("请输入元素：")
       while Element!='#':
           self.SL.append(int(Element))
           Element=input("请输入元素：")
   #输出SL中元素的个数
   def count(self):
       self.SL=int()
       print("SL中元素的个数为：")
   #获取SL中元素5的位置
   def FindElement(self):
       key=int(input('请输入想要查找的元素值：'))
       if key in self.SL:
           ipos=self.SL.index(key)
           print("查找成功！值为",self.SL[ipos],"的元素，位于当前顺序表的第",ipos+1,"个位置。")
       else:
           print("查找失败！当前顺序表中不存在值为",key,"的元素")
   #在元素5之后插入元素11
   def InsertElement(self):
       ipos=int(input('请输入待插入元素的位置：'))
       Element=int(input('请输入待插入的元素值：'))
       self.SL.insert(ipos,Element)
       print("插入元素后，当前顺序表为：\n",self.SL)
   #删除值为16的元素
   def DeleteElement(self):
       dpos=int(input('请输入待删除元素的位置：'))
       print("正在删除元素",self.SL[dpos],"...")
       self.SL.remove(self.SL[dpos])
       print("删除后顺序表为：\n",self.SL)
   #将SL中元素依次输出
   def TraverseElement(self):
       SLLen=len(self.SL)
       print("遍历顺序表中元素")
       for i in range(0,SLLen):
           print("第",i+1,"个元素的值为",self.SL[i])

   #销毁

SL = SequenceList()
SL.CreateSequenceList()
SL.TraverseElement()
SL.FindElement()
SL.InsertElement()
SL.DeleteElement()






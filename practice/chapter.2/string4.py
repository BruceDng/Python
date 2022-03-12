#浮点数
from decimal import Decimal
from decimal import getcontext
Decimal('4.20')+Decimal('2.10')
#元组
1,2,3
(1,2,3)
()
#访问元组
tup1=(12,34.56)
tup2=('abc','xyz')
tup3=tup1+tup2
print(tup3)
#删除元组
tup=('physics','chemistry',1997,2000)
print(tup)
del tup
print("After deleting tup:")
print("tup")
#元组运算符
len((1,2,3))
(1,2,3)+(4,5,6)
('Hi',)*4
3 in (1,2,3)
#元组索引与截取
L=('spam','Spam','SPAM!')
#无关闭分隔符
print('abs',-4.24e93,18+6.6j,'xyz')
x,y=1,2
print("Value of x,y：",x,y)
#元组内置函数
#多维元组
tup1=(('physics','chemistry',1997,2000)),('chemistry',1997,2000),('physics',2000)
print("tup1[0]:",tup1[0])
#列表
list1=['physics','chemistry',1997,2000]
list2=[1,2,3,4,5]
list3=["a","b","c","d"]
print(list1)
print(list2)
print(list3)
#列表的访问
list1=['physics','chemistry',1997,2000]
list2=[1,2,3,4,5,6,7]
print("list1[0]:",list1[0])
print("list2[1:5]",list2[1:5])
#更新列表
list=['physics','chemistry',1997,2000]
print("Value available at index2:")
print(list[2])
list[2]=2001
print("New value available at index2:")
print(list[2])
#删除列表元素
list1=['physics','chemistry',1997,2000]
print(list1)
del list1[2]
print("After deleting value at index2:")
print(list1)

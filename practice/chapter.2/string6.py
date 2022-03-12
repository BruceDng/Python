#字典
dict1={'Alice':'2341','Beth':'9102','Cecil':'3258','Hello':'3258'}
print(dict1)
#访问字典里的值
dict={'Name':'Zara','Age':7,'Class':'First'}
print("dict['Name']:",dict['Name'])
print("dict['Age']:",dict['Age'])
#修改字典
dict={'Name':'Zara','Age':7,'Class':'First'}
dict['Age']=8    #update existing entry
dict['School']="DPS School"  #Add new entry
print("dict['Age']:",dict['Age'])
print("dict['School']:",dict['School'])
#删除字典元素
dict={'Name':'Zara','Age':7,'Class':'First'}
del dict['Name']  #删除键是'Name'的条目
dict.clear()  #清空词典所有条目
del dict  #删除词典
print("dict['Age']:",dict['Age'])
print("dict['School']:",dict['School'])
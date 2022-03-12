#字符串更新
#!/usr/bin/python
#-*-coding:UTF-8 -*-
var1="Hello World!"
print("更新字符串 :-",var1[:6]+'Runoob!')
#字符串运算符
a="Hello"
b="Python"
print("a+b 输出结果: ",a+b)
print("a*2 输出结果: ",a*2)
print("a[1] 输出结果: ",a[1])
print("a[1:4] 输出结果 :",a[1:4])
if("H" in a):

    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")
if("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")
print(r'\n')#原始字符串不会对反斜杆做特殊处理
print(R'\n')
#字符串格式化
print("My name is %s and weight is %d kg!"%('Zara',21))
#Unicode字符串
u'Hello World!'

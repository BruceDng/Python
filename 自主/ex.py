import pandas as pd
c = pd.Series([1,2,3,4,5], index=list('ABCDE'))  # 创建一个pandas的一维数组Series对象。
print(c, type(c))
print(c.describe())  # 查看Series的描述信息。包括：计数、平均值、标准差、最小最大值、四分位数、元素的数据类型等。
print(c[0], c.A, c.loc['A'], c.iloc[0],c.at['A'], c.iat[0])  # 选择Series对象的元素：下标、属性、loc函数、iloc函数、at函数、iat函数。
print(c+1)  # Series一维数组的运算：和一个数运算，由于矢量化特性，会迭代计算。
print(c+[5,4,3,2,1])  # Series一维数组的运算：与数组运算，需要shape一致，分别计算。
d = c.add(pd.Series([1,2,3,4,5], index=list('ABXYZ')))  # 数组的index不一致时的相加结果。
print(d)
print(d.dropna())  # 删除数组缺失值
print(d.fillna(value=1))  # 填充数组缺失值
df = pd.DataFrame({
    '时间':['2019-01-01','2019-01-02','2019-01-03'],
    '商品编码':[1001,1002,1003],
    '商品名称':['苹果','梨子','香蕉'],
    '销售数量':[1,2,3]
}, index=list('ABC'))  # 使用字典创建一个pandas的二维数组DataFrame对象。
print(df, type(df))
print(df.mean(),df.mean(axis=0), df.mean(axis=1))  # 查看二维数组的平均值。
print(df.时间, df['商品名称'], df.loc['A'], df.iloc[0:3,1:3])  # 选择二维数组的元素。
print(df[['商品名称','销售数量']])  # 通过列表来选择特定的几列。
print(df[df['销售数量']>=2])  # 布尔索引，筛选符合条件的行。
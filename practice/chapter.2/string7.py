#字典键的特性
dict={'Name':'Zara','Age':7,'Name':'Manni'}
print("dict['Name']:",dict['Name'])
dict={['Name']:'Zara','Age':7}#键必须不可变，所以可以用数字、字符串或元组充当，但不可用列表
print("dict['Name']:",dict['Name'])

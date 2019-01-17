"""
tuple
本质 ： 是一种有序集合
特点 ：
1. 与列表非常相似
2. 一旦初始化就不能修改
3. 使用小括号
"""
# 创建空的元组
tuple1 = ()
print(tuple1)
# 创建带有元素的元组
# 元组中的元素的类别可以不同
tuple2 = (1, 2, 3, "good", True)
print(tuple2)
# 定义只有一个元素的元组
tuple3 = (1, )
print(tuple3)
print(type(tuple3))

# 元组元素的访问
# 格式：元组名[下标]    下标从零开始
print(tuple2[0])
print(tuple2[-1])    # 获取最后一个元素
print(tuple2[-2])
# 修改元组
# tuple2[0] = 100   报错，因为元组不能变
tuple4 = (1, 2, 3, 4, [5, 6, 7])
tuple4[-1][0] = 100
print(tuple4)    # 因为在栈区中的tuple引用了在堆区的(1, 2, 3，0x200)的内存地址，而列表[5, 6, 7]
# 保存在堆区的另一个内存地址里，元组只是引用了数组的内存地址，所以只要保证列表的内存地址不变，
# 列表里的元素是可以改变的。元组不可变是指元组里的数据不能变，但列表是另一片内存了

# 删除元组
tuple5 = (5, 6, 7)
del tuple5

# 元组的操作
t6 = (1, 2, 3)
t7 = (4, 5, 6)
t8 = t6 + t7
print(t8)
# 元组重复
print(t6*3)
# 判断元素是否在元组中
print(1 in t6)
# 元组的截取
print(t8[3: 5])  # 左闭右开
# 二维元组: 元素为一维元组的元组
t9 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(t9[1][2])
# 元组的方法
t10 = (1, 2, 3, 4, 5)
print(len(t10))    # 返回元组中元素的个数
print(max(t10))    # 返回元组中的最大值
print(min(t10))    # 返回元组中的最小值
list1 = [1, 2, 3]
tuple11 = tuple(list1)
print(tuple11)     # 将列表转为元组
# 元组的遍历
for i in (1, 2, 3, 4, 5):
    print(i)

# String(字符串)
# split(str=""[, num])  以str为分隔符截取字符串,指定num，则仅截取num个字符串
str1 = "Tom*****is**a****good***man"
print(str1.split("*", 6))
list2 = str1.split("*")
c = 0
for i in list2:
    if len(i) > 0:
        c += 1
print(c)
# splitlines([keepends])  按照(‘\r’,‘\r\n’,‘\n’)分隔,keepends == True  会保留换行符
str2 = '''Tom is a good man
Tom is a nice man
Tom is a handsome man
'''
print(str2.splitlines())
print(str2.splitlines(True))
# join(seq)    以指定的字符串分割符，将seq中的所有元素组合成一个字符串
list3 = ["Tom", "is", "a", "good", "man"]
str3 = " ".join(list3)
print(str3)
# max() min()
str4 = "Tom is a good man!z"
print(max(str4))
print("*"+min(str4)+"*")
# replace(oldstr, newstr, count) 用newstr替换oldstr，默认是全部替换
str5 = "Tom is a good good man"
str6 = str5.replace("good", "nice", 1)
print(str5)
print(str6)
# 创建一个字符串映射表
t7 = str.maketrans("om", "65")  # o---6 m---5
str8 = str5.translate(t7)
print(str8)
# startwith(str, start=0, end=len(str)) 在给定的范围内判断是否以给定的字符串开头
str9 = "Tom is a good man开"
print(str9.startswith("T", 5, 16))
# endwith(str, start=0, end=len(str))   在给定的范围内判断是否以给定的字符串结尾
print(str9.endswith("man"))
# encode(encoding="utf-8", errors="strict") 编码
data = str9.encode("utf-8", "ignore")   # ignore忽略错误
print(data)
print(type(data))
str10 = data.decode("gbk", "ignore")    # 解码    注意：要与编码时的编码格式一致
print(str10)
# isalpha() 如果字符串中有且仅有一个字符且所有的字符都是字母返回True,否则返回False
str11 = "Tom is a good man"
print(str11.isalpha())
# isalnum() 如果字符串中有且仅有一个字符且所有的字符都是字母或数字返回True,否则返回False
str12 = "1a2bd "
print(str12.isalnum())
# isupper() 如果字符串中至少有一个英文字符且所有的英文字符都是大写的英文字母返回True,
# 否则返回False
print("ABC".isupper())
print("ABC2".isupper())
print("ABC#".isupper())
print("ABCa".isupper())
# islower() 如果字符串中至少有一个英文字符且所有的英文字符都是小写的英文字母返回True,
# 否则返回False
print("abc1".islower())
print("abcA".islower())
# istitle() 如果字符串是标题化的返回True,否则返回False
print("Tom Is A Good Man".istitle())
# isdigit() 如果字符串中只包含数字字符返回True,否则返回False
print("123a".isdigit())
# isnumeric()同上
print("1234".isnumeric())
print("1234a".isnumeric())
# isdecimal()如果字符串中只包含十进制字符返回True,否则返回False
print("1234".isdecimal())
print("123z".isdecimal())
# 如果字符串中只包含空格则返回True,否则返回False
print("  ".isspace())
print("\t".isspace())
print("\n".isspace())
print("\r".isspace())
print("\f".isspace())


# dict(字典)
"""
概述：使用键-值(key-value)存储，具有极快的查找速度
注意：字典是无序的
key的特性：
1. 字典中的key必须唯一
2. key必须是不可变对象
3. 字符串、整数等都是不可变的，可以作为key
4. list是可变的，不能作为key
思考：保存多位学生的姓名与成绩
使用字典,学生姓名为key，学生成绩作为值
"""
dict1 = {"tom": 60, "nike": 70}

# 元素的访问
# 获取：字典名[key]
print(dict1["nike"])
print(dict1.get("alice"))
# 添加
dict1["john"] = 99
dict1["nike"] = 80  # 因为一个key对应一个value,所以多此对一个key的value赋值，其实就是修改值
print(dict1)
# 删除
dict1.pop("tom")
print(dict1)

# 遍历
for key in dict1:
    print(key, dict1[key])
print(dict1.values())
for value in dict1.values():
    print(value)
print(dict1.items())
for k, v in dict1.items():
    print(k, v)
for k, v in enumerate(dict1):
    print(k, v)
# 和list比较
"""
1. 查找和插入的速度极快，不会随着key-value的增加而变慢
2. 需要占用大量的内存，内存浪费多
"""

str13 = '''tom is a good man tom is a nice man tom is a handsome man tom is a good man 
tom is a nice man tom is a handsome man tom is a great man tom is a noble man 
tom is a cool man tom is a good man
'''
d = {}
l1 = str13.split(" ")
for i in l1:
    c = d.get(i)
    if c is None:
        d[i] = 1
    else:
        d[i] += 1
print(d)

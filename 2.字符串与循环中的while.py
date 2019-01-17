# 字符串（字符串是以单引号或双引号括起来的任意文本）
str1 = "Tom is a good man"
str3 = "Tom is a nice man"
str5 = "Tom is a handsome man"

# 字符串运算
# 字符串连接
str6 = "Tom is a "
str7 = "good man"
print("str6 + str7", str6+str7)
# 重复输出字符串
str8 = "good"
str9 = str8 * 3
print("str9 = ", str9)
# 访问字符串中的某一个字符
# 通过索引下标查找字符，索引从0开始
print(str1[1])
""""
str1[1] = "a"
print("str1 =", str1)(会报错，因为字符串不可变)
"""

# 截取字符串中的一部分
str10 = str3[6:14]  # 空格也是一个字符,6包含14不包含
print(str10)
print(str3[:3])
print(str3[10:])

print("good" in str5)
print("man" not in str5)

# 格式化输出
str2 = "Tom is a good man"
num = 10
f = 3.1415
print("num = %d , str2 = %s , f=%f" % (num, str2, f))  # 默认小数点后面6位
print("f = %.3f" % f)  # 精确到小数点后面3位，会四舍五入
# %d %s %f  占位符

# 转义字符
# \n    \"  \'  \t(制表符)
print(" num=%d\n str2=%s\n" % (num, str2))
print('''
good
nice
handsome
''')
"""如果字符中有好多字符串都需要转义，就需要加入好多\,为了简化，python允许用r表示内部的字符串默认
不转义
"""
print(r"\\\t\\")

# eval()
# 功能：将字符串str当成有效的表达式来求值并返回计算结果
num1 = eval("123")
print(num1)
print(type(num1))
print(eval("+123"))
print(eval("-123"))
print(eval("12+3"))
print(eval("12-3"))
# len()     返回字符串的长度
print(len("Tom is a good man"))
# lower() 转换字符串中大写字母为小写字母
str11 = "TOM is a GOOD MAN"
print(str11.lower())    # 字符串本身不能改变
# upper()
print("TOM is a GOOD MAN".upper())
print("Tom is a good Man".swapcase())  # 转化字符串中小写字母为大写字母，大写字母为小写字母
print("tom is A GOOD MAN".capitalize())  # 首字母大写，其他小写
print(str11.title())    # 每个单词的首字母大写
print(str11.center(40, "*"))    # 返回一个指定宽度的居中字符串，"*"为填充的字符(默认空格)
print(str11.ljust(40, "%"))  # 返回一个指定宽度的左对齐字符串，"%"为填充的字符(默认空格)
print(str11.rjust(20))
print(str11.zfill(40))  # 右对齐，"0"为填充的字符
str12 = "Tom is a nice man"
print(str12.count("a"))
print(str12.count("a", 4, len(str12)))  # 返回字符串中str出现的个数,
# 可以指定一个范围，默认从头到尾
print(str12.find("i"))  # 从左到右检测str字符串是否包含在字符串中，可以指定范围，默认从头到尾。
# 得到的是第一次出现的开始下标，没有返回-1
print(str12.rfind("o"))  # 从右向左查找
print(str12.index("i"))    # 和find()一样，只不过如果str不存在的时候会报错
print(str12.rindex("o"))
str13 = "    **Tom is a good man"
print(str13.lstrip())  # 截掉字符串左侧指定的字符，默认为空格
str14 = "Tom is a good man*******"
print(str14.rstrip("*"))
str15 = "*****Tom is a good man****"
print(str15.strip("*"))

# while 语句
"""
while 表达式：
    语句
"""
num = 1
while num <= 5:
    print(num)
    num += 1

str16 = "a"
print(ord(str16))  # ASCII值
str17 = chr(65)
print(str17)

# 注释
"""
12345
上山打老虎
"""
import keyword
import math
import random
print("tom is a good man")
print("tom is a good man ", " tom is a nice man", "tom is a handsome man")
age = input("请输入你的年龄")  # 等号前后也要空格
print("age=", age)  # 逗号后要空格(空几个无所谓),逗号相当于一个空格
print(keyword.kwlist)
name = "小明"
print("name= ", name)
num1 = input("请输入一个数字")
num2 = input("请再输入一个数字")  # python中input输入的都为字符串类
print("num1 + num2 =", num1+num2)
num3 = int(input("请输入一个数字"))
num4 = int(input("请再输入一个数字"))  # python可以处理任意大小的数字（一个亿），当然包括负整数
print("num3 + num4 =", num3+num4)
del age  # 删除后无法引用
print(type(num1), type(num3))
num3 = 5
print(id(num3))  # 查询变量内存地址
num3 = 100
num5 = num3
print(id(num3))
print(id(num5))  # 内存地址一样

# 数学函数
print(pow(2, 5))  # 2^5 2的5次方
print(round(3.1415))
print(round(3.5614))
print(round(3.1415, 1))
print(round(3.5614, 2))  # 四舍五入

print(math.ceil(16.5))
print(math.floor(15.9))   # math.ceil和math.floor为向上取整和向下取整，需导入math
print(math.modf(22.3))  # 返回整数部分与小数部分
print(math.sqrt(16))   # 开方

print(random.choice([1, 3, 5, 7, 9]))  # 从序列的元素中随机挑选一个元素
print(random.choice(range(5)))   # range(5)==[0, 1, 2, 3, 4](不包括5)
print(random.choice("Tom is a good boy"))
print((random.choice(range(100)))+1)  # 随机生成1到100
print(random.randrange(1, 100, 2))  # 随机生成1到100之间(包括1不包括100)的奇数
print(random.random())  # 随机生成0到1之间浮点数

list1 = [1, 2, 3, 4, 5]
random.shuffle(list1)
print(list1)  # 将序列的所有元素随机排序

print(random.uniform(3, 9))  # 随机生成一个实数，它在[3, 9],两侧都包含

# 运算符和表达式
# 算术运算符
"""
+       -       *       /     %         **         //
加      减      乘     除     取余     求幂       取整
"""
# 赋值运算符(=)
# 复合运算符
"""
+=  -=  *=  /=  %=   **=    //=
a+=b 相当于 a=a+b
"""
# 位运算符:按位运算符是把数字看做二进制数来进行计算
# &     按位与运算符
print(5 & 7)
"""
101
111
----
101    两个都为1取1，其他都为0
"""
# |     按位或运算符
# ^     按位异或运算符
# ~     按位取反运算符
# <<    左移动运算符   各二进制位全部左移动若干位，由<<右侧的数字决定，高位丢弃，低位补0
# >>    右移动运算符
print(3 << 2)   # 3左移2位
# 关系运算符
"""
==   !=   >    <     >=     <=
1+2 >3+4
"""
print(1+4 > 3+5)
# 逻辑运算符(与 ，或 ，非)(and ,or ,not)

# 成员运算符(in , not in)
# in:如果在指定的序列中找到值返回True,否则返回False

# 身份运算符(is , is not)
# is:判断两个标识符是不是引用一个对象

# 运算符优先级
"""
**
~   +   -   正负号
*   /   %   //
+   -
>>  <<
&
|   ^
<=  <   >   >=
==  !=
=   +=  -=  %=  ...
is  is not
in  not in
not or   and
"""
# 短路原则
# 表达式1(假) and 表达式2 and 表达式3
# 表达式1(真) or 表达式2 or 表达式3

# if语句
"""
格式：
    if 表达式:
        语句
"""
num6 = 8
num7 = 10
if num6 == num7:
    num6 = 100
# if-else语句
"""
格式：
if 表达式:
    语句1
else:
    语句2
"""

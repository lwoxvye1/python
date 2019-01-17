from collections import Iterable
from collections import Iterator
""" set:类似dict,是一组key的集合，不存储value
本质：无序和无重复元素的集合
"""
# 创建
# 创建set需要一个list或者tuple或者dict作为输入集合
# 重复元素在set中会自动被过滤
s1 = set([1, 2, 3, 4, 5, 3])
print(s1)
s2 = set((1, 2, 3, 3, 2, 1))
print(s2)
s3 = set({1: "good", 2: "nice"})
print(s3)
# 添加
s1.add(6)   # 可以添加重复的，但是没有效果
print(s1)
# s1.add([7, 8, 9])     set的元素不能是列表，因为列表是可变的
s1.add((7, 8, 9))
print(s1)
# s1.add([{1: "a"}])    set的元素不能是字典，因为字典是可变的
print(s1)
#  插入整个list,tuple,字符串，打碎插入
s2.update([6, 7, 8])
print(s2)
s2.update((9, 10))
print(s2)
s2.update("Tom")
print(s2)
# 删除
s3.remove(2)
print(s3)
# 遍历
s4 = set([1, 2, 3, 4, 5])
for i in s4:
    print(i)
# set没有索引的
for index, data in enumerate(s4):
    print(index, data)
s5 = set((3, 4, 5, 6, 7))
# 交集
a1 = s4 & s5
print(a1)
print(type(a1))
# 并集
a2 = s4 | s5
print(a2)
print(type(a2))

# 类型转换
l1 = [1, 2]
s6 = set(l1)
print(s6)
l2 = list(s6)
print(l2)       # set是为了给list、tuple去重

# 迭代器
"""
可迭代对象:可以直接作用于for循环的对象统称为可迭代对象(Iterable),可以用isinstance()去
 判断一个对象是否是Iterable对象
 
 可以直接作用于for的数据类型一般分两种
 1.集合数据类型，如list, tuple, dict, set, string
 2.是generator,包括生成器和带yield的generator function 
"""
print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance({}, Iterable))
print(isinstance("", Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(1, Iterable))
"""
迭代器：不但可以作用于for循环， 还可以被next()函数不断调用并返回下一个值， 直到最后跳出
一个StopIteration错误表示无法继续返回下一个值
可以被next()函数调用并不断返回下一个值的对象称为迭代器(Iterator对象)
可以使用isinstance()函数判断一个对象是否是Iterator对象
"""
print(isinstance([], Iterator))
print(isinstance((), Iterator))
print(isinstance({}, Iterator))
print(isinstance("", Iterator))
print(isinstance((x for x in range(10)), Iterator))

l = (x for x in range(5))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))

m = (y for y in [23, 4, 5, 64, 3435])
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))

# 转成Iterator对象
a = iter([1, 2, 3, 4, 5])
print(next(a))

print(isinstance(iter((1, 2, 3, 4, 5)), Iterator))

# 案例
"""endstr = "end"
str1 = ""
for line in iter(input, endstr):
    str1 += line + "\n"
print(str1)
"""

"""
认识函数：在一个完整的项目中，某些功能会反复的使用，那么我们会将功能封装成函数，当我们
要使用功能的时候直接调用函数即可
本质：函数就是对功能的封装
优点:1.简化代码结构，增加了代码的复用度(重复使用的程度)
2.如果想修改某些功能或者修改某个BUG，只需要修改对应的函数即可
"""
"""
定义函数：
格式：
def 函数名(参数列表):
    语句
    return 表达式
def:函数代码块以def关键字开始
函数名:遵循标识符规则
():是参数列表的开始和结束
参数列表:任何传入函数的参数和变量必须放在圆括号之间，用逗号分隔。函数从函数的调用者
那里获取的信息
冒号:函数内容(封装的功能)以冒号开始，并且缩进
语句:函数封装的功能
return:一般用于结束函数，并返回信息给函数的调用者
表达式:即为要返回给函数的调用者的信息
注意：最后的return表达式，可以不写，相当于return None

函数的调用:
格式:函数名(参数列表)
函数名：是要使用的功能的函数名字
参数列表:函数的调用者给函数传递的信息，如果没有参数，小括号也不能省略

函数调用的本质：实参给形参赋值的过程
"""
# 最简单的函数(无参无返回值)


def myPrint():
    print("Tom is a good man")
    print("Tom is a nice man")
    print("Tom is a handsome man")


myPrint()

# 函数的参数


def myPrint1(str1, age):    # 形参(形式参数):定义函数时小括号中的变量，本质是变量
    print(str1, age)        # 参数必须按顺序传递，个数目前要对应


myPrint1("Tom is a good man", 18)  # 实参(实际参数):调用函数时给函数传递的数据，本质是值

# 函数的返回值


def mySum(num1, num2):
    sum1 = num1 + num2
    return sum1         # 将结果返回给函数的调用者
    print("*******")    # 执行完return语句，该函数就结束了，return后面的代码不执行


sum2 = mySum(5, 9)
print(sum2)

# 参数的传递
"""
值传递:传递的不可变类型    string、tuple、number
引用传递:传递的可变类型    list、dict、set是可变的
"""


def func1(num):
    print(id(num))
    num = 10
    print(id(num))


temp = 20
print(id(temp))
func1(temp)     # 栈区中的temp把20这个值赋予了在堆区的函数里的num，然而修改的却只有num
print(temp)     # 所以是两个变量


def func2(list1):
    list1[0] = 100


list2 = [1, 2, 3, 4, 5]
func2(list2)    # 而此处list2和list1只是引用了[1, 2, 3, 4, 5]的内存地址，
print(list2)    # 所以通过内存地址修改列表的值，两个都会改变

# 关键字参数
"""
概念:允许函数调用时参数的顺序与定义时不一致 

"""


def myPrint2(str1, age):
    print(str1, age)


# 使用关键字参数
myPrint2(age=18, str1="Tom is a good man")

# 默认参数
"""
概念：调用函数时，如果没有传递参数，则使用默认参数
"""


def myPrint3(str1="Tom is a good man", age=18):
    print(str1, age)


myPrint3()
myPrint3("Tom is a nice man", 19)


def myPrint4(str1, age=18):  # 以后要用默认参数，将默认参数放到最后
    print(str1, age)


myPrint4("Tom is a handsome man")

# 不定长参数
"""
概念:能处理比定义时更多的参数
"""


def func3(name, *args):   # 加了星号(*)的变量存放所有未命名的变量参数，如果在函数
    print(name)          # 调用时没有指定参数，它就是一个空元组
    print(type(args))
    for x in args:
        print(x)


func3("Tom", "good", "nice", "handsome")


def mySum2(*l):
    sum1 = 0
    for i in l:
        sum1 += i
    return sum1


print(mySum2(1, 2, 3, 4))


def func4(**kwargs):       # **代表键值对的参数字典，和*所代表意义类似
    print(kwargs)
    print(type(kwargs))


func4(x=1, y=2, z=3)


def func5(*args, **kwargs):  # 可以接收任意参数
    pass    # 代表一个空语句


# 匿名函数
"""
概念：不使用def这样的语句定义函数，使用lambda来创建匿名函数

特点：1.lambda只是一个表达式，函数体(语句能实现的功能)比def简单
2.lambda的主体是一个表达式，而不是代码块，仅仅只能在lambda表达式中封装简单的逻辑
3.lambda函数有自己的命名空间，且不能访问自由参数列表之外的或全局命名空间的参数
4.虽然lambda是一个表达式且看起来只能写一行，与C和C++内联函数不同。python是没有效率可言

格式：lambda 参数1，参数2，....,参数n: expression
"""
sum1 = lambda num1, num2: num1 + num2
print(sum1(5, 9))

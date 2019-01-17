import functools

# 装饰器
"""
概念:是一个闭包，把一个函数当作参数返回一个替代版的函数
，本质上就是一个返回函数的函数
"""


# 简单的装饰器


def func1():
    print("Tom is a good man")


def outer():
    print("******")
    func1()


outer()


def outer2(func):
    def inner():
        print("*****")
        func()

    inner()
    return inner


f = outer2(func1)  # f()是函数func1的加强版本
f()


# 复杂一点的装饰器


def outer3(func):
    def inner(age):
        if age < 0:
            age = 0
        func(age)

    return inner


@outer3  # 相当于say = outer(say)
# 使用@符号将装饰器应用到函数
def say(age):
    print("Tom is %d years old" % age)


say(-10)


# 通用装饰器


def outer4(func):
    def inner(*args, **kwargs):
        # 添加修饰的功能
        print("&&&&")
        func(*args, **kwargs)

    return inner


@outer4
def say(name, age):  # 函数的参数理论上是无限制的，但实际上最好不要超过6、7个
    print("my name is %s,I am %d years old" % (name, age))


say("Tom", 18)

# 偏函数
print(int("1010", base=2))


def int2(str1, base=2):
    return int(str1, base)


print(int2("1011"))

# 把一个参数固定住，形成一个新的函数
int3 = functools.partial(int, base=2)
print(int3("1111"))

# 变量的作用域
"""
作用域：变量可以使用的范围

程序的变量并不是在所有位置都能使用的，访问的权限决定于变量的位置

作用域：
局部作用域
全局作用域
内建作用域
"""

# 异常处理
"""
需求: 当程序遇到问题时不让程序结束，而遇到错误继续向下执行
try......except......else
格式:
try:
    语句t
except 错误代码  as e:
    语句1
except 错误代码  as e:
    语句2
......
else:
    语句e

注意:else语句可有可无
作用：用来检测try语句块中的错误，从而让except语句捕获错误信息并处理
逻辑：当程序执行到try-except-else语句时
1.如果当try语句t执行出现错误时，会匹配第一个错误码，如果匹配上就执行对应“语句”
2.如果当try语句t执行出现错误时，没有匹配的异常，错误将会被提交到上一层的
try语句,或者到程序的最上层
3.如果当try语句t执行没有出现错误，执行else下的“”语句e
"""
try:
    print(3 / 0)
    print(num)
except  ZeroDivisionError as e:
    print("除数为0")
except NameError as e:
    print("没有该变量")
else:
    print("代码没有问题")
print("*******")

# 使用except而不使用任何的错误类型
try:
    print(4 / 0)
except:
    print("程序出现了异常")

# 使用except带着多种异常
try:
    pass
except(NameError, ZeroDivisionError):
    print("出现了NameError或ZeroDivisionError")

# 特殊
# 1、错误其实是class(类)，所有的错误都继承自BaseException，所以在捕获的时候
# ，它捕获了该类型的错误，还把子类一网打尽
try:
    print(5 / 0)
except BaseException as e:
    print("异常一")
except ZeroDivisionError as e:
    print("异常二")


# 2、跨越多层调用


def func1(num):
    print(1 / num)


def func2(num):
    func1(num)


def main(num):
    func2(num)  # main调用了func2，func2调用了func1，func1出现了错误


#  ，这时只要main捕获到了就可以处理


try:
    main(0)
except ZeroDivisionError as e:
    print("****")

# try.....except...finally
"""
格式:
try:
    语句t
except 错误代码  as e:
    语句1
except 错误代码  as e:
    语句2
......
finally:
    语句f
作用：语句t无论是否有错误都将执行最后的语句f
"""
try:
    print(1 / 0)
except ZeroDivisionError as e:
    print("为0了")
finally:
    print("必须执行我")

# 断言


def func(num, div):
    assert (div != 0), "div不能为0"
    return(num / div)


print(func(10, 2))

# 文件读写
# 1.读文件(与C兼容)
"""
过程:
1.打开文件
open(path, flag[，encoding][, errors ])
path:要打开文件的路径
flag:打开方式
r   以只读的方式打开文件，文件的描述符放在文件的开头
rb  以二进制格式j-jh在文件的开头
r+  打开一个文件用于读写，文件的描述符放在文件的开头
w   打开一个文件只用于写入，如果该文件已经存在会覆盖，如果不存在则创建新文件
wb  打开一个文件只用于写入二进制，如果该文件已经存在会覆盖，如果不存在则创建新文件
w+  打开一个文件用于读写，如果该文件已经存在会覆盖，如果不存在则创建新文件
a   打开一个文件用于追加，如果文件存在，文件描述符将会放到文件末尾
a+  打开一个文件用于读写，如果文件存在，文件描述符将会放到文件末尾
encoding:编码方式
errors:错误处理
2.读文件内容
(1)读取文件全部内容
str1 = f.read()
print(str1)
(2)读取指定字符数
(3)读取整行，包括/n字符
(4)读取所有行并返回列表
3.关闭文件
f.close()
"""
path = r"D:\学习\python\project\file1.txt"
# f = open(path, "r", encoding="utf-8", errors="ignore")  # 忽略错误
f = open(path, "r", encoding="utf-8")

# 读取指定字符数
str1 = f.read(10)
print(str1)
str2 = f.read(10)
print("*"+str2+"*")

# 读取整行，包括/n字符
f.seek(0)       # 修改文件描述符的位置
str4 = f.readline()
print(str4)
str5 = f.readline()
print(str5)

# 读取所有行并返回列表
f.seek(0)
list6 = f.readlines()
print(list6)

f.close()

# 一个完整的过程
try:
    f1 = open(path, "r", encoding="utf-8")
    print(f1.read())
finally:
    if f1:  # 如果是打开失败了就没有必要关闭了
        f1.close()

# 另一种打开方式
with open(path, "r", encoding="utf-8") as f2:   # with最后会自动把文件关上
    print(f2.read())

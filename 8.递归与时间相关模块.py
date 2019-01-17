import _collections
import os
import time
import datetime
import calendar
"""
递归调用：一个函数，调用了自身，称为递归调用
递归函数：一个会调用自身的函数称为递归函数

凡是循环能干的事，递归都能干
"""
"""
方式：
1.写出临界条件
2.找这一次和上一次的关系
3.假设当前函数已经能用，调用自身计算上一次的结果，再求出本次的结果
"""

# 输入一个数(大于等于1)，求1+2+3+....+n的和


def sum1(n):
    sum2 = 0
    for i in range(1, n+1):
        sum2 += i
    return sum2


res = sum1(5)
print("res = ", res)

"""
sum3(1) +2 =sum3(2)
sum3(2) +3 =sum3(3)
sum3(3) +4 =sum3(4)
sum3(4) +5 =sum3(5)
"""


def sum3(n):
    if n == 1:
        return 1
    else:
        return n+sum3(n-1)


print(sum3(10))

# 栈和队列
# 栈
# 模拟栈结构
stack = []
# 压栈(向栈里存数据)
stack.append("A")
print(stack)
stack.append("B")
print(stack)
stack.append("C")
print(stack)
# 出栈(在栈里取数据)
res1 = stack.pop()
print("res1 =", res1)
print(stack)        # 先压栈进去的是A而先出栈的是C
res2 = stack.pop()
print("res2 =", res2)
print(stack)
res3 = stack.pop()
print("res3 =", res3)
print(stack)        # 栈结构是先进后出

# 队列
# 创建一个队列
queue = _collections.deque()
print(queue)
# 进队
queue.append("A")
print(queue)
queue.append("B")
print(queue)
queue.append("C")
print(queue)
# 出队(取数据)
res1 = queue.popleft()
print("res1 =", res1)
print(queue)
res2 = queue.popleft()
print("res2 =", res2)
print(queue)
res3 = queue.popleft()
print("res3 =", res3)
print(queue)            # 队列的结构是先进先出


# 目录遍历
# 1.递归遍历目录


def getAllDirRecursion(path, space="  "):
    # 得到当前目录下的所有文件
    filesList = os.listdir(path)
    space += "  "
    # 处理每一个文件
    for fileName in filesList:
        # 拼接成绝对路径
        fileAbsPath = os.path.join(path, fileName)
        # 判断是否是目录
        if os.path.isdir(fileAbsPath):
            print(space+"目录：", fileName)
            getAllDirRecursion(fileAbsPath, space)
        else:
            print(space+"普通文件：", fileName)


getAllDirRecursion(r"D:\学习\python\project")
print("*************")

# 2.栈模拟递归遍历目录(深度遍历)


def getAllDirDeep(path):
    stack = []
    stack.append(path)
    # 处理栈，当栈为空的时候结束循环
    while len(stack) != 0:
        # 从栈里取出数据
        dirPath = stack.pop()       # 先进后出
        # 目录下所有文件
        filesList = os.listdir(dirPath)
        # 处理每一个文件，如果是普通文件则打印出来，如果是目录则将该目录的地址压栈
        for fileName in filesList:
            fileAbsPath = os.path.join(dirPath, fileName)
            if os.path.isdir(fileAbsPath):
                # 是目录就压栈
                print("目录：", fileName)
                stack.append(fileAbsPath)
            else:
                # 否则打印普通文件
                print("普通文件", fileName)


getAllDirDeep(r"D:\学习\python\project")
print("*************")

# 3.队列模拟递归遍历目录(广度遍历)


def  getAllDirQueue(path):
    queue = _collections.deque()
    # 进队
    queue.append(path)
    while len(queue) != 0:
        # 出队
        dirPath =queue.popleft()
        # 找出所有文件
        filesList = os.listdir(dirPath)
        for fileName in filesList:
            # 绝对路径
            fileAbsPath = os.path.join(dirPath, fileName)
            if os.path.isdir(fileAbsPath):
                # 是目录就进队
                print("目录：", fileName)
                queue.append(fileAbsPath)
            else:
                # 不是就打印
                print("普通文件", fileName)


getAllDirQueue(r"D:\学习\python\project")


# time
"""
UTC(世界协调时间):格林尼治天文时间，世界标准时间，在中国来说是UFC+8
DST(夏令时)：是一种节约能源而人为规定的时间制度，在夏季调快1个小时

时间的表示形式：
1.时间戳：以整型或浮点型表示时间的一个以秒为单位的时间间隔。这个时间间隔的基础值是
从1970年1月1日零点开始算起
2.元组：一种python的数据结构表示，这个元组有9个整型内容
year    month   day     hours   minutes     seconds     weekday     Julia day   flag(1 or -1 或 0)
3.格式化字符串
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12） 
%M 分钟数（00=59）
%S 秒（00-59）
%f 毫秒（000000-999999）

%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身 
"""
# 返回当前时间的时间戳，浮点数形式，不需要参数
c = time.time()
print(c)
# 将时间戳作为UTC时间元组
t = time.gmtime(c)
print(t)
# 将时间戳转为本地时间元组
b = time.localtime(c)
print(b)
# 将本地时间元组转成时间戳
m = time.mktime(b)
print(m)
# 将时间元组转成字符串
s = time.asctime(b)
print(s)
# 将时间戳转为字符串
p = time.ctime(c)
print(p)
# 将时间元组转换成给定格式的字符串，参数2为时间元组，默认本地当前时间
q = time.strftime("%Y-%m-%d %H:%M:%S", b)
print(q)
# 将时间字符串转为时间元组
w = time.strptime(q, "%Y-%m-%d %X")
print(w)
# 延迟一个时间，整型或者浮点型
time.sleep(2)
# 返回当前程序的cpu执行时间(运行这段代码花了多少时间)
# Unix系统始终返回全部的运行时间
# windows从第二次开始，都是以第一次调用此函数的开始时间戳作为基数
y1 = time.clock()
print(y1)
time.sleep(1)
y2 = time.clock()
print(y2)
time.sleep(1)
y3 = time.clock()
print(y3)


# datetime
"""
datetime比time高级不少，可以理解为datetime基于time进行了封装，提供了更为实用的函数，
datetime模块的接口(方法)更直观，更容易调用

模块中的类：
datetime    同时有时间和日期
timedelta   主要用于计算时间的跨度
tzinfo      时区相关
time        只关注时间
date        只关注日期
"""
# 获取当前时间
d1 = datetime.datetime.now()
print(d1)
print(type(d1))
# 获取指定时间
d2 = datetime.datetime(1997, 11, 6, 10, 28, 25, 123456)
print(d2)
# 将时间转为字符串
d3 = d1.strftime("%y-%m-%d %X")
print(d3)
print(type(d3))
# 将格式化字符串转为datetime对象       注意：转换的形式要与字符串一致
d4 = datetime.datetime.strptime(d3, "%y-%m-%d %X")

d5 = d1-d2
print(d5)
print(type(d5))
# 间隔的天数
print(d5.days)
# 间隔天数除外的秒数
print(d5.seconds)


# calendar  日历模块
# 使用
# 返回指定某年某月的日历
print(calendar.month(2018, 11))
# 返回指定某年的日历
print(calendar.calendar(2018))
# 判断闰年
print(calendar.isleap(2010))
# 返回某个月的第一天与星期天相差的天数和这个月的总天数
print(calendar.monthrange(2018, 12))
# 返回某个月以每一周为元素的列表
print(calendar.monthcalendar(2018, 11))

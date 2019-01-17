import random
import turtle

# 布尔值和空值
"""
布尔值：一个布尔值只有True和False两种值。
空值：是Python里一个特殊的值，用None表示。None在Python中不能理解为0。因为
0是有意义的，而None是一个特殊值。
"""
n1 = True
n2 = False
print(n1, n2)
n3 = None
print(n3)

# list(列表)
# 创建列表
# 格式： 列表名 = [列表选项1, 列表选项2, ...]
list1 = []
list2 = [18, 19, 20, 21, 22]
# 注意：列表中的元素数据可以是不同类型
list3 = [1, 2, "Tom", "good", True]
print(list3)
# 列表元素的访问
# 取值    格式 ： 列表名[下标](从0开始)  注意不要越界(下标超过可表示的范围)
print(list3[2])
# 替换
list3[2] = 300
print(list3)

# 列表操作
# 列表组合
list5 = [1, 2, 3]
list6 = [4, 5, 6]
list7 = list5 + list6
print(list7)
# 列表的重复
list8 = [1, 2, 3]
print(list8 * 3)
# 判断元素是否在列表中
print(3 in list5)
# 列表截取
print(list7[2:5])  # 左闭右开
print(list7[:5])
print(list7[3:])
# 二维列表
list9 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list9[1][2])
# 列表方法
list10 = [1, 2, 3, 4, 5]
list10.append(6)  # 在列表末尾添加新的元素
list10.append([7, 8, 9])
print(list10)
list11 = [1, 2, 3, 4, 5]
list11.extend([6, 7, 8])  # 在末尾一次性追加另一个列表中的多个值
print(list11)
list12 = [1, 2, 3, 4, 5]
list12.insert(1, 100)  # 在下标前添加一个元素，不覆盖原数据，原数据向后顺延
print(list12)
list12.insert(2, [200, 300])
print(list12)

list13 = [1, 2, 3, 4, 5]
list13.pop(2)  # pop(x=list[-1])   移除列表中指定下标出的元素(默认最后一个元素)
# ，并返回删除的数据
print(list13)
print(list13.pop(3))

list14 = [1, 2, 3, 4, 5, 4, 4]
list14.remove(4)  # 移除列表中的指定元素第一个匹配的结果
print(list14)

list15 = [1, 2, 3, 4, 5]
list15.clear()
print(list15)

list16 = [1, 2, 3, 4, 5]
index = list16.index(3)  # 从列表中找出某个值的第一个匹配的下标
print(index)
list17 = [1, 2, 3, 4, 5, 2, 5, 3, 5]  # 圈定一个范围
print(list17.index(3, 3, 8))

list18 = [1, 2, 3, 4, 5]
print(len(list18))  # 列表元素的个数

list19 = [1, 2, 3, 4, 5, 3, 4, 3]
print(list19.count(3))  # 查看元素在列表中出现的次数
num = 0
a = list19.count(3)
while num < a:
    list19.remove(3)
    num += 1
print(list19)

list20 = [1, 2, 3, 4, 5]
print(max(list20))  # 获取列表中的最大值
print(min(list20))  # 获取列表中的最小值

list21 = [1, 2, 3, 4, 5]
list21.reverse()  # 倒序
print(list21)

list22 = [2, 1, 3, 5, 4]
list22.sort()  # 排序  默认升序
print(list22)

list23 = [1, 2, 3, 4, 5]
list24 = list23  # 浅拷贝(引用拷贝)
list24[1] = 100  # 如果修改list24,list23也会被修改
print(list23)  # 因为栈区的成员变量只是引用了在堆区创建的[1,2,3,4,5]的内存地址,而list24
# 是将这个内存地址拷贝下来，两不同变量指向一个内存地址。因此修改堆区的数据，两变量都会被修改
print(list24)
print(id(list23), id(list24))

list25 = [1, 2, 3, 4, 5]
list26 = list25.copy()  # 深拷贝     内存的拷贝
list26[2] = 100  # .copy()会在堆区再开辟一片空间并将数据拷贝，两变量指向不同内存地址
print(list25, list26)
print(id(list25), id(list26))

list27 = list((1, 2, 3, 4))  # 将元组转换为列表(元组为小括号)
print(list27)

# 找出十个数据第二大的值
"""
listNum = []
num = 0
while num < 10:
    value = int(input("请输入十个数"))
    listNum.append(value)
    num += 1
print(listNum)
listNum.sort()
count = listNum.count(listNum[len(listNum)-1])
c = 0
while c < count:
    listNum.pop()
    c += 1
print(listNum[len(listNum)-1])
"""
# 或者
list27 = []
num = 0
while num < 10:
    value = random.choice(range(100)) + 1
    list27.append(value)
    num += 1
print(list27)
if list27[0] >= list27[1]:
    max1 = list27[0]
    sec = list27[1]
else:
    max1 = list27[1]
    sec = list27[0]
index = 2
while index < len(list27):
    if list27[index] > sec:
        if list27[index] > max1:
            sec = max1
            max1 = list27[index]
        elif list27[index] == max1:
            sec = sec
            max1 = max1
        else:
            sec = list27[index]
    index += 1
if sec == max:
    print("debug")
print(max1, sec)

"""
if-elif-else语句
格式：
if  表达式1：
    语句1
elif    表达式2：
    语句2
elif    表达式：
    语句3
....    #每个elif都是对它上面所有表达式的否定
else:   # 可有可无
    语句e

死循环
while 1:
    print("Tom is a good man")

使用else语句
while 表达式：
    语句1
else:
    语句2

for语句 
for 变量名 in 集合：
    语句
"""
for i in [1, 2, 3, 4, 5]:
    print(i)
"""
range([start, ]end[, step])函数 (左闭右开)  列表生成器
功能：生成数列
"""
for i in range(10):
    print(i)
for i in range(2, 20, 2):
    print(i)

# 同时便利下标和元素
for index, m in enumerate([1, 2, 3, 4, 5]):
    print(index, m)

sum1 = 0
for i in range(1, 101):
    sum1 += i
print(sum1)

# break语句
# 作用：跳出for和while循环
# 注意:只能跳出距离他最近的那一层循环

# continue语句
# 作用：跳过当前循环中的剩余语句，然后继续下一次循环
# 注意：跳过距离最近的循环
for i in range(10):
    print(i)
    if i == 3:
        continue
    print("*")
    print("&")

# turtle模块绘图
"""
是一个简单的绘图工具
提供一个小海龟，可以把它理解为一个机器人，只能听懂有限的命令
绘图窗口的原点在正中间，默认海龟的方向是右侧
    运动命令
        forward(d) 向前移动d长度
        backward(d) 向后移动d长度
        right(d)    向右转动多少度
        left(d)     向左转动多少度
        goto(x, y)   移动到坐标为(x, y)的位置
        speed(speed) 笔画绘制的速度[0, 10]
    笔画控制命令
        up()        笔画抬起，在移动的时候不会绘图
        down()      笔画落下，移动会绘图
        setheading(d)  改变海龟的朝向
        pensize(d)  笔画的宽度
        pencolor(colorstr)  笔画的颜色
        reset()     恢复所有设置，清空窗口，重置turtle状态
        clear()     清空窗口，不会重置turtle
        circle(r[, step=e]) 绘制一个圆形，r为半径，e为几边形
        begin_fill()    填充  三个一起使用
        fillcolor(colorstr) 填充指定颜色
        end_fill()      结束填充
    其他命令
        done() 程序继续执行
        undo() 撤销上一次动作
        hideturtle()    隐藏海龟
        showturtle()    显示海龟
"""

turtle.speed(2)
turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.goto(-100, 200)
turtle.up()
turtle.goto(-100, 100)
turtle.down()
turtle.pencolor("red")
turtle.pensize(10)
turtle.forward(30)
turtle.setheading(50)
turtle.clear()
# turtle.reset()
turtle.begin_fill()
turtle.fillcolor("blue")
turtle.circle(30)
turtle.end_fill()
turtle.circle(100, steps=7)
turtle.forward(50)
turtle.undo()
turtle.hideturtle()
turtle.showturtle()
turtle.done()

# 第一个python类(创建类)
"""
类名：见名之意，首字母大写，其他遵循驼峰原则
属性：见名之意，其他遵循驼峰原则
行为(方法/功能)：见名之意，其他遵循驼峰原则

类名：Car
属性：color  type
行为：跑
"""
"""
创建类
类：一种数据类型，本身并不占内存空间，跟所学的number,string,boolean等类似。用类创建
实例化对象(变量)，对象占内存空间
格式：
class  类名(父类列表)：
    属性
    行为
"""


class Person(object):  # object:基类，超类，是所有类的父类，一般没有合适的父类就写object
    # 定义属性(定义变量)
    name = ""
    age = 0
    height = 0
    weight = 0
    # 定义方法
    # 注意：方法的参数必须以self当第一个参数
    # self代表类的实例(某个对象)

    def run(self):
        print(self.__money)
        print("run")

    def eat(self, food):
        print("eat " + food)

    def say(self):
        print("Hello! my name is %s, I am %d years old" % (self.name, self.age))
        print(self.__class__)
        p = self.__class__("Tom", 18, 175, 60, 10000)
        print(p)

    def __init__(self, name, age, height, weight, money):
        print(name, age, height, weight)
        self.name = name    # self相当于java中的this，指当前对象,但self不是关键字
        self.age = age
        self.height = height
        self.weight = weight    # 使用这个，最上面的属性可以去掉
        print("这里是init")
        self.__money = money

    def __del__(self):
        print("这里是析构函数")

# 通过内部的方法，来修改私有属性
# 通过自定义的方法实现对私有属性的赋值和取值
    def setMoney(self, money):
        if money < 0:
            money = 0
        self.__money = money

    def getMoney(self):
        return self.__money


"""   def __str__(self):
        return "%s-%d-%d-%d" % (self.name, self.age, self.height, self.weight)
"""

# 使用类实例化对象
"""
格式： 对象名 = 类名(参数列表)
注意：没有参数小括号也不能省略
"""
# 实例化一个对象
per1 = Person("hanmeimei", 20, 170, 50, 100)
print(per1)
print(type(per1))
print(id(per1))
# 变量per1是在栈区，而对象(实例化对象)则是在堆区，per1只是引用了对象的内存地址
per2 = Person("baba", 21, 180, 70, 10000)
print(per2)
print(type(per2))
print(id(per2))

# 访问对象的属性和方法
"""
访问属性
格式：对象名.属性名
赋值：对象名.属性名 = 新值

访问方法
格式:对象名.方法名(参数列表)
"""
per1.name = "Tom"
per1.age = 18
per1.height = 180
per1.weight = 70
print(per1.name, per1.age, per1.height, per1.weight)
per1.run()
per1.eat("apple")

# 问题：目前来看Person所创建的所有对象属性都是一样的
# 对象的初始状态(构造函数)
"""
构造函数：__init__()     在使用类创建对象的时候自动调用
注意：如果不显示的写出构造函数，默认会自动添加一个空的构造函数
"""

# self
"""
self代表类的实例，而非类

哪个对象调用方法，那么该方法中的self就代表哪个对象，但self不是关键字

self.__class__  代表类名
"""
per1.say()


# 析构函数
"""
析构函数：__del__()  释放对象时自动调用 
堆区的内存一般都要由程序员手动释放，但是python有自己的垃圾处理机制
"""
per3 = Person("John", 20, 160, 160, 10000)
del per3  # 手动释放对象

# while 1:
#     pass


# 在函数里定义的对象，会在函数结束时自动释放，这样可以用来减少内存空间的浪费
def func():
    per4 = Person("aa", 1, 1, 1, 1)
    per4.run()


func()


# 重写__repr__与__str__函数
"""
重写：将函数重新定义写一遍
__str__():在调用print打印对象时自动调用，是给用户用的，是一个描述对象的方法。
__repr__():是给机器用的，在python解释器(cmd)里面直接敲对象名在回车后调用的方法
注意：在没有__str__()时,且有__repr__()时，__str__() = __repr__() 
"""
print(per1)  # 相当于print(per1.__str__())
# 优点： 当一个对象的属性值很多，并且都需要打印，重写了__str__()方法后，简化了代码


# 访问限制
# 如果要让内部的属性不被外部直接访问，在属性前加两个下划线(__),在python中如果在属性
# 前加两个下划线，那么这个属性就变成了私有属性private
# 但是在python中没有绝对私有的属性

# print(per1.__money)       #外部使用
per1.run()  # 内部可以使用
per1.setMoney(1000)
per1.getMoney()
# 不能直接访问per.__money是因为python解释器把__money变成了_Person__money,
# 仍然可以用_Person__money去访问，但是强烈建议不要这么干
# ，不同的解释器可能存在解释的变量名不一致

# 在python中 __XX__ 属于特殊变量，可以直接访问
# 在python中 _XXX 变量，这样的实例变量外部是可以访问的，但是，按照约定的规则，当我们
# 看到这样的变量时，意思时“虽然我可以被访问，但是请把我视为私有变量，不要直接访问我”


# 继承
# 单继承的实现
class PersonA(object):
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.__money = money

    def run(self):
        print("run")

    def eat(self, food):
        print("eat " + food)

    def setMoney(self, money):
        if money < 0:
            money = 0
        self.__money = money

    def getMoney(self):
        return self.__money


class Student(PersonA):
    def __init__(self, name, age, money, stuId):
        # 调用父类中的__init__()
        super(Student, self).__init__(name, age, money)  # 让父类中的self代表的是当前子类中的对象
        # 子类可以有一些自己独有的属性
        self.stuId = stuId
    """def stuFunc(self):
        return self.__money
    """


stu = Student("Tom", 18, 0, 0)
print(stu.name, stu.age)
stu.run()
stu.stuId = 1000
print(stu.stuId)
# print(stu.__money)    私有属性无法访问
print(stu.getMoney())   # 通过继承过来的公有方法访问私有属性
# stu.stuFunc()         无法用子类的公有方法访问私有属性


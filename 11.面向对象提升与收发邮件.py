from types import MethodType
# 多继承的实现


class Father(object):
    def __init__(self, money):
        self.money = money

    def play(self):
        print("play")

    def func(self):
        print("func1")


class Mother(object):
    def __init__(self, faceValue):
        self.faceValue = faceValue

    def eat(self):
        print("eat")

    def func(self):
        print("func2")


class Child(Father, Mother):
    def __init__(self, money, faceValue):
        Father.__init__(self, money)
        Mother.__init__(self, faceValue)


def main():
    c = Child(300, 100)
    print(c.money, c.faceValue)
    c.play()
    c.eat()
    c.func()    # 注意：父类中方法名相同，默认调用的是在括号中排前面的父类中的方法


if __name__ == "__main__":
    main()


# 多态
"""
多态：一种事物的多种形态

最终目标：人可以喂任何一种动物
"""


class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + "吃")


class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)


class Mouse(Animal):
    def __init__(self, name):
        super(Mouse, self).__init__(name)


class Person(object):
    """
    def feedCat(self, Cat):
        print("给你食物")
        Cat.eat()

    def feedMouse(self, Mouse):
        print("给你食物")
        Mouse.eat()
    """
    def feedAnimal(self, animal):
        print("给你食物")
        animal.eat()


tom = Cat("tom")
jerry = Mouse("jerry")
per = Person()
tom.eat()
jerry.eat()
per.feedAnimal(tom)
per.feedAnimal(jerry)


# 对象属性与类属性

class PersonA(object):
    # 这里的属性实际上属于类属性(用类名来调用),继承后也会保留类属性
    name = "Person"

    def __init__(self, name):
        # 对象属性
        self.name = name


print(PersonA.name)
per = PersonA("Tom")  # 对象属性的优先级高于类属性
print(per.name)
# 动态的给对象添加对象属性
per.age = 18    # 只针对于当前对象生效，对于类创建的其他对象没有作用
print(PersonA.name)
# 删除对象中的name属性，再调用会使用到同名的类属性
del per.name
print(per.name)
# 注意：以后千万不要将对象属性与类属性重名，因为对象属性会屏蔽掉类属性。但是当删除对象
# 属性后，再使用又能使用类属性了。


# 动态给实例添加属性与方法并使用
# 创建一个空类
class PersonB(object):
    __slots__ = ("name", "age", "weight", "height", "speak")


per1 = PersonB()
# 动态添加属性，这体现了动态语言的特点(灵活)
per1.name = "Tom"
print(per1.name)
# 动态添加方法


def say(self):
    print("my name is " + self.name)


per1.speak = MethodType(say, per1)
per1.speak()
# 思考：如果想要限制实例的属性怎么办？
# 比如：只允许给对象添加name,age,weight,height属性
# 解决：定义类的时候，定义一个特殊的属性(__slots__),可以限制动态添加的属性


# -@property
class PersonC(object):
    def __init__(self, age):
        # 属性直接对外暴露
        # 不安全，没有数据的过滤
        # self.age = age
        # 限制访问
        self.__age = age    # 使用限制访问，需要自己写get和set方法才能访问
    """
    def getAge(self):
        return self.__age

    def setAge(self, age):
        if age < 0:
            age = 0
        self.__age = age
    """
    @property  # property：可以让你对受限制访问的属性使用点语法
    # 方法名为受限制的变量去掉双下划线
    def age(self):
        return self.__age

    @age.setter  # 去掉下划线.setter
    def age(self, age):
        if age < 0:
            age = 0
        self.__age = age


per2 = PersonC(18)
# per.age = -10
# print(per2.age)
# per2.setAge(15)
# print(per2.getAge())
per2.age = 100  # 相当于调用setAge
print(per2.age)  # 相当于调用getAge
# 但是 __age还是访问受限的


# 运算符重载
print(1 + 2)
print("1" + "2")
# 不同的类型用加法会有不同的解释


class PersonD(object):
    def __init__(self, num):
        self.num = num
    # 运算符重载

    def __add__(self, other):
        return PersonD(self.num + other.num)

    def __str__(self):
        return "num = " + str(self.num)


per3 = PersonD(1)
per4 = PersonD(2)
print(per3 + per4)  # per3 + per4 ==
# print(per3.__add__(per4))
print(per3)
print(per4)


# 发短信和邮件

# 互亿无线-短信验证码
# 发短信
"""
APIID：C83337409
APIKEY：4f62add3dce15c1370425e069051df27
"""
# 接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
# 账户注册：请通过该地址开通账户http://sms.ihuyi.com/register.html
# 注意事项：
# （1）调试期间，请用默认的模板进行测试，默认模板详见接口文档；
# （2）请使用APIID（查看APIID请登录用户中心->验证码短信->产品总览->APIID）及 APIkey来调用接口；
# （3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；
"""
# !/usr/local/bin/python
# -*- coding:utf-8 -*-
import http.client
import urllib

host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

# 用户名是登录用户中心->验证码短信->产品总览->APIID
account = "C83337409"
# 密码 查看密码请登录用户中心->验证码短信->产品总览->APIKEY
password = "4f62add3dce15c1370425e069051df27"


def send_sms(text, mobile):
    params = urllib.parse.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


if __name__ == '__main__':
    mobile = "18201923078"
    text = "您的验证码是：121254。请不要把验证码泄露给其他人。"

    print(send_sms(text, mobile))
"""


# 发邮件的库
import smtplib
# 邮件文本
from email.mime.text import MIMEText


# SMTP服务器
SMTPServer = "smtp.163.com"
# 发邮件的地址
account = "18201923078@163.com"
# 发送者邮箱的密码(客户端授权密码)
password = "wxyjsw971106"

# 设置发送的内容
message = "sunck is a good man"
# 将字符串转换成邮件文本
email = MIMEText(message)
# 主题
email["Subject"] = "来自帅哥的问候"
# 发送者
email["From"] = account

# 创建SMTP服务器
mailServer = smtplib.SMTP(SMTPServer, 25)  # 25为端口号，一般邮件的端口号都是25
# 登入邮箱
mailServer.login(account, password)
# 发送邮件
mailServer.sendmail(account, ["18201923078@163.com"], email.as_string())  # 转换成一种邮件形式的字符串
# 退出邮箱
mailServer.quit()

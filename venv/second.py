# 注释
"""
12345
上山打老虎
"""
import keyword
print("tom is a good man")
print("tom is a good man ", " tom is a nice man", "tom is a handsome man")
age = input("请输入你的年龄")  # 等号前后也要空格
print("age=", age)  # 逗号后要空格
print(keyword.kwlist)
name = "小明"
print("name= ", name)
num1 = input("请输入一个数字")
num2 = input("请再输入一个数字")  # python中input输入的都为字符串类
print("num1 + num2 =", num1+num2)
num3 = int(input("请输入一个数字"))
num4 = int(input("请再输入一个数字"))
print("num3 + num4 =", num3+num4)
del age  # 删除后无法引用
print(type(num1), type(num3))
print(id(num4))  # 查询变量内存地址

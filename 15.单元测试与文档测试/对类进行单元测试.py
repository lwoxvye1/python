import unittest


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getAge(self):
        return self.age + 1


per = Person("tom", 20)
print(per.getAge())


class Test(unittest.TestCase):
    def test_init(self):  # 必须加test_ 不然不会进行测试
        p = Person("hanmeimei", 20)
        self.assertEqual(p.name, "hanmeimei", "属性赋值有误")

    def test_getAge(self):
        p = Person("hanmeimei", 22)
        self.assertEqual(p.getAge(), p.age, "getAge函数有误")


if __name__ == '__main__':
    unittest.main()
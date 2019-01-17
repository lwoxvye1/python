from functools import reduce
import telnetlib

# py2与py3的区别   见python-16-2
"""
性能:    py3.x起始比py2.x效率低，但是py3.x有极大的优化控件，效率正在追赶

编码：   py3.x原码文件默认使用UTF-8编码，使得变量名更为广阔

语法：  去除了<>,改用 !=
        加入as和with关键字，还有True,False,None
        整型触发返回浮点数，整除请使用//
        加入nonlocal语句
        去除print语句，加入print()函数
        去除了raw_input,加入input()函数
        新的super()，可以不再给super()传参数
        改变了顺序操作符的行为，例如x<y,当x和yl类型不匹配时输出TypeError而不是返回随即的bool值
        新式的8进制变量

数据类型：Py3.X去除了long类型，现在只有一种整型--int，但它的行为就像2.X版本的long
          新增了bytes类型，对应于2.X版本的八位串

面向对象：引入抽象基类

异常： 所有异常都从BaseException继承，并删除了StardardError
        python2     try:
                    except Exception,e:

        python3     try:
                    except Exception as e:

其他： xrange()改名为range()，要想使用range()获得一个list,必须显示调用
        file类被废弃
"""


# 高阶函数—map与reduce
# python内置了map()和reduce()函数

# map()
# 原型 map(fn, lsd)
# 参数1是函数    参数2是序列
# 功能： 将传入的函数依次作用在序列中的每一个元素，并把结果作为新的Iterator返回

# 将单个字符转成对应的字面量整数
def chr2int(chr):
    return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}[chr]


list1 = ["5", "4", "1", "8", "8"]
res = map(chr2int, list1)
# 相当于[chr2int("5"), chr2int("4"), chr2int("1"), chr2int("8"), chr2int("8")]
print(res)
print(list(res))  # 惰性列表，要将其转成列表才能显示出内容
# 将整数元素的序列转为字符串型
list2 = map(str, [1, 2, 3, 4])
print(list(list2))

# reduce(fn, lsd)
# 参数1为函数， 参数2为序列
# 功能：一个函数作用在序列上，这个函数必须接受两个参数，
# reduce把结果继续和序列的下一个元素累计运算
# reduce(f, [a, b, c, d])
# f(f(f(a, b), c), d)

# 求一个序列的和
list3 = [1, 2, 3, 4, 5]


def mySum(x, y):
    return x + y


r = reduce(mySum, list3)
print(r)

# 将字符串转成对应字面量数字


def str2int(str):
    def fc(x, y):
        return x*10 + y

    def fs(chr):
        return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}[chr]

    return reduce(fc, map(fs, list(str)))


print(str2int("13579"))


# 高阶函数—filter
# 原型：filter(fn, lsd)
# 参数1为函数， 参数2为序列
# 功能：用于过滤序列(把传入的函数依次作用于序列每个元素，
# 根据返回的是True还是False决定是否保留该元素)

list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 筛选条件
def func(num):
    # 偶数保留
    if num % 2 == 0:
        return True
    # 奇数剔除
    return False


list5 = filter(func, list4)
print(list(list5))


# 高阶函数—sorted
# 排序：冒泡，选择(低端)     快速，插入，计数器

# 普通排序
list6 = [4, 7, 6, 1, 9]
list7 = sorted(list6)  # 默认升序排序
print(list7)

# 降序
list8 = [4, 7, 6, 1, 9]
list9 = sorted(list8, reverse=True)
print(list9)

# 按绝对值大小排序
list10 = [-4, -7, 6, 1, 9]
# key接受函数来实现自定义排序规则
list11 = sorted(list10, key=abs)
print(list11)

# 自定义排序


def myLen(str):  # 函数可以自己写
    return len(str)


list12 = ["b333", "e1111", "c4", "a22222", "d55"]
list13 = sorted(list12, key=myLen)
print(list13)


# 单元测试
"""
作用：用来对一个函数、一个类或者一个模块来进行正确性校验工作

结果：
1.单元测试通过，说明我们测试的函数功能正常
2.单元测试不通过，说明函数功能有BUG，要么测试条件输入有误
"""
# 对函数进行单元测试
# 对类进行单元测试
# 文档测试


# 远程控制windows
def telnet(IP, user, passwd, command):
    # 连接服务器
    telnet = telnetlib.Telnet(IP)
    # 设置调式级别
    telnet.set_debuglevel(2)
    # 读取信息
    rt = telnet.read_until("Login username:".encode("UTF-8"))
    # 写入用户名
    telnet.write(user + "\r\n").encode("UTF-8")
    rt = telnet.read_until("Login password:".encode("UTF-8"))
    telnet.write(passwd + "\r\n").encode("UTF-8")
    rt = telnet.read_until("Domain name:".encode("UTF-8"))
    telnet.write(IP + "\r\n").encode("UTF-8")
    # 登入成功，写指令
    rt = telnet.read_until(">").encode("UTF-8")
    telnet.write(command + "\r\n").encode("UTF-8")
    # 上面命令执行成功,会继续读到>， 失败一般不会是>
    rt = telnet.read_until(">".encode("UTF-8"))
    telnet.close()
    return True


if __name__ == '__main__':
    IP = "192.168.31.8"
    user = "jsw"
    passwd = "19971106s"
    command = "tasklist"
    telnet(IP, user, passwd, command)

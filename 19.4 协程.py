
# 4.协程
"""
子程序/函数：在所有语言中都是层级调用，比如A调用B，在B执行的过程中又可以调用C，C执行完毕返回，
B执行完毕返回，最后是A执行完毕。是通过栈实现的，一个线程就是执行一个子程序，子程序调用总是一个入口
，一次返回，调用的顺序是明确的

协程概述：看上去也是子程序，但执行过程中，在子程序的内部可中断，然后转而执行别的子程序，不是
函数调用。有点类似CPU中断


def  A():
    print(1)
    print(2)
    print(3)

def  B():
    print("x")
    print("y")
    print("z")

1
x
2
3
y
z
执行出这个结果
但是A中是没有B的调用
看起来A、B执行过程有点像线程，但协程的特点在于是一个线程执行


与线程相比，协程的执行效率极高，因为只有一个线程，也不存在同时写变量的冲突，
在协程中共享资源不加锁，只需要判断状态就行了
"""

# (1)协程原理
"""
Python对协程的支持是通过generator实现的
"""


def run():
    print(1)
    yield 10
    print(2)
    yield 20
    print(3)
    yield 30


# 协程的最简单风格，控制函数的阶段执行，节约线程或者进程的切换
# 返回值是一个生成器
m = run()
print(next(m))
print(next(m))
next(m)


# (2)数据传输
def run2():
    # 空变量，存储的作用，data始终为空
    data = ""
    r = yield data
    print(1, r, data)
    r = yield data
    print(2, r, data)
    r = yield data
    print(3, r, data)
    r = yield data


m = run2()
# 启动m
print(m.send(None))
print(m.send("a"))
print(m.send("b"))
print(m.send("c"))
print("***********")

# (3)生产者与消费者


def producer(c):
    c.send(None)
    for i in range(5):
        print("生产者产生数据%d" % i)
        r = c.send(str(i))
        print("消费者消费了数据%s" % r)
    c.close()


def customer():
    data = ""
    while True:
        n = yield data
        if not n:
            return
        print("消费者消费了%s" % n)
        data = n


c = customer()
producer(c)

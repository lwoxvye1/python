import time
from multiprocessing import Process
from multiprocessing import Pool
import os
import random
from multiprocessing import Queue
# 1.多任务原理
"""
现代操作系统(Windows、Mac  OS X、Linux、UNIX等)都支持“多任务”

什么叫多任务?
操作系统同时可以运行多个任务

单核CPU实现多任务原理：操作系统轮流让各个任务交替执行，QQ执行2us,切换到微信，再执行2us,
再切换到陌陌，执行2us……。表面上看，每个任务反复执行下去，但是CPU调度执行速度太快了，
导致我们感觉就像所有任务都在同时执行一样。


多核CPU实现多任务原理：真正的并行执行多任务只能在多核CPU上实现，但是由于任务数量远远多于
CPU的核心数量，所以，操作系统也会自动把很多任务轮流调度到每个核心上执行
并发：看上去一起执行，任务数多于CPU核心数
并行：真正一起执行，任务数小于等于CPU核心数


实现多任务的方式：
1、多进程模式
2、多线程模式
3、协程模式
4、多进程+多线程模式
"""


# 2.进程
"""
对于操作系统而言，一个任务就是一个进程

进程是系统中程序执行和资源分配的基本单位。每个进程都有自己的数据段、代码段和堆栈段
"""
# (1)单任务现象
"""
def run():
    while True:
        print("Tom is a nice man")
        time.sleep(1.2)


if __name__ == "__main__":
    while True:
        print("Tom is a good man")
        time.sleep(1)    
    run()
    # 不会执行到run()方法，只有上面的while循环结束才可以执行
"""
# (2)启动进程实现多任务
"""
multiprocessing库
跨平台版本的多进程模块，提供了一个Process类来代表一个进程对象
"""

"""
def run1(str1):
    while True:
        # os.getpid()获取当前进程id号  可以在任务管理器中查看
        # os.getppid()获取当前进程的父进程id号
        print("Tom is a %s man--%s--%s" % (str1, os.getpid(), os.getppid()))
        time.sleep(1.2)


if __name__ == "__main__":
    print("主(父)进程启动--%s" % os.getpid())
    # 创建子进程
    # target说明进程执行的任务
    p = Process(target=run1, args=("nice",))
    # 启动进程
    p.start()
    while True:
        print("Tom is a good man")
        time.sleep(1)
"""
# (3)父子进程的先后顺序


def run2():
    print("子进程启动")
    time.sleep(3)
    print("子进程结束")


if __name__ == "__main__":
    print("父进程启动")
    p2 = Process(target=run2)
    p2.start()
    # 父进程的结束不影响子进程，让父进程等待子进程结束再执行父进程
    p2.join()
    print("父进程结束")

# (4)全局变量在多个进程中不能共享
num = 100


def run3():
    print("子进程开始")
    global num  # global表示全局变量
    num += 1
    print(num)
    print("子进程结束")


if __name__ == "__main__":
    print("父进程开始")
    p3 = Process(target=run3)
    p3.start()
    p3.join()
    print("父进程结束--%d" % num)
    # 在子进程中修改全局变量对父进程中的全局变量没有影响
    # 在创建子进程时对全局变量做了一个备份，父进程中的与子进程中的num是完全不同的两个变量

# (5)启动大量子进程


def run4(name):
    print("子进程%d启动--%s" % (name, os.getpid()))
    start = time.time()
    time.sleep(random.choice([1, 2, 3]))
    end = time.time()
    print("子进程%d结束--%s--耗时%.2f" % (name, os.getpid(), end-start))


if __name__ == "__main__":
    print("----------------")
    print("父进程启动")
    # 创建多个进程
    # Pool--进程池
    # 参数1：表示可以同时执行的进程数量，Pool默认大小是CPU核心数
    pp = Pool(4)
    for i in range(5):
        # 创建进程，放入进程池统一管理
        pp.apply_async(run4, args=(i,))
    # 在调用join之前必须先调用close,调用close之后就不能再继续添加新的进程了
    pp.close()
    # 进程池对象调用join，会等待进程池中所有的子进程结束完毕再去执行父进程
    pp.join()
    print("父进程结束")


# (6)拷贝文件

def copy_file(rpath, wpath):
    fr = open(rpath, "rb")
    fw = open(wpath, "wb")
    context = fr.read()
    fw.write(context)
    fr.close()
    fw.close()


path = r"D:\学习\python\project\15.单元测试与文档测试"
to_path = r"D:\学习\python\project\to_file"
"""
filesList = os.listdir(path)
start = time.time()
for fileName in filesList:
    copy_file(os.path.join(path, fileName), os.path.join(to_path, fileName))
end = time.time()
print("总耗时：%2f" % (end-start))
"""
# (7)多进程实现文件拷贝
if __name__ == "__main__":
    filesList = os.listdir(path)
    start = time.time()
    pp1 = Pool()
    for fileName in filesList:
        pp1.apply_async(copy_file, args=(os.path.join(path, fileName), (os.path.join(to_path, fileName))))
    pp1.close()
    pp1.join()
    end = time.time()
    print("总耗时:%0.2f" % (end-start))
    # 因为创建进程也会耗时，而要拷贝的文件太小，所以这里的多进程耗时比单进程多

# (8)封装进程对象
# 对Process进行二次封装


class SunckProcess(Process):
    def __init__(self, name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print("子进程(%s-%s)启动" % (self.name, os.getpid()))
        time.sleep(3)
        print("子进程(%s-%s)结束" % (self.name, os.getpid()))


if __name__ == "__main__":
    print("父进程启动")
    p = SunckProcess("test")
    p.start()
    p.join()
    print("父进程结束")

# (9)进程间通信-Queue


def write(q):
    print("启动write子进程%s" % os.getpid())
    for chr in ["A", "B", "C", "D"]:
        q.put(chr)
        time.sleep(1)
    print("结束write子进程%s" % os.getpid())


def read(q):
    print("启动read子进程%s" % os.getpid())
    while True:
        value = q.get(True)
        print("value = " + value)


if __name__ == "__main__":
    # 父进程创建队列，并传递给子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()  # pr进程里是个死循环，无法等待其结束，只能强行结束
    print("父进程结束")

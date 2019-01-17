import threading
from time import sleep
import queue
import random
# 3.线程
"""
在一个进程的内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”叫做线程

线程通常叫做轻型的进程。线程是共享内存空间的并发执行的多任务，每一个线程都共享一个进程的资源

线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统决定，程序自己
不能决定什么时候执行，执行多长时间

模块
1. _thread模块        低级模块(比较接近底层，python底层是对C语言的封装)
2. threading模块      高级模块(对_thread进行了封装)

"""
# (1)启动一个线程


def run(num1):
    print("子线程(%s)启动" % threading.current_thread().name)
    sleep(2)
    print(num1)
    print("子线程(%s)结束" % threading.current_thread().name)


if __name__ == "__main__":
    # 任何进程默认就会启动一个线程，称为主线程，主线程可以启动新的子线程
    # current_thread():返回当前线程的实例
    print("主线程(%s)启动" % threading.current_thread().name)

    # 创建子线程                          线程的名称
    t = threading.Thread(target=run, name="runThread", args=(1,))
    t.start()
    # 等待线程结束
    t.join()
    print("主线程(%s)结束" % threading.current_thread().name)

# (2)线程间共享数据
"""
多线程和多进程最大的不同在于，多进程中，同一个变量各自有一份拷贝存在每个进程中，互不影响。
而多线程中，所有变量都由所有线程共享。所以，任何一个变量都可以被任意一个线程修改，因此，线程
之间共享数据最大的危险在于多个线程同时修改一个变量，容易把内容改乱了。
"""
num = 100


def run1(n):
    global num
    for i in range(1000000):
        num += n
        num -= n


if __name__ == "__main__":
    t1 = threading.Thread(target=run1, args=(6,))
    t2 = threading.Thread(target=run1, args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("num = " + str(num))
    # 之所以造成数据混乱的原因是:  如果线程1线程2同时执行
    # num +=6   num +=9
    # 那赋予num的值会是9或者6，而不是15

# (3)线程锁解决数据混乱
"""
两个线程同时工作，一个存钱，一个取钱。可能导致数据异常

思路：加锁
"""
# 锁对象
lock = threading.Lock()
num = 100


def run2(n):
    global num
    for i in range(1000000):
        # 锁

        # 确保了这段代码只能由一个线程从头到尾的完整执行
        
        # 阻止了多线程的并发执行，包含锁的某段代码实际上只能以单线程模式执行，所以效率大大地降低了
        
        # 由于可以存在多个锁，不同线程持有不同的锁，并试图获取其他的锁，可能造成死锁，导致多个线程挂起。
        # 只能靠操作系统强制终止
        """
        lock.acquire()
        try:
            num += n
            num -= n
        finally:
            # 修改完一定要释放锁,不然会造成堵塞
            lock.release()
        """
        # 与上面代码功能相同，with lock可以自动上锁与解锁
        with lock:
            num += n
            num -= n


if __name__ == "__main__":
    t3 = threading.Thread(target=run2, args=(6,))
    t4 = threading.Thread(target=run2, args=(9,))
    t3.start()
    t4.start()
    t3.join()
    t4.join()
    print("num = " + str(num))

# (4)ThreadLocal
num = 100
# 创建一个全局的ThreadLocal对象，使每个线程有独立的存储空间
# 每个线程对ThreadLocal对象都可以读写，但是互不影响
local = threading.local()


def run3(x, n):
    x = x + n
    x = x - n


def func(n):
    # 每个线程都有local.x,就是相当于线程的局部变量
    local.x = num
    for i in range(1000000):
        run3(local.x, n)
    print("%s---%d" % (threading.current_thread().name, local.x))


if __name__ == "__main__":
    t5 = threading.Thread(target=func, args=(6,))
    t6 = threading.Thread(target=func, args=(9,))
    t5.start()
    t6.start()
    t5.join()
    t6.join()
    print("num = " + str(num))
# 作用：为每个线程绑定一个数据库连接、HTTP请求、用户身份信息等，这样一个线程的所有调用到的处理
# 函数都可以非常方便地访问这些资源

# (5)QQ
# (6)信号量控制线程数量
"""
sem = threading.Semaphore(2)  # 控制并发执行的线程数量


def run4():
    with sem:
        for i in range(5):
            print("%s---%d" % (threading.current_thread().name, i))
            sleep(1)


if __name__ == '__main__':
    for i in range(3):
        threading.Thread(target=run4).start()
"""
# (7)凑够一定数量才能一起执行
"""
print("-------------------------------")
bar = threading.Barrier(4)


def run5():
    print("%s---start" % threading.current_thread().name)
    sleep(1)
    bar.wait()
    print("%s---end" % threading.current_thread().name)


if __name__ == '__main__':
    for i in range(5):
        threading.Thread(target=run5).start()
"""

# (8)定时线程


def run6():
    print("sunck is a good man")


if __name__ == '__main__':
    t = threading.Timer(3, run6)  # 延时执行线程
    t.start()
    t.join()
    print("父线程结束")

# (9)线程通信


def func():
    # 事件对象
    event = threading.Event()

    def run7():
        for i in range(5):
            # 阻塞，等待事件的触发
            event.wait()
            # 重置阻塞，如果不重置第二次就不会阻塞了
            event.clear()
            print("sunck is a good man!!%d" % i)
    threading.Thread(target=run7).start()
    return event


if __name__ == '__main__':
    e = func()
    # 触发事件
    for i in range(5):
        e.set()
        sleep(2)
    # 可以在暂停下载时用到

# (10)生产者与消费者
# 生产者
"""

def producer(id, q):
    while True:
        num1 = random.randint(0, 1000)
        q.put(num1)
        print("生产者%d生产了%d数据放入了队列" % (id, num1))
        sleep(3)
    # 任务完成
    q.task_done()  # 表示生产结束，哪天结束再说

# 消费者
def customer(id, q):
    while True:
        item = q.get()
        if item is None:
            break
        print("消费者%d消费了%d数据" % (id, item))
        sleep(2)
    # 任务完成
    q.task_done()


if __name__ == '__main__':
    # 消息队列
    q = queue.Queue()
    # 启动生产者
    for i in range(4):
        threading.Thread(target=producer, args=(i, q)).start()
    # 启动消费者
    for i in range(3):
        threading.Thread(target=customer, args=(i, q)).start()
"""

# (11)线程调度

# 线程条件变量
cond = threading.Condition()


def run8():
    with cond:
        for i in range(0, 10, 2):
            print(threading.current_thread().name, i)
            sleep(1)
            cond.wait()
            cond.notify()


def run9():
    with cond:
        for i in range(1, 10, 2):
            print(threading.current_thread().name, i)
            sleep(1)
            cond.notify()
            cond.wait()


if __name__ == '__main__':
    threading.Thread(target=run8).start()
    threading.Thread(target=run9).start()
    # 线程的执行是毫无规律的

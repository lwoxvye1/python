import pickle   # 数据持久型模块
import os
import win32con
import time
import random
import win32com.client      # 系统客户端
import win32gui
import win32process     # 进程模块
import win32api
import ctypes
# 文件读写
path = r"D:\学习\python\project\file2.txt"
f = open(path, "w", encoding="utf-8")
# 写文件
# 1.将信息写入缓冲区
f.write("Tom is a good man")
# 2.刷新缓冲区     直接把内部缓冲区的数据立刻写入文件，而不是被动的等待(close或者缓冲区满了)
# 自动刷新缓冲区写入
f.flush()
f.close()
with open(path, "a", encoding="utf-8") as f2:
    f2.write("\nhandsome man")

# 编码与解码
# 编码
path = r"D:\学习\python\project\file3.txt"
with open(path, "wb") as f3:
    str1 = "Tom is a good man"
    f3.write(str1.encode("utf-8"))
with open(path, "rb") as f4:
    data = f4.read()
    print(data)
    print(type(data))
    newData = data.decode("utf-8")  # 编码和解码必须一致
    print(newData)
    print(type(newData))

# list/tuple/dict/set的文件操作
myList = [1, 2, 3, 4, 5, "Tom is a good man"]
with open(path, "wb") as f5:
    pickle.dump(myList, f5)
with open(path, "rb") as f6:
    tempList = pickle.load(f6)
    print(tempList)


# os模块
"""
os:包含了普遍的操作系统的功能
"""
print(os.name)  # 获取操作系统类型  nt -> windows    posix ->Linux、Unix或Mac OS X
print(os.environ)  # 获取操作系统中的所有环境变量
print(os.environ.get("APPDATA"))  # 获取指定环境变量
print(os.curdir)    # 获取当前目录
print(os.getcwd())  # 获取当前工作目录，即当前python脚本所在的目录
print(os.listdir("D:\学习\python\project"))  # 以列表的形式返回指定目录下的所有文件
os.mkdir("Tom")   # 在当前目录下创建新目录
# os.rmdir("Tom")  # 删除目录
print(os.stat("file1.txt"))  # 获取文件属性
os.rename("Tom", "John")  # 重命名
os.rmdir("John")
# os.remove("file1.txt")  # 删除普通文件
# 运行shell命令
# os.system("notepad")  # 记事本
# os.system("write")  # 写字板
# os.system("mspaint")  # 画板
# os.system("shutdown -s -t 500")  # 关机
# os.system("shutdown -a")  # 取消关机

# 有些方法存在os模块里，还有些存在于os.path
print(os.path.abspath("./file1.txt"))  # 查看当前的绝对路径
p1 = "D:\学习\python\project"
p2 = r"Tom\abc"  # 注意：参数2里开头不要有斜杠
print(os.path.join(p1, p2))  # 拼接路径
p3 = r"D:\学习\python\project\Tom\abc.txt"
print(os.path.split(p3))    # 拆分路径
print(os.path.splitext(p3))  # 获取扩展名
print(os.path.dirname(p3))  # 获取文件的目录
print(os.path.basename(p3))  # 获取文件名
print(os.path.isdir(p3))  # 判断是否是目录
print(os.path.isfile(p3))  # 判断文件是否存在
p4 = "D:\学习\python\project"
print(os.path.exists(p4))  # 判断目录是否存在
print(os.path.getsize(path))  # 获得文件大小(字节)


# 窗口控制
# 控制窗体的显示和隐藏
# 找出窗口的编号
QQWin = win32gui.FindWindow("TXGuiFoundation", "QQ")     # 需打开QQ登陆界面并用spy
# 隐藏窗体
win32gui.ShowWindow(QQWin, win32con.SW_HIDE)    # 程序必须运行才能实现
time.sleep(2)
# 显示窗体
win32gui.ShowWindow(QQWin, win32con.SW_SHOW)
"""
一启动QQ就会执行
while True:
    QQWin = win32gui.FindWindow("TXGuiFoundation", "QQ")
    win32gui.ShowWindow(QQWin, win32con.SW_HIDE)
    time.sleep(1)
    win32gui.ShowWindow(QQWin, win32con.SW_SHOW)
    time.sleep(1)
"""
# 控制窗体的位置和大小
QQWin = win32gui.FindWindow("TXGuiFoundation", "QQ")  # 参数1：控制的窗体
# 参数2：大致方位，HWND_TOPMOST上方 ，参数3：位置x ，参数4：位置y ，参数5：长度 ，参数6：宽度
# win32gui.SetWindowPos(QQWin, win32con.HWND_TOPMOST, 100, 100, 600, 300, win32con.SWP_SHOWWINDOW)
"""随机位置
while True:
    x = random.randrange(900)
    y = random.randrange(600)
    win32gui.SetWindowPos(QQWin, win32con.HWND_TOPMOST, x, y, 600, 300, win32con.SWP_SHOWWINDOW)
"""


# 语音合成  (控制面板-轻松使用-语音识别-文本到语音转换)
dehua = win32com.client.Dispatch("SAPI.SPVOICE")
dehua.Speak("Tom is a good man")

"""详情见python-8-07  
# 内存修改
PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)  # 最高权限
# 找窗体
win = win32gui.FindWindow("MainWindow", "植物大战僵尸中文版")
# 根据窗体找到进程号  (任务管理器也可以找到)
hid, pid = win32process.GetWindowThreadProcessId(win)
# 以最高权限打开进程
p = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, pid)

data = ctypes.c_long()  # 长整型
# 加载内存模块
md = ctypes.windll.LoadLibrary(r"C:\Windows\System32\kernel32")  # 32位内核
# 读取内存
md.ReadProcessMemory(int(p), 311944712, ctypes.byref(data), 4, None)
print("data = ", data)
# 新值
newData = ctypes.c_long(10000)
# 修改
md.WriteProcessMemory(int(p), 311944712, ctypes.byref(newData), 4, None)
"""
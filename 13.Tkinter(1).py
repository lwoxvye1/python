import tkinter

win = tkinter.Tk()
win.title("Tom")
win.geometry("400x800+200+20")
# 7.Checkbutton多选框控件


def updata():
    message = ""
    if hobby1.get():
        message += "money\n"
    if hobby2.get():
        message += "power\n"
    if hobby3.get():
        message += "people\n"
    # 清除text中的所有内容
    text.delete(0.0, tkinter.END)
    text.insert(tkinter.INSERT, message)


# 绑定变量
hobby1 = tkinter.BooleanVar()
check1 = tkinter.Checkbutton(win, text="money", variable=hobby1, command=updata)
hobby2 = tkinter.BooleanVar()
check2 = tkinter.Checkbutton(win, text="power", variable=hobby2, command=updata)
hobby3 = tkinter.BooleanVar()
check3 = tkinter.Checkbutton(win, text="people", variable=hobby3, command=updata)
check1.pack()
check2.pack()
check3.pack()

text = tkinter.Text(win, width=50, height=5)
text.pack()

# 8.Radiobutton控件


def updata2():
    print(r.get())


r = tkinter.IntVar()
radio1 = tkinter.Radiobutton(win, text="one", value=1, variable=r, command=updata2())
radio1.pack()
radio2 = tkinter.Radiobutton(win, text="two", value=2, variable=r, command=updata2())
radio2.pack()

# 9.Listbox控件
"""
列表框控件：可以包含一个或者多个文本框
作用：在listbox控件的小窗口显示一个字符串
"""
# 创建一个listbox，添加几个元素
lb = tkinter.Listbox(win, selectmode=tkinter.BROWSE, height=4)
lb.pack()
for item in ["good", "nice", "handsome", "vg", "vn"]:
    # 按顺序添加
    lb.insert(tkinter.END, item)  # lb.insert(tkinter.END, ["good", "nice"])将列表当成一个元素添加的
# 在开始添加
lb.insert(tkinter.ACTIVE, "cool")
# 删除    参数1为开始的索引， 参数2为结束的索引，如果不指定参数2，只删除第一个索引处的内容
# lb.delete(1, 3)
# lb.delete(1)
# 选中
lb.select_set(2, 4)
# 取消
lb.select_clear(3)
# 获取到列表中的元素的个数
print(lb.size())
# 从列表中取值
print(lb.get(2, 4))
# 返回当前的索引项，不是item元素
print(lb.curselection())
# 判断    一个选项是否被选中
print(lb.select_includes(1))


# 绑定变量
lbv = tkinter.StringVar()
# 与BORWSE相似，但是不支持鼠标按下后移动选中位置
lb2 = tkinter.Listbox(win, selectmode=tkinter.SINGLE, listvariable=lbv, height=4)
lb2.pack()
for item in ["good", "nice", "handsome", "vg", "vn"]:
    lb2.insert(tkinter.END, item)
# 打印当前列表中的选项
print(lbv.get())
# 设置选项
lbv.set(("1", "2", "3"))
# 绑定事件


def myPrint(event):
    print(lb2.get(lb2.curselection()))


lb2.bind("<Double-Button-1>", myPrint)  # 鼠标左键双击两下按钮

# EXTENDED 可以使listbox支持shift和control
lb3 = tkinter.Listbox(win, selectmode=tkinter.EXTENDED, height=4)
for item in ["good", "nice", "handsome", "vg", "vn", "good2", "nice2", "handsome2", "vg2", "vn2",
             "good3", "nice3", "handsome3", "vg3", "vn3", "good4", "nice4", "handsome4", "vg4", "vn4",
             "good", "nice", "handsome", "vg", "vn", "good2", "nice2", "handsome2", "vg2", "vn2",
             "good3", "nice3", "handsome3", "vg3", "vn3", "good4", "nice4", "handsome4", "vg4", "vn4"]:
    lb3.insert(tkinter.END, item)

# 滚动条
sc = tkinter.Scrollbar(win)
sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)
lb3.configure(yscrollcommand=sc.set)
lb3.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
# 额外给属性赋值
sc["command"] = lb3.yview

# MULTIPLE 支持多选
lb4 = tkinter.Listbox(win, selectmode=tkinter.MULTIPLE, listvariable=lbv)
lb4.pack()
for item in ["good", "nice", "handsome", "vg", "vn"]:
    lb4.insert(tkinter.END, item)
win.mainloop()

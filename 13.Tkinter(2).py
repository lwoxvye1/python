import tkinter
from tkinter import ttk
win = tkinter.Tk()
win.title("Tom")
win.geometry("400x400+200+0")
# 10.Scale控件
"""
供用户通过拖拽指示器改变变量的值，可以水平也可以竖直,tkinter.HORIZONTAL  水平
                                                     tkinter.VERTICAL 竖直
                                                     length 水平时表示宽度，竖直时表示高度
                                                     tickinterval 间距
"""
scale1 = tkinter.Scale(win, from_=0, to=100, orient=tkinter.HORIZONTAL, tickinterval=10, length=200)
scale1.pack()
# 设置值
scale1.set(20)
# 取值


def showNum():
    print(scale1.get())


tkinter.Button(win, text="按钮", command=showNum).pack()
# 11.Spinbox数值范围控件


def updata():
    print(v.get())


# 绑定变量
v = tkinter.StringVar()
# increment:步长 默认为1     values做好不要与from to同时使用   values=(0, 2, 4, 6, 8)
sp = tkinter.Spinbox(win, from_=0, to=100, increment=5, textvariable=v, command=updata)
sp.pack()
# 赋值取值
v.set(20)
print(v.get())

# 12.Menu顶层菜单
# 菜单条
menubar = tkinter.Menu(win)
win.config(menu=menubar)


def func():
    print("Tom is a good man")


# 创建一个菜单选项
menu1 = tkinter.Menu(menubar, tearoff=False)
# 给菜单选项添加内容
for item in ["Python", "C", "C++", "OC", "Swift", "C#", "shell", "Java", "JS", "PHP", "汇编", "NodeJS", "退出"]:
    if item == "退出":
        # 添加分割线
        menu1.add_separator()
        menu1.add_command(label=item, command=lambda: win.quit())
    else:
        menu1.add_command(label=item, command=func)
# 向菜单条上添加菜单菜单选项
menubar.add_cascade(label="语言", menu=menu1)

menu2 = tkinter.Menu(menubar, tearoff=False)
menu2.add_command(label="red")
menu2.add_command(label="blue")
menubar.add_cascade(label="颜色", menu=menu2)

# 13.Menu鼠标右键菜单
# 菜单条
menubar2 = tkinter.Menu(win)
# 菜单
menu3 = tkinter.Menu(menubar2, tearoff=False)
for item in ["Python", "C", "C++", "OC", "Swift", "C#", "shell", "Java", "JS", "PHP", "汇编", "NodeJS", "退出"]:
    menu3.add_command(label=item)
menubar2.add_cascade(label="语言", menu=menu3)


def showMenu(event):
    menubar2.post(event.x_root, event.y_root)


win.bind("<Button-3>", showMenu)

# 14.Combobox下拉控件
cv = tkinter.StringVar()
com = ttk.Combobox(win, textvariable=cv)
com.pack()
# 设置下拉数据
com["value"] = ("黑龙江", "吉林", "辽宁")
# 设置默认值
com.current(0)
# 绑定事件


def func2(event):
    print(com.get())  # 都可以
    print(cv.get())


com.bind("<<ComboboxSelected>>", func2)

# 15.Frame控件
# 框架控件：在屏幕上显示一个矩形区域，多作为容器控件
frm = tkinter.Frame(win)
frm.pack()
# left
frm_l = tkinter.Frame(frm)
tkinter.Label(frm_l, text="左上", bg="pink").pack(side=tkinter.TOP)
tkinter.Label(frm_l, text="左下", bg="blue").pack(side=tkinter.TOP)
frm_l.pack(side=tkinter.LEFT)
# right
frm_r = tkinter.Frame(frm)
tkinter.Label(frm_r, text="右上", bg="red").pack(side=tkinter.TOP)
tkinter.Label(frm_r, text="右下", bg="yellow").pack(side=tkinter.TOP)
frm_r.pack(side=tkinter.RIGHT)

win.mainloop()

import tkinter
from tkinter import ttk

# 16.表格数据
win = tkinter.Tk()
win.title("Tom")
win.geometry("600x800+200+0")

tree = ttk.Treeview(win)
tree.pack()
# 定义列
tree["columns"] = ("姓名", "年龄", "身高", "体重")
# 设置列,列还不显示
tree.column("姓名", width=100)
tree.column("年龄", width=100)
tree.column("身高", width=100)
tree.column("体重", width=100)
# 设置表头
tree.heading("姓名", text="姓名(name)")
tree.heading("年龄", text="年龄(age)")
tree.heading("身高", text="身高(height)")
tree.heading("体重", text="体重(weight)")
# 添加数据
tree.insert("", 0, text="line1", values=("A", "20", "170", "55"))
tree.insert("", 1, text="line2", values=("B", "21", "185", "105"))
tree.insert("", 2, text="line3", values=("C", "25", "165", "45"))
tree.insert("", 3, text="line4", values=("D", "35", "190", "130"))

# 17.树状数据
tree2 = ttk.Treeview(win)
tree2.pack()
# 添加一级树枝
treeF1 = tree2.insert("", 0, "中国", text="中国", values="F1")  # values是元组
treeF2 = tree2.insert("", 1, "美国", text="美国", values="F2")
treeF3 = tree2.insert("", 2, "英国", text="英国", values="F3")
# 二级树枝
treeF1_1 = tree2.insert(treeF1, 0, "黑龙江", text="中国黑龙江", values="F1_1")
treeF1_2 = tree2.insert(treeF1, 1, "吉林", text="中国吉林", values="F1_2")
treeF1_3 = tree2.insert(treeF1, 2, "辽宁", text="中国辽宁", values="F1_3")
treeF2_1 = tree2.insert(treeF2, 0, "德克萨斯州", text="美国德克萨斯州", values="F2_1")
treeF2_2 = tree2.insert(treeF2, 1, "加利福尼亚州", text="美国加利福尼亚州", values="F2_2")
treeF2_3 = tree2.insert(treeF2, 2, "阿拉斯加", text="美国阿拉斯加", values="F2_3")
# 三级树枝
treeF1_1_1 = tree2.insert(treeF1_1, 0, "哈尔滨", text="黑龙江哈尔滨", values="F1_1_1")
treeF1_1_2 = tree2.insert(treeF1_1, 1, "五常", text="黑龙江五常", values="F1_1_2")

# 18.绝对布局
label1 = tkinter.Label(win, text="good", bg="blue")
label2 = tkinter.Label(win, text="nice", bg="red")
label3 = tkinter.Label(win, text="cool", bg="pink")

# 绝对布局,窗口的变化对位置没有影响
label1.place(x=10, y=10)
label2.place(x=50, y=50)
label3.place(x=100, y=100)

"""
# 19.相对布局   窗体的改变对控件有影响
label1.pack(fill=tkinter.Y, side=tkinter.LEFT)
label2.pack(fill=tkinter.X, side=tkinter.TOP)
label3.pack()
"""
"""
# 20.表格布局  (表格和pack不能一起用)
label4 = tkinter.Label(win, text="handsome", bg="yellow")
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
label4.grid(row=1, column=1)
"""
# 21.鼠标点击事件


def func(event):
    print(event.x, event.y)


button1 = tkinter.Button(win, text="leftmouse button")
button1.bind("<Button-1>", func)
button1.pack()
label = tkinter.Label(win, text="leftmouse button")  # 任何的小控件都能触发事件
label1.bind("<Button-1>", func)  # <Button-1>鼠标左键  <Button-2>鼠标中键  <Button-3>鼠标右键
# <Double-Button-1>鼠标左键双击 <Double-Button-2>鼠标中键双击 <Double-Button-3>鼠标右键双击
# <Triple-Button-1>鼠标左键三击 <Triple-Button-2>鼠标中键三击 <Triple-Button-3>鼠标右键三击
# bind 给控件绑定事件
label1.pack()

# 22.鼠标移动事件
label4 = tkinter.Label(win, text="Tom is a good man")
label4.pack()
# <B1-Motion>当鼠标左键被按住在小控件且移动鼠标时事件发生,B1表示左键移动，<B2-Motion>，<B3-Motion>
label4.bind("<B1-Motion>", func)

# 23.鼠标释放事件
label5 = tkinter.Label(win, text="Tom is a good man", bg="red")
label5.pack()
label5.bind("<ButtonRelease-1>", func)
# <ButtonRelease-1> 释放鼠标左键  <ButtonRelease-2>  <ButtonRelease-3>

# 24.进入、离开事件
label6 = tkinter.Label(win, text="Tom is a good man", bg="brown")
label6.pack()
label6.bind("<Enter>", func)
# <Enter>鼠标光标进入控件时触发
# <Leave>鼠标光标离开控件时触发

# 25.响应所有按键事件
label7 = tkinter.Label(win, text="Tom is a good man", bg="pink")
# 设置焦点  所有按键事件都是发生在焦点上的，没有焦点就不会触发按键事件
# 把小控件label改为窗体win也能执行
label7.focus_set()
label7.pack()


def func2(event):
    print("event.char = ", event.char)
    print("event.keycode = ", event.keycode)


label7.bind("<Key>", func2)
# <Key>响应所有的按键

# 26.响应特殊按键事件
label8 = tkinter.Label(win, text="Tom is a good man", bg="yellow")
label8.focus_set()
label8.pack()
label8.bind("<Shift_L>", func2)
# <Shift_L>左shift    <Shift_R>右shift    <F5>     <Return>回车   <BackSpace>退格

# 27.指定按键事件
label9 = tkinter.Label(win, text="Tom is a good man", bg="purple")
label9.focus_set()
label9.pack()
label9.bind("a", func2)

# 28.组合按键事件
label10 = tkinter.Label(win, text="Tom is a good man", bg="black")
label10.focus_set()
label10.pack()
label10.bind("<Control-Alt-a>", func2)

win.mainloop()

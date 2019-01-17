import tkinter
from tkinter import ttk
import os


class TreeWindows(tkinter.Frame):
    def __init__(self, master, path, otherWin):
        super(TreeWindows, self).__init__()
        self.otherWin = otherWin

        frame = tkinter.Frame(master)
        frame.pack()
        self.tree = ttk.Treeview(frame)
        self.tree.pack(side=tkinter.LEFT, fill=tkinter.Y)
        root = self.tree.insert("", "end", text=os.path.splitext(path), open=True, values=path)
        self.list = self.loadTree(root, path, [])

        # 滚动条
        self.sy = tkinter.Scrollbar(frame)
        self.sy.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.sy.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=self.sy.set)

        # 绑定事件
        self.tree.bind("<<TreeviewSelect>>", self.func)

    def func(self, event):
        self.v = event.widget.selection()  # widget 找到触发事件的小构件
        for sv in self.v:
            file = self.tree.item(sv)["text"]
            self.otherWin.ev.set(file)
            num = int(self.tree.item(sv)["values"][0])
            path = self.list[num - 1]
            if not os.path.isdir(path):
                self.otherWin.txt.delete(1.0, tkinter.END)
                f = open(path, "r", encoding="UTF-8")
                str1 = f.read()
                self.otherWin.txt.insert(tkinter.INSERT, str1)
                f.close()

    def loadTree(self, parent, parentpath, absList):
        for fileName in os.listdir(parentpath):
            absPath = os.path.join(parentpath, fileName)
            absList.append(absPath)
            # 插入树枝
            treey = self.tree.insert(parent, "end", text=self.getLastPath(absPath), values=len(absList))
            # 判断是否是目录
            if os.path.isdir(absPath):
                self.loadTree(treey, absPath, absList)
        return absList

    def getLastPath(self, path):
        pathList = os.path.split(path)
        return pathList[-1]


class infoWindows(tkinter.Frame):
    def __init__(self, master):
        super(infoWindows, self).__init__()
        frame = tkinter.Frame(master)
        frame.pack()
        self.ev = tkinter.Variable()
        self.entry = tkinter.Entry(frame, textvariable=self.ev)
        self.entry.pack(side=tkinter.TOP)

        self.txt = tkinter.Text(frame)
        self.txt.pack()


if __name__ == '__main__':
    win = tkinter.Tk()
    win.title("Tom")
    win.geometry("400x800+200+20")
    infoWin = infoWindows(win)
    tree = TreeWindows(win, "D:\学习\python", infoWin)
    win.mainloop()

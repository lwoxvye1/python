import time
import random
import pickle
import os
import tkinter


class Admin(object):
    admin = "1"
    password = "1"

    def printAdminView(self):
        print("*************************************************")
        print("*                                               *")
        print("*                                               *")
        print("*               欢迎登入伟哥银行                *")
        print("*                                               *")
        print("*                                               *")
        print("*************************************************")

    def printsysFunctionView(self):
        print("*************************************************")
        print("*       开户(1)                  查询(2)        *")
        print("*       取款(3)                  存款(4)        *")
        print("*       转账(5)                  改密(6)        *")
        print("*       锁定(7)                  解锁(8)        *")
        print("*       补卡(9)                  销户(0)        *")
        print("*                    退出(q)                    *")
        print("*************************************************")

    def adminOption(self):
        inputAdmin = input("请输入管理员账号:")
        if self.admin != inputAdmin:
            print("账号输入有误！！")
            return -1
        inputPassword = input("请输入管理员密码:")
        if self.password != inputPassword:
            print("密码输入有误！！")
            return -1

        print("操作成功！请稍后......")
        time.sleep(3)
        return 0


class User(object):
    def __init__(self, name, idCard, phone, card):
        self.name = name
        self.idCard = idCard
        self.phone = phone
        self.card = card


class Card(object):
    def __init__(self, cardId, cardPassword, cardMoney):
        self.cardId = cardId
        self.cardPassword = cardPassword
        self.cardMoney = cardMoney
        self.cardLock = False


class ATM(object):
    def __init__(self, allUsers):
        self.allUsers = allUsers

    # 验证密码
    def checkPassword(self, realPassword):
        for i in range(3):
            tempPassword = input("请输入密码")
            if tempPassword == realPassword:
                return True

        return False

    # 生成卡号
    def randomCardId(self):
        while True:
            str = ""
            for i in range(6):
                num = chr(random.randrange(ord("0"), ord("9") + 1))
                str += num
            if not self.allUsers.get(str):
                return str

    def createUser(self):
        # 向用户字典中添加一对键值对(卡号-用户)
        name = input("请输入您的姓名:")
        idCard = input("请输入您的身份证号码：")
        phone = input("请输入您的电话号码：")
        prestoreMoney = int(input("请输入预存款金额："))
        if prestoreMoney < 0:
            print("存款输入有误！!开户失败......")
            return -1

        onePassword = input("请设置密码：")
        # 验证密码
        if not self.checkPassword(onePassword):
            print("密码输入错误！！开户失败......")
            return -1

        cardStr = self.randomCardId()
        card = Card(cardStr, onePassword, prestoreMoney)
        user = User(name, idCard, phone, card)
        # 存到字典
        self.allUsers[cardStr] = user
        print("开户成功!!请牢记卡号(%s)......" % cardStr)

    def searchUserInfo(self):
        cardNum = input("请输入您的卡号")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！查询失败")
            return -1

        # 判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定！！请解锁后再进行其他操作......")
            return -1

        # 验证密码
        if not self.checkPassword(user.card.cardPassword):
            print("密码输入错误！！该卡已被锁定！！请解锁后再进行其他操作......")
            user.card.cardLock = True
            return -1
        print("账号：%s    余额：%d" % (user.card.cardId, user.card.cardMoney))

    def getMoney(self):
        cardNum = input("请输入您的卡号")
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！取款失败......")
            return -1

        if user.card.cardLock:
            print("该卡已被锁定！！请解锁后再使用其他功能......")
            return -1

        if not self.checkPassword(user.card.cardPassword):
            print("密码输入错误！！该卡已被锁定！！请解锁后再进行其他操作......")
            user.card.cardLock = True
            return -1

        # 取款
        money = int(input("请输入取款金额"))
        if money > user.card.cardMoney:
            print("余额不足！！取款失败......")
            return -1
        if money < 0:
            print("输入错误！！取款失败......")
            return -1
        user.card.cardMoney -= money
        print("取款成功!!余额：%d" % user.card.cardMoney)

    def saveMoney(self):
        cardNum = input("请输入您的卡号")
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！存款失败......")
            return -1

        if user.card.cardLock:
            print("该卡已被锁定！！请解锁后再使用其他功能......")
            return -1

        if not self.checkPassword(user.card.cardPassword):
            print("密码输入错误！！该卡已被锁定！！请解锁后再进行其他操作......")
            user.card.cardLock = True
            return -1

        money = int(input("请输入存款金额"))
        if money < 0:
            print("输入错误！！存款失败......")
            return -1
        user.card.cardMoney += money
        print("存款成功!!余额：%d" % user.card.cardMoney)

    def transferMoney(self):
        cardNum = input("请输入您的卡号")
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！转账失败......")
            return -1

        if user.card.cardLock:
            print("该卡已被锁定！！请解锁后再使用其他功能......")
            return -1

        if not self.checkPassword(user.card.cardPassword):
            print("密码输入错误！！该卡已被锁定！！请解锁后再进行其他操作......")
            user.card.cardLock = True
            return -1

        cardNum2 = input("请输入您要转账的卡号")
        user2 = self.allUsers.get(cardNum2)
        if not user2:
            print("该卡号不存在！！转账失败......")
            return -1
        money = int(input("请输入转账金额"))
        if money > user.card.cardMoney:
            print("余额不足！！转账失败......")
            return -1
        if money < 0:
            print("输入错误！！转账失败......")
            return -1
        num = int(input("确定要向卡号%s转账%d元吗(1确定  2退出)" % (cardNum2, money)))
        if num == 1:
            user.card.cardMoney -= money
            user2.card.cardMoney += money
            print("转账成功!!余额：%d" % user.card.cardMoney)
        else:
            return -1

    def changePassword(self):
        cardNum = input("请输入您的卡号")
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！转账失败......")
            return -1

        if user.card.cardLock:
            print("该卡已被锁定！！请解锁后再使用其他功能......")
            return -1

        if not self.checkPassword(user.card.cardPassword):
            print("密码输入错误！！该卡已被锁定！！请解锁后再进行其他操作......")
            user.card.cardLock = True
            return -1

        newPassword = input("请输入新密码")
        if not self.checkPassword(newPassword):
            print("密码输入错误！！该卡已被锁定！！请解锁后再进行其他操作......")
            user.card.cardLock = True
            return -1
        user.card.cardPassword = newPassword
        print("改密成功......")

    def lockUser(self):
        cardNum = input("请输入您的卡号")
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！锁定失败......")
            return -1

        if user.card.cardLock:
            print("该卡已被锁定！！请解锁后再使用其他功能......")
            return -1

        if not self.checkPassword(user.card.cardPassword):
            print("密码输入错误！！锁定失败......")
            return -1

        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证号码输入错误！！锁定失败......")
            return -1
        user.card.cardLock = True
        print("锁定成功......")

    def unlockUser(self):
        cardNum = input("请输入您的卡号")
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！解锁失败......")
            return -1

        if not user.card.cardLock:
            print("该卡没有锁定！！无需解锁......")
            return -1

        if not self.checkPassword(user.card.cardPassword):
            print("密码输入错误！！解锁失败......")
            return -1

        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证号码输入错误！！解锁失败......")
            return -1
        user.card.cardLock = False
        print("解锁成功......")

    def newCard(self):
        cardNum = input("请输入您的卡号")
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！补卡失败......")
            return -1

        if user.card.cardLock:
            print("该卡已被锁定！！请解锁后再使用其他功能......")
            return -1

        if not self.checkPassword(user.card.cardPassword):
            print("密码输入错误！！该卡已被锁定！！请解锁后再进行其他操作......")
            user.card.cardLock = True
            return -1

        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证号码输入错误！！补卡失败......")
            return -1
        num = int(input(("您确定补卡卡号%s吗(1确定  2退出)" % cardNum)))
        if num == 1:
            cardStr = self.randomCardId()
            user.card.cardId = cardStr
            self.allUsers[cardStr] = user
            self.allUsers.pop(cardNum)
            print("补卡成功!!您的新卡号为%s" % cardStr)
        else:
            return -1

    def delUser(self):
        cardNum = input("请输入您的卡号")
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！销户失败......")
            return -1

        if user.card.cardLock:
            print("该卡已被锁定！！请解锁后再使用其他功能......")
            return -1

        if not self.checkPassword(user.card.cardPassword):
            print("密码输入错误！！该卡已被锁定！！请解锁后再进行其他操作......")
            user.card.cardLock = True
            return -1

        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证号码输入错误！！销户失败......")
            return -1
        num = int(input(("您确定销户卡号%s吗(1确定  2退出)" % cardNum)))
        if num == 1:
            self.allUsers.pop(cardNum)
        else:
            return -1
        print("销户成功......")


def main():
    # 界面对象
    admin = Admin()
    admin.printAdminView()
    if admin.adminOption():
        return -1

    # 提款机对象
    filepath = os.path.join(os.getcwd(), "allusers.txt")
    f1 = open(filepath, "rb")
    allUsers = pickle.load(f1)
    f1.close()
    print("**************")
    print(allUsers)
    atm = ATM(allUsers)

    while True:
        admin.printsysFunctionView()
        # 等待用户的操作
        option = input("请输入您的操作：")
        if option == "1":
            atm.createUser()

        elif option == "2":
            atm.searchUserInfo()

        elif option == "3":
            atm.getMoney()

        elif option == "4":
            atm.saveMoney()

        elif option == "5":
            atm.transferMoney()

        elif option == "6":
            atm.changePassword()

        elif option == "7":
            atm.lockUser()

        elif option == "8":
            atm.unlockUser()

        elif option == "9":
            atm.newCard()

        elif option == "0":
            atm.delUser()

        elif option == "q":
            if not admin.adminOption():
                filepath = os.path.join(os.getcwd(), "allusers.txt")
                with open(filepath, "wb") as f:
                    pickle.dump(atm.allUsers, f)
                return -1

        time.sleep(2)


"""
if __name__ == "__main__":
    main()

"""
# tkinter
"""
Tkinter模块("Tk接口")是python的标准Tk Gui工包的接口。Tk和Tkinter可以在大多数的Unix平台下使用。
同样可以应用在Windows和Macintosh系统里。Tk8.0的后续版本可以实现本地窗口风格，并良好地运用在
绝大多数平台中。

python提供了多个图形开发界面的库(Tkinter, wxPython, Jython)
"""
# 简单示例
# 创建主窗口
win = tkinter.Tk()
win.title("Tom")    # 设置标题
win.geometry("400x400+200+0")      # 设置大小和位置  长x宽+距左侧200+距上面0
"""
# 1.Label控件

# Label:标签控件可以显示文本

# win: 父窗体 text:显示的文本内容  bg:背景色  fg:字体颜色 wraplength:指定text文本中多宽进行换行
# justify:设置换行后的对齐方式    anchor:位置 n e s w center ne se......
label = tkinter.Label(win, text="Tom is a good man", bg="pink", fg="red", font=("黑体", 20),
                      width=20, height=20, wraplength=10, justify="left", anchor="e")
# 挂载
label.pack()
"""
# 2.Button控件


def func():
    print("Tom is a good man")


button1 = tkinter.Button(win, text="按钮", command=func, width=10, height=10, )
button1.pack()

button2 = tkinter.Button(win, text="按钮", command=lambda: print("Tom is a nice man"))
button2.pack()

button3 = tkinter.Button(win, text="按钮", command=win.quit)
button3.pack()

# 3.Entry控件
"""
# 输入控件
# 用于显示简单的文本内容
"""
# show:密文显示
entry1 = tkinter.Entry(win, show="*")
entry1.pack()
# 绑定变量
e = tkinter.Variable()

entry2 = tkinter.Entry(win, textvariable=e)
# e就代表输入框这个对象
# 设置值
e.set("Tom is a good man")
# 取值
print(e.get())
print(entry2.get())

entry2.pack()

# 4.点击按钮输出输入框中的内容


def showInfo():
    print(entry3.get())


entry3 = tkinter.Entry(win)
entry3.pack()

button4 = tkinter.Button(win, text="按钮", command=showInfo)
button4.pack()

# 5.text控件
# 文本控件：用于显示多行文本
# height:显示的行数
text1 = tkinter.Text(win, width=30, height=4)
text1.pack()
str1 = '''Tom is a good man
Tom is a nice man
Tom is a handsome man
Tom is a great man
'''
text1.insert(tkinter.INSERT, str1)
"""
# 6.带滚动条的text   最好把上面的大小位置注释掉
# 创建滚动条
scroll = tkinter.Scrollbar()
text2 = tkinter.Text(win, width=30, height=3)
# side:放到窗体的哪一侧   fill:填充
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text2.pack(side=tkinter.LEFT, fill=tkinter.Y)
# text与scroll关联
scroll.config(command=text2.yview)  # 滚动条动控制文本动
text2.config(yscrollcommand=scroll.set)  # 文本动控制滚动条动
str1 = '''Tom is a good man
Tom is a nice man
Tom is a handsome man
Tom is a great man
...
...
...
...
...
...
'''
text2.insert(tkinter.INSERT, str1)
"""
win.mainloop()

import tkinter
import socket
import threading
win = tkinter.Tk()
win.title("客户端")
win.geometry("400x400+200+20")
ck = None


def get_info():
    while True:
        data = ck.recv(1024).decode("utf-8") + "\n"
        text.insert(tkinter.INSERT, data)


def connect_server():
    global ck
    ip_str = eip.get()
    port_str = eport.get()
    user_str = euser.get()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip_str, int(port_str)))
    client.send(user_str.encode("utf-8"))
    ck = client
    # 等待接收数据
    t = threading.Thread(target=get_info)
    t.start()


def send_mail():
    send_str = esend.get()
    friend = efriend.get()
    send_str = friend + ":" + send_str
    ck.send(send_str.encode("utf-8"))


label_user = tkinter.Label(win, text="user").grid(row=0, column=0)
euser = tkinter.Variable()
entry_user = tkinter.Entry(win, textvariable=euser).grid(row=0, column=1)
label_ip = tkinter.Label(win, text="ip").grid(row=1, column=0)
eip = tkinter.Variable()
entry_ip = tkinter.Entry(win, textvariable=eip).grid(row=1, column=1)
label_port = tkinter.Label(win, text="port").grid(row=2, column=0)
eport = tkinter.Variable()
entry_port = tkinter.Entry(win, textvariable=eport).grid(row=2, column=1)
button = tkinter.Button(win, text="连接", command=connect_server).grid(row=3, column=0)
text = tkinter.Text(win, width=30, height=5)
text.grid(row=4, column=0)

esend = tkinter.Variable()
entry_send = tkinter.Entry(win, textvariable=esend).grid(row=5, column=0)

efriend = tkinter.Variable()
entry_friend = tkinter.Entry(win, textvariable=efriend).grid(row=6, column=0)
button2 = tkinter.Button(win, text="发送", command=send_mail).grid(row=6, column=1)

win.mainloop()

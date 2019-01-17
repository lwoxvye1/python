import tkinter
import socket
import threading
win = tkinter.Tk()
win.title("QQ服务器")
win.geometry("400x400+200+20")
users = {}


def run(client_socket):
    user_name = client_socket.recv(1024).decode("utf-8")
    users[user_name] = client_socket
    print_str = "\n" + user_name + "连接"
    text.insert(tkinter.END, print_str)
    while True:
        data = client_socket.recv(1024).decode("utf-8")
        info_list = data.split(":")
        users[info_list[0]].send((user_name + "说:" + info_list[1]).encode("utf-8"))


def start():
    ip_str = eip.get()
    port_str = eport.get()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip_str, int(port_str)))
    server.listen(5)
    print_str = "服务器启动成功"
    text.insert(tkinter.INSERT, print_str)
    while True:
        client_socket, client_address = server.accept()
        t1 = threading.Thread(target=run, args=(client_socket,))
        t1.start()


def start_server():
    s = threading.Thread(target=start)
    s.start()


label_ip = tkinter.Label(win, text="ip", font=("黑体", 10)).grid(row=0, column=0)
label_port = tkinter.Label(win, text="port", font=("黑体", 10)).grid(row=1, column=0)
eip = tkinter.Variable()
eport = tkinter.Variable()
entry_ip = tkinter.Entry(win, textvariable=eip).grid(row=0, column=1)
entry_port = tkinter.Entry(win, textvariable=eport).grid(row=1, column=1)
button = tkinter.Button(win, text="启动", command=start_server, font=("黑体", 10)).grid(row=2, column=0)
text = tkinter.Text(win, width=30, height=10)
text.grid(row=3, column=1)

win.mainloop()

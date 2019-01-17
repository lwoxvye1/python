import socket
import threading
# 创建一个socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定IP端口
server.bind(('192.168.0.175', 8050))
# 监听
server.listen(5)
print("服务器启动成功……")
# 等待链接
"""
client_socket, client_address = server.accept()
# 这里现在只能实现单用户链接，等学完线程才可以实现多用户同时链接
print("%s  --------  %s 链接成功" % (str(client_socket), client_address))
while True:    
    data = client_socket.recv(1024)
    print("收到" + str(client_socket) + "的数据：" + data.decode("utf-8"))
    send_data = input("请输入返回给客户端的数据")
    client_socket.send(send_data.encode("utf-8"))
"""

# 多线程实现多用户同时链接


def run(client_socket):
    data = client_socket.recv(1024)
    print("收到数据：" + data.decode("utf-8"))
    client_socket.send("sunck is a good man".encode("utf-8"))


while True:
    client_socket, client_address = server.accept()
    print("%s  --------  %s 链接成功" % (str(client_socket), client_address))
    t1 = threading.Thread(target=run, args=(client_socket,))
    t1.start()

import socket
# 2.UDP编程
"""
TCP是建立可靠的连接，并且通信双方都可以以流的形式发送数据。
相对于TCP，UDP则是面向无连接的协议

使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发送数据包。
但是，能不能到达就不知道了。

虽然UDP传输数据不可靠，但它的优点是和TCP比，速度快，对于要求不高的数据可以使用UDP
"""
# 客户端与服务端通信
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    data = input("请输入数据")
    client.sendto(data.encode("utf-8"), ("192.168.43.202", 8084))
    info = client.recv(1024).decode("utf-8")
    print("服务器说：", info)

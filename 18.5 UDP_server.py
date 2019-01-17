import socket

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(("192.168.43.202", 8084))
while True:
    data, addr = udp_server.recvfrom(1024)
    print("客户端说：", data.decode("utf-8"))
    send_data = input("请输入返回给客户端的数据")
    udp_server.sendto(send_data.encode("utf-8"), addr)

import socket
"""
网络编程:
1.网络概述:     (1)自从互联网诞生以来，现在基本上所有的程序都是网络程序，很少有单机版的程序了
                (2)计算机网络就是把各个计算机连接到一起，让网络中的计算机可以互相通信。网络编程就是如何在程序中实现两台计算机的通信
                (3)用python进行网络编程,就是在python程序本身这个进程内，连接别的服务器进程的通信端口进行通信

2.IPv4包头结构：
    IP包首部：  详情见IPv4包头结构.png
    结构说明:    版本——IP头中前四位标识了IP的操作版本，比如版本4或版本6
                Internet头长度——头中下面4位包括头长度，以32位为单位表示
                服务类型
                总长度
                标识——每个IP报文被赋予一个唯一的16位标识，用于标识数据报的分段
                分段标志——下一个域包括3个1位标志，标识报文是否允许被分段和是否使用了这些域
                分段偏移——8位的域指出分段报文相当于整个报文开始处的偏移。这个值以64位为单位递增
                生存时间——IP报文不允许在广域网中永久漫游。它必须限制在一定的TTL内
                协议——8为域表示IP头之后的协议，如VINES、TCP、UDP等
                校验和——校验和是16位的错误检测域。目的机、网络中的每个网关要重新计算报文头的校验和，就如同源机器所做的一样
                源IP地址——源计算机的IP地址
                目的IP地址——目的计算机的IP地址
                填充——为了保证IP头长度是32位的整数倍，要填充额外的0

3.TCP包头结构：
    TCP数据在IP数据报中的封装：    IP数据报：20字节IP首部，20字节TCP首部，最后是TCP数据
    TCP包首部:                     详情见TCP包首部.jpg
    结构：
                TCP源端口：        16位的源端口y域包含初始化通信的端口号
                                   源端口和源IP地址的作用是标识报文的返回地址
                TCP目的端口：      16位的目的端口域定义传输的目的
                                   这个端口指明报文接受计算机上的应用程序地址接口
                TCP序列号：        32位的序列号由接收端计算机使用，重组分段的报文成最初形式
                TCP应答号：        TCP使用32位的应答域标识下一个希望收到的报文的第一个字节
                数据偏移：         这个4位域包括TCP头大小
                                   以32位数据结构或称为"双字"为单位
                保留：             6位恒置0的域
                                   为将来定义新的用途保留
                标志：             6位标志域，每1位标志可以打开一个控制功能
                                   这六个标志是:紧急标志、有意义的应答标志、推、重置连接标志
                                                、同步序列号标志、完成发送数据标志
                窗口大小：         目的机使用16位的域告诉源主机，它想收到的每个TCP数据段大小
                校验和：           TCP头也包括16位的错误检查域——"校验和"域
                紧急：             紧急指针域是一个可选的16位指针，指向段内的最后一个字节位置
                                    ，这个域只在URG标志设置了时才有效
                选项：             至少一字节的可变长域标识哪个选项
                数据：             域的大小是最大的MSS，MSS可以在源和目的机器之间协商
                填充：             其目的是确保空间的可预测性、定时和规范大小
                                    这个域中加入额外的0以保证TCP头是32位的整数倍

4.TCP/IP简介：
    (1)计算机网络的出现比互联网要早很多
    (2)计算机为了联网，就必须规定通信协议，早期的计算机网络，都是由各厂商自己规定一套协议，IBM、Apple
    和Microsoft都有各自的网络协议，互不兼容，这就好比一群人有的说英语，有的说中文，有的说德语，
    说同一种语言的人可以交流，不同的语言之间就不行了
    (3)为了把全世界的所有不同类型的计算机都连接起来，就必须规定一套全球通用的协议，为了实现互联网这个目标，
    互联网协议簇就是通用协议标准。Internet是由inter和net两个单词组合起来的，原意就是连接“网络”的网络，
    有了Internet，任何私有网络，只要支持这个协议，就可以连入互联网
    (4)因为互联网协议包含了上百种协议标准，但是最重要的两个协议是TCP和IP协议，所以，大家把互联网的协议
    简称TCP/IP协议
    (5)通信的时候，双方必须知道对方的标识，好比发邮件必须知道对方的邮件地址。互联网上每个计算机的唯一标识
    就是IP地址，类似123.123.123.123.如果一台计算机同时接入到两个或更多的网络，比如路由器，它就会有两个
    或多个IP地址，所以，IP地址对应的实际上是计算机的网络接口，通常是网卡
    (6)IP协议负责把数据从一台计算机通过网络发送到另一台计算机。数据被分隔成一小块一小块，然后通过IP包发送
    出去。由于互联网链路复杂，两台计算机之间经常有多条线路，因此，路由器就负责决定如何把一个IP包转发出去。
    IP包的特点是按块发送，途径多个路由，但不保证能到达，也不保证顺序到达
    (7)IP地址实际上是一个32位整数(称为IPv4)，以字符串表示的IP地址如192.168.0.1实际上是把32位整数按8位分组
    后的数字表示，目的是便于阅读
    (8)IPv6地址实际上是一个128位整数，它是目前使用的IPv4的升级版，以字符串表示类似于
    2001:0db8:85a3:0042:1000:8a2e:0370:7334
    (9)TCP协议则是建立在IP协议之上的。TCP协议负责在两台计算机之间建立可靠连接，保证数据包按顺序到达。
    TCP协议会通过握手建立连接，然后，对每个IP包编号，确保对方按顺序收到，如果包丢了，就自动重发
    (10)建立一个TCP链接:
                三次握手：   客户端/请求器  发送SYN标志、ISN及目的端口号                   到服务器
                             服务器         发送SYN标志、ISN及确认信息(ACK)                到客户端/请求器
                             客户端/请求器  发送确认信息(ACK)                              到服务器

    (11)断开一个TCP链接：    服务器         发送FIN标识，停止服务器端到客户端的数据传输    到客户端/请求器
                             客户端/请求器  发送确认信息(ACK)                              到服务器
                             客户端/请求器  发送FIN标识，停止客户端到服务器端的数据传输    到服务器
                             服务器         发送确认信息(ACK)                              到客户端/请求器
"""
# TCP编程
# 1.客户端
"""
客户端：创建TCP链接时，主动发起连接的叫做客户端
服务端：接受客户端的连接
"""
# 创建一个socket
# 参数1：指定协议  AF_INET(IPv4) 或 AF_INET6(IPv6)
# 参数2：SOCK_STREAM执行使用面向流的TCP协议    详情见Ctrl+B
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
# 参数：是一个元组，第一个元素为要连接的服务器的IP地址，第二个元素为端口
s.connect(("www.baidu.com", 80))

s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')  # 拿到的是网址类型的
# \r\n为回车

# 等待接收数据
data = []
while True:
    # 每次接收1K数据
    tempData = s.recv(1024)
    if tempData:
        data.append(tempData)
    else:
        break
dataStr = (b''.join(data)).decode("utf-8")

# 断开链接
s.close()
# print(dataStr)

headers, HTML = dataStr.split('\r\n\r\n', 1)
print(headers)
print("----------------------------")
print(HTML)


# 2.客户端与服务端间的数据交互
# 先开启18.2 server.py
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.0.175", 8050))
while True:
    data = input("请输入给服务器发送的数据")
    client.send(data.encode("utf-8"))
    info = client.recv(1024)
    print("服务器说：", info.decode("utf-8"))

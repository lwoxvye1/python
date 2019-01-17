import urllib.request
import json
import urllib.parse
import ssl
import re
"""
为什么用python写爬虫?
语法优美、代码简介、开发效率高、三方模块多，调用其他接口也方便。
有强大的爬虫Scrapy，以及成绩高效的scrapy-redis分布式策略。

如何抓取页面：HTTP请求处理,urllib处理后的请求可以模拟浏览器发送请求,获取服务器响应的文件
解析服务器响应的内容：re、BeautifulSoup5、jsonpath、pyquery
                    目的是使用某种描述性语法来提取匹配规则的数据

如何采取动态HTML、验证码的处理：通用的动态页面采集：Selenlum+PhantomJS(无界面浏览器)，模拟真实浏览器
                                加载js,ajax等非静态页面数据。
                                Tesseract:机器学习库，机器图像识别系统(识别图片中的文本)

Scrapy框架：中国常见的框架Scrapy、Pyspider
            高定制性高性能(异步网络框架twisted)，所以数据下载速度非常快，提供了数据存储、数据下载、提取规则等组件
            scrapy-redis

分布式策略：scrapy-redis
            在Scrapy的基础上添加了一套已Redis数据库为核心的一套组件，让scrapy框架支持分布式的功能，
            主要在Redis里做请求指纹去重，请求分配、数据临时存储

反爬虫技术：User-Agent
            代理
            验证码
            动态数据加载
            加密数据

网络爬虫的类型：通用网络爬虫：概念：搜索引擎用的爬虫系统
                            用户群体：搜索引擎用的爬虫系统
                            目标：尽可能把互联网上的所有网页下载下来，放到本地服务器里形成备份。
                                 再对这些网页做相关处理(提取关键字、去掉广告等)，最后提供一个用户检测接口
                            抓取流程：1.首先选取一部分已有的URL，把这些URL放到带爬队列
                                      2.从队列里提取出这些URL，然后解析DNS得到主机IP，然后去这个IP对应的服务器
                                       里下载HTML页面，保存到搜索引擎的本地服务器里，之后把爬过的URL放入已爬取队列
                                      3.分析这些网页内容，找出网页里的URL链接，继续执行第二步，直到爬取条件结束。
                            搜索引擎如何获取一个新网站的URL：1.主动向搜索引擎提交网址(百度站长平台https://ziyuan.baidu.com/linksubmit/url)
                                                            2.在其他网站里设置网站的外链接
                                                            3.搜索引擎会合DNS服务商合作，可以快速收录新的网站
                            通用爬虫并不是万物皆可爬的，它需要遵守规则：Robots协议：1.协议会指明通用爬虫可以爬取网页的权限
                                                                                    2.Robots.txt只是一个建议，并不是所有爬虫
                                                                                     都遵守，一般只有大型的搜索引擎爬虫才会遵守
                            通用爬虫工作流程：1.爬取网页
                                              2.存储数据
                                              3.内容处理
                                              4.提供检索/排名服务
                            搜索引擎排名：PageRank值：根据网站的流量(点击量、浏览值、人气)统计，流量越高，网站越值钱，排名越靠前
                                        竞争排名：谁钱多谁排名高
                            通用爬虫的缺点：1.只能提供和文本相关的内容(HTML、Word、pdf)等，但是不能提供；多媒体(音乐、图片、视频)和
                                            二进制文件(程序、脚本)等
                                            2.提供结果千篇一律，不能针对不同人群提供不同的搜索结果
                                            3.不能理解人类语义上的搜索
                聚焦网路爬虫：概念：爬虫程序员写的针对某种内容的爬虫
                              特点：面向主体爬虫，面向需求爬虫：会针对某种特定的内容去爬取信息，而且会保证信息和需求尽可能相关
                增量式网络爬虫
                深层网络爬虫
URL：统一资源定位符，是互联网上的资源地址
"""

# 1.urllib爬取网页

# 向指定的url地址发起请求，并返回服务器响应的数据(文件的对象)
response = urllib.request.urlopen("http://www.baidu.com")  # 这里还不支持https协议的url,因为涉及ssl协议
# 读取文件的全部内容，会把读取到的数据赋值给一个字符串变量
"""
data = response.read()
print(data)
print(type(data))
"""
# 读取一行
# data2 = response.readline()
# 读取文件的全部内容,会把读取到的数据赋值给一个列表变量
data3 = response.readlines()
# print(data3)
print(type(data3))
print(type(data3[0]))
# 将爬取到的网页写入文件
with open(r"D:\学习\python\project\17.spiderfiles\1.html", "wb") as f:
    for i in range(len(data3)):
        f.write(data3[i])

# response属性
# 返回当前环境的有关信息
print(response.info())
# 返回状态码
print(response.getcode())
if response.getcode() == 200 or response.getcode() == 304:
    # 200表示请求成功304表示有缓存
    pass
# 返回当前正在爬取的URL地址
print(response.geturl())

url = "https://www.baidu.com/s?wd=%E5%87%AF%E5%93%A5&rsv_spt=1&rsv_iqid=0xe641c04f00059de2&issp=1&f=8&rsv_bp=0&" \
      "rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=15&rsv_sug1=18&rsv_sug7=101&rsv_sug2=0&inputT=5645&" \
      "rsv_sug4=6385"
# 解码
newUrl = urllib.request.unquote(url)
print(newUrl)
# 编码
newUrl2 = urllib.request.quote(newUrl)
print(newUrl2)


# 2.爬到的网页直接写入文件
urllib.request.urlretrieve("http://www.baidu.com", filename=r"D:\学习\python\project\17.spiderfiles\2.html")
# urlretrieve在执行的过程当中，会产生一些缓存

# 清除缓存
urllib.request.urlcleanup()  # 如果你执行一遍程序就结束了就没有必要清除了

# 3.模拟浏览器 (如果网站设置反爬虫，用上述方法无法爬取数据)
url2 = "http://www.baidu.com"
# 模拟请求头
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
# 浏览器 ==> F12 ==> Network ==> Name(第一个) ==> Headers ==> User-Agent
# 设置一个请求体
req = urllib.request.Request(url, headers=headers)  # 反反爬虫，能绕过一小部分网站的反爬虫
# 发起请求
response = urllib.request.urlopen(req)
data4 = response.read().decode("utf-8")
# print(data4)
"""
但是如果一直用同一个agent爬取数据(一秒钟请求几十次)，网站也能检测出来
agentsList = ["", "", "", ""]
agentStr = random.choice(agentsList)
req = urllib.request.Request(url)  不在这里添加，因为此处要添加字典
req.add_header("User-Agent", "agentStr") 向请求体里添加了User-Agent
可以百度查找
"""

# 4.设置超时
# 如果网页长时间未响应，系统判断超时，无法爬取
for i in range(1, 20):
    try:
        response = urllib.request.urlopen("http://www.baidu.com", timeout=0.1)
        print(len(response.read().decode("utf-8")))
    except:
        print("请求超时，继续下一个爬取")


# 5.HTTP请求
"""
使用场景:进行客户端与服务端之间的消息传递时使用
GET:通过URL网址传递信息，可以直接在URL网址上添加要传递的信息
POST:可以向服务器提交数据，是一种比较流行的比较安全的数据传递方式
PUT:请求服务器存储一个资源，通常要指定存储的位置
DELETE:请求服务器删除一个资源
HEAD:请求获取对应的HTTP报头信息
OPTIONS:可以获取当前URL所支持的请求类型
"""


# 6.GET请求
"""
特点：把数据拼接到请求路径的后面传递给服务器
优点：速度快
缺点：承载的数据量小，不安全
"""
url3 = "https://www.baidu.com/s?wd=%E5%87%AF%E5%93%A5&rsv_spt=1&rsv_iqid=0xe641c04f00059de2&" \
       "issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_" \
       "pg&rsv_enter=1&rsv_sug3=15&rsv_sug1=18&rsv_sug7=101&rsv_sug2=0&inputT=5645&rsv_sug4=6385"
response = urllib.request.urlopen(url3)
data5 = response.read().decode("utf-8")
# print(data5)
print(type(data5))
# ?后面的便是GET请求，服务器接收到wd=%E5%87%AF%E5%93%A5&rsv_spt=1……的请求然后返回json格式字符串


# 7.json数据解析
"""
概念:一种保存数据的格式
作用:可以保存本地的json文件，也可以将json串进行传输，通常将json称为轻量级的传输方式

json文件组成
{}      代表对象(字典)
[]      代表列表
:       代表键值对
,       分隔两个部分
"""
jsonStr = '{"name":"sunck", "age":"18", "hobby":["money", "power", "english"], "parames":{"a":1,"b":2}}'
# 将json格式的字符串转为python数据类型的对象
jsonData = json.loads(jsonStr)
print("--------------------")
print(jsonData)
print(type(jsonData))
print(jsonData["hobby"])
# 将python数据类型的对象转为json格式的字符串
jsonStr2 = {"name": "sunck", "age": "18", "hobby": ["money", "power", "english"], "parames": {"a": 1, "b": 2}}
jsonData2 = json.dumps(jsonStr2)
print("--------------------")
print(jsonData2)
print(type(jsonData2))

# 读取本地的json文件
path1 = r"D:\学习\python\project\json.json"
with open(path1, "rb") as f:
    data6 = json.load(f)
    print(data6)
    print(type(data6))  # 字典类型

# 写本地json
path2 = r"D:\学习\python\project\json2.json"
jsonStr3 = {"name": "sunck", "age": "18", "hobby": ["money", "power", "english"], "parames": {"a": 1, "b": 2}}
# 写的话要写字典  将字典写进文件就是json的了
with open(path2, "w") as f2:
    json.dump(jsonStr3, f2)


# 8.Post请求
"""
特点：把参数进行打包，单独传输
优点：数量大，安全(当对服务器数据进行修改时建议使用post)
缺点：速度慢
"""
# 将要发送的数据合成一个字典
# 字典的键去网址里找，一般为input标签的name属性的值
url = "https://www.alipay.com/"
data7 = {
    "logonId": "18201923078",
    "password_rsainput": "19971106s"
}
# 对要发送的数据进行打包,记住编码
postData = urllib.parse.urlencode(data7).encode("utf-8")
# 请求体
req = urllib.request.Request(url, data=postData)
# 请求
req.add_header("User-Agent", "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36")
response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))  # 得到的可以是网页也可以是json字符串等等


# 9.抓取网页动态Ajax请求的数据
# 有的网站需要点击查看更多或者滚轮划到底才能查看全部数据


def ajaxCrawler(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    req = urllib.request.Request(url, headers=headers)
    # 使用ssl创建未验证的上下文(爬取https时使用)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    jsonStr = response.read().decode("utf-8")
    jsonData = json.loads(jsonStr)
    return jsonData


"""
url = "https://movie.douban.com/j/chart/top_list?type=10&interval_id=100%3A90&action=&start=20&limit=20"
info = ajaxCrawler(url)
print("----------------------------------------------")
print(info)
"""
for i in range(1, 11):
    url = "https://movie.douban.com/j/chart/top_list?type=10&interval_id=100%3A90&action=&start="+str(i * 20)\
          + "&limit=20"
    info = ajaxCrawler(url)
    print(len(info))


# 10.糗事百科爬虫
def jokeCrawler(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    HTML = response.read().decode("utf-8")
    # print(HTML)
    pat = r'<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">'
    # 这里的.不匹配换行
    re_joke = re.compile(pat, re.S)
    divsList = re_joke.findall(HTML)
    # print(divsList)
    # print(len(divsList))
    dic = {}
    for div in divsList:
        # 用户名
        re_u = re.compile(r"<h2>(.*?)</h2>", re.S)
        username = re_u.findall(div)
        username1 = username[0].strip()
        # 段子
        re_d = re.compile(r'<div class="content">\n<span>(.*?)</span>', re.S)
        duanzi = re_d.findall(div)
        duanzi1 = duanzi[0].strip()

        dic[username1] = duanzi1
    return dic


url = "https://www.qiushibaike.com/text/page/1/"
info = jokeCrawler(url)
for k, v in info.items():
    print(k + "\n" + v + "\n")
"""
for i in range(1, 14):
    url = "https://www.qiushibaike.com/text/page/" + i + "/"
    info = jokeCrawler(url)
"""
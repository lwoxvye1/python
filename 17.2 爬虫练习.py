import urllib.request
import re
import os
import ssl
import collections   # 8.递归与时间模块
# 爬取1号店男装


def imageCrawler(url, toPath):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    HtmlStr = response.read().decode("utf-8")
    pat = r'<div style="position: relative">\n<img src="//(.*?)"/>\n</div>'
    re_image = re.compile(pat, re.S)
    imagesList = re_image.findall(HtmlStr)
    # print(imagesList)
    # print(len(imagesList))
    num = 1
    for i in imagesList:
        path = os.path.join(toPath, str(num) + ".jpg")
        num += 1
        # 把图片下载到本地存储
        urllib.request.urlretrieve("http://" + i, filename=path)


url = "http://search.yhd.com/c0-0/k%25E7%2594%25B7%25E8%25A3%2585/#page=3&sort=1"
toPath = r"D:\学习\python\project\17.spiderfiles\image"
# imageCrawler(url, toPath)


# 爬取网络中的QQ号码
def writeFileBytes(htmlBytes, toPath):
    with open(toPath, "wb") as f:
        f.write(htmlBytes)


def writeFileStr(htmlBytes, toPath):
    with open(toPath, "w", encoding="utf-8") as f:
        f.write(htmlBytes.decode("utf-8"))


def qqCrawler(url, toPath):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    req = urllib.request.Request(url, headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    htmlBytes = response.read()
    writeFileBytes(htmlBytes, r"D:\学习\python\project\17.spiderfiles\file1.html")
    writeFileStr(htmlBytes, r"D:\学习\python\project\17.spiderfiles\file2.txt")
    htmlStr = htmlBytes.decode("utf-8")
    # 拿到所有的QQ
    pat = r"[1-9]\d{4,9}"   # 这里一定不能加空格!
    re_qq = re.compile(pat)
    qqList = re_qq.findall(htmlStr)
    # 去重
    qqList = list(set(qqList))
    # print(qqList)
    # print(len(qqList))
    f = open(toPath, "a")
    for qqStr in qqList:
        f.write(qqStr + "\n")
    f.close()

    # 拿到所有的网址
    pat = '(((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))' \
          '(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?)'
    re_url = re.compile(pat)
    urlList = re_url.findall(htmlStr)
    urlList = list(set(urlList))
    # print(urlList)
    # print(len(urlList))
    # print(urlList[100])
    return urlList


url1 = "https://www.douban.com/group/topic/110094603/"
toPath1 = r"D:\学习\python\project\17.spiderfiles\qqFile.txt"
# qqCrawler(url1, toPath1)


# 中央控制器
def center(url, toPath):
    queue = collections.deque()
    queue.append(url)
    while len(queue) != 0:
        try:
            target_url = queue.popleft()
            url_list = qqCrawler(target_url, toPath)
            for item in url_list:
                temp_url = item[0]
                queue.append(temp_url)
        except:
            print("无此网站！")


url2 = "https://www.douban.com/group/topic/110094603/"
toPath2 = r"D:\学习\python\project\17.spiderfiles\qqFile2.txt"
# 现在是单线程,所以处理的很慢
center(url2, toPath2)

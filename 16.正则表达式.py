import itertools
import time
import re
# 破解密码

# 排列
mylist1 = list(itertools.permutations([1, 2, 3, 4], 3))
print(mylist1)
print(len(mylist1))
# 组合
mylist2 = list(itertools.combinations([1, 2, 3, 4], 3))
print(mylist2)
print(len(mylist2))
# 排列组合
mylist3 = list(itertools.product([1, 2, 3, 4, 5], repeat=4))
print(mylist3)
print(len(mylist3))
# 破解密码
"""
passwd1 = ("".join(x) for x in itertools.product("0123456789", repeat=3))
while True:
    try:
        time.sleep(0.1)
        str1 = next(passwd1)
        print(str1)
    except StopIteration as e:
        break
"""

# 正则表达式

# 判断手机号码


def checkPhone(str1):
    if len(str1) != 11:
        return False
    elif str1[0] != "1":
        return False
    elif str1[1:3] != "31" and str1[1:3] != "39":
        return False
    for i in range(3, 11):
        if str1[i] < "0" or str1[i] > "9":
            return False
    return True


print(checkPhone("13912345678"))

# 正则概述
"""
Python自1.5以后增加了re的模块，提供了正则表达式模式
re模块使Python语言拥有了全部的正则表达式功能
"""

# re模块简介
r"""
pip 包管理工具

re.match函数
原型：match(pattern, string, flags=0)
参数：
pattern:匹配的正则表达式
string:要匹配的字符串
flags:标志位，用于控制正则表达式的匹配方式，值如下
re.I    忽略大小写
re.L    做本地化识别
re.M    多行匹配，影响^(shift+6)和$
re.S    使.匹配包括换行符在内的所有字符
re.U    根据Unicode字符集解析字符,影响\w  \W  \b   \B
re.X    使我们以更灵活的格式理解正则表达式
功能：尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，返回None
"""
# Ctrl+B查看函数的定义和使用方法
# www.baidu.com
print(re.match("www", "www.baidu.com"))
print(re.match("www", "www.baidu.com").span())  # 得到在字符串中的位置
print(re.match("www", "ww.baidu.com"))
print(re.match("www", "baidu.wwwcom"))
print(re.match("www", "wwW.baidu.com"))
print(re.match("www", "wwW.baidu.com", flags=re.I))
# 扫描整个字符串,返回从起始位置成功的匹配

"""
re.search函数
原型：search(pattern, string, flags=0)
参数：
pattern:匹配的正则表达式
string:要匹配的字符串
flags:标志位，用于控制正则表达式的匹配方式
功能：扫描整个字符串，并返回第一个成功的匹配
"""
print("------------------------------------------------")
print(re.search("Tom", "good man is Tom!Tom is a good man"))

"""
re.findall函数
原型：findall(pattern, string, flags=0)
参数：
pattern:匹配的正则表达式
string:要匹配的字符串
flags:标志位，用于控制正则表达式的匹配方式
功能：扫描整个字符串,并返回结果列表
"""
print("------------------------------------------------")
print(re.findall("Tom", "good man is Tom!Tom is a good man"))
print(re.findall("Tom", "good man is tom!Tom is a good man", flags=re.I))

# 正则表达式的元字符
# 匹配单个字符与数字
r"""
.               匹配除换行符以外的任意字符
[0123456789]    []是字符集合，表示匹配方括号中所包含的任意一个字符
[a-z]           匹配任意小写字母
[A-Z]           匹配任意大写字母
[0-9]           匹配任意数字，类似[0123456789]
[0-9a-zA-Z]     匹配任意数字和字母(不加空格！加空格会多匹配一个空格)
[0-9a-zA-Z_]    匹配任意数字、字母和下划线
[^tom]          匹配除了t、o、m以外的所有字符，中括号里的^称为脱字符，表示不匹配集合中的字符
[^0-9]          匹配所有的非数字字符
\d              匹配数字，效果同[0-9]
\D              匹配非数字字符,效果同[^0-9]
\w              匹配数字、字母和下划线，效果同[0-9a-zA-Z_]         
\W              匹配非数字、字母和下划线，效果同[^0-9a-zA-Z_]
\s              匹配任意的空白符(空格，换行，回车，换页，制表)，效果同[ \f\n\r\t] 
\S              匹配任意的非空白符，效果同[^ \f\n\r\t] 
"""
print("--------------匹配单个字符与数字------------------")
print(re.search(".", "tom is a good man"))
print(re.search("[0123456789]", "tom is a good man 7 "))
print(re.findall("[^\d]", "tom is a good man 7 "))
print(re.findall("\w", "_tom is a good man 7 "))
print(re.findall(".", "_tom is a go\nod man 7 "))
print(re.findall(".", "_tom is a go\nod man 7 ", flags=re.S))

# 锚字符(边界字符)
r"""
^               行首匹配，和在[]里的^不是一个意思
$               行尾匹配
\A              匹配字符串开始,它和^的区别是\A只匹配整个字符串的开头，即使在re.M模式下也不会匹配他行的行首
\Z              匹配字符串结尾，它和$的区别是\Z只匹配整个字符串的结尾，即使在re.M模式下也不会匹配他行的行尾
\b              匹配一个单词的边界,也就是指单词和空格间的位置
                "er\b"可以匹配never,不能匹配nerve(需要注意引号前应该加r，否则\b会转义)
\B              匹配非单词边界
                "er\B"不能匹配never,可以匹配nerve，\B须在单词里面找
"""
print("--------------锚字符(边界字符)------------------")
print(re.search("^tom", "tom is a good man"))
print(re.search("man$", "tom is a good man"))
print(re.findall("^tom", "tom is a good man\ntom is a nice man", re.M))
print(re.findall("\Atom", "tom is a good man\ntom is a nice man", re.M))
print(re.findall("man$", "tom is a good man\ntom is a nice man", re.M))
print(re.findall("man\Z", "tom is a good man\ntom is a nice man", re.M))
print(re.search(r"er\b", "never"))
print(re.search(r"er\b", "nerve"))
print(re.search("er\B", "never"))
print(re.search("er\B", "nerve"))

# 匹配多个字符
"""
说明：下方的x、y、z均为假设的普通字符，不是正则表达式的元字符
(xyz)           匹配小括号内的xyz(作为一个整体去匹配)
x?              匹配0个或者1个x
x*              匹配0个或者任意多个x(.*  表示匹配0个或者任意多个字符，换行符除外)
x+              匹配至少一个x
x{n}            匹配确定的n个x(n是一个非负整数)
x{n,}           匹配至少n个x
x{n,m}          匹配至少n个最多m个x,注意：n <= m
x|y             |表示或，匹配的是x或y
"""
print("--------------匹配多个字符------------------")
print(re.findall(r"(tom)", "tomgood is a good man,tom is a nice man"))
print(re.findall(r"a?", "aaabaa"))  # 非贪婪匹配(尽可能少的匹配)
print(re.findall(r"a*", "aaabaa"))  # 贪婪匹配(尽可能多的匹配)
print(re.findall(r"a+", "aaabaa"))
print(re.findall(r"a{3}", "aaabaaaaabaa"))
print(re.findall(r"a{3,}", "aaabaaaaabaa"))
print(re.findall(r"a{3,4}", "aaabaaaaabaa"))
print(re.findall(r"((s|S)unck)", "sunck--SuNck--Sunck"))
# 需求，提取tom……man
str1 = "tom is a good man!tom is a nice man!tom is a handsome man"
print(re.findall(r"^tom.*man$", str1))  # 贪婪匹配，中间所有的都能匹配上,因为匹配的是以tom开头man结尾的字符所以就一个
print(re.findall(r"tom.*?man", str1))

# 特殊
print("--------------特殊------------------")
"""
*?  +?  (xyz)?  最小匹配    通常都是尽可能多的匹配，可以使用这种方式解决贪婪匹配

(?:x)           类似(xyz)，但不表示一个组           
"""
print(re.findall(r"//*.*?/*/", r"/*   part1   */   /*   part2   */"))
# //* 表示/*开头，之所以转义是因为/*会有歧义，可以表示0或任意个/，也可表示/*开头，/*/同理，转义的是*


def checkPhone2(str2):
    pat = r"^1(([3578]\d)|(47))\d{8}$"
    res = re.match(pat, str2)
    return res


print(checkPhone2("13912345678"))
print(checkPhone2("139123456788"))
print(checkPhone2("13912a45678"))
print(checkPhone2("23912345678"))

# re模块深入
"""
字符串切割
"""
str2 = "tom    is a good man"
print(str2.split(" "))
print(re.split(r" +", str2))
"""
re.finditer函数
原型：finditer(pattern, string, flags=0)
参数：
pattern:匹配的正则表达式
string:要匹配的字符串
flags:标志位，用于控制正则表达式的匹配方式
功能：与findall类似，扫描整个字符串，返回的是一个迭代器
"""
str3 = "tom is a good man! tom is a nice man! tom is a handsome man"
d = re.finditer(r"(tom)", str3)
while True:
    try:
        l = next(d)
        print(l)
    except StopIteration as e:
        break
"""
字符串的替换和修改
sub(pattern, repl, string, count=0, flags=0)
subn(pattern, repl, string, count=0, flags=0)
pattern:    正则表达式(规则)
repl:       指定的用来替换的字符串
string:     目标字符串
count:      最多替换次数
功能：      在目标字符串中以正则表达式的规则匹配字符串，再把他们替换成指定的字符串。可以指定替换的次数。
如果不指定，替换所有的匹配字符串
区别：      前者返回一个被替换的字符串，后者返回一个元组，第一个元素是被替换的字符串，
第二个元素表示被替换的次数
"""
str4 = "tom is a good good good man"
print(re.sub(r"(good)", "nice", str4, count=2))
print(type(re.sub(r"(good)", "nice", str4)))
print(re.subn(r"(good)", "nice", str4, count=2))
print(type(re.subn(r"(good)", "nice", str4)))
"""
分组
概念:除了简单的判断是否匹配之外，正则表达式还有提取子串的功能。用()表示的就是提取出来的分组
"""
str5 = "010-53247654"
m = re.match(r"(\d{3})-(\d{8})", str5)
# 使用序号获取对应组的信息，group(0)一直代表的原始字符串
print(m.group(0))
print(m.group(1))
print(m.group(2))
# 查看匹配的各组的情况
print(m.groups())

m = re.match(r"((\d{3})-(\d{8}))", str5)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.groups())
# 起名字
m = re.match(r"(?P<first>\d{3})-(?P<last>\d{8})", str5)
print(m.group("first"))
"""
编译：当我们使用正则表达式时,re模块会干两件事
1、编译正则表达式，如果正则表达式本身不合法，会报错
2、用编译后的正则表达式去匹配对象
compile(pattern, flags=0)
pattern:要编译的正则表达式
"""
pat = r"1(([3578]\d)|(47))\d{8}$"
# 编译成正则对象
re_telephone = re.compile(pat)
print(re_telephone.match("13600000000"))

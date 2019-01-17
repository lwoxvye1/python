import doctest
# doctest模块可以提取注释中的代码执行
# doctest严格按照python交互模式(cmd>>>python进入的便是交互模式)的输入提取


def mySum(x, y):
    """此处打三个引号

    :param x:
    :param y:
    :return:

    example:
    >>> print(mySum(1, 2))  # 注意>>>后有空格
    3


    """
    return x + y + 1


# 进行文档测试
doctest.testmod()


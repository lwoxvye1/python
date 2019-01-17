import redis
"""
Redis
数据操作
redis是key-value的数据，所以每个数据都是一个键值对
键的类型是字符串
值的类型分为五种(字符串string、哈希hash、列表list、集合set、有序集合zset)

数据操作的全部命令 http://redis.cn/commands.html
"""
"""
redis命令
一、String
    概述：String是redis最基本的类型，最大能存储512MB的数据，String类型是二进制安全的，
          即可以存储任何数据，比如数字、图片、序列化对象等
    
    1、设置
        a、设置键值
            set key value
            示例：set a "sunck is a good man"
        b、设置键值及过期时间，以秒为单位
            setex key seconds value
        c、设置多个键值
            mset key value key value...
    2、获取
        a、根据键获取值，如果键不存在则返回null
            get key
        b、根据多个键获取多个值
            mget key  key ...
    3、运算
        要求：值是字符串类型的数字
        a、将key对应的值加一
            incr key    
        b、将key对应的值键一
            decr key
        c、将key对应的值加整数
            incrby key intnum 
            incrby f 2
        d、将key对应的值减整数
            decrby key intnum 
    4、其它
        a、追加值
            append  key value
            append a !
        b、获取值长度
            strlen key
二、key
    1、查找键,参数支持正则
        keys pattern 
    2、判断键是否存在，如果存在返回1，不存在返回0
        exists key  
    3、查看键对应的value类型
        type key
    4、删除键及对应的值
        del key [key...]
    5、设置过期时间，以秒为单位
        expire key seconds
    6、查看有效时间，以秒为单位
        ttl key
三、hash
    概述：hash用于存储对象
    
    1、设置
        a、设置单个值
            hset key  field value
            hset  p1  name  tom
            hset  p1  age   18
        b、设置多个值
            hmset   key  field   value  [field   value....]
            hmset  p2   name lilei  age 20
    2、获取
        a、获取一个属性的值
            hget key field 
        b、获取多个属性的值
            hmget key field [field ....]
        c、获取所有属性和值
            hgetall  key
        d、获取所有属性
            hkeys key
        e、获取所有值
            hvals key
        f、返回包含属性的个数
            hlen key 
    3、其它
        a、判断属性是否存在,存在返回1，不存在返回0
            hexists key field
        b、删除属性及值
            hdel key  field  [field ....]
        c、返回值的字符串长度
            hstrlen key field
四、list
    概述：列表的元素类型为string，按照插入顺序排序，在列表的头部或尾部添加元素
    
    1、设置
        a、在头部插入
            lpush  key value [value...]   (向左(头)添加)
        b、在尾部插入
            rpush key value [value...]     (向右(尾)添加)
        c、在一个元素的前|后插入新元素
            linsert key before|after   pivot value
        d、设置指定索引的元素值
            lset key index value
            注意:index从0开始
            注意：索引值可以是负数，表示偏移量是从list的尾部开始，如-1表示最后一个元素
    2、获取
        a、移除并返回key对应的list的第一个元素
            lpop  key
        b、移除并返回key对应的list的最后一个元素
            rpop key
        c、返回存储在key的列表中的指定范围的元素
            lrange key start end
            注意：start end 都是从0开始      偏移量可以是负数
            lrange s1 0 -1
    3、其他
        a、裁剪列表，改为原集合的一个子集
            ltrim key start end
        b、返回存储在key里的list的长度
            llen key
        c、返回列表中索引对应的值
            lindex key index
五、set 
    概述：无序集合，元素类型为String类型，元素具有唯一性
    1、设置
        a、添加元素
            sadd    key member  [member.....]
    2、获取
        a、返回key集合中所有元素
            smembers key
        b、返回集合元素个数
            scard key
    3、其他
        a、求多个集合的交集
            sinter key [key .....]
        b、求多个集合的差集
            sdiff key [key...]
        c、求多个集合的合计
            sunion key [key...]
        d、判断元素是否在集合中，存在返回1，不存在返回0
            sismember key member
六、zset
    概述：a、有序集合，元素类型为String，元素具有唯一性，不能重复
        b、每个元素都会关联一个double类型的score(表示权重)，通过权重的大小排序，元素的score可以相同
    
    1、设置
        a、添加
            zadd key score member [score member]
            zadd z1 1 a 5 b 3 c 2 d 4 e
    2、获取
        a、返回指定范围的元素
            zrange key start end
            zrange z1 0 -1
        b、返回元素个数
            zcard key
        c、返回有序集合key中，score在min和max之间的元素的个数
            zcount key min max
            zcount z1 2 4
        d、返回有序集合key中，成员member的score
            zscore key member 
"""

# Redis与Python交互

# 连接
r = redis.StrictRedis(host="localhost", port=6379, password="password")
"""
# 方法1：根据数据类型的不同，调用响应的方法
# 写
# r.set("q1", "good")

# 读
# print(r.get("q1"))
"""

# 方法2:pipeline
# 缓冲多条命令，然后依次执行，减少服务器-客户端之间的TCP数据包
pipe = r.pipeline()
pipe.set("q2", "nice")
pipe.set("q3", "handsome")
pipe.set("q4", "cool")
pipe.execute()  # 只需要发起一次请求


# 封装
class SunckRedis(object):
    def __init__(self, passwd, host="localhost", port=6379):
        self.__redis = redis.StrictRedis(host=host, port=port, password=passwd)

    def set(self, key, value):
        self.__redis.set(key, value)

    def get(self, key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return ""


"""
redis主要用于缓存，因为redis效率比mysql快

如果高峰时间段一个一个从mysql里面拿数据再传到服务器效率太低，所以先把
数据存在Redis里,只有当Redis里没有请求数据的时候再去mysql里拿，然后把
拿到的数据同时也写入redis一份以防下次

redis适合存一些经常查询的数据(登录账号密码等)
"""
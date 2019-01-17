import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId  # 用于id查询

"""
NoSQL简介：
概述： NoSQL，全名叫Not Only SQL，指的是非关系型数据库
       随着访问量的上升，网站的数据库性能出现了问题，于是nosql被设计出来

优点： 高可扩展性
       分布式计算
       低成本
       构架的灵活性，半结构化数据
       没有复杂的关系

缺点： 没有标准化
       有限的查询功能(到目前为止)
       最终一致是不直观的程序

分类   列存储：       代表(Hbase、Cassandra、Hypertable)
                      特点：顾名思义，是按列存储数据的。最大的特点是方便存储结构化和半结构化数据
                            ，方便做数据压缩，对针对某一列或者某几列的查询有非常大的IO优势
       文档存储：     代表(MongoDB、CouchDB)
                      特点：文档存储一般用类似json的格式存储，存储的内容是文档型的。这样也就有机会对
                            某些字段建立索引，实现关系数据库的某些功能
       key-value存储：代表(Tokyo Cabinet/Tyrant、Berkeley DB、Memcache DB、Redis)
                      特点：可以通过key快速查询到其value。一般来说，存储不管value的格式，照单全收。
                            (Redis包含了其他功能)
       图存储：       代表(Neo4J、FlockDB)
                      特点：图形关系的最佳存储。使用传统关系数据库来解决的话性能低下，而且设计
                            使用不方便
       对象存储：     代表(db4o、Versant)
                      特点：通过类似面向对象语言的语法操作数据库，通过对象的方式存取数据
       xml数据库：    代表(Berkeley DB XML、BaseX)
                      特点：高效的存储XML数据，并支持XML的内部查询语法，比如XQuery，XPath
"""
"""
MongoDB简介
一、什么是MongoDB?
1、MongoDB是由C++语言编写的，是一个基于分布式文件存储的开源数据库系统。在高负载的情况下，
添加多的节点，可以保证服务器性能。
2、MongoDB旨在为WEB应用提供可扩展的高性能数据存储解决方案。
3、MongoDB将数据存储为一个文档，数据结构由键值对组成。MongoDB文档类似与JSON对象。字段值
可以包含其他文档，数组及文档数组。

二、主要特点
1、MongoDB提供了一个面向文档的存储，基本的思路就是将原来"行"的概念换成更加灵活的"文档"模型。
一条记录可以表示非常复杂的层次关系。
2、Mongo支持丰富的查询表达式。查询指令使用JSON形式的标记，可轻易查询文档中内嵌的对象及数组。
3、非常容易扩展。面对数据量的不断上升，通常有两种方案，一种是购买更好的硬件，另一种是分散数据，
进行分布式的扩展，前者有着非常大的缺点，因为硬件通常是有物理极限的，当达到极限以后，处理能力就
不可能再进行扩展了。所以建议的方式是使用集群进行扩展。MongoDB所采用的面向文档的数据模型使其
可以自动在多台服务器之间分隔数据。它还可以平衡集群的数据和负载，自动重排文档。
4、MongoDB支持各种编程语言：RUBY、PYTHON、JAVA、C++、PHP、C#等多种语言。
5、丰富的功能。包括索引、存储JavaScript、聚合、固定集合、文件存储等。
6、方便的管理，除了启动数据库服务器之外，几乎没有什么必要的管理操作。管理集群只需要知道有新增加
的节点，就会自动集成和配置新节点。
"""


"""
MongoDB基本操作
一、操作mongodb数据库
    1、创建数据库
        语法：use 数据库名
        说明：如果数据库不存在则创建数据库，否则切换到指定的数据库
        注意：如果刚刚创建的数据库不在列表内，要显示它，我们需要向刚刚创建的数据库中插入一些数据
              (  db.student.insert({name:"tom",age:18,gender:1,address:"北京",isDelete:0})  )
    2、删除数据库
        前提：使用当前数据库(use 数据库名)
        db.dropDatabase()
    3、查看所有数据库
        show dbs
    4、查看当前正在使用的数据库
        a、db
        b、db.getName()
    5、断开连接
        exit
    6、查看命令api
        help
        
二、集合操作
    1、查看当前数据库下有哪些集合
        show collections
    2、创建集合
        a、
            语法：db.createCollection("集合名")
            示例：db.createCollection("class")
        b、
            语法：db.集合名.insert(document)
            示例：db.student.insert({name:"tom",age:18,gender:1,address:"北京",isDelete:0})
            注意：必须要写个文档
            
        区别：两者的区别在于前者创建的是一个空的集合，后者创建一个空的集合并添加一个文档
    3、删除当前数据库中的集合
        语法：db.集合名.drop()
        示例：db.class.drop()

三、文档操作
    1、插入文档
        a、使用insert()方法插入文档
            语法：db.集合名.insert(document)
            插入一个：db.student.insert({name:"lilei",age:19,gender:1,address:"北京",isDelete:0})
            
            语法：db.集合名.insert([文档1，文档2，...])
            插入多个：db.student.insert([{name:"hanmeimei",age:17,gender:0,address:"北京",isDelete:0},
                        {name:"hanmei",age:20,gender:0,address:"上海",isDelete:0}])
            
        b、使用save()方法插入文档
            语法：db.集合名.save(文档)
            说明：如果不指定_id字段，save()方法类似于insert()方法。如果指定_id字段，则会更新
                  _id字段的数据
            示例1：db.student.save({name:"poi",age:22,gender:1,address:"石家庄",isDelete:0})
            示例2：db.student.save({_id:ObjectId("5c2daa4b3f667fdfe2290e9b"),name:"poi",
                                    age:23,gender:1,address:"石家庄",isDelete:0})
    
    2、文档更新
        a、update()方法用于更新已存在的文档
            语法：db.集合名.update(
                query,
                update,
                {
                    upset:<boolean>,
                    multi:<boolean>,
                    writeConcern:<document>
                }
            )
            参数说明：
                query:update的查询条件，类似于sql里update语句内where后面的内容
                update:update的对象和一些更新的操作符($set,$inc)等,$set直接更新，$inc在原有
                        的基础上累加后更新
                upset:可选，如果不存在update的记录，是否当新数据插入，true为插入，默认为false
                multi:可选，mongodb默认为false,只更新找到的第一条记录，如果这个参数为true，
                      就按照条件查找出来的数据全部更新
                writeConcern:可选，抛出异常的级别
            示例：db.student.update({name:"lilei"},{$set:{age:25}})    
                  累加：db.student.update({name:"lilei"},{$inc:{age:25}})
                  全改：db.student.update({name:"poi"},{$set:{age:40}},{multi:true})
                
        b、save()方法通过传入的文档替换已有文档
            语法:db.集合名.save(
                document,
                {
                     writeConcern:<document>   
                }
            )
            参数说明：
                document:文档数据
                writeConcern:可选，抛出异常的级别
                
    3、文档删除
        说明:在执行remove()函数前，先执行find()命令来判断执行的条件是否存在是一个良好习惯
        语法：db.集合名.remove(
                    query,
                    {
                        justOne:<boolean>,
                        writeConcern:<document>   
                    }
                )
        参数说明：
            query:可选，删除的文档的条件
            justOne:可选，如果为true或1，则只删除一个文档,默认false
            writeConcern:可选，抛出异常的级别
        示例:
            db.student.remove({name:"tom"})
            db.student.remove({name:"tom"},{justOne:true})
            
    4、文档查询
        a、find()方法
            查询集合下所有的文档()
            语法：db.集合名.find()
            示例：db.student.find()
        b、find()方法查询指定列
            语法:db.集合名.find(
                    query,
                    {
                        <key>:1,
                        <key>:1
                    }
                )
            参数说明:
                query:查询条件
                key:要显示的字段,1表示显示
            示例：db.student.find({gender:1},{name:1,age:1})
                  db.student.find({},{name:1,age:1})
        c、pretty()方法以格式化的方式来显示文档
            示例：db.student.find().pretty()
        d、findOne()方法查询匹配结果的第一条数据
            示例：db.student.findOne({gender:0})
            
    5、查询条件操作符
        作用：条件操作符用于比较两个表达式并从mongodb集合中获取数据
        a、大于                    -   $gt
            语法：db.集合名.find({<key>:{$gt:<value>}})
            示例：db.student.find({age:{$gt:20}})
        b、大于等于                -   $gte
            语法：db.集合名.find({<key>:{$gte:<value>}})
        c、小于                    -   $lt
            语法：db.集合名.find({<key>:{$lt:<value>}})
        d、小于等于                -   $lte
            语法：db.集合名.find({<key>:{$lte:<value>}})
        e、大于等于 和 小于等于    -   $in 和 $nin
            语法：db.集合名.find({<key>:{$gte:<value>,$lte:<value>}}) 
        f、等于                    -   :
            语法：db.集合名.find({<key>:{<value>}})
        g、使用_id进行查询
            语法：db.集合名.find({"_id":ObjectId("id值")})
            示例：db.student.find({"_id":ObjectId("5c2da7a03f667fdfe2290e97")})
        h、查询某个结果集的数据条数
            db.student.find().count()
        i、查询某个字段的值当中是否包含另一个值
            db.student.find({name:/ile/})
        j、查询某个字段的值是否以另一个值开头
            db.student.find({name:/^li/})
    
    6、条件查询  and 和 or
        a、AND条件
            语法：db.集合名.find({条件1,条件2，...})
            示例：db.student.find({gender:0,age:{$gt:16}})        
        b、OR条件
            语法：db.集合名.find(
                    {
                        $or:[{条件1}，{条件2}，...]
                    }
                )
            示例：db.student.find({$or:[{age:17},{age:{$gte:20}}]})
        c、AND和OR联合使用
            语法：db.集合名.find(
                    {
                        条件1，
                        条件2，
                        $or:[{条件3}，{条件4}]
                    }
                )
    
    7、limit、skip
        a、limit():读取指定数量的数据记录
            db.student.find().limit(2)
        b、skip()跳过指定数量的数据
            db.student.find().skip(3)
        c、skip与limit联合使用
            通常用这种方式来实现分页功能
            示例:db.student.find().skip(3).limit(3)

    8、排序
        语法：db.集合名.find().sort({<key>:1|-1})
        示例：db.student.find().sort({age:1})
              db.student.find().sort({age:-1})
        注意：1表示升序，-1表示降序
"""


# 连接服务器
conn = MongoClient("localhost", 27017)

# 连接数据库
db = conn.test

# 获取集合
collection = db.student

# 1、添加文档
# collection.insert_one({"name": "sunck", "age": 18, "gender": 1, "address": "黑龙江", "isDelete": 0})
# collection.insert_many([{"name": "sunck", "age": 18, "gender": 1, "address": "黑龙江", "isDelete": 0},
#                       {"name": "kaige", "age": 18, "gender": 1, "address": "黑龙江", "isDelete": 0}])

# 2、查询文档

# 查询部分文档
res = collection.find({"age": {"$gt": 18}})
for row in res:
    print(row)
    print(type(row))

"""
# 查询所有文档
res = collection.find()
for row in res:
    print(row)
"""

# 统计查询
res = collection.count_documents({"age": {"$gt": 18}})
# 相当于res = collection.find({"age": {"$gt": 18}}).count()
print(res)

# 根据id查询
res = collection.find({"_id": ObjectId("5c2da8f33f667fdfe2290e99")})
print(res[0])

# 排序
"""
res = collection.find().sort("age", pymongo.DESCENDING)
for row in res:
    print(row)
"""

# 分页
print("-------------------------")
res = collection.find().skip(3).limit(5)
for row in res:
    print(row)


# 3、更新文档
collection.update_one({"name": "hanmei"}, {"$set": {"age": 25}})


# 4、删除文档
# collection.delete_one({"name": "lilei"})


# 断开
conn.close()

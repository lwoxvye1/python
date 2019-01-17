import pymysql
# MySQL基本命令脚本
"""
字段类型：  数字：   int(整数)             decimal(小数)(也可以是整数填充0)
           字符串： char(固定长度字符串)  varchar(可变长度字符串)    text(大量字符串)
           日期：   datetime
           布尔     bit(二进制)
"""
"""
MySQL基本命令脚本
一、基本命令
1、启动服务：
     以管理员身份运行cmd
     格式：net start 服务名称
     示例：net start mysql80

2、停止服务：
     以管理员身份运行cmd
     格式：net stop 服务名称
     示例：net stop mysql80

3、连接数据库
     格式：mysql -u  用户名 -p
     示例：mysql -u  root -p

4.退出登录(断开连接)
     quit或 exit

5、查看版本
    select version();

6、显示当前时间
    select now(); 

7、远程连接
    格式：mysql -h ip地址  -u  用户名  -p
    输入对方mysql密码
    
二、数据库操作
    1、创建数据库
        create database  数据库名 charset=utf8;
    2、删除数据库
        drop database 数据库名;   
    3、切换数据库
        use 数据库名;
    4、查看当前选择的数据库
        select database();
        
三、表操作
    1、查看当前数据库中所有表
        show tables;
    2、创建表
        create table 表名(列及类型);
        说明：auto_increment表示 自增长   
              primary key 表示 主键   
              not null表示 不为空
        示例：create table student(id int auto_increment primary key,name varchar(20)  not null,
                                    age int not null, gender bit not null  default 1,
                                    address varchar(20), isDelete bit default 0);
    3、删除表
        drop  table  表名;
    4、查看表结构
        desc  表名;
    5、修改表
        alter table  表名  add/change/drop  列名  类型;
    6、查看建表语句
        show create table 表名;
    7、重命名表名
        rename table 原表名 to 新表名;
        
四、数据操作
    1.增
        a、全列插入
            insert into 表名 values();
            student表主键列是自动增长的，但是在全列插入时需要占位，通常使用0，插入成功后以实际数据为准
            insert into student values(0, "tom", 19, 1, "北京", 0);
        b、缺省插入
            insert into 表名(列1, 列2,...) values(值1, 值2,...);
            insert into student(name,age,address) values("lilei",19,"上海");
        c、同时插入多条数据：
            insert into 表名 values(...),(...),... ;
            insert into student values(0,"hanmeimei",18,0,"北京",0),(0,"poi",22,1,"海南",0);
    2.删
        delete from 表名 where 条件;
        delete from student where id=4;
        注意: 没有条件是全部删除
    3.改
        update  表名  set 列1=值1,列2=值2,... where 条件;
        update student set age=16 where id=2;
        注意:如果没有条件是全部列都修改
    4.查

五、查
    1、基本语法
        a、select * from 表名;
        b、from关键字后面是表名，表示数据来源于这张表
        select后面写表中的列名，如果是*表示在结果集中显示表中的所有列
        c、在select后面的列名部分，可以使用as为列名起别名，这个别名显示在结果集中
        d、如果要查询多个列，之间使用逗号分隔
        
        select * from student;
        select name,age from student;
        select name as a,age from student;
    2、消除重复行
        在select后面列前面使用distinct可以消除重复的行
        
        select distinct  gender from student;    
    3、条件查询
        a、语法
            select * from 表名 where 条件;        
        b、比较运算符
            等于      =   
            大于      >
            小于      <
            大于等于  >=  
            小于等于  <=
            不等于    !=或<>
            
            select * from student where id>2;
        c、逻辑运算符
            and       并且
            or        或者
            not       非
            
            select * from student where id>2  and gender=0;
        d、模糊查询
            like
            %         表示任意多个任意字符
            _         表示一个任意字符
            
            select * from student where name like "习%";
            select * from student where name like "习_";
        e、范围查询
            in        表示在一个非连续的范围内
            between  and  表示在一个连续的范围内
        
            select * from student where id in (2,5,7);
            select * from student where id between 2 and 5;    
        f、空判断
            注意：null与""是不同的  
            判断空:is null
            判断非空:is not null
            
            select * from student where address is null;
            select * from student where address is not null;
        g、优先级
            小括号，not，比较运算符，逻辑运算符
            and比or的优先级高
    4、聚合
        为了快速得到统计数据，提供了5个聚合函数
        a、count(*)      表示计算总行数，括号中可以写*和列名
        b、max(列)       表示求此列的最大值
        c、min(列)       表示求此列的最小值
        d、sum(列)       表示求此列的和
        e、avg(列)       表示求此列的平均值
        
        select count(*) from student;
        select max(id) from student where gender=0;
        select min(id) from student where gender=1;
        select sum(age) from student;
        select avg(age) from student;        
    5、分组
        按照字段分组,表示此字段相同的数据会被放到一个集合中
        分组后，只能查询出相同的数据列，对于有差异的数据列，无法显示在结果集中
        可以对分组后的数据进行统计，做集合运算
        select 列1，列2，聚合... from 表名 group by 列1，列2... ; 
        select 列1，列2，聚合... from 表名 group by 列1，列2...  having 列1，列2...;
        
        select gender,count(*) from student group by gender;
        select name,gender,count(*) from student group by gender,age;
        select gender,count(*) from student group by gender having gender=1;
        
        where与having的区别:
        where是对from后面指定的表进行筛选，属于对原始数据筛选
        having是对group by 的结果进行筛选
    6、排序
        select * from 表名 order by 列1 asc/desc,列2 asc/desc,...;    
        a、将数据按照列1进行排序，如果某些列1的值相同，则按照列2进行排序
        b、默认按照从小到大的顺序排序
        c、asc升序
        d、desc降序
        
        select * from student where isDelete=0 order by age;
        select * from student where isDelete=0 order by age desc;
        select * from student where isDelete=0 order by age desc,id desc;        
    7、分页
        select * from 表名 limit start,count;
        start索引从0开始,看count条数据
        
        select * from student limit 0,3;
        select * from student limit 3,3;

六、关联
        建表语句：
        1、create table class(id int auto_increment primary key,
                              name varchar(20) not null, stuNum int not null);
        2、create table students(id int auto_increment primary key,
                                 name varchar(20) not null,
                                 gender bit default 1,
                                 classid  int not null,
                                 foreign key(classid) references class(id));
                                 
        插入一些数据：
        insert into class values(0,"python01",55),(0,"python02",50),(0,"python03",60),
                                (0,"python04",40);
        insert into students values(0,"tom",1,1);
        insert into students values(0,"jack",1,2);

        关联查询：        
        select students.name,class.name from class inner join students on class.id=students.classid;

        select students.name,class.name from class left join students on class.id=students.classid;

        select students.name,class.name from class right join students on class.id=students.classid;

        分类：
        1、表A inner join 表B  on  A.列名=B.列名;
            表A与表B匹配的行会出现在结果集中
        2、表A left join 表B   on  A.列名=B.列名;
            表A与表B匹配的行会出现在结果集中，外加表A中独有的数据，未对应的数据使用null填充
        3、表A right join 表B   on  A.列名=B.列名;
            表A与表B匹配的行会出现在结果集中，外加表B中独有的数据，未对应的数据使用null填充
"""

# MySQL与Python交互
# 1.连接数据库
# 参数1:mysql服务所在主机的IP
# 参数2:用户名
# 参数3:密码
# 参数4:要连接的数据库名
# db = pymysql.connect("localhost", "root", "password", "test")
"""如果不能使用IP，打开navicat,找到mysql数据库，打开user表,将user为root的Host改为%
然后以管理员身份打开cmd(c-windows-system32-cmd 右键 管理员) 重启mysql(net stop mysql80)
(net start mysql80)"""
db = pymysql.connect("192.168.0.175", "root", "password", "test")
# 创建一个cursor对象
cursor = db.cursor()

sql = "select version()"

# 执行sql语句
cursor.execute(sql)

# 获取返回的信息
data = cursor.fetchone()
print(data)

# 断开
cursor.close()
db.close()

# 2.创建数据库表、插入数据、更新数据
db2 = pymysql.connect("localhost", "root", "password", "test")
cursor2 = db2.cursor()

# 检查表是否存在，如果存在则删除
cursor2.execute("drop table if exists bandcard")
# 建表
sql = 'create table bandcard(id int auto_increment primary key, money int not null)'
cursor2.execute(sql)

sql = 'insert into bandcard values(0,100)'
try:
    cursor2.execute(sql)
    db2.commit()  # 提交事务，execute只是相当于写到缓存里，commit才真正写入数据库
except:
    # 如果提交失败，回滚到上一次数据
    db2.rollback()

sql = 'update bandcard set money=10000 where id=1'
try:
    cursor2.execute(sql)
    db2.commit()
except:
    db2.rollback()
cursor2.close()
db2.close()

# 3、数据库查询数据
"""
fetchone()
功能：获取下一个查询结果集，结果集是一个对象

fetchall()
功能：接收全部的返回行

rowcount:是一个只读属性，返回execute()方法影响的行数
"""
db3 = pymysql.connect("localhost", "root", "password", "test")
cursor3 = db3.cursor()
sql = 'insert into bandcard values(0,300),(0,400),(0,500),(0,600),(0,700)'
try:
    cursor3.execute(sql)
    db3.commit()
except:
    db3.rollback()

sql = 'select * from bandcard where money>400'
cursor3.execute(sql)  # 查询不用commit()
reslist = cursor3.fetchall()
for row in reslist:
    print("%d---%d" % (row[0], row[1]))

cursor3.close()
db3.close()

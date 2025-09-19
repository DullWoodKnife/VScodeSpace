# MongoDB

## 安装MongoDB

官方网站：https://www.mongodb.com/try/download/community-kubernetes-operator2

### 软件安装

权限不足：https://www.javaclub.cn/database/56541.html

**step1:**

**打开安装包直接点击Next**

![](.\image\安装1.png)

**step2：继续点击Next**

![](.\image\安装2.png)

**step3：点击自定义安装**

![](.\image\安装3.png)

**step4：选择好安装路径，点击Next**

![](.\image\安装4.png)

**step5：点击Next**

![](.\image\安装5.png)

**step6：取消可视化界面勾线，直接点击Next安装**

![](.\image\安装6.png)

### 软件配置

**step1：配置环境变量，找到MongoDB安装路径下的bin目录**

![](.\image\bin.png)



**step2：计算机--右击--属性--高级系统设置--环境变量--系统变量--path--新建，将bin目录复制进去即可**

![](.\image\环境变量.png)

补充：进到data目录里面，新建两个文件夹，一个是db，一个是log

**step3：以管理员打开cmd，输入mongod -dbpath "F:\MongoDB\data\db" -logpath "F:\MongoDB\data\log\mongo.log"**

![](.\image\配置.png)



**step4:重新打开一个cmd窗口，输入mongo来启动MongoDB shell 端**

![](.\image\MongoDBshell.png)



## MongoDB操作



### 数据库相关操作

创建\删除数据库

~~~python
use database_name
# 如果数据库不存在，则创建数据库，否则切换到指定数据库。

db.dropDatabase()
# 删除数据库之前，先进入数据库，之后执行
# 删除当前数据库
~~~



实例：

~~~
>use data_name
switched to db data_name
>db
data_name
~~~

如果你想查看所有数据库，可以使用 **show dbs** 命令：

~~~
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
~~~

可以看到，我们刚创建的数据库 data_name并不在数据库的列表中， 要显示它，我们需要向 data_name 数据库插入一些数据。



### 增删改查操作

MongoDB中的一张表被称为一个集合

#### 插入数据

* 语法：

~~~python
# db.集合名.insert({})  数据格式为json
db.demo.insert({name:"坤哥"})
# { "_id" : ObjectId("63465fb77811f81334940270"), "name" : "坤哥" }
~~~



在数据库demo中，我们可以先通过 **show collections** 命令查看已存在的集合：

```python
use demo
# switched to db demo
show collections
# func1
# func2
```

#### 查询数据

* 语法：

~~~python
# 查找所有
db.集合名.find()

# 条件查询
db.集合名.find({name:"坤哥"})
~~~



#### 修改数据

~~~python
db.集合名.insert({name:"李四",sex:"男",love:"篮球"})
# 将李四修改为坤哥
db.集合名.update({name:"李四"},{$set:{name:"阿坤"}})
~~~

#### 删除数据

~~~
db.集合名.remove({name:"张三"})
~~~

* 删除集合

~~~python
db.集合名.drop()
true
~~~

## MongoDB与python

* 链接数据库pymongo   pip install pymongo

~~~python
import pymongo


class MongoDB(object):
    def __init__(self):
        # 建立连接
        self.client = pymongo.MongoClient(host="localhost", port=27017)
        # 指定数据库
        self.db = self.client["demo"]
	
    # 插入一条数据
    def add_one_data(self):
        result = self.db.func.insert_one({"name": "张三", "age": 18, "sex": "男"})
        print(result)
	#插入多条数据
    def add_many_data(self, data):
        result = self.db.func1.insert_many(data)
        print(result)
	
    # 查看数据
    def get_one_data(self):
        result = self.db.func1.find_one()
        print(result)
	# 查看多个数据
    def get_many_data(self):
        result = self.db.func1.find({"name":"李四"})
        for data in result:
            print(data)


if __name__ == '__main__':
    mdb = MongoDB()
    data = [
        {"name": "张三", "age": 58, "sex": "男", "love": "唱歌"},
        {"name": "李四", "age": 48, "sex": "男", "love": "跳舞"},
        {"name": "王五", "age": 38, "sex": "女", "love": "rap"},
        {"name": "赵六", "age": 28, "sex": "女", "love": "篮球"}
    ]
    mdb.get_many_data()
~~~

# 作业

将链家前三页数据抓取，并存储到MongoDB


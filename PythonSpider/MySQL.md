# MySQL

MySQL 是一个关系型数据库管理系统，由瑞典 MySQL AB 公司开发，目前属于 Oracle 公司。MySQL 是一种关联数据库管理系统，关联数据库将数据保存在不同的表中，而不是将所有数据放在一个大仓库内，这样就增加了速度并提高了灵活性。

## 安装MySQL

* 下载地址：https://dev.mysql.com/downloads/mysql/

![](.\image\下载MySQL.png)

> **下载完后，我们将 zip 包解压到相应的目录，这里我将解压后的文件夹放在 F:\MySQL\mysql-8.0.11 下。**
>
> **接下来我们需要配置下 MySQL 的配置文件**



* 打开刚刚解压的文件夹F:\MySQL\mysql-8.0.11 ，在该文件夹下创建 **my.ini** 配置文件，编辑 **my.ini** 配置以下基本信息

~~~python
[client]
# 设置mysql客户端默认字符集
default-character-set=utf8
 
[mysqld]
# 设置3306端口
port = 3306
# 设置mysql的安装目录
basedir=F:\MySQL\mysql-8.0.11
# 设置 mysql数据库的数据的存放目录，MySQL 8+ 不需要以下配置，系统自己生成即可，否则有可能报错
# datadir=F:\MySQL\\sqldata
# 允许最大连接数
max_connections=20
# 服务端使用的字符集默认为8比特编码的latin1字符集
character-set-server=utf8
# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB
~~~

**接下来我们来启动下 MySQL 数据库：**

* 以**管理员**身份打开 cmd 命令行工具，切换目录：

![](.\image\进入MySQL.png)

* **初始化数据库**

~~~
mysqld --initialize --console
~~~

> **执行完成后，会输出 root 用户的初始默认密码，如：**

~~~python
...
2018-04-20T02:35:05.464644Z 5 [Note] [MY-010454] [Server] A temporary password is generated for root@localhost: APWCY5ws&hjQ
...
~~~

> APWCY5ws&hjQ 就是初始密码，后续登录需要用到，你也可以在登陆后修改密码。
>
> mysqladmin -u用户名 -p旧密码 password 新密码



* 安装数据库

~~~
mysqld install
~~~

> 安装结束后启动服务即可

* 启动服务

~~~
net start mysql
~~~

### 登陆MySQL

当 MySQL 服务已经运行时, CD到bin目录，打开命令提示符, 输入以下格式的命名:

~~~
mysql -h 主机名 -u 用户名 -p

~~~

- -h : 指定客户端所要登录的 MySQL 主机名, 登录本机(localhost 或 127.0.0.1)该参数可以省略;
- -u : 登录的用户名;
- -p : 告诉服务器将会使用一个密码来登录, 如果所要登录的用户名密码为空, 可以忽略此选项。



## 数据库的操作



### 查看数据库

**语法：**

~~~mysql
show databases;
~~~



### 创建数据库

**语法：**

~~~mysql
create database 库名；
~~~



### 删除数据库

**语法：**

~~~mysql
drop database 库名；
~~~



### 选择数据库

语法：

~~~mysql
use 库名；
~~~

------



## 数据表的操作



### 创建数据表

创建MySQL数据表需要以下信息：

- 表名
- 表字段名
- 定义每个表字段类型

~~~mysql
create table 表名(
    ID int auto_increment,
	表字段名 类型,
    表字段名 类型,
    表字段名 varchar(),
	)DEFAULT CHARSET=utf8;
~~~

> MySQL 中定义数据字段的类型对你数据库的优化是非常重要的。
>
> MySQL 支持多种类型，大致可以分为三类：数值、日期/时间和字符串(字符)类型



### 删除数据\表

语法：

~~~mysql
drop table 表名;
# 删除表
~~~

* **清空表数据**

~~~mysql
truncate table 表名；
~~~

> **truncate只会清除表数据，drop不光清除表数据还要删除表结构。**

~~~mysql
delete from 表名 where id='1';
delete from 表名;
~~~

> **如果不加where条件，则是删除表所有的数据**



### 插入数据 

语法：

~~~mysql
insert into 表名(name1,name2,name3) values (data1,data2,data3)
~~~

> 如果数据是字符型，必须使用单引号或者双引号，如："data"



### 查询数据

语法：

~~~mysql
select * from 表名；
# 查看表中的所有数据

select name from 表名;
# 查看指定数据

desc 表名：
# 查看表结构

show tables; 
# 查看表 - 选择数据库
~~~





## 数据库的链接

* **python与MySQL交互**

* **安装第三方模块--pymysql**		pip install pymysql

### pycharm链接MySQL

~~~python
import pymysql

# 创建链接
db = pymysql.Connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="xh1234",
    db="spider_data"
)
# 创建游标，用于传递python给MySQL的命令和MySQL返回的内容
cursor = db.cursor()
~~~



### 数据库插入操作

~~~python
# -*- coding:utf-8 -*-
import pymysql

db = pymysql.Connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="xh1234",
    db="text"
)
# 创建游标，用于传递python给MySQL的命令和MySQL返回的内容
cursor = db.cursor()
# SQL插入语句
sql = "insert into student(name, age, sex) values ('李四',20,'男')"
# 执行SQL语句
cursor.execute(sql)
# 提交到数据库执行
db.commit()
~~~



# 作业

将爬虫获取的数据成功存储到mysql


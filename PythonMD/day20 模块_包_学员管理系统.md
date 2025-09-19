<a name="Zxvsv"></a>
# 模块
<a name="RDCXZ"></a>
### random模块
random模块是随机模块 
<a name="s4puE"></a>
#### random模块常用方法
**random.random()        -->** 随机生成[0,1)的数<br />**random.randint()        -->**  随机生成整数[]<br />**random.choice()         --> ** 随机在序列取元素<br />**random.shuffle()        --> ** 打乱传入的容器内部顺序并返回<br />**random.sample()**       ** --> ** 随机取样<br />**random.randrange()   -->**  随机取整数[)
```python
import random

# print(random.random())

# print(random.randint(1, 100))  # 随机生成1-100之间的随机数 范围 [1<=num<=100]

# li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(random.choice(seq=li))  # seq是默认值参数 可以写 可以不写

# li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(li)
# random.shuffle(li)  # 打乱的是列表本身
# print(li)

# li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(random.sample(li, 4))  # 随机取样 要有参数 要知道你取几个

print(random.randrange(1, 10))  # 在范围内随机取整数


# 使用随机数实现简单的验证码  验证码格式为6位数字
import random

print(random.randint(100000, 999999))


def fun():
    for i in range(6):
        print(random.randint(0, 9), end="")


fun()
```
<a name="hze0B"></a>
### Json模块
JSON是一种使用广泛的轻量数据格式. Python标准库中的json模块提供了JSON数据的处理功能。  <br />由于JSON与python中的字典格式非常像。所以python中的json模块也相当于是用来使json与字典做转换。但是要注意的是，json中的数据必须使用双引号包裹。
<a name="6ETDw"></a>
#### Json模块常用方法
**json.loads()            --> ** json转为字典(适用于语句)<br />**json.dumps()         --> ** 字典转为json(适用于语句)<br />**json.load()             --> ** json转为字典(适用于文件)<br />**json.dump()           -->**  字典转为json(适用于文件)
```python
# import json
#
# a = "python"
# print(a, type(a))
# b = {"city": "hunan"}
# print(b, type(b))
# c = '{"city": "hunan"}'
# print(c, type(c))
#
# # dict-->str
# # 第一种方法
# res = str(b)
# print(res, type(res))  # {'name': '张三'} <class 'str'>
# # 第二种方法
# res = json.dumps(b)
# print(res, type(res))  # {"city": "hunan"} <class 'str'>
#
# # str -->dict
# data = '{"age":18}'
# print(data, type(data))
# # 第一种方法  报错
# # res = dict(data)   # 报错
# # print(res)
#
# # 第二种方法
# res = json.loads(data)
# print(res, type(res))
#
# # 怎么去拿到18
# print(res["age"])
# print(res.get("age"))


import json

# data = {"name": "yueyue"}
# f = open("data.json", mode="w")
# f.write(data)  # must be str, not dict
# # 写进去
# json.dump(data, f)  # 将字典转换成json文件 然后写入文件

# 读取文件
f = open("data.json", mode="r")
res = f.read()
# print(type(res), res)
# f.seek(0)
# 运行下面之前先把上面的read注释掉  因为指针在最后面了 读取不了了 或者seek到0
j_data = json.load(f)  # 将json对象转换成字典
print(j_data)
print(type(j_data), j_data.get("name"))
```
<a name="MbJPX"></a>
# 包
基于Python模块，我们可以在编写代码的时候，导入许多外部代码来丰富功能。但是，如果Python的模块太多了，就可能造成一定的混乱，那么如何管理呢? 通过Python包的功能来管理。
<a name="ReQgt"></a>
#### 什么是包 
从物理上看，包就是一个文件夹，在该文件夹下包含了一个_ _init _ _.py 文件，通过这个文件表示一个文件夹是Python的包，而非普通的文件夹，**包的本质依然是模块.**
<a name="G45Fd"></a>
#### 导入包的方法

- import 包名.模块名
- from 包名 import 模块名
- from 包名 import *	——>  模块名.方法名()访问 ，用__all__暴露接口
```python
import mypackage.module1
mypackage.module1.printinfo1()
mypackage.module1.printinfo11()
import mypackage.module2
mypackage.module2.printinfo2()
mypackage.module2.printinfo22()

from mypackage import module1,module2
module1.printinfo1()
module1.printinfo11()
module2.printinfo2()
module2.printinfo22()


# 必须在`_init_.py`文件中添加__all__= [控制允许导入的模块列表]
from mypackage import *
module1.printinfo1()

# 如果想在单个文件下控制导入的函数 同样需要添加__all__
from mypackage.module1 import *
printinfo1()
```
<a name="Xu6b0"></a>
### python包的总结
1.什么是Python的包?<br />包就是一个文件夹，里面可以存放许多Python的模块（代码文件)，通过包，在逻辑上将一批模块归为一类，方便使用。<br />2._ _init_ _.py文件的作用?<br />创建包会默认自动创建的文件，通过这个文件来表示一个文件夹是Python的包，而非普通的文件夹。<br />3._ _all_ _变量的作用?<br />同模块中学习到的是一个作用，控制import*能够导入的内容
<a name="XudhK"></a>
# 面向对象版本学员管理系统
```python
具体看课堂派资料studentmanage包文件
```

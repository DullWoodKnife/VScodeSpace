<a name="b26d4f34"></a>
# 面向对象
<a name="AkBt2"></a>
## 面向对象编程介绍
面向对象编程：Object Oriented Programming，简称OOP，是一种程序设计思想。<br />**需要注意的是**，与之对应的是面向过程编程思想。实际上，能够使用面向对象编程思想实<br />现的程序，也都能通过面向过程完成。只是看哪种思想更适合当前开发需求。
<a name="lIHfm"></a>
## 面向过程与面向对象区别
**面向过程**：根据业务逻辑从上到下写代码  <br />**面向对象**：将数据与函数绑定到一起，进行封装。减少重复代码的重写过程 
<a name="7fe97680"></a>
## 类和对象
<a name="4509bd5c"></a>
### 理解类和对象
<a name="fad060bd"></a>
#### 类
类是抽象的概念，仅仅是模板。用来描述具有相同属性和方法的对象的集合。比如："人"是一个类。
<a name="b1449413"></a>
#### 对象
某一个具体事物的存在 ,在现实世界中可以是看得见摸得着的。 比如："胡歌"就是一个对象。
> 注意：开发中，先有类，再有对象。

<a name="Kc2nD"></a>
#### 类与对象的关系
那么实际上，我们可以进行**对象归类。**<br />比如：分析班级同学公有特征归类。<br />![](https://cdn.nlark.com/yuque/0/2020/svg/704747/1584000149163-1458cf49-125e-4127-88db-9f79bc38ecd6.svg)<br />那么，我们就可以将学生公有的特征进行归类。而建立一个学生类。<br />**如下：**<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/704747/1584000575708-9048e383-aafd-4065-adb5-3cdb343ed374.png#averageHue=%23f6f6f6&height=191&id=tPYZT&name=image.png&originHeight=228&originWidth=444&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6895&status=done&style=none&title=&width=371)<br />**练习：**<br />下面哪些是类，哪些是对象？

- 汽车 
- 奔驰大G550
- 水果 
- 红富士苹果
<a name="mBl7u"></a>
#### 类的构成
类由3个部分构成 

- 类的名称：类名
- 类的属性：一组数据
- 类的方法：允许对类进行操作的方法

注意：类名通常采用驼峰式命名方式，尽量让字面意思体现出类的作用。 
<a name="BYmDi"></a>
#### 类的定义
Python使用class关键字来定义类，其基本结构如下：
```python
class 类名:
    pass
```
<a name="l0cVf"></a>
#### 创建对象
python中，可以根据已经定义的类去创建出一个个对象<br />创建对象的格式为:
```python
对象名 = 类名()
```
<br />**练习**<br />●创建类：学生类<br />●创建对象：张三<br />●在类中定义方法输出：张三学习Python<br />![](https://cdn.nlark.com/yuque/0/2020/png/704747/1584002401454-3e917ae4-a2b3-402c-82df-4c78b3aa9039.png#averageHue=%23f3f3f3&from=url&id=gQuYp&originHeight=197&originWidth=387&originalType=binary&ratio=1.100000023841858&rotation=0&showTitle=false&status=done&style=none&title=)<br />**总结**
```python
# 定义
class 类名：
    def 方法名(self,参数):  # 类中函数：称为方法
        pass
        
# 执行
s = 类名()         # 创建对象(实例) 这个过程就是实例化
s.方法名(参数)     # 调用类中方法
```
<a name="ZEjan"></a>
#### self参数
在类当中定义方法时，会发现系统帮我们自动创建了self参数，并且在调用对象的该方法时，也无需传入self参数。那这个self是什么？<br />实际上，我们需要明确self的两个概念

- self本身是**形参**
- self就是**当前对象本身**

**练习**

- 定义类为：学生类
- 创建对象：李四
- 在类中定义方法：打印李四信息
```python
class Student(object):

    def info(self):
        print(ls.name,ls.age)

ls = Student()
ls.name = "李四"
ls.age = 18
ls.info()
```
那么实际上，在这个过程当中，对象将自身信息在类的外部定义赋值，封装到了类的内部。<br />如下图：<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/704747/1584003481911-64a270d3-e38e-42e0-aafe-821710af4a44.png#averageHue=%23f6f6f6&height=174&id=F51Jf&name=image.png&originHeight=204&originWidth=423&originalType=binary&ratio=1&rotation=0&showTitle=false&size=8102&status=done&style=none&title=&width=361)<br />当我再想创建一个对象，并且打印出对象信息时，发现如果这样做不灵活。所以优化如下：
```python
class Student(object):

    def info(self):
        print(self.name,self.age)

ls = Student()
ls.name = "李四"
ls.age = 18
ls.info()

ww = Student()
ww.name = "王五"
ww.age = 20
ww.info()
```
但是这样仍然有缺陷，大家会发现，用户信息暴露在类的外部。
<a name="f3e3883f"></a>
## 魔术方法
在Python的类中，以两个下划线开头、两个下划线结尾的方法，如常见的 ：<br />__init__、__str__、__del__等，就被称为「魔术方法」（Magic methods）。**之所以**<br />**会叫魔法方法原因是这些方法都是到达某个条件自动触发 无需调用**，如果希望根据自<br />己的程序定制特殊功能的类，那么就需要对这些方法进行重写。使用这些「魔法方<br />法」，我们可以非常方便地给类添加特殊的功能。
<a name="90eea164"></a>
### **init**()
**__init__() ：初始化对象**
```python
class My_Phone():
    def __init__(self):
        self.width = 10
        self.heigth = 15

    def main(self):
        print(self.width)
        print(self.heigth)

apple = My_Phone()
```
> **init**() ⽅法，在创建⼀个对象时默认被调⽤，不需要⼿动调⽤

> init(self) 中的self参数，不需要开发者传递，python解释器会⾃动把当前的对象引⽤传递过去。

- **带参数的init**

⼀个类可以创建多个对象，如何对不同的对象设置不同的初始化属性呢？<br />传参即可
```python
class My_Phone():
    def __init__(self,width,heigth):
        self.width = width
        self.heigth = heigth

    def apple_phont(self):
        print("苹果手机的宽为：",self.width)
        print("苹果手机的高为：",self.heigth)

    def huawei_phont(self):
        print("华为手机的宽为：",self.width)
        print("华为手机的高为：",self.heigth)

apple = My_Phone(10,20)
apple.apple_phont()
```
<a name="d7fd42a1"></a>
### **str**()
当使⽤print输出对象的时候，默认打印对象的内存地址。如果类定义了 **str** ⽅法，那么就会打印在这个⽅法中 return 的数据。<br />解释类的属性或作用
```python
# -*- coding:utf-8 -*-

class Demo():
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    def __str__(self):
        return f"你这个手机的宽是{self.width},高度是{self.heigth}"

a = Demo(10,20)
print(a)
```
<a name="7084316c"></a>
### **del**()
当删除对象时，python解释器也会默认调⽤ **del**() ⽅法。在对象销毁的时候被调用，当对象不再被使用时，**del**()方法运行：
```python
# -*- coding:utf-8 -*-

class Demo():
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    def __del__(self):
        print("对象已经删除")

a = Demo(10,20)


# del方法
class Demo:
    def __del__(self):  # 当由该类创建的实例对象，被删除或者说在内存中被释放，将会自动触发执行。
        print("被释放了！")


d = Demo()
print("*" * 20)
# del d  # 相当于提前执行了del方法
print("*" * 20)
```
<a name="86a54392"></a>
## 类属性与方法
<a name="2e6975be"></a>
### 类的私有属性
**__private_attrs**：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问
```python
class Demo():
    __num = 0  # 私有属性
    result = 0  # 公开属性

    def count(self):
        self.__num += 1
        self.result += 1
        print(self.__num)

    def getnum(self):
        return self.__num

run = Demo()
run.count()
print(run.result)
# print(run.__num)    # 报错，实例不能访问私有变量
__num = run.getnum()
print(__num)
```
<a name="JsNsn"></a>
### 类的私有方法
```python
class func:
    def fun1(self):
        print("1")

    def __fun2(self):
        print("2")

    def fun3(self):
        return (self.__fun2())


f = func()

f.fun1()
# f.__fun2()
f.fun3()

# 对象._类名__私有属性
print(f._func__fun2)  # 不建议使用
```
<a name="jQ3LE"></a>
### 实例属性
```python
# 实例属性
class Province:
    def __init__(self, country, province):
        self.country = country
        self.province = province

    def print_info(self):
        print(self.country, self.province)  # 通过self去访问  这个要方便很多
        print(zs.country, zs.province)   # 通过每个对象去访问


zs = Province("中国", "湖南")
zs.print_info()

ls = Province("中国", "湖北")
ls.print_info()
```
<a name="g9HEh"></a>
### 实例方法
```python
class Demo:
    def __init__(self):
        self.name = "岳岳"

    # 实例方法  
    def fun1(self):
        print(self.name)


a = Demo()
a.fun1()

```
<a name="9050a76e"></a>
## 综合应用-烤地瓜
需求涉及⼀个事物： 地⽠，故案例涉及⼀个类：地⽠类

- **地⽠的属性**

		--- 被烤的时间<br />		--- 地⽠的状态<br />		--- 添加的调料

- **地⽠的⽅法**

			**被烤**<br />					--- ⽤户根据意愿设定每次烤地⽠的时间<br />					--- 判断地⽠被烤的总时间是在哪个区间，修改地⽠状态<br />			**添加调料**<br />					--- ⽤户根据意愿设定添加的调料<br />					--- 将⽤户添加的调料存储

- **显示对象信息**
<a name="e6cefb85"></a>
### 需求
1、被烤的时间和对应的地⽠状态：<br />		0  -  5分钟 ：	⽣的<br />		5 - 10分钟 ：    半⽣不熟<br />		10-12分钟 ：	烤熟了<br />		超过12分钟：   烤糊了<br />2、添加调料：
<a name="83175ad0"></a>
### 代码实现
```python
# -*- coding:utf-8 -*-

class Test_Potato():
    def __init__(self):
        # 考的时间
        self.cook_time = 0
        # 考的状态
        self.cook_sratic = "生的"
        # 放的调料
        self.cook_seasoning = [] 

    def cook(self, time):
        self.cook_time += time
        if 0 <= self.cook_time < 5:
            self.cook_sratic = "生的"
        if 5 <= self.cook_time < 10:
            self.cook_sratic = "半生半熟"
        if 10 <= self.cook_time <= 12:
            self.cook_sratic = "熟了"
        if self.cook_time > 12:
            self.cook_sratic = "烤糊了"

    def add_seasoning(self,*seasoning):
        self.cook_seasoning.append(seasoning)

    def __str__(self):
        return f"当前地瓜考了--{self.cook_time}--分钟，他的状态是--{self.cook_sratic}--,添加的调料是--{self.cook_seasoning}"



if __name__ == '__main__':
    main = Test_Potato()
    main.cook(11)
    main.add_seasoning("辣椒","花生","孜然")
    print(main)
```


<a name="RSDhO"></a>
# 面向对象三大特性 
<a name="smT0H"></a>
## 概述
Python 是面向对象的语言，也支持面向对象编程的三大特性:继承、封装、多态。
<a name="W36JJ"></a>
## 封装
<a name="U63Ec"></a>
### 什么是封装 
在程序设计中，封装（Encapsulation）是对具体对象的一种抽象，即将某些部分隐藏起来，在程序外部看不到，其含义是其他程序无法调用。<br />要了解封装，离不开“私有化”，就是将类或者是函数中的某些属性限制在某个区域之内，外部无法调用。
<a name="Wt33s"></a>
### 为什么要进行封装？
1、保护隐私（把不想别人知道的东西封装起来）<br />2、隔离复杂度（比如：电视机，我们看见的就是一个黑匣子，其实里面有很多电器元<br />件，对于用户来说，我们不需要清楚里面都有些元件，电视机把那些电器元件封装在黑匣<br />子里，提供给用户的只是个按钮接口，通过按钮就能实现对电视机的操作。）
<a name="MyDCg"></a>
### 封装的两个层面 
封装其实分为两个层面，但无论哪种层面的封装，都要对外界提供好访问你内部隐藏内容的接口（接口可以理解为入口，有了这个入口，使用者无需且不能够直接访问到内部隐藏的细节，只能走接口，并且我们可以在接口的实现上附加更多的处理逻辑，从而严格控制使用者的访问）<br />**第一个层面的封装（什么都不用做）：**创建类和对象会分别创建二者的名称空间，我们只能用类名.或者obj.的方式去访问里面的名字，这本身就是一种封装。<br />**第二个层面的封装：**类中把某些属性和方法隐藏起来(或者说定义成私有的)，只在类的内部使用、外部无法访问，或者留下少量接口（函数）供外部访问。
<a name="xOcTv"></a>
### 封装实例 	
```python
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def __getname(self):
        # print(self.__name)
        print(f'{self.__name}')

    def printinfo(self):
        print(f'{self.__name},{self.age}')


p = Person('zhangsan', 18)
p.printinfo()
p._Person__getname()
```
<a name="FsJnI"></a>
## 继承
<a name="pUL7J"></a>
### 继承的概念
继承是面向对象程序设计的重要特征，也是实现代码复用的重要手段，如果一个新类继承自一个设计好的类，就直接具备了已有类的特征，就大大降低了工作难度。已有的类，我们称为父类或者基类，新的类，我们称为子类或者派生类。
<a name="afhtE"></a>
### 继承的种类
<a name="dx2Ci"></a>
#### 单继承
单继承指的是子类只继承一个父类 当对象调用方法时，查找顺序先从自身类找，如果自身没找到，则去父类找，父类无，再到父类的父类找，直到object类，若还无，则报错。这也称为 深度优先机制。<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/25414438/1679746283360-aa60c4c2-667d-4ce9-b473-1f748b7e8dec.png#averageHue=%23f5f5f5&clientId=ud846f5a8-4033-4&from=paste&height=217&id=u1c7b0490&name=image.png&originHeight=299&originWidth=335&originalType=binary&ratio=1.375&rotation=0&showTitle=false&size=19909&status=done&style=none&taskId=u14142e92-392f-4408-896e-c506274d606&title=&width=243.63636363636363)
```python
# 单继承
class Grandfather:
    def __init__(self):
        print('Grandfather')

    def sleep(self):
        print("sleep")


class Father(Grandfather):
    def eat(self):
        print("eat")

    def drink(self):
        print("drink")


class Son(Father):
    def study_python(self):
        print("python")


s = Son()
s.study_python()
s.eat()
s.sleep()
```
<a name="BogJ1"></a>
#### 多继承
多继承指的是子类继承了多个父类。并且具有它们的特征。<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/25414438/1679746572579-4c71b8b1-2730-4ae9-ad58-1acb58479c36.png#averageHue=%23f7f7f7&clientId=ud846f5a8-4033-4&from=paste&height=243&id=u904e5a75&name=image.png&originHeight=334&originWidth=554&originalType=binary&ratio=1.375&rotation=0&showTitle=false&size=22559&status=done&style=none&taskId=ud10bb4ba-f48b-4105-9eef-0533f178482&title=&width=402.90909090909093)
```python
"""情景1"""
class Father1:
    def run(self):
        print("father1 run")


class Father2:
    def run(self):
        print("father2 run")


class Son(Father1, Father2):  # 拥有相同方法时，左边优先执行
    pass


s = Son()
s.run()
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/25414438/1679746591737-206ac688-a40f-40ea-88b1-0f9410fb9954.png#averageHue=%23f9f9f9&clientId=ud846f5a8-4033-4&from=paste&height=273&id=u0e1294e2&name=image.png&originHeight=376&originWidth=602&originalType=binary&ratio=1.375&rotation=0&showTitle=false&size=27545&status=done&style=none&taskId=u565f746a-9d80-4374-a5ce-e79e2c925dc&title=&width=437.8181818181818)
```python
"""情景2"""
class Grandfather:
    def sleep(self):
        print("Grandfather sleep")


class Father1(Grandfather):
    def run(self):
        print("father1 run")


class Father2:
    def sleep(self):
        print(" Father2 sleep")


class Son(Father1, Father2):  # 必须要左边的执行完了,才会执行右边的父类
    pass


s = Son()
s.sleep()
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/25414438/1679746605689-45c4cdf5-d4e8-4add-9cff-d029f797262c.png#averageHue=%23f8f8f8&clientId=ud846f5a8-4033-4&from=paste&height=304&id=ue7891c0c&name=image.png&originHeight=418&originWidth=594&originalType=binary&ratio=1.375&rotation=0&showTitle=false&size=23650&status=done&style=none&taskId=u45e7ec9e-2f08-4e1f-bc3f-4fc9bd48d22&title=&width=432)
```python
class Grandfather1:
    def sleep(self):
        print("sleep 12")


class Father1(Grandfather1):
    def run(self):
        print("father1 run")


class Father2(Grandfather1):
    def sleep(self):
        print("sleep 6")


class Son(Father1, Father2):  # 如果同根的话，根是最后才执行的
    pass


s = Son()
s.sleep()
print(Son.__mro__)  # 通过mro方法可以程序执行或者继承顺序的情况

```
<a name="vfT2X"></a>
### 方法的重写  
当子类与父类拥有同名称的方法时，子类对象调用该方法 优先执行自身 的方法。那么实际上就是子类的方法 覆盖 父类的方法，也称为 重写。实际的开发中，遵循开放封闭原则。我们并不会完全的重写父类的方法，而是希望同时实现父类的功能。
```python
class A():
    def __init__(self):
        print('A')

    def test(self):
        print("aaaa")


class B(A):
    def __init__(self):
        print('B')
        # A.__init__(self)
        # super(B, self).__init__()

    def test(self):
        print("bbbb")
        super(B, self).test()
        # A.test(self)


b = B()
b.test()
```
<a name="mcy31"></a>
## 多态 
Python中函数的参数是没有类型限制的，所以多态在python中的体现并不是很严谨。多态的概念是应用于Java和C#这一类强类型语言中，而Python崇尚“鸭子类型”。python是弱语言类型。

- 多态（polymorphism）：指的是一类事物有多种形态，一个抽象类有多个子类（因而多态的概念依赖于继承），不同的子类对象调用相同的方法，产生不同的执行结果，多态可以增加代码的灵活度
<a name="Y4QR0"></a>
#### 实现多态的步骤：
1、定义一个父类（Base），实现某个方法（比如：run）<br />2、定义多个子类，在子类中重写父类的方法（run），每个子类run方法实现不同的功能<br />3、假设我们定义了一个函数，需要一个Base类型的对象的参数，那么调用函数的时候，传入Base类不同的子类对象，那么这个函数就会执行不同的功能，这就是多态的体现。
```python
class Animal(object):
    """动物类"""
    def func(self):
        print('动物发出了声音')


class Cat(Animal):
    """猫类"""
    def func(self):
        print('喵 喵 喵')


class Dog(Animal):
    """狗类"""
    def func(self):
        print('汪 汪 汪 ')

class Hero:
    def func(self):
        print('这个是英雄类的方法，不是动物类的对象')

def work01(Animal):
    Animal.func()


work01(Dog())  # 传入的对象
# 传入不同的对象，产生不同的结果
# 调用灵活 更容易编写出通用的代码
```
<a name="jjkep"></a>
#### 多态的意义：
(1)**在程序运行过程中展现出动态的特性**，在程序编译的时候无法知道调用哪个函数<br />(2)**函数重写必须多态实现**，否则没有意义<br />(3)**多态是面向对象组件化程序设计**的基础特性

**注意点：Python中函数的参数是没有类型限制的，所以多态在python中的体现并不是很严谨。多态的概念是应用于Java和C#这一类强类型语言中，而Python崇尚“鸭子类型”。**
<a name="eEYuF"></a>
## 鸭子类型

- 鸭子类型概念：他并不要求严格的继承体系，关注的不是对象的类型本身，而是它是否具有要调用的方法（行为）
```python
class Duck:
    def quack(self):
        print("嘎嘎嘎嘎。。。。。")

class Bird:
    def quack(self):
        print("bird imitate duck....")

class geese:
    def quack(self):
        print("geese imitate duck....")

def in_the_forest(duck):
    duck.quack()


duck = Duck()
bird = Bird()
geese = geese()
for x in [duck, bird, geese]:
    in_the_forest(x)

```

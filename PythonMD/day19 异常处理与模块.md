# 异常与捕获
## 前言
当检测到⼀个错误时，解释器就无法继续执行了，反而出现了⼀些错误的提示，这就是所谓的"异常"。
python提供了两个非常重要的功能来处理python程序在运行中出现的异常和错误。你可以使用该功能来调试python程序。
## 什么是异常

- **异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行。**
- **一般情况下，在Python无法正常处理程序时就会发生一个异常。**
- **异常是Python对象，表示一个错误。**
- **当Python脚本发生异常时我们需要捕获处理它，否则程序会终止执行。**
## 异常语法
```python
try:
    正常程序执行此块代码
except:
    抛出错误执行此代码块
```
### 异常快速体验
```python
ipt = input("请输入:")
ipt = float(ipt)
print(ipt)
ipt = 1
print(ipt)

try:
    # 正常程序时执行代码块
    ipt = input("请输入:")
    ipt = float(ipt)
    print(ipt)

except:
    # 异常程序时执行代码块
    ipt = 1
    print(ipt)
```
## 异常类型捕获
**仅仅使用以上异常捕获，虽然不会报错终止程序。但是无法记录下具体异常种类。如需记录下具体异常种类，则需要捕获该具体异常。**
### 语法
```python
try:
    pass
except 当前异常对象 as e:  # e = 当前异常对象 
    print(e) 
```
**常见异常类型**

| **异常名称** | **描述** |
| --- | --- |
| **AttributeError** | **对象没有这个属性** |
| **OSError** | **操作系统错误** |
| **ImportError** | **导入模块/对象失败** |
| **IndexError** | **序列中没有此索引(index)** |
| **KeyError** | **没有这个键** |
| **NameError** | **未声明/初始化对象 (没有属性)** |
| **SyntaxError** | **Python 语法错误** |
| **TypeError** | **对类型无效的操作** |
| **ValueError** | **传入无效的参数** |
| **Warning** | **警告的基类** |

### 练习
```python
li = [1, 2, 3, 4]
print(li[4])  # IndexError: list index out of range

a = 1
b = 0
c = a / b
print(c)  # ZeroDivisionError: division by zero

print(int("a"))  # ValueError: invalid literal for int() with base 10: 'a'

try:
    li = [1, 2, 3, 4]
    li[4]  # 报错  我想把异常信息打印出来
except IndexError as e:  # e = IndexError
    print(e)
    print("hello")

需要注意的是，该捕获方式仅能捕获IndexError这一类异常。那么实际上，这种细分的异常种类有很多，
可以通过其共同父类Exception捕获输出。
except Exception as e:
    # 类的对象实例调用__class__属性时会指向该实例对应的类，而后再调用 __name__ 就会输出该实例对应的类的类名
    print(e.__class__.__name__,":",e)

```
## try-except-else

- 如果**抛出异常**执行**except**内部代码
- 如果**程序正常**执行**else**内部代码
```python
try:
    li = [1, 2, 3, 4]
    li[4]  # 报错  我想把异常信息打印出来
# except IndexError as e:  # e = IndexError
#     print(e)
#     print("hello")
except Exception as e:
    # 类的对象实例调用__class__属性时会指向该实例对应的类，而后再调用 __name__ 就会输出该实例对应的类的类名
    print(e.__class__.__name__,":",e)
else:
    print('123')
```
## try-except-finally
不管程序有无发生异常，都将执行**finally**内部代码。
```python
try:
    li = [1, 2, 3, 4]
    # li[4]  # 报错  我想把异常信息打印出来
# except IndexError as e:  # e = IndexError
#     print(e)
#     print("hello")
except Exception as e:
    # 类的对象实例调用__class__属性时会指向该实例对应的类，而后再调用 __name__ 就会输出该实例对应的类的类名
    print(e.__class__.__name__,":",e)
else:
    print('123')

finally:
    print('我最NB')

```
## 主动触发异常
在实际开发中，在程序不满足某条件时，通常会主动抛出异常。
### 语法
```python
raise Exception()
```
### 实例
判断煎饼熟了没，当烹饪时间小于5时，则主动触发没熟异常；否则熟了。
```python
def test(level):
    if level<5:
        raise Exception("没熟没熟")


try:
    test(4)
except Exception as e:
    print(e)
else:
    print("熟了 请吃") 
```
## 自定义异常 
当需要自定义满足一些规则时，就可以自定义异常。自定义异常通过创建一个新的异常
类，自定义名字与内容，并且需要继承Exception类实现。
```python
# 判断密码长度  如果密码长度小于6 主动触发异常 并抛出异常信息(打印提示)
class ShortInputError(Exception):
    # 初始化方法
    def __init__(self, lenght, min_lenght):
        self.lenght = lenght
        self.min_lenght = min_lenght

    def __str__(self):
        return f"你输入的密码长度为{self.lenght},不能低于{self.min_lenght}"


def fun():
    try:
        password = input("请输入你的密码:")
        if len(password) < 6:
            raise ShortInputError(len(password), 6)  # 主动触发异常  并返回提示信息
    except Exception as e:
        print(e)
    else:
        print("密码已正确输入!")


fun()
```
## 断言 
assert断言用于判断一个表达式，当表达式条件为False时触发断言异常AssertionError。
注意，断言用于强制用户服从，可捕获，但是一般不捕获。
### 语法
```python
assert 断言
```
### 示例
```python
print("*" * 20)
if  2 == 2:
    raise AssertionError
print("*" * 20)


print("*" * 20)
if  2 == 2:
    try:
        raise AssertionError
    except Exception as e:
        print(e.__class__.__name__)
print("*" * 20)
```
# 模块 
## 模块介绍 
模块是一个包含所有你定义的函数和变量的文件，其扩展名为.py。模块可以被其它程序引入，以使用 该模块中的函数等功能。这也是使用python标准库的方法。
## 导入模块的方式

- import 模块名
- from 模块名 import 功能名
- from 模块名 import *
- import 模块名 as 别名
- from 模块名 import 功能名 as 别名
## 常用内置模块
### time模块
time模块是与时间相关的模块 
#### time模块常用方法
**time.sleep()             --> **延迟执行时间
**time.time()              --> **秒时间戳
**time.localtime()      --> **本地时间
**time.strftime()        --> **接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定。
**datetime**也是与时间相关的模块
**datetime.datetime.now() --> **输出当前时间
```python
import time

print(111111111)
time.sleep(1)
print(222222222)

print(time.time())  # 1644672521.4064693  秒时间戳  从1970年的凌晨到现在

print(time.localtime())  # 本地的时间
# tm_wday=2, 一周的第几天
# tm_yday=47,一年的第几日
# tm_isdst=0  夏令时

print(time.strftime("%Y/%m/%d  %H:%M:%S", time.localtime()))

import datetime

print(datetime.datetime.now())
```
### random模块
random模块是随机模块 
#### random模块常用方法
**random.random()        -->** 随机生成[0,1)的数
**random.randint()        -->**  随机生成整数[]
**random.choice()         --> ** 随机在序列取元素
**random.shuffle()        --> ** 打乱传入的容器内部顺序并返回
**random.sample()**       ** --> ** 随机取样
**random.randrange()   -->**  随机取整数[)
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


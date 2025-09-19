<a name="qovR3"></a>
### 函数的作用域
作用域又可以被称为命名空间，指变量起作用的范围。Python变量作用域可以分为四种，分别为局部作用域、嵌套作用域、全局作用域、内置作用域。

| 作用域 | 英文 |
| --- | --- |
| 局部作用域 | Local |
| 嵌套作用域 | Enclosing |
| 全局作用域 | Global |
| 内置作用域 | Buiit-in |

<a name="XspSe"></a>
### 变量作用域
一个程序的所有的变量并不是在哪个位置都可以访问的。访问权限决定于这个变量是在哪里赋值的。<br />变量的作用域决定了在哪一部分程序你可以访问哪个特定的变量名称。两种最基本的变量作用域如下：

- 全局变量
- 局部变量
<a name="YLybU"></a>
### 全局变量和局部变量
定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。<br />局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在<br />函数内声明的变量名称都将被加入到作用域中。如下实例：
```python
x = 2
def func(x):
    x = 3 
    print(x)
func()
print x
来猜一猜他的运行结果
```
当我们在代码里使用变量时，Python创建对象，改变对象或查找对象都是在一个所谓**命名空间**下进行的(一个保存变量名的地方)。<br />而函数除了打包代码之外，还定义了一个新的变量空间，一个函数所有的变量，都与函数的命名空间相关联：

- def 内定义的变量名能够被 def内的代码使用，不能在函数外部引用这样的变量名
- def之中的变量名与def之外的变量名并不冲突

也就是说：

- 如果一个变量在def内被赋值，它就被定义在这个函数之内
- 如果在def之外赋值，它就是整个文件全局的

回到最开始的问题 
```python
x = 2
def func(x):
    x = 3 
尽管这两个变量名都是x，但是他们作用域(命名空间)可以把他们区别开。
作用域(命名空间)有助于防止程序之间变量名的冲突，而且，有助于函数成为更加独立的单元。
在Python中，函数定义了一个函数本地内的作用域，
而像x = 2这样赋值语句定义了一个全局作用域(模块级别的变量，使用范围仅限于单个文件)。
而像x = 3这样赋值语句定义了一个局部作用域(范围仅限于函数内部)。
```
<a name="Dy7dA"></a>
### 函数中修改不了全局作用域的变量如需修改，加global关键字，声明变量为全局变量
```python
y = 10
def func():
    # global y
    y = 5
    print('y1 =', y)

func()
print('y2 =', y)
```
<a name="eNjZg"></a>
### E(enclosing)：嵌套的父级函数的局部作用域
```python
# E(enclosing)：嵌套的父级函数的局部作用域
def mytest1():
    b = 6
    def mytest2():
        nonlocal b  # nonlocal 关键字用于在嵌套函数内部使用变量
        b = 7  # 重新开辟了内存空间  注释掉直接打印b
        print(b, id(b))
    mytest2()
    print(b, id(b))

mytest1()
```
<a name="IMHCE"></a>
### built-in 内建作用域
内建作用域是特质python api内置的一些操作，例如 len 、max等函数，无需声明就可使用。
```python
x = max(1, 6)  # max为系统变量，它的作用域为python的所有模块
y = 1  # y为全局变量，它的作用域为当前模块

def outer():
    i = 3    # i的作用域为当前函数，包括嵌套函数   
    def inner():
        count = 2   # count为局部变量，作用域只在当前函数有效
```
<a name="EufdZ"></a>
### 函数作用域的优先级
![image.png](https://cdn.nlark.com/yuque/0/2023/png/25414438/1678515742838-9911daa5-416d-41f0-ab4c-21b222b5f6af.png#averageHue=%23f3f3f3&clientId=u0f4e6f1e-76af-4&from=paste&height=263&id=zSuEF&name=image.png&originHeight=411&originWidth=1143&originalType=binary&ratio=1.5625&rotation=0&showTitle=false&size=63525&status=done&style=none&taskId=u2096aa2a-8a05-4fe1-a70d-d67ad6be287&title=&width=731.52)
<a name="nXHhl"></a>
### 高阶函数 
<a name="Wqhpe"></a>
#### 什么是高阶函数？
高阶函数：一个函数可以作为参数传给另外一个函数，或者一个函数的返回值为另外一个函数（若返回值为该函数本身，则为递归），满足其一则为高阶函数。
<a name="P8Q9F"></a>
#### 一个函数的函数名作为参数传给另外一个函数
```python
def func():
    print("定义一个普通函数")

def high_level(func):
    print("定义一个高阶函数")
    # 在函数内部，通过传入的函数参数调用
    func()
high_level(func)
```
<a name="IL9LG"></a>
#### 一个函数返回值（return）为另外一个函数（返回为自己，则为递归）
```python
def func():
    print("定义一个普通函数")

def high_level(func):
    print("定义一个高阶函数")
    return func
    #  return func() 这个是直接返回函数调用，递归函数就是如此
res = high_level(func)
# 高阶函数返回函数之后在调用func函数
res()
```
<a name="cbmch"></a>
#### 内置高阶函数 
<a name="PGSRF"></a>
##### map()函数
map函数接收的是两个参数，一个函数，一个序列，其功能是将序列中的值处理再依次返回至列表内。其返回值为一个迭代器对象--》例如：<map object at 0x00000214EEF40BA8>。其用法如图：<br />![](https://cdn.nlark.com/yuque/0/2023/png/25414438/1678520286033-0e885363-f1d1-44a3-8826-d3fcd6fb21e0.png#averageHue=%23fbf9f9&clientId=u201da5c1-a1a2-4&from=paste&id=u9bf5bc32&originHeight=289&originWidth=988&originalType=url&ratio=1.5625&rotation=0&showTitle=false&status=done&style=none&taskId=ue8707008-7472-4cba-93dd-76e63e9bce4&title=)
```python
lis = [1, 2, 3, 4, 5]
def square(x):
    return x ** 2
print(map(square,lis ), type(map(square, lis)))
res = map(square, lis)
for i in res:
    print(i)
print(list(map(square, lis)))
```
<a name="eotY8"></a>
##### filter()函数
 	filter函数也是接收一个函数和一个序列的高阶函数，其主要功能是过滤。其返回值也是迭代器对象，例如：<filter object at 0x000002042D25EA90>。
```python
# 在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1

print(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
```
<a name="PuQc8"></a>
##### reduce()函数
reduce函数也是一个参数为函数，一个为可迭代对象的高阶函数，其返回值为一个值而不是迭代器对象，故其常用与叠加、叠乘等，图示例如下：<br />![](https://cdn.nlark.com/yuque/0/2023/png/25414438/1678521183150-20579e25-cd87-4539-a5b6-d9352dfd0818.png#averageHue=%23fdfbfb&clientId=u201da5c1-a1a2-4&from=paste&id=uc0796309&originHeight=318&originWidth=878&originalType=url&ratio=1.5625&rotation=0&showTitle=false&status=done&style=none&taskId=uae5a4abf-5f85-4ea5-8a82-35312c18b40&title=)
```python
from functools import reduce
def fn(x, y):
    return x + y

res = reduce(fn, [1, 3, 5, 7, 9])
print(res)
```

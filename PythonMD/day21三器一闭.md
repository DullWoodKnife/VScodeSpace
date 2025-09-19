<a name="KZ9Fk"></a>
# 迭代器 
<a name="OoLKG"></a>
## 1、什么是迭代
迭代是访问集合元素的一种方式。对list、tuple、str等类型的数据使用for...in...的循环语法从其中依次拿到数据进行使用，我们把这样的过程称为遍历，也叫迭代。
<a name="tIr2w"></a>
## 2、什么是可迭代对象
只要是可以通过for...in…的形式进行遍历的，那么这个数据类型就是可以迭代的。
<a name="w2jXs"></a>
## 3、怎么判断数据是否可以迭代 
python之中的内置函数isinstance()就是用来判断一个对象是否为指定数据类型的，如果是的话就会返回True值，反之则是返回False。但是在python中是没有这个可迭代对象这个数据类型的，不过可以通过导入模块中的类来实现。
```python
from collections.abc import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance((1,), Iterable))
print(isinstance(set(),Iterable))
print(isinstance('abc', Iterable))
print(isinstance(100, Iterable))
print(isinstance(range(1,10), Iterable))


```
<a name="FMklM"></a>
## 4、什么是迭代器
**迭代是python中访问集合元素的一种非常强大的一种方式。迭代器是一个可以记住遍历位置的对象，迭代器对象从第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。因此不会像列表那样一次性全部生成，而是可以等到用的时候才生成，因此节省了大量的内存资源。迭代器有两个方法：iter()和next()方法。**
<a name="GYDr0"></a>
## 5、迭代器的本质 
我们可以通过iter()函数获取这些可迭代对象的迭代器。然后我们可以对获取到的迭代器不断使用next()函数来获取下一条数据。 
<a name="eI8et"></a>
## 6、使用迭代器取数据
```python
from collections.abc import Iterator

nums = [1, 2, 3] # 可迭代对象
nums = iter(nums)  # 了迭代器
print("nums", isinstance(nums, Iterator))  # 判断是否是迭代器
# 取出迭代器的数据
num1 = next(nums)
print(num1)
num1 = next(nums)
print(num1)
num1 = next(nums)
print(num1)


```
注意: 若迭代的次数超过了可迭代对象的长度， 就会报StopIteration异常
<a name="lU7l6"></a>
## 7、自定义迭代器
使用__iter__和__next__方法自定义迭代器<br />只要在类中，定义__iter__方法，那么这个类创建出来的对象一定是可迭代对象<br />如果类中实现了__iter__方法和__next__方法的对象，就是迭代器。<br />当我们调用iter()函数提取一个可迭代对象的 迭代器时，实际上会自动调用这个对象的__iter__方法，并且这个方法返回迭代器。<br />实例
```python
from collections.abc import Iterator,Iterable
class MyNumbers:
  def __iter__(self):  # 返回的是迭代器对象
    self.a = 1
    print(self,'self')
    return self  # 表示实例对象本身是自己的迭代器对象
  def __next__(self):
    self.a += 1
    return self.a


myclass = MyNumbers() # 创建对象
print(isinstance(myclass,Iterable))
myiter = iter(myclass) # 获取迭代器
print(myiter,'myiter')
print(isinstance(myclass,Iterator))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
```
<a name="Lrsj3"></a>
## 8、迭代器总结

1. 凡是可作用于for循环的对象都是Iterable 类型；
2. 凡是可作用于 next() 函数的对象都是Iterator 类型；
3. 集合数据类型如list 、dict、str等是 Iterable但不是Iterator，不过可以通过 iter()函数获得一个Iterator对象。
<a name="WGGA0"></a>
# 生成器
在python中一边循环一边计算的这种机制，叫做生成器<br />以 list 容器为例，在使用该容器迭代一组数据时，必须事先将所有数据存储到容器中，才能开始迭代；而生成器却不同，它可以实现在迭代的同时生成元素。<br />也就是说，对于可以用某种算法推算得到的多个数据，生成器并不会一次性生成它们，而是什么时候需要，才什么时候生成。<br />理解生成器，最好的方法就是给他取个突出其本质的别名：**生成数据的机器代码**。<br />生成器是一种用时间换空间的做法。比如，利用list列表储存全体正整数，无穷个正整数再大的内存也无法装得下，这个时候就可以使用生成器，实现用一段代码来储存全部正整数的作用。
<a name="w5FSM"></a>
#### 生成器的创建 
不仅如此，生成器的创建方式也比迭代器简单很多，大体分为以下 2 步：

1. 定义一个以 yield 关键字标识返回值的函数；
2. 调用刚刚创建的函数，即可创建一个生成器。

实例
```python
def intNum():
    print("开始执行")
    for i in range(5):
        yield i
        print("继续执行")


num = intNum()
print(num)
print(num.__next__())
print(num.__next__())
print(num.__next__())
print(num.__next__())
print(num.__next__())


for i in num:
  print(i)
```

由此，我们就成功创建了一个 num 生成器对象。显然，和普通函数不同，intNum() 函数的返回值用的是 yield 关键字，而不是 return 关键字，此类函数又成为生成器函数。

和 return 相比，yield 除了可以返回相应的值，还有一个更重要的功能，即每当程序执行完该语句时，程序就会暂停执行。不仅如此，即便调用生成器函数，Python 解释器也不会执行函数中的代码，它只会返回一个生成器（对象）。

要想使生成器函数得以执行，或者想使执行完 yield 语句立即暂停的程序得以继续执行，有以下 2 种方式：

1. 通过生成器（上面程序中的 num）调用 next() 内置函数或者 __next__() 方法；
2. 通过 for 循环遍历生成器。
<a name="RJscp"></a>
# 闭包
要想了解装饰器，首先要了解一个概念，闭包。什么是闭包，一句话说就是，在函数中再嵌套一个函数，并且引用外部函数的变量，这就是一个闭包了。光说没有概念，直接上一个例子。
```python
def outer(x):
    def inner(y):
        return x + y
    return inner

print(outer(6)(5))
```
如代码所示，在outer函数内，又定义了一个inner函数，并且inner函数又引用了外部函数outer的变量x，这就是一个闭包了。在输出时，outer(6)(5),第一个括号传进去的值返回inner函数，其实就是返回6 + y，所以再传第二个参数进去，就可以得到返回值，6 + 5。
<a name="Heb8u"></a>
#### 构成条件
1、函数嵌套<br />2、外部函数返回内部函数名<br />3、内部函数使用外部函数的变量
<a name="USesT"></a>
# 装饰器
<a name="jTLVP"></a>
#### 什么是装饰器 
所谓的装饰器，其实就是通过装饰器函数，来修改原函数的一些功能，使得原函数不需要修改。理解起来好像就是装饰器本身可以增强其他函数的功能，一个函数平平无奇，没有关系，有我装饰器，定能让你变的闪闪发光。 这么说可能也有点绕，举个栗子，比如你是一个男程序员，然后你带上假发，穿上女装，再画个妆，那你可能会成为一个女装大佬，那么假发、女装、化妆就是装饰器，你还是你，但是因为有了这些装饰器，你成为了一个女装大佬。enmmmm...，大概就是这样。<br />下面看一个世界上最简单的函数，放宽心，绝对不是Hello World!
```python
def hello():
    print("你好，装饰器！")
```
那如果我想让hello()函数再实现个其他的功能，比如打印个执行函数时的时间。 有人说可以在hello()函数里加上打印时间的代码不就好了。
```python
import datetime


def hello():
    print("当前时间:", datetime.datetime.now())
    print("你好，装饰器！")
```
那么问题来了，如果还有hello1()、hello2()、hello3()等等大量的函数，那也一个一个的加上吗，那就会造成大量的重复代码，为了避免重复代码，我们可以重新定义一个函数，专门用来打印当前时间，打印完时间再执行真正的业务代码。
```python
def print_time(func):
    print("当前时间:", datetime.datetime.now())
    func()


def hello():
    print("你好，装饰器！")


print_time(hello)
```
这样逻辑上虽然没多大毛病，但是这样的话，我们每次都要传递一个函数给print_time()函数，这种做法破坏了原有的代码逻辑结构，原来执行业务逻辑，我们只需要调用hello()函数，而现在我们必须要调用print_time()函数才行，那有没有更好的方式，当然，那就是装饰器。
<a name="OWAYM"></a>
#### 装饰器的实现 
```python
import datetime


def my_decorator(func):
    def print_time():
        print("当前时间:", datetime.datetime.now())
        func()

    return print_time


# hello = my_decorator(hello)
# hello()
@my_decorator
def hello():
    print("你好，装饰器！")


hello()

当前时间: 2023-04-03 18:56:07.354061
你好，装饰器！
```
**注：@符号是装饰器的语法糖，在定义函数的时候使用，可以避免再一次赋值操作**。<br />此处@my_decorator，相当于
```python
hello = my_decorator(hello) 
hello() 
```
很显然，这样不但可以实现需要的功能，代码也更加简洁。 解释一下，当运行最后的hello()函数时，调用过程是这样的：

- 先是执行hello = my_decorator(hello)，此时变量hello指向的是my_decorator()。
- my_decorator(func)中传参是hello，返回的print_time，而print_time又会调用到原函数hello()。
- 所以，先执行print_time()函数里的代码，然后才执行hello()函数里的。

上述代码里的my_decorator()就是一个装饰器，它“增强”了hello()的功能，但是并没有去真正的改变hello()函数的内部实现。


<a name="yjNNE"></a>
### 高阶函数回顾
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
<a name="uzYbh"></a>
### 什么是递归？
在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。记住哦->在函数内部调用其他函数不是函数的嵌套，而在函数内部定义子函数才是函数的嵌套。
<a name="oUMLt"></a>
#### 递归的特点
一个函数 内部 调用自己。函数内部可以调用其他函数，当然在函数内部也可以调用自己。
<a name="sKZh0"></a>
#### 代码的特点 
1、函数内部的 代码 是相同的，只是针对参数不同，处理的结果不同；<br />2、当参数满足一个条件 时，函数不再执行；<br />这个非常重要，通常被称为递归的出口，否则 会出现死循环！
<a name="UPcbk"></a>
#### 递归与递推实例
```python
# 用正向递推的方式计算阶乘
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))


# 递归实现阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)
"""
总结果: factorial(5)
第一次调用     factorial(5) =  5 * factorial(4)
第二次调用     factorial(4) =  4 * factorial(3)
第三次调用     factorial(3) =  3 * factorial(2)
第四次调用     factorial(2) =  2 * factorial(1)
第五次调用     factorial(1) =  1 
表达式:  5 * 4 * 3 * 2 *  1 
"""


factorial(5)                        # 第 1 次调用使用 5
5 * factorial(4)                    # 第 2 次调用使用 4
5 * (4 * factorial(3))              # 第 3 次调用使用 3
5 * (4 * (3 * factorial(2)))        # 第 4 次调用使用 2
5 * (4 * (3 * (2 * factorial(1))))  # 第 5 次调用使用 1 
5 * (4 * (3 * (2 * 1)))             # 从第 5 次调用返回
5 * (4 * (3 * 2))                   # 从第 4 次调用返回
5 * (4 * 6)                         # 从第 3 次调用返回
5 * 24                              # 从第 2 次调用返回
120                                 # 从第 1 次调用返回
```
<a name="Wn282"></a>
### 匿名函数 
概念: Python 使用 **lambda** 来创建匿名函数。所谓匿名，意即不再使用 **def** 语句这样标准的形式定义一个函数。
<a name="fZa5W"></a>
#### 语法格式
```python
lambda [arg1 [,arg2,.....argn]]:expression
"""
lambda ： Python 预留的关键字，类似普通函数中 def 
[arg…] ： 是参数列表，它的结构与 Python 中函数(function)的参数列表是一样的，
          需要注意的是，普通函数不同，这里不需要用括号将 lambda 函数的参数括起来，
          如果 lambda 函数有两个或更多参数，用逗号列出它们。
expression ：一个参数表达式，表达式中出现的参数需要在[arg......]中有定义，并且表达式只能是单行的，只能有一个表达式。
"""
```
<a name="aN6ik"></a>
#### 实例之两数相加和
```python
def add(x, y):
    return x+ y
print(add(3,4))


add = lambda x,y:x+y
print(add(3,4))
```

<a name="LGh0M"></a>
#### lamada参数实例
```python
import random

# 无参数
sdds = lambda: random.random()
sdds()

# 一个参数
fun1 = lambda x: x
print(fun1('hello python'))

# 默认参数 (缺省参数)
fun2 = lambda a, b, c=100: a + b + c
print(fun2(10,19,1000))

# 可变参数之args
fun3 = lambda *args: args
print(fun3((1,2,3,4,5)))

# 可变参数之kwargs
fun4 = lambda  **kwargs: kwargs
print(fun4(name='yueyue',age=18,height='178cm'))

# 带判断的lambda表达式
asd = lambda x: x if (x > 10) else 10
print(asd(5))
#### 它是以下带有def和return 关键字的普通函数的更简单版本：
def fun(x):
    if x > 10:
        return x
    else:
        return 10
print(fun(5))
```

<a name="qbqZN"></a>
#### 列表中字典数据排序
```python
# 列表中的字典排序
# 需求:假设我们需要对字典中的年龄进行排序
user_list = [
    {"name": 'zhangsan1', 'age': 18},
    {"name": 'lisi1', "age": 19},
    {"name": 'wangwu1', "age": 17}
]

def getAge(element):
    return element['age']

# 传递给key参数的是一个函数，它指定可迭代对象中的每一个元素来按照该函数进行排序
user_list.sort(key=getAge,reverse=True)
print(user_list)


# 我们需要使用匿名函数，使用sort函数中的key这个参数，来指定字典比大小的方法
# reverse参数控制升序与降序排列
user_list.sort(key=lambda x:x['age'],reverse=True)
print(user_list)
```





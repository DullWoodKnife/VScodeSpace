<a name="zzqxt"></a>
### 函数简介
函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。
<a name="wrl8D"></a>
### 定义一个函数 

- 函数代码块以 **def** 关键词开头，后接函数标识符名称和圆括号()。
- 任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
- 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
- 函数内容以冒号起始，并且缩进。
- **return [表达式]** 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None
```python
def 函数名(参数):
    "函数文档字符串"
    代码1
    代码2
    ......
```
<a name="6dc23cc0"></a>
### 函数的调用
> **定义一个函数只给了函数一个名称，指定了函数里包含的参数，和代码块结构。**
> **函数必须调用才会进行执行**

```python
# 函数名(参数)
```
> **不同的需求，参数可有可无。**
> **在Python中，函数必须先定义后使用。**

```python
# 定义函数
def demo():
   print("我是dmeo函数")
 
# 调用函数
demo()
```
<a name="qOPHO"></a>
### 函数的参数 
在python中定义函数的时候，函数名后面的括号里就是用来定义参数的，如果有多个参数的话，那么参数之间直接用逗号, 隔开
```python
# 利用函数的参数，定义一个可以完成任意两个数相加的函数
def add_num(a,b):
    c = a + b
    print(c)
```
函数定义了参数，那么调用函数的时候就需要传入参数
```python
add_num(11,22)
#运行结果
33
```
上面的案列中，我们定义函数的时候在函数名后面的括号里**定义的参数叫做形参**，<br />而我们调用函数的时候**传入的参数叫做实参**，**形参是用来接收实参的**。<br />![](https://cdn.nlark.com/yuque/0/2023/png/25414438/1675757344973-05cabebc-a218-4288-a704-00ef4365a292.png#averageHue=%23f6f4f3&clientId=uaddd56b2-3b1d-4&from=paste&id=uda0934a5&originHeight=456&originWidth=681&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=ud7f177bc-ef90-4ab9-8274-381dfd09c03&title=)
<a name="Nicqg"></a>
### 参数的分类
<a name="OnQef"></a>
##### 1、根据实参进行分类

- 位置参数 (未命名参数)
```python
def func(a,b,c):
    print(a)
    print(b)
    print(c)
      
func(11,22,33)
#运行结果
11
22
33
上述案列中的函数的三个形参是按位置接收传入的实参，我们把这样的传参的形式叫做位置参数，
```

- 关键字参数 (命名参数)
```python
def func(a,b,c):
    print(a)
    print(b)
    print(c)
      
func(11,c=99,b=33)
#运行结果
11
33
99
调用函数函数的时候，实参通过参数名指定传给某个形参，这样的传参形式，我们把它叫做关键字参数
注意：传参的时候先写位置参数，再写关键字参数
```
<a name="NDcZk"></a>
##### 2、根据形参进行分类

- 必备参数
```python
在调用函数的时候必须要传的参数
def add(a,b):
    c=a+b
    print(c)
     
add(11,22）
上面函数中的a,b就是必备参数，在调用的函数的时候必须要传，不然就会报错
```

- 默认参数
```python
调用函数的时候可以传可以不传，不传就用默认值
def func(a,b,c=99):
    print(a)
    print(b)
    print(c)
func(11,22,33)
print('-----------')
func(55,66)
注意：带有默认值的参数一定要位于参数列表的最后面。
```

- 不定长参数 (*args和 **kwargs)
   - *args：接收多传入的位置参数，以元祖的形式保存
```python
def func(*args):
　　print(args)
 
func(33,44,55,66,77)
func(*(33,44,55,66,77))
 
#运行结果
(33,44,55,66,77)
(33,44,55,66,77)

*args，args接收的是一个元祖；
调用的时候可以直接传入：func(33,44,55,66,77)，
也可以可以先组装list或tuple，再通过*拆包传入：func(*(33,44,55,66,77))；
```

   - **kwargs：接收多传入的关键字参数，以字典的形式保存
```python
def func(**kwargs):
    print(kwargs)
func(e=33,h=44,f=55,d=66,c=77)
func(**{'e':33,'h':44,'d':66,'c':77})
#运行结果
{'e': 33, 'h': 44, 'f': 55, 'd': 66, 'c': 77}
{'e': 33, 'h': 44, 'f': 55, 'd': 66, 'c': 77}

**kwargs，kw接收的是一个字典；
关键字参数既可以直接传入：func(11,22,e=33,h=44,f=55,d=66,c=77)，
也可以先组装dict，再通过**拆包传入：func(**{'e':33,'h':44,'d':66,'c':77})。
```
**注意点：**使用*args和**kwargs是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
<a name="NIXeI"></a>
### 函数的返回值
<a name="cmsJw"></a>
##### 前言
我们创建函数都只是为我们做一些事，做完了就结束。但实际上，有时还需要对事情的结果进行获取。这类似于主管向下级职员下达命令，职员去做，最后需要将结果报告给主管，为函数设置返回值的作用就是将函数的处理结果返回给调用它的程序。
<a name="EhtMo"></a>
##### 对返回值的理解
1、函数返回值： 函数执行后会返回一个对象，给调用方返回值，如果函数内部有return就可以返回，否则返回None。<br />2、返回值类型：取决于return后面的类型。<br />3、函数内可出现多个return，但只会起作用一个。若执行了return，意为这函数执行完退出了。
```python
def Sum(a,b):
    sum = a +b
    return sum
print(Sum(1,3))
```
<a name="tzRK4"></a>
### 函数的多个返回值 
```python
# 函数的多个返回值
def my_test2():
    a, b, c = (1, 2, 3)
    # return a  # 当函数中有多个return时，不会报错，但是只会执行第一个
    # return b  # 后面的代码为什么不会被执行  return返回到函数调用处了
    # return c
    return a, b, c  # 写在一起 但返回的类型为元组


values = my_test2()
print(values)
print(type(values))
```
<a name="gzZgf"></a>
### 函数的嵌套调用
函数的嵌套：在函数里面还有函数。分为外函数和内函数。<br />嵌套函数是为函数内部服务的，比如减少代码的重复，想要调用函数，要使用函数名，内函数也一样。如果不用函数名调用内函数，内函数就永远不会执行。
```python
怎么在函数外部调用内函数呢？首先，不能直接调用内函数 ，需要先执行外函数的代码块。
def func1():
    print("这是外部函数")
    def func2():
        print("这是内部函数")
func2() 
没有执行外函数内部的代码块，python找不到内函数，所以报name ‘func2’ is not defined，
函数func2()没有定义
有几种方式可以实现对内函数的调用。
1.在外函数内部调用内函数，即用函数名调用
def func1():
    print("这是外部函数")
    def func2():
        print("这是内部函数")
    func2() #函数名调用内函数
func1() 
2.可以用return调用内函数
def func1():
    print("这是外部函数")
    def func2():
        print("这是内部函数")
    return func2
func1()() ##执行func1()会返回func2然后再func2()
# m = func1()
# m()


在一个函数里面调用别的函数
def print1():
    print("这是第一个函数")
def print2():
    print("这是定义的第二个函数")
    print1() #在print2()中调用print1()
print2()
```



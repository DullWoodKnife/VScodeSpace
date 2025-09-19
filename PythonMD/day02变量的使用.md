<a name="UcLW7"></a>
### ![image.png](https://cdn.nlark.com/yuque/0/2023/png/25414438/1675314907518-ec6d90b1-4402-42f7-b949-75a67fc18999.png#averageHue=%23e9e8e8&clientId=ucc8c0869-90a2-4&from=paste&height=160&id=u510bbafd&name=image.png&originHeight=159&originWidth=767&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9410&status=done&style=none&taskId=u8f421d13-1f2f-4369-bf48-8f1603185fc&title=&width=770.8799743652344)
<a name="lEyNU"></a>
### 什么是变量 
**变量**：在程序运行过程中，**值会**发生**变化**的量。
<a name="QGDyR"></a>
### 变量的定义 
把程序运算的中间结果临时存到内存里，以备后面的代码继续调用，这几个名字的学名就叫做“**变量**”。
<a name="yVKiM"></a>
### 变量的作用
变量用于存储要在计算机程序中引用和操作的信息。它提供了一种用描述性名称标注数据的方法，这样读者和我们自己就可以更清楚地理解我们的程序。<br />我们可以将**变量**看作保存信息的**容器**。它们的目的是在内存中标注和存储数据。然后，可以在整个程序中使用这些数据。 
<a name="i06m2"></a>
### 变量的创建
<a name="eHhap"></a>
#### 1.Python 中的变量不需要声明类型。
```python
>>> a = 4
>>> type(a)
<class 'int'>

>>> b = "hello"
>>> type(b)
<class 'str'>
```
这些变量都是不需要声明它的类型的，在C和Java中是必须要声明的。这里的`=`是赋值而不是等于的意思。每个变量在使用前都必须赋值，变量赋值以后才会被创建。如果一个变量没有赋值，直接用的话。系统会报出错误

这里的等号要理解并读作“赋值”，而不是“等于”，“赋值”是对变量的操作，而“等于”是对两个变量进行比较。
<a name="StAyg"></a>
#### 2.每个变量在使用前都必须赋值，变量赋值以后才会被创建。
新的变量通过赋值的动作，创建并开辟内存空间，保存值。如果没有赋值而直接使用会抛出赋值前引用的异常或者未命名异常
```python
>>> a      
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a = 1   
>>> a
1
```
<a name="DsrCV"></a>
#### 3.Python中，一切事物都是对象，变量引用的是对象或者说是对象在内存中的地址。(后续详解)
<a name="pDqCK"></a>
#### 4.在Python中，变量本身没有数据类型的概念
通常所说的“变量类型”是变量所引用的对象的类型，或者说是变量的值的类型
```python
>>> a = 1
>>> a = "haha"
>>> a = [1, 2, 3]
>>> a = { "k1":"v1"}
```
例子中，变量a在创建的时候，赋予了值为1的整数类型，然后又被改成字符串“haha”，再又变成一个列表，最后是个字典。变量a在动态的改变，它的值分别是不同的数据类型，这是动态语言的特点。
<a name="Gq38Y"></a>
#### 5.“=”号这个赋值运算符是从右往左的计算顺序。
```python
>>> a = 1
>>> b = 2
>>> c = a + b       # 先计算a+b的值，再赋给c
>>> c
3
```
<a name="yb75q"></a>
#### 6.Python允许同时为多个变量赋值。
例如：输出a,b,c的值都为2
```python
>>> a = b = c = 2
>>> a
2
>>> b
2
>>> c
2
```
例如：输出a,b,c的值分别为1,2,3
```python
>>> a,b,c = 1,2,3
>>> a
1
>>> b
2
>>> c
3
```
思考
```python
a = 'Jack'
b = a
a = 'Tom'
print(b)
print(a)
```
执行a = ‘Jack’，解释器创建字符串‘Jack’对象和变量a，并把a指向‘Jack’对象；<br />执行b = a,解释器创建变量b，并且将其指向变量a指向的字符串‘Jack’对象；<br />执行a = ‘Tom’,解释器创建字符串‘Tom’对象，并把a改为指向‘Tom’对象，与b无关。<br />![](https://cdn.nlark.com/yuque/0/2019/png/704747/1577693288114-b83e8090-8655-48e4-bda5-1209e5ed2b10.png#averageHue=%23f7f3ef&from=url&id=UH6uX&originHeight=300&originWidth=904&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
<a name="bubUn"></a>
### 变量的命名规则 
<a name="wn4jz"></a>
#### 1.第一个字符必须是字符表中的字符或者下划线
<a name="I6QIl"></a>
#### 2.标识符的其他的部分由字母、数字和下划线组成（**首字符不可以是数字**）
<a name="TgcMo"></a>
#### 3.标识符对大小写敏感
<a name="WRTqC"></a>
##### 4.不能使用python内置关键字作为变量名 
<a name="KNYS4"></a>
##### 5.尽量见名知意
<a name="XinkT"></a>
### 注释 
我们写的程序里，不光有代码，还要有很多注释。**注释**有说明性质的、帮助性质的，它们**在代码执行过程中相当于不存在，透明的**。
<a name="dfda63a5"></a>
#### 1.单行注释
Python中，以符号'**#**'为单行注释的开始，从它往后到本行的末尾，都是注释内容。快捷键:**CTRL+/**
```python
# 打印输出hello world
print("hello world")
```
<a name="d85d7433"></a>
#### 2.多行注释
Python没有真正意义上的多行注释（块注释）语法。选中需注释的代码，再使用快捷键**CTRL+/**
```python
# 第一行注释
# 第二行注释
# 第三行注释
```
<a name="6807dbf8"></a>
#### 3.注释文档
在某些特定的位置，用三引号包括起来的部分，也被当做注释。
```python
"""
    这个是函数的说明文档。
    :param a: 加数
    :param b: 加数
    :return: 和
"""
'''
	也可以实现多行注释
    与三个双引号作用一致
'''
```
<a name="ypdtz"></a>
### 初识数据类型 
**在 Python ⾥为了应对不同的业务需求，也把数据分为不同的类型。**<br />![数据类型.png](https://cdn.nlark.com/yuque/0/2023/png/25414438/1675325898292-b8c1187a-2c78-4640-b6b0-7f6351a98ba0.png#averageHue=%23f3f3f3&clientId=ue97369e8-5827-4&from=ui&id=u3a215499&name=%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B.png&originHeight=653&originWidth=1040&originalType=binary&ratio=1&rotation=0&showTitle=false&size=68451&status=done&style=none&taskId=u9fc742c4-6ab6-48b4-985f-f9307794d46&title=)<br />实例说明<br />查看数据类型的⽅法： type()
```python


a = 1
>>>type(a) # <class 'int'> -- 整型

b = 1.1
>>>type(b) # <class 'float'> -- 浮点型

c = True
>>>type(c) # <class 'bool'> -- 布尔型

d = '12345'
>>>type(d) # <class 'str'> -- 字符串

e = [10, 20, 30]
>>>type(e) # <class 'list'> -- 列表

f = (10, 20, 30)
>>>type(f) # <class 'tuple'> -- 元组

h = {10, 20, 30}
>>>type(h) # <class 'set'> -- 集合

g = {'name': 'TOM', 'age': 20}
>>>type(g) # <class 'dict'> -- 字典
```

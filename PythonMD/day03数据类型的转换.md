![image.png](https://cdn.nlark.com/yuque/0/2023/png/25414438/1675314991849-595a436f-2120-4801-8bec-12c27acd38d3.png#averageHue=%23e8e7e6&clientId=u8b4fd9e7-e30d-4&from=paste&height=341&id=u4ec5ac1d&name=image.png&originHeight=322&originWidth=764&originalType=binary&ratio=1&rotation=0&showTitle=false&size=31240&status=done&style=none&taskId=u88d24bd2-1114-4d28-aba4-0abe5e00aff&title=&width=807.9599914550781)

<a name="GdmIz"></a>
### input输入函数 
**input()**是内置函数，用来**获取用户输入**，**返回值**为**字符串**。
<a name="IEW54"></a>
#### 1.返回值为字符串

- 输入name为Bob，返回的是string类型的'Bob'
```python
>>> name = input("请输入你的名字:")
请输入你的名字:Bob
>>> name
'Bob'
>>> type(name)
<class 'str'>
```

- 输入age为11，返回的是string类型的'11'
```python
>>> age = input("请输入你的年龄:")
请输入你的年龄:11
>>> age
'11'
>>> type(age)
<class 'str'>
```

- 输入回车，返回的是''空字符串
```python
>>> ipt = input("请输入:")
请输入:
>>> ipt
''
>>> type(ipt)
<class 'str'>
```

- 输入a and b，返回的是保留了空格格式的字符串	
```python
>>> ipt = input("请输入:")
请输入:'a and b'
>>> ipt
"'a and b'"
>>> type(ipt)
<class 'str'>
```
以上代码可以看出，输入的值不管是什么，类型都是**字符串**。
<a name="FXUEY"></a>
#### 2.阻塞或暂停程序
```python
print("程序前面部分执行完毕......")
input("请按回车继续......")       # 在这里程序会暂停，等待你的回车动作
print("继续执行程序的后面部分......")
```
此时的input函数不会将输入的值保存下来，只是用作暂停程序动作
<a name="DihTw"></a>
### print格式化输出函数 
<a name="O6vVc"></a>
##### print 默认输出
print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""
```python
x="a"
y="b"
# 换行输出
print( x )
print( y )
 
print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()
```
<a name="Mtoy0"></a>
##### %格式化输出  
![](https://cdn.nlark.com/yuque/0/2019/png/704747/1577703452070-6446d750-7f11-4c01-a026-68e4aecbdef1.png#averageHue=%23e3e2e1&from=url&id=Ngh3E&originHeight=357&originWidth=469&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
```python
print("我叫%s 今年%d岁"%('Bob',18))

浮点数输出 
number = 180.5
# %f ——保留小数点后面六位有效数字
print("我的身高是:%f"%number)
# %.3f，保留3位小数位
print("我的身高是:%.3f"%number)

# %e ——保留小数点后面六位有效数字，指数形式输出
print("我的身高是:%e"%number)
# %.3e，保留3位小数位，使用科学计数法
print("我的身高是:%.3e"%number)

# %g ——在保证六位有效数字的前提下，使用小数方式，否则使用科学计数法
print("我的身高是:%g"%number)
# %.3g，保留3位有效数字，使用小数或科学计数法
print("我的身高是:%.3g"%number)
```
<a name="bwMvD"></a>
##### format的用法
相对基本格式化输出采用‘%’的方法，format()功能更强大，该函数把字符串当成一个模板，通过传入的参数进行格式化，并且使用大括号‘{}’作为特殊字符代替‘%’
```python
name = "小明"
age = 18
love = "打游戏"

# 1、不带编号
print("大家好,我是{},今年{}岁,喜欢{}".format(name,age,love))

# 2、带数字编号
print("大家好,我是{2},今年{0}岁,喜欢{1}".format(age,love,name))

# 3、附带关键字
print("大家好,我是{name},今年{age}岁,喜欢{love}".format(age=age,name=name,love=love))
```
<a name="LFsX8"></a>
##### f表达式 
在字符串前面加上f以达到格式化的目的，在{}里加入对象，此为format的另一种形式
```python
name = "小明"
age = 18
love = "打游戏"
print(f"大家好,我是{name},今年{age}岁,喜欢{love}")

```
<a name="pofke"></a>
### 数据类型之间的转换 

- 数据类型转换的必要性
- 数据类型转换常⽤⽅法

![类型转化.png](https://cdn.nlark.com/yuque/0/2023/png/25414438/1675328909717-b09f516b-65d0-4ace-a821-8021af147518.png#averageHue=%23e7ebe3&clientId=u17b8c7db-c9ea-4&from=ui&id=u2491b215&name=%E7%B1%BB%E5%9E%8B%E8%BD%AC%E5%8C%96.png&originHeight=184&originWidth=450&originalType=binary&ratio=1&rotation=0&showTitle=false&size=96349&status=done&style=none&taskId=u55eb977e-d76f-4a11-946f-831e138a0e5&title=)<br />**奥特曼在打怪兽的时候，经常切换形态**

- 天上飞的：换蓝色
- 地上跑的：换红色
- 能飞能跑的：两个颜色都要有
<a name="ac48da5f"></a>
## 转化数据类型的作用
问：input()接收⽤户输⼊的数据都是字符串类型，如果⽤户输⼊1，想得到整型该如何操作？<br />答：转换数据类型即可，即将字符串类型转换成整型。

| 函数 | 说明 |
| --- | --- |
| **int(x)** | **将x转化为整数** |
| **float(x)** | **将x转化为浮点数** |
| **str(x)** | **将x转化为字符串** |
| **eval(str)** | **将字符串中的数据转换成Python表达式原本类型** |
| **tuple(s )** | **将序列 s 转换为⼀个元组** |
| **list(s )** | **将序列 s 转换为⼀个列表** |
| chr(x ) | 将⼀个整数转换为⼀个Unicode字符 |
| ord(x ) | 将⼀个字符转换为它的ASCII整数值 |
| hex(x ) | 将⼀个整数转换为⼀个⼗六进制字符串 |
| oct(x ) | 将⼀个整数转换为⼀个⼋进制字符串 |
| bin(x ) | 将⼀个整数转换为⼀个⼆进制字符串 |

**快速体验**
```python
# 1. 接收⽤户输⼊
num = input('请输⼊您的幸运数字：')

# 2. 打印结果
print(f"您的幸运数字是{num}")

# 3. 检测接收到的⽤户输⼊的数据类型 -- str类型
print(type(num))
# 4. 转换数据类型为整型 -- int类型
print(type(int(num)))
```
**实例**
```python
# 1. float() -- 转换成浮点型
num1 = 1
print(float(num1))
print(type(float(num1)))

# 2. str() -- 转换成字符串类型
num2 = 10
print(type(str(num2)))

# 3. tuple() -- 将⼀个序列转换成元组
list1 = [10, 20, 30]
print(tuple(list1))
print(type(tuple(list1)))

# 4. list() -- 将⼀个序列转换成列表
t1 = (100, 200, 300)
print(list(t1))
print(type(list(t1)))

# 5. eval() -- 将字符串中的数据转换成Python表达式原本类型
str1 = '10'
str2 = '[1, 2, 3]'
str3 = '(1000, 2000, 3000)'
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))
```

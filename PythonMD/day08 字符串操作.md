<a name="cc4dd1da"></a>
# 字符串
**字符串是 Python 中最常用的数据类型。我们可以使用引号 ( ' 或 " ) 来创建字符串。创建字符串很简单，只要为变量分配一个值即可**
```python
# 单引号
var1 = 'Hello World!'
# 双引号
var2 = "Python Runoob"
# 三引号
var3 = """hello world
		i love you	"""
```
<a name="12f01ba6"></a>
# 字符串的输入输出
**格式化输出**
```python
name = "TOM"
age = 18
heigth = 180.5

print("我的名字是%s"%name)
print("我今年%d岁了"%age)
print("我的身高是%.2f"%heigth)
print("大家好，我叫{},我今年{}岁，我的升高是{}".format(name,age,heigth))
print(f"大家好，我叫{name},我今年{age}岁，我的升高是{heigth}")
```
**输入input()**
```python
>>>name = input("请输入你的名字：")
>>>"tom"
>>>print(type(name))

>>>age = input("请输入你的年龄：")
>>>18
>>>print(type(age))
```

---

<a name="zYNaI"></a>
# 访问字符串中的值
**下标**⼜叫 **索引**,就是编号。⽐如⽕⻋座位号，座位号的作⽤：按照编号快速找到对应的座位。<br />注意点：下标从0开始进行计算 
```python
var1 = "hello python"
print(var1[1])
print(var1[2])
print(var1[4])

# 输出结果
>>>e
>>>l
>>>o
```

---

<a name="261b8a9f"></a>
# 字符串中的切片
> **切⽚是指对操作的对象截取其中⼀部分的操作。字符串、列表、元组都⽀持切⽚操作**

- 不包含结束位置下标对应的数据， 正负整数均可；
- 步⻓是选取间隔，正负整数均可，默认步⻓为1。
```python
name = "hellopython"
print(name[2:5])    # 从2开始，到5结束(不会拿到5本身)
print(name[2:5:1])  # 从2开始，到5结束，步长为1(不会拿到5本身)
print(name[:5])     # 从0开始，下表为5结束(不会拿到本身)
print(name[1:])     # 从1开始，一直到结束
print(name[:])      # 拿取所有
print(name[::2])    # 从0开始，步长为2，拿取所有
print(name[:-1])    # 从0开始，到最后一个数结束(-1代表最后一个数，不包含-1本身)
print(name[-4:-1])  # 从倒数第四个开始，到倒数第一个结束(不包含-1本身)
print(name[::-1])   # 从-1开始，倒着打印字符串，步长为1
print(name[::-2])   # 从-1开始，倒着打印字符串，步长为2
```
<a name="iNY8t"></a>
# 字符串常用操作方法
**Python**3 的**字符串操作方法**包括 string 替换、复制、连接、比较、查找、大小写转换、分割 、判断等。
<a name="UBBf0"></a>
## 查找
**含义: 所谓字符串查找⽅法即是查找⼦串在字符串中的位置或出现的次数。**
<a name="orcKD"></a>
#### find()：检测某个字符串是否包含在这个字符串中，如果在，返回这个字符串开始的位置下标，否则则返回-1。

- **语法**
```python
lstr.find(str, start=0, end=len(lstr))

开始和结束位置下标可以省略，表示在整个字符串序列中查找。
```

- **实例**
```python
# 字符串序列.find(⼦串, 开始位置下标, 结束位置下标)
var = "hello and python and hello world"

print(var.find("and"))          # 查找到and首字母下标
print(var.find("and",8,20))     # 查找到下标为8-20，and首字母下标
print(var.find("ors"))          # 查找ors，如果没有，则返回-1
```
<a name="JQSo9"></a>
#### index()：检测某个⼦串是否包含在这个字符串中，如果在返回这个⼦串开始的位置下标，否则则报异常。

- **语法**
```python
lstr.index(str, start=0, end=len(lstr))

注意：开始和结束位置下标可以省略，表示在整个字符串序列中查找。
```

- **实例**
```python
# 字符串序列.index(⼦串, 开始位置下标, 结束位置下标)

var = "hello and python and hello world"
print(var.index("and"))          # 查找到and首字母下标
print(var.index("and",8,20))     # 查找到下标为8-20，and首字母下标
print(var.index("ors"))          # 查找ors，如果没有，则报错
```
<a name="wXo1i"></a>
#### count()：返回某个⼦串在字符串中出现的次数

- **语法**
```python
lstr.count(str, start=0, end=len(lstr))
注意：开始和结束位置下标可以省略，表示在整个字符串序列中查找。
```

- **实例**
```python
# 字符串序列.count(⼦串, 开始位置下标, 结束位置下标) 

var = "hello and python and hello world"

print(var.count("and"))         # 查看在字符串var中，and出现了多少次
print(var.count("ands"))        # 如果没有，则返回0次
print(var.count("and",8,20))    # 在一个区间内查找and出现的次数
```
<a name="PUnWJ"></a>
#### 拓展(了解即可)
```python
var = "hello and python and hello world"

# rfind()： 和find()功能相同，但查找⽅向为右侧开始。
print(var.rfind("and"))

# rindex()：和index()功能相同，但查找⽅向为右侧开始。
print(var.rindex("and"))
```
<a name="8347a927"></a>
## 修改
**含义:对字符串当中的内容进行修改**
<a name="QWBNC"></a>
### replace():替换内容

- **语法**
```python
1str.replace(str1, str2,  1str.count(str1))

```

- **实例**
```python
# 字符串序列.replace(旧⼦串, 新⼦串, 替换次数) 
var = "hello and python and hello world"
print(var.replace("and","和"))       # 将里面所有的and替换为和
print(var.replace("and","和",1))     # 将and替换为和，只替换一次
注意：替换次数如果超出⼦串出现次数，则替换次数为该⼦串出现次数。
```
**注意：数据按照是否能直接修改分为可变类型和不可变类型两种。**<br />**字符串类型的数据修改的时候不能改变原有字符串，属于不能直接修改数据的类型即是不可变类型。**
<a name="kpMFG"></a>
### split()：按照指定字符分割字符串。

- **语法**
```python
1str.split(str=" ", maxspilt='')
注意：maxspilt表示的是分割字符出现的最大次数
```

- **实例**
```python

var = "hello and python and hello world"
print(var.split("and"))         # 以and为界，分隔开其他字符串，返回一个列表
print(var.split("and",1))       # 以and为界，分隔开其他字符串，只分割一次，返回一个列表
```
<a name="HwUfZ"></a>
## 连接
<a name="gaUNi"></a>
### join()：⽤⼀个字符或⼦串合并字符串，即是将多个字符串合并为⼀个新的字符串。

- **语法**
```python
语法：  'sep'.join(iterable)
参数说明
sep：分隔符。可以为空
seq：要连接的元素序列、字符串、元组、字典
上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串
返回值：返回一个以分隔符sep连接各个元素后生成的字符串
```

- **实例**
```python
# 字符或⼦串.join(多字符串组成的序列)

list1 = ["hello", "python", "i", "love", "you"]
t1 = ("hello", "python", "i", "love", "you")
set1 = {"hello", "python", "i", "love", "you"}

print("__".join(list1))     # 将列表转化为字符串，并且使用指定符号隔开
print(",".join(t1))         # 将元组转化为字符串，并且使用指定符号隔开
print("|".join(set1))       # 将集合转化为字符串，并且使用指定符号隔开
```
<a name="XdeFi"></a>
## 删除
<a name="eSEet"></a>
#### lstrip()：删除字符串左侧空⽩字符。
```python
var = "    hello and python and hello world      "

print(var.lstrip())				# 删除左侧空格
```
<a name="OyeWl"></a>
#### rstrip()：删除字符串右侧空⽩字符。
```python
var = "    hello and python and hello world      "

print(var.rstrip())				# 删除右侧空格
```
<a name="lzL0j"></a>
#### strip()：删除字符串两侧空⽩字符。
```python
var = "    hello and python and hello world      "

print(var.strip())				# 删除两侧空格
```
<a name="lIK0H"></a>
## 判断
<a name="nz2wv"></a>
#### isalpha()：如果字符串所有字符都是字⺟则返回 True, 否则返回 False。
**语法**
```python
mystr1 = 'hello'
mystr2 = 'hello12345'

print(mystr1.isalpha())		# 结果：True
print(mystr2.isalpha())		# 结果：False
```
<a name="XGAWB"></a>
#### isdigit()：如果字符串只包含数字则返回 True 否则返回 False。
**语法**
```python
mystr1 = 'aaa12345'
mystr2 = '12345'

print(mystr1.isdigit())		# 结果： False
print(mystr2.isdigit())		# 结果：False
```
<a name="eNj6w"></a>
#### isalnum()：如果字符串所有字符都是字⺟或数字则返 回 True,否则返回False。
**语法**
```python
mystr1 = 'aaa12345'
mystr2 = '12345-'

print(mystr1.isalnum())		# 结果：True
print(mystr2.isalnum())		# 结果：False
```
<a name="WRAhw"></a>
#### isspace()：如果字符串中只包含空⽩，则返回 True，否则返回 False。
**语法**
```python
mystr1 = '1 2 3 4 5'
mystr2 = ' '

print(mystr1.isspace())		# 结果：False
print(mystr2.isspace())		# 结果：True
```
<a name="KF456"></a>
## 其他方法
<a name="EI2r3"></a>
#### startswith()：检查字符串是否是以指定⼦串开头
**语法**
```python
# 字符串序列.startswith(⼦串, 开始位置下标, 结束位置下标) 
var = "hello and python and hello world"

print(var.startswith("hello"))			# 开头是hello，返回True
print(var.startswith("and"))			# 开头不是and，返回False
print(var.startswith("and",6,20))		# 在索引6-20，开头是and，返回True
```
<a name="SaZCq"></a>
#### endswith()：检查字符串是否是以指定⼦串结尾
**语法**
```python
var = "hello and python and hello world"

print(var.endswith("and"))				# 结尾不是and，返回False
print(var.endswith("world"))			# 结尾时world，返回True
print(var.endswith("and",0,9))			# 在0到9的索引范围，是and结尾，返回True
```
<a name="FnGdN"></a>
#### capitalize()：将字符串第⼀个字符转换成⼤写。
```python
var = "hello and python and hello world"

print(var.capitalize())			# 将字符串第⼀个字符转换成⼤写。
```
<a name="vIPqM"></a>
#### title()：将字符串每个单词⾸字⺟转换成⼤写。
```python
var = "hello and python and hello world"

print(var.title())				# 将字符串每个单词⾸字⺟转换成⼤写。
```
<a name="OIOuG"></a>
#### upper()：将字符串中⼩写转⼤写。
```python
var = "hello and python and hello world"

print(var.upper())				# 将字符串中⼩写转⼤写。
```
<a name="hwpcN"></a>
#### lower()：将字符串中⼤写转⼩写。
```python
var = "hello and python and hello world"

print(var.lower())				# 将字符串中⼤写转⼩写。
```
<a name="n8mLO"></a>
#### ljust()：返回⼀个原字符串左对⻬,并使⽤指定字符(默认空格)填充⾄对应⻓度 的新字符串
<a name="NjEbF"></a>
#### rjust()：返回⼀个原字符串右对⻬,并使⽤指定字符(默认空格)填充⾄对应⻓度 的新字符串
<a name="SQ7Sf"></a>
#### center()：返回⼀个原字符串居中,并使⽤指定字符(默认空格)填充⾄对应⻓度 的新字符串

<a name="4d6b1389"></a>
# 字符串运算
a = "Hello",b = "Python"

| + | 字符串连接 | >>>a + b | 'HelloPython' |
| --- | --- | --- | --- |
| [] | 通过索引获取字符串中字符 | >>>a[1] | 'e' |
| [ : ] | 截取字符串中的一部分 | >>>a[1:4] | 'ell' |
| in | 成员运算符 - 如果字符串中包含给定的字符返回 True | >>>"H" in a | True |
| not in | 成员运算符 - 如果字符串中不包含给定的字符返回 True | >>>"M" not in a | True |
| r | 取消转义 | >>>r“你\\n好” | 你\\n好 |
| % | 格式字符串 |  |  |



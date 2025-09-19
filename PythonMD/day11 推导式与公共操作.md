<a name="841709d2"></a>
# 一：公共操作
- 运算符
- 公共⽅法
- 容器类型转换
<a name="9cdd4a78"></a>
## 运算符
| 运算符 | 描述 | 支持的容器类型 |
| --- | --- | --- |
| + | 合并 | 字符串，列表，元组 |
| * | 复制 | 字符串，列表，元组 |
| in | 是否存在 | 字符串，列表，元组，字典，集合 |
| not in | 是否不存在 | 字符串，列表，元组，字典，集合 |

<a name="9fbd26cd"></a>
### +合并
```python
# 1. 字符串
str1 = 'aa'
str2 = 'bb'
str3 = str1 + str2
print(str3) # aabb

# 2. 列表
list1 = [1, 2]
list2 = [10, 20]
list3 = list1 + list2
print(list3) # [1, 2, 10, 20]

# 3. 元组
t1 = (1, 2)
t2 = (10, 20)
t3 = t1 + t2
print(t3) # (10, 20, 100, 200)
```
<a name="ccd2f0a0"></a>
### *复制
```python
# 1. 字符串
print('-' * 10) # ----------

# 2. 列表
list1 = ['hello']
print(list1 * 4) # ['hello', 'hello', 'hello', 'hello']

# 3. 元组
t1 = ('world',)
print(t1 * 4) # ('world', 'world', 'world', 'world')
```
<a name="3eabaf98"></a>
### in或not in
```python
# 1. 字符串
print('a' in 'abcd') # True
print('a' not in 'abcd') # False

# 2. 列表
list1 = ['a', 'b', 'c', 'd']
print('a' in list1) # True
print('a' not in list1) # False

# 3. 元组
t1 = ('a', 'b', 'c', 'd')
print('aa' in t1) # False
print('aa' not in t1) # True
```
<a name="b7407a1e"></a>
## 公共⽅法
| **函数** | **描述** |
| --- | --- |
| len() | 计算容器中元素个数 |
| del  | 删除 |
| max() | 返回容器中元素最⼤值 |
| min() | 返回容器中元素最⼩值 |
| range(start,end, step) | ⽣成从start到end的数字，步⻓为 step，供for循环使⽤ |
| enumerate() | 函数⽤于将⼀个可遍历的数据对象(如列表、元组或字符串)组合为⼀个索引序列，同时列出数据和数据下标，⼀般⽤在 for 循环当中。 |
| sum() | 序列求和 |
| zip() | 合并系列 |

<a name="63db0b9d"></a>
### max()
```python
# 1. 字符串
str1 = 'abcdefg'
print(max(str1)) # g  # 比较的是ascll码值 

# 2. 列表
list1 = [10, 20, 30, 40]
print(max(list1)) # 40
```
<a name="dc6df86c"></a>
### min()
```python
# 1. 字符串
str1 = 'abcdefg'
print(min(str1)) # a

# 2. 列表
list1 = [10, 20, 30, 40]
print(min(list1)) # 10
```
<a name="b37e2dde"></a>
### enumerate()
**语法**
```python
enumerate(可遍历对象, start=0)
list1 = ['a', 'b', 'c', 'd', 'e']
for i in enumerate(list1):
    print(i)

for index, char in enumerate(list1, start=1):
    print(f'下标是{index}, 对应的字符是{char}')
```
> **start参数⽤来设置遍历数据的下标的起始值，默认为0**

**zip()**<br />**zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。**<br />**如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。**
```python
a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]
d = {'name': 'yue', 'age': 18, 'gender': 1}
zipped = zip(a, b)
print(zipped)
print(list(zipped))
zipped = zip(a, c)
print(zipped)
print(list(zipped))

x1, x2 = list(zip(*zipped))
print(x1, x2)

```
<a name="dc467eab"></a>
## 容器类型转换
<a name="1e029e79"></a>
### tuple()
> **将某个序列转换成元组**

```python
list1 = [10, 20, 30, 40, 50, 20]
s1 = {100, 200, 300, 400, 500}
print(tuple(list1))
print(tuple(s1))
```
<a name="cd8361d0"></a>
### list()
> **将某个序列转换成列表**


```python
t1 = ('a', 'b', 'c', 'd', 'e')
s1 = {100, 200, 300, 400, 500}
print(list(t1))
print(list(s1))
```
<a name="4d3be1c3"></a>
### set()
> **将某个序列转换成集合**

```python
list1 = [10, 20, 30, 40, 50, 20]
t1 = ('a', 'b', 'c', 'd', 'e')
print(set(list1))
print(set(t1))
```
<a name="a21cbcc5"></a>
# 二：推导式

- 列表推导式
- 字典推导式
- 集合推导式
- 元组推导式
```python
[表达式 for 变量 in 列表 if 条件]
{健：值 for 变量 in 字典.items() if 条件}
{表达式 for 变量 in 集合 if 条件}
(表达式 for 变量 in 元组 if 条件)
```
> **⽤⼀个表达式创建⼀个有规律的列表或控制⼀个有规律列表。**

<a name="d5863ed2"></a>
## 列表推导式
**创建一个空列表，追加1到10这几个数字**

- **for循环实现过程**
```python
list1 = []
for i in range(1,11):
    list1.append(i)
print(list1)
```

- **列表推导式实现过程**
```python
list1 = [i for i in range(1,11)]
print(list1)
```
<a name="764e1a47"></a>
### 带if的列表推导式
**将1到10的偶数添加到列表**
> **方法一：利用步长实现**

```python
list1 = [i for i in range(0, 11, 2)]
print(list1)
```
> **方法二：if实现**

```python
list1 = [i for i in range(10) if i % 2 == 0]
print(list1)
```
<a name="ffdd4cbc"></a>
## 字典推导式
**创建⼀个字典：字典key是1-5数字，value是这个数字的2次⽅**

```python
# dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
dict1 = {i: i**2 for i in range(1, 6)}
print(dict1)
```
**将两个列表变为⼀个字典**
```python
list1 = ['name', 'age', 'sex']
list2 = ['Tom', 20, '男']
dict1 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict1)
```
**提取字典中⽬标数据**
```python
computs = {'AUC': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
# 需求：提取上述电脑数量⼤于等于200的字典数据

count1 = {key: value for key, value in computs.items() if value >= 200}
print(count1) # {'MBP': 268, 'DELL': 201}
```
<a name="a2cdd6e6"></a>
## 集合推导式
计算数字 1,2,3 的平方数
```python
setnew = {i**2 for i in (1,2,3)}
print(setnew)
```
输出非abc的字母
```python
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
{'d', 'r'}
```
<a name="859a1361"></a>
## 元组推导式
生成包含1到9数字的元组
```python
a = (x for x in range(1,10))
print(a)
# 返回的是生成器对象
# <generator object <genexpr> at 0x7faf6ee20a50> 

# 使用 tuple() 函数，可以直接将生成器对象转换成元组
print(tuple(a))       
(1, 2, 3, 4, 5, 6, 7, 8, 9)

print(tuple((x for x in range(1,10))))
(1, 2, 3, 4, 5, 6, 7, 8, 9)
```


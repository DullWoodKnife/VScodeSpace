<a name="67dc854f"></a>
# 列表
<a name="d6c84792"></a>
## 列表的应用场景
> **思考：如果⼀个班级100位学⽣，每个⼈的姓名都要存储，应该如何书写程序？声明100个变量吗？**<br />**答：列表即可， 列表⼀次性可以存储多个数据。**

<a name="0868ba3c"></a>
## 列表的创建 
**列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。列表的数据项不需要具有相同的类型创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。**
```python
使用 [ ] 直接创建列表
li = [1,2,3,4,"张三","李四"]
使用 list() 函数创建列表
li2 = list('123456789')
```
> **列表可以⼀次性存储多个数据，且可以为不同数据类型**

<a name="RSwpR"></a>
## 列表的常用操作
> **列表的作用是⼀次性存储多个数据，程序员可以对这些数据进行的操作有：增、删、改、查等等。**

<a name="ils4D"></a>
### 访问列表中的值
<a name="6bdc03f7"></a>
#### 根据索引访问列表元素
```python
使用索引访问列表元素的格式为:
listname[i]

name_list = ['张三', '李四', '王五','赵六']
print(name_list[0])
print(name_list[1])
print(name_list[2])
```
<a name="QJZan"></a>
#### 根据切片访问列表元素
```python
使用切片访问列表元素的格式为：
listname[start : end : step]
name_list = ['张三', '李四', '王五','赵六']
print(name_list[0:4:2])
```
<a name="870a51ba"></a>
#### 通过内置函数返回列表下标

- **index()：返回指定数据所在位置的下标 。**

**语法**
```python
# 列表序列.index(数据, 开始位置下标, 结束位置下标)
name_list = ['张三', '李四', '王五','赵六']
print(name_list.index('张三', 0, 2))
```
> **注意：如果查找的数据不存在则报错。**

- **count()：统计指定数据在当前列表中出现的次数。**
```python
name_list = ['张三', '李四', '王五','张三']
print(name_list.count('张三'))
```

- **len()：访问列表长度，即列表中数据的个数。**
```python
name_list = ['张三', '李四', '王五','赵六']
print(name_list.count('Tom'))
```
<a name="6f037ef5"></a>
#### in与not in
> **in：判断指定数据在某个列表序列，如果在返回True，否则返回False**
> **not in：判断指定数据不在某个列表序列，如果不在返回True，否则返回False**

```python
name_list = ['张三', '李四', '王五','赵六']
name = input('请输⼊您要搜索的名字：')
if name in name_list:
    print(f'您输⼊的名字是{name}, 名字已经存在')
else:
    print(f'您输⼊的名字是{name}, 名字不存在')
```
<a name="ZHtBM"></a>
### 列表添加元素
> **作⽤：增加指定数据到列表中。**

<a name="JbtN6"></a>
#### append()方法用于在列表的末尾追加元素
**语法**
```python
# 列表序列.append(数据)
name_list = ['张三', '李四', '王五','赵六']
name_list.append('阿坤')
print(name_list)
```
> 如果append()追加的数据是⼀个序列，则追加整个序列到列表

```python
name_list = ['张三', '李四', '王五','赵六']
alist = ["唱","跳","rap","篮球"]
name_list.append(alist)
print(name_list)
# ['张三', '李四', '王五', '赵六', ['唱', '跳', 'rap', '篮球']]
```
<a name="PyMAW"></a>
#### extend()方法用于在列表的末尾追加或者扩展元素
> **列表结尾追加数据，如果数据是⼀个序列，则将这个序列的数据逐⼀添加到列表。**

```python
name_list = ['张三', '李四', '王五','赵六']
name_list.extend('阿坤')
print(name_list)
# ['张三', '李四', '王五', '赵六', '阿', '坤']
```
> **如果添加一个序列，则会将序列里面每一个元素添加进去**

```python
name_list = ['张三', '李四', '王五','赵六']
alist = ["唱","跳","rap","篮球"]
name_list.extend(alist)
print(name_list)
```
<a name="jveYT"></a>
#### insert()指定位置新增数据。
**语法**
```python
# 列表序列.insert(位置下标, 数据)
name_list = ['张三', '李四', '王五','赵六']
name_list.insert(1, '阿坤')
# 结果：['张三','阿坤', '李四', '王五','赵六']
print(name_list)
```
<a name="t16kP"></a>
### 删除列表元素
<a name="lIGya"></a>
#### del 

- **是 Python 中的关键字，专门用来执行删除操作，它不仅可以删除整个列表，还可以删除列表中的某些元素。**
```python
name_list = ['张三', '李四', '王五','赵六']
del name_list
print(name_list)
```
**删除指定数据**（根据索引删除）
```python
name_list = ['张三', '李四', '王五','赵六']
del name_list[1]
print(name_list)
# ['张三', '王五', '赵六']
```
<a name="oEfnE"></a>
#### pop()
**删除指定下标的数据(默认为最后⼀个)，并返回该数据。**
```python
name_list = ['张三', '李四', '王五','赵六']
name_list.pop(1)
print(name_list)
# ['张三', '王五', '赵六']
```
<a name="zdu2d"></a>
#### remove()
**根据元素值进行删除移除列表中某个数据的第⼀个匹配项。**
```python
# 列表序列.remove(数据)
name_list = ['张三', '李四', '王五','赵六']
name_list.remove("张三")
print(name_list)
# ['李四', '王五', '赵六']
```
<a name="Jzmi0"></a>
#### clear()
**清空列表**
```python
name_list = ['张三', '李四', '王五','赵六']
name_list.clear()
print(name_list)
# []
```
<a name="8347a927"></a>
### 修改列表元素
**Python 支持通过切片语法给一组元素赋值。在进行这种操作时，如果不指定步长（step 参数），Python 就不要求新赋值的元素个数与原来的元素个数相同；这意味，该操作既可以为列表添加元素，也可以为列表删除元素。**
<a name="tjmR5"></a>
####  修改单个与一组元素
```python
name_list = ['张三', '李四', '王五','赵六']
name_list[0] = '阿坤'
print(name_list)

nums = [40, 36, 89, 2, 36, 100, 7]
#修改第 1~4 个元素的值（不包括第4个元素）
nums[1: 4] = [45.25, -77, -52.5]
print(nums)
```
<a name="c4jn8"></a>
#### reverse()函数的使用
**逆置**
```python
num_list = [1, 5, 2, 3, 6, 8]
num_list.reverse()
print(num_list)
# [8, 6, 3, 2, 5, 1]
```
<a name="V4KsU"></a>
#### sort()函数的使用
**排序**<br />**语法**
> **reverse表示排序规则，reverse = True 降序， reverse = False 升序（默认）**

```python
# 列表序列.sort(reverse=False)
li = [2,3,5,6,1,4,8]
li.sort(reverse=False)
print(li)
# [1, 2, 3, 4, 5, 6, 8]

li.sort(reverse=True)
print(li)
# [8, 6, 5, 4, 3, 2, 1]
```
<a name="9dcb6e51"></a>
### 列表的**复制**
<a name="WTTUL"></a>
#### copy()函数的使用
复制一个列表
```python
name_list = ['张三', '李四', '王五','赵六']
name_li2 = name_list.copy()
print(name_li2)
# ['张三', '李四', '王五','赵六']
```
<a name="332c51aa"></a>
## 列表的循环遍历
**依次打印列表中的各个数据**<br />**for循环**

```python
name_list = ['张三', '李四', '王五','赵六']
for i in name_list:
    print(i)
```
**while循环**
```python
i = 0
name_list = ['Tom', 'Lily', 'Rose']
while i < len(name_list):
    print(name_list[i])
    i += 1
```
<a name="379c1abe"></a>
## 列表的嵌套
> 所谓列表嵌套指的就是⼀个列表⾥⾯包含了其他的⼦列表

```python
# 找到篮球
name_list = [['张三', '李四', '阿坤'], ['唱', '跳', '篮球'], ['甲', '乙', '丙']]
# 第⼀步：按下标查找到篮球所在的列表
print(name_list[1])
# 第⼆步：从李四所在的列表⾥⾯，再按下标找到数据李四
print(name_list[1][2])
```
<a name="cda9f200"></a>
# 元组
> **思考：如果想要存储多个数据，但是这些数据是不能修改的数据，怎么做？**

<a name="15fde6a1"></a>
## 元组的创建
**Python 的元组与列表类似，不同之处在于元组的元素不能修改。元组使用小括号，列表使用方括号。**<br />**元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。**
```python
使用 ( ) 直接创建
# 多个数据元组
t1 = (10, 20, 30)
# 单个数据元组
t2 = (10,)
使用tuple()函数创建元组
tup1 = tuple("hello")
print(tup1)
```
> 注意：如果定义的元组只有⼀个数据，那么这个数据后⾯也好添加逗号，否则数据类型为唯⼀的这个数据的数据类型

<a name="93850362"></a>
## 元组的常⻅操作
> **元组数据不⽀持修改，只⽀持查找，具体如下**

- 根据下标查找
```python
tuple1 = ('aa', 'bb', 'cc', 'bb')
print(tuple1[0])
```

- **index()：**

**查找某个数据，如果数据存在返回对应的下标，否则报错，语法和列表、字符串的index⽅法相同。**
```python
tuple1 = ('aa', 'bb', 'cc', 'bb')
print(tuple1.index('aa'))
```

- **count()：**

**统计某个数据在当前元组出现的次数。**
```python
tuple1 = ('aa', 'bb', 'cc', 'bb')
print(tuple1.count('bb'))
```

- **len()：**

**统计元组中数据的个数。**
```python
tuple1 = ('aa', 'bb', 'cc', 'bb')
print(len(tuple1))
```
**元组内的直接数据如果修改则⽴即报错**<br />**但是如果元组⾥⾯有列表，修改列表⾥⾯的数据则是⽀持的。**
```python
tuple2 = (10, 20, ['aa', 'bb', 'cc'], 50, 30)
print(tuple2[2]) # 访问到列表
# ['aa', 'bb', 'cc']
tuple2[2][0] = 'aaaaa'
print(tuple2)
# (10, 20, ['aaaaa', 'bb', 'cc'], 50, 30)
```

- **del 同样支持**

**当创建的元组不再使用时，可以通过 del 关键字将其删除**
```python
tup = ("python"，"yyds")
print(tup)
del tup
print(tup)
```
<a name="HOtE0"></a>
# 列表与元组的区别

- **列表是动态数组，它们可变且可以重设长度（改变其内部元素的个数）。**
- **元组是静态数组，它们不可变，且其内部数据一旦创建便无法改变。**
- **元组缓存于Python运行时环境，这意味着我们每次使用元组时无须访问内核去分配内存。**
- **可变与不可变性**
   - **列表：可变**
   - **元组：不可变**
<a name="UDgeQ"></a>
# 什么是可变类型与不可变类型？
**可变数据类型 ：当该数据类型的对应变量的值发生了改变，那么它对应的内存地址不发生改变，对于这种数据类型，就称可变数据类型。**<br />**不可变数据类型： 当该数据类型的对应变量的值发生了改变，那么它对应的内存地址也会发生改变，对于这种数据类型，就称不可变数据类型。**

```python
"""数值"""
a = 1
print(a, id(a))
a = a + 1
print(a, id(a))
"""字符串"""
b = '1'
print(b, id(b))
b = b.upper()
print(b, id(b))
"""列表"""
li = [1, 2, 3, 4, 5]
print(li, id(li))
li.append(6)
print(li, id(li))
"""元组"""
tup = (1, 2, 3, [4, 5])
print(tup, id(tup))
tup[-1].append(6)
print(tup, id(tup))

```




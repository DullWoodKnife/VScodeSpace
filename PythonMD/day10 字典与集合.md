<a name="frnvw"></a>
# 字典
<a name="716863df"></a>
## 字典的介绍
**字典(Dictionary)是Python提供的一种常用的数据结构，由键（key）和值（value）成对组成，键和值中间以冒号：隔开，项之间用逗号隔开，整个字典由大括号{}括起来**。

**一个班级，100人，如何快速存储姓名，性别，年龄？**
> **字典⾥⾯的数据是以键值对形式出现，字典数据和数据顺序没有关系，即字典不⽀持下标，后期⽆论数据如何变化，只需要按照对应的键的名字查找数据即可。**


```python
姓名：张三，年龄：22，性别：男
姓名：李四，年龄：21，性别：男
姓名：王五，年龄：24，性别：男
姓名：阿坤，年龄：25，性别：男
```
<a name="69665763"></a>
## 字典的创建

- **符号为大括号**
- **数据为键值对形式出现**
- **各个键值对之间用逗号隔开**
<a name="mohvd"></a>
#### 手动方式创建 
```python
# 有数据字典
dict1 = {'name': '张三', 'age': 20, 'gender': '男'}
```
> **注意：⼀般称冒号前⾯的为键(key)，简称k；冒号后⾯的为值(value)，简称v。**

<a name="ZjSFV"></a>
#### 使用内置函数dict()创建
```python
a_dict = dict(name='DYX', age=24)  # 键=值对
print(a_dict)  # {'age': 24, 'name': 'DYX'}
```
<a name="2783c0bd"></a>
## 字典常见操作
<a name="hAyfc"></a>
### 查找数据
<a name="fg5Rf"></a>
##### key根据键查找值
**与列表类似，可以使用下标的方式来访问字典中的元素，但不同的是字典的下标是字典的“键”，而列表和元组访问时下标必须为整数值。使用下标的方式访问字典“值”时，若指定的键不存在则抛出异常。**
```python
dict1 = {'name': '张三', 'age': 20, 'gender': '男'}
print(dict1['name']) # 张三
print(dict1['id']) # 报错
```
<a name="sg93h"></a>
##### get()
**使用字典对象的get()方法可以获取指定”键“对应的”值”，并且可以在指定“键“不存在的时候返回指定值，如果不指定，则默认返回None。相对于上文的方法，该方法更安全。**
```python
# 字典序列.get(key, 默认值)
dict1 = {'name': '张三', 'age': 20, 'gender': '男'}
print(dict1.get('name')) # 张三
print(dict1.get('id', 110)) # 110
print(dict1.get('id')) # None
```
<a name="j1316"></a>
##### keys()**查找所有的键**
```python
dict1 = {'name': '张三', 'age': 20, 'gender': '男'}
print(dict1.keys()) # dict_keys(['name', 'age', 'gender'])
```
<a name="h7PDE"></a>
##### values()查找所有的值
```python
dict1 = {'name': '张三', 'age': 20, 'gender': '男'}
print(dict1.items()) # dict_items([('name', '张三'), ('age', 20), ('gender','男')])
```
<a name="UiHu8"></a>
##### items()
```python
dict1 = {'name': '张三', 'age': 20, 'gender': '男'}
print(dict1.items()) # dict_items([('name', '张三'), ('age', 20), ('gender','男')])
```
<a name="cd7c2aa3-1"></a>
### 增加与修改数据
<a name="c3eOo"></a>
#### 字典序列[key] = 值
> **注意：如果key存在则修改这个key对应的值；如果key不存在则新增此键值对。**

```python
dict1 = {'name': '张三', 'age': 20, 'gender': '男'}
dict1['name'] = '李四'
print(dict1)
# 结果：{'name': '李四', 'age': 20, 'gender': '男'}

dict1['id'] = 110
print(dict1)
# {'name': '李四', 'age': 20, 'gender': '男', 'id': 110}
```
> **注意：字典为可变类型。**

<a name="gIyyt"></a>
#### update()方法添加键值对
**字典对象的update()方法，可以将另一个字典全部添加到当前字典中，如果两个字典中存在相同的“键”，则以另一个字典中的“值”为准，对当前字典进行更新。**
```python
a_dict = { 'ranking': [98, 97] ,  'age': 24 ,  'name': 'DYX' ,  'sex': 'male' }
#字典中的“值”可以是列表、数字、字符串元组等等,是很宽泛的
#字典中的“键”要注意不能使用列表、集合、字典作为字典的“键”
print(a_dict.items())
#dict_items([('sex', 'male'), ('age', 24), ('name', 'DYX'), ('ranking', [98, 97])])
a_dict.update( {'a':'a','b':'b'} )  
print(a_dict)  #查看添加后的字典
#{'sex': 'male', 'age': 24, 'ranking': [98, 97], 'name': 'DYX', 'a': 'a', 'b': 'b'}
```
<a name="40f8f022-1"></a>
### 删除数据
<a name="ooD5E"></a>
#### del：**删除字典或删除字典中指定键值对**
```python
dict1 = {'name': '张三', 'age': 20, 'gender': '男'}
del dict1['gender']
print(dict1)
# {'name': '张三', 'age': 20}

del(dict1)
print(dict1)
# NameError: name 'dict1' is not defined
```
<a name="yUtHq"></a>
#### clear():**清空字典**
```python
dict1 = {'name': '张三', 'age': 20, 'gender': '男'}
dict1.clear()
print(dict1) # {}
```
<a name="SzsUP"></a>
#### pop()方法
**pop()方法删除并返回指定“键”的元素。**
```python
dict1 = {'name': '张三', 'age': 20, 'gender': '男'}
dict1.pop('name')
print(dict1) # {}
```
<a name="JhL9P"></a>
## for循环遍历字典
<a name="cd6c01bd"></a>
### 遍历字典的key
```python
dict1 = {'name': '张三', 'age': 20, 'gender': '男'}
for key in dict1.keys():
    print(key)
# name
# age
# gender
```
<a name="c670bff0"></a>
### 遍历字典的value
```python
dict1 = {'name': '张三', 'age': 20, 'gender': '男'}
for value in dict1.values():
    print(value)
# 张三
# 20
# 男
```
<a name="b219c288"></a>
### 遍历字典的元素
```python
dict1 = {'name': '张三', 'age': 20, 'gender': '男'}
for value in dict1.items():
    print(value)
    
# ('name', '张三')
# ('age', 20)
# ('gender', '男')
```
<a name="JtsIQ"></a>
# 集合
**集合（set）是一个无序的不重复元素序列。**<br />**可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。**
<a name="WnERn"></a>
## 集合的创建
> **创建集合使⽤ {} 或 set() ， 但是如果要创建空集合只能使⽤ set() ，因为 {} ⽤来创建空字典。**

```python
s1 = {10, 20, 30, 40, 50}
print(s1)

s2 = {10, 30, 20, 10, 30, 40, 30, 50}
print(s2)

s3 = set('abcdefg')
print(s3)

s4 = set()
print(type(s4)) # set

s5 = {}
print(type(s5)) # dict
```

- 集合可以去掉重复数据；
- 集合数据是⽆序的，故不⽀持下标
<a name="zpkpA"></a>
## 集合常见操作方法
<a name="RiT3f"></a>
### 增加数据
<a name="BBifK"></a>
#### add()
**需要注意的是，使用 add() 方法添加的元素，只能是数字、字符串、元组或者布尔类型（True 和 False）值，不能添加列表、字典、集合这类可变的数据，否则 Python 解释器会报 TypeError 错误。**
```python
s1 = {10, 20}
s1.add(100)
s1.add(10)
print(s1)
```
> **因为集合有去重功能，所以，当向集合内追加的数据是当前集合已有数据的话，则不进⾏任何操作**

<a name="JVwdw"></a>
#### update()
**追加的数据是序列。**
```python
s1 = {10, 20}
# s1.update(100) # 报错
s1.update([100, 200])
s1.update('abc')
print(s1)
```
<a name="wVdzc"></a>
### 删除数据
<a name="zRcEx"></a>
#### remove()
**删除集合中的指定数据，如果数据不存在则报错。**
```python
s1 = {10, 20}
s1.remove(10)
print(s1)

s1.remove(10) # 报错
print(s1)
```
<a name="pYFYZ"></a>
#### discard()
**删除集合中的指定数据，如果数据不存在也不会报错。**
```python
s1 = {10, 20}
s1.discard(10)
print(s1)

s1.discard(10)
print(s1)
```
<a name="MYCp4"></a>
#### pop()
**随机删除集合中的一个数据，并返回这个数据。**
```python
s1 = set('12345')
del_num = s1.pop()
print(del_num)
print(s1)
```
<a name="kKwAf"></a>
### 查找数据
**in：判断数据在集合序列**<br />**not in：判断数据不在集合序列**

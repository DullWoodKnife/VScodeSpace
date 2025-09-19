<a name="52cefcb2"></a>
# 文件操作
<a name="zp5AZ"></a>
## 文件操作介绍
在实际操作中，通常需要将数据写入到本地文件或者从本地文件中读取数据等操作，那么作为Python爱好者的我们，必须掌握用Python语言去对本地文件进行操作。<br />比如<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/704747/1585205581278-58b231b9-eeaa-4e5b-8b58-cd3b0986d859.png#averageHue=%23f6f2f0&height=248&id=dWtfm&name=image.png&originHeight=893&originWidth=1049&originalType=binary&ratio=1&rotation=0&showTitle=false&size=639937&status=done&style=none&title=&width=291)
<a name="M7Dj5"></a>
## 本地文件操作步骤

- 找到文件所在位置
- 打开文件
- 操作文件
- 关闭文件
<a name="w9Ez7"></a>
## 文件操作的作用
> **⽂件操作包含：打开、关闭、读、写、复制......**
> **⽂件操作的的作用是：读取内容、写⼊内容、备份内容......**

文件操作的作用就是把⼀些内容(数据)存储存放起来，可以让程序下⼀次执行的时候直接使用，而不必重新制作⼀份，省时省力 。
<a name="kuEGr"></a>
## 打开open()函数
在python，使⽤open()函数，可以打开⼀个已经存在的文件，或者创建⼀个新文件，语法如下：<br />**open(file, mode='r',encoding=None)   -->  打开文件**

- **file **                      --> 文件路径
- **mode **                  --> 操作文件模式
   - r                     --> 只读模式
   - w                    --> 写入
   - a                     --> 追加
- **encoding**             --> 指定文件编码
   - utf-8               --> 当文件中文乱码时，则指定编码为utf-8解决。

> **file：是要打开的目标文件名的字符串(可以包含文件所在的具体路径)。**<br />**mode：设置打开文件的模式(访问模式)：只读、写入、追加等。**

| 模式 | 描述 |
| --- | --- |
| r | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。 |
| rb | 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。 |
| r+ | 打开一个文件用于读写。文件指针将会放在文件的开头。 |
| rb+ | 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。 |
| w | 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb | 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。 |
| w+ | 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb+ | 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。 |
| a | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| ab | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| a+ | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。 |
| ab+ | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。 |

<a name="S3KRi"></a>
## 文件对象方法
<a name="hMfuq"></a>
#### 只写模式w

- **f.writable() **         -->  判断是否可写
- **f.write(str) **          -->  写入内容，返回值为写入字符串的长度
- **f.writelines(seq) ** --> 写入多行，但需要自己添加换行符

**注意**

- w模式，当文件不存在时创建文件
- 再次写入会覆盖
```python
f = open('filetest.txt', mode='w', encoding='utf-8')

# 判断是否可写
print(f.writable())
# 写入内容
f.write('i am yueyue\nasdasda\n')
# 写入多行
f.writelines('I love You\nasdasdasdsad')
# 关闭文件
f.close()
```
<a name="kGrwG"></a>
#### 追加模式a
**注意**

- a模式，当文件不存在时创建文件
- 再次写入为追加
```python
f = open('filetest.txt', mode='a', encoding='utf-8')
# 判断是否可写
print(f.writable())
# 写入内容
f.write('i am yueyue\nasdasda\n')
# 写入多行
f.writelines('I love You\nasdasdasdsad')
# # 关闭文件
f.close()
```
> **w 和 a 模式：如果文件不存在则创建该文件；如果文件存在， w 模式先清空再写入， a 模式直接末尾追加。**

<a name="Im6iq"></a>
#### 只读模式r

- **f.readable()**          --> 判断是否可读，返回值为布尔
- **f.read(n)**               --> 读取全部，在python3中n为字符
- **f.readline()**           --> 逐行读取，包括\n
- **f.readlines()**          --> 读取所有，返回值为列表，包括\n
- **f.tell()                   **--> 文件指针所处文件位置
- **seek()                   --> **作用：用来移动文件指针
```python
f = open('filetest.txt', mode='r', encoding='utf-8')
# 判断是否可读
print(f.readable())
# 逐行读取
print(f.readline(),end='')
# 读取所有 返回值为列表
print(f.readlines())
# # 读取文件全部内容
print(f.read())
```
**tell的使用**
```python
f = open("filetest.txt", mode="r", encoding="utf-8")
'''
filetest2.txt
helloworld
你好
'''
# 汉字代表三个字节 换行代表两个字节  字母数字代表的是一个字节
print(f.tell())
print(f.readline(), end="")
print(f.tell())
print(f.readline())
print(f.tell())



```
**seek的使用**
```python
f = open("filetest.txt", mode="rb")
'''
filetest2.txt
helloworld
你好
'''


# 改变指针位置
"""
offset: 偏移量
whence: 0 从文件头开始  1 当前位置开始  2 文件尾
注意，当offset值非0时，Python要求文件必须要以二进制格式打开，
否则会抛出 io.UnsupportedOperation 错误。
"""
print(f.tell())
# 读取一个字节，文件指针自动后移1个数据
print(f.read(1))
print(f.tell())
# 将文件指针从文件开头，向后移动到 5 个字符的位置
f.seek(5)
print(f.tell())
print(f.read(1))
# 将文件指针从当前位置，向后移动到 5 个字符的位置
f.seek(5, 1)
print(f.tell())
print(f.read(1))
# 将文件指针从文件结尾，向前移动到距离 2 个字符的位置
f.seek(-1, 2)
print(f.tell())
print(f.read(1))

```
<a name="b9cf5461"></a>
### 文件备份
需求：用户输入当前目录下任意文件名，程序完成对该文件的备份功能(备份文件名为xx备份后缀，例如：test备份.txt)

1. 接收用户输入的文件名
2. 规划备份文件名
3. 备份文件写入数据
<a name="83175ad0"></a>
#### 代码实现
**接收用户户输入目标文件名**<br />	1、提取目标文件后缀<br />	2、组织备份的文件名，xx备份.后缀
```python
old_name = input("请输入文件名:")
index = old_name.rfind(".")
new_name = old_name[:index]+"备份"+old_name[index:]
```
**备份文件写入数据**<br />	 1、打开源文件 和 备份文件<br />       2、将源文件数据写⼊备份文件<br />       3、关闭文件<br />代码演示
```python
old_name = input("请输入文件名:")
index = old_name.rfind(".")
new_name = old_name[:index]+"备份"+old_name[index:]

# 老文件
old_f = open(old_name,"r")
# 新文件
new_f = open(new_name,"w")

cont = old_f.readlines()
print(cont)
new_f.writelines(cont)

old_f.close()
new_f.close()
```
<a name="d7ba04b0"></a>
## 文件和文件夹的操作
> 在Python中文件和文件夹的操作要借助os模块里面的相关功能，具体步骤如下

**os.getcwd()           --> **用来打印当前工作目录<br />**os.chdir()              -->  **改变当前工作目录<br />**os.makedirs()        -->  **以递归方式创建多个文件夹<br />**os.removedirs()    -->   **以递归方式删除多个空文件夹<br />**os.mkdir()             -->  **创建单个文件夹<br />**os.rmdir()             -->   **删除单个空文件夹<br />**os.path.exists()     -->   **判断该路径下的文件或文件夹是否存在<br />**os.path.join()        -->   **拼接路径<br />1、导入os模块
```python
import os
```
⽂件重命名
```python
os.rename(⽬标⽂件名, 新⽂件名)
```
删除⽂件
```python
os.remove(⽬标⽂件名)
```
创建⽂件夹
```python
os.mkdir(文件名名字)
```
删除⽂件夹
```python
os.rmdir(⽂件夹名字)
```
获取当前⽬录
```
os.getcwd()
```
改变默认⽬录
```
os.chdir(⽬录)
```
获取⽬录列表
```
os.listdir(⽬录)
```
<a name="ca8abd87"></a>
## 批量重命名
**文件夹添加字符串**
```python
import os

# 先切换路径  
os.chdir('testsad')
print(os.getcwd())
# 遍历此路径下的文件
file_list = os.listdir(os.getcwd())
print(file_list)
for file in file_list:
    # 循环拼接
    new_name = "python_" + file
    # print(new_name)
    os.rename(file,new_name)
```

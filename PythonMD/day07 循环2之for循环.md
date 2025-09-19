<a name="NDftH"></a>
# 缩进补充
在 Python 中，对于类定义、函数定义、**流程控制语句**、异常处理语句等，行尾的冒号和下一行的缩进，表示下一个代码块的开始，而缩进的结束则表示此代码块的结束。<br />	注意，Python 中实现对代码的缩进，可以使用空格或者 Tab 键实现。但无论是手动敲空格，还是使用 Tab 键，通常情况下都是采用 4 个空格长度作为一个缩进量（默认情况下，一个 Tab 键就表示 4 个空格）。
```python
dream = int(input('请输入你的愿望选项:'))
if dream == 1:
    print('有钱')
elif dream == 2:
    print('时光倒流')
elif dream == 3:
    print('和岳岳结婚')
elif dream == 4:
    print('长生')
elif dream == 5:
    print('钢铁的肾')
else:
    print('你在做梦！')

```
Python 对代码的缩进要求非常严格，同一个级别代码块的缩进量必须一样，否则解释器会报 SyntaxError 异常错误。
<a name="bx0sl"></a>
# 语句与代码块补充
语句由关键字、标识符、表达式组成。
```python
a = 1
print(a)
print(1)
```
而代码块由若干条语句组成。通常Python中的代码块是通过缩进来创建的。
```python
age = 18
if age>=18:
    print('你已经成年了！')

```
在Python中，使用冒号:指出接下来是一个代码块，并将该代码块中的每行代码都缩进相同的程度。发现缩进量与之前相同时，你就知道当前代码块到此结束了。<br />使用缩进来表示新的代码块是Python语言的特色之一。

<a name="NvAzI"></a>
# pass占位符补充
python3中的pass语句是一个空语句，什么都不做，执行它时什么也没有发生，是一个空操作。<br />      pass语句通常用作占位符(place-holder)，即当用户不知道要编写什么代码时，用户只需在那行上放置pass。<br />      在语法上需要有条语句但是确不希望执行任何命令或代码时可以使用pass。用户可以简单地将pass放置在不允许空代码的地方，例如函数定义、类定义(通常用于创建最小类)、循环或if语句中。用户使用pass语句可以避免这个错误。
<a name="xqIQT"></a>
# while...else
Python中的循环可以和else配合使用，else下方缩进的代码指的是**当循环正常结束之后要执行的代码**。
<a name="Wjrod"></a>
### 语法规则
```python
while 条件:
    条件成立重复执行的代码
else:
    循环正常结束之后要执行的代码
```
<a name="e8yJP"></a>
### while...else之终止与退出循环 
```python
i = 1
while i <= 5:
    if i == 3:
        print('这遍道歉说的不真诚')
        break
    print('媳妇，我错了')
    i += 1
else:
    print('媳妇原谅我了,哈哈哈')

总结： 所谓else指的是循环正常结束之后要执行的代码，即如果是break终止循环的情况，
else下方缩进的代码将不执行。

i = 1
while i <= 5:
    if i == 3:
        i += 1  # 当用到continue时，计数器一定要加上，不然会出现死循环
        continue
    print('媳妇，我错了')
    i += 1
else:
    print('媳妇原谅我了,哈哈哈')

总结：因为continue是退出当前你一次循环，继续下一次循环，所以该循环在continue控制下是可以正常结束的，
当循环结束后，则执行了else缩进的代码。
```
<a name="aad25aa1"></a>
# for...in...循环
> **Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。**
> for-in遍历的对象必须是**可迭代**对象。

<a name="fUaCu"></a>
### 语法规则
```python
for 临时变量 in 待处理数据集:
	重复执行代码
```
> 理论上来讲，for循环无法构建无限循环(待处理的数据集不可能无限大)

**实例**
```python
# 遍历字符串
for i in 'Python':     # 第一个实例
    print(i)
```
> 可以看出for循环是将字符串的内容**依次取出**，所以for循环也被称之为**遍历循环**

**练习**
```python
# 字符串 name = "hello world python i love you"
# 通过for循环遍历所有的o
name = "hello world python i love you"
for i in name:
    if i == "o":
        print(i)
```

---

<a name="d18c2f48"></a>
# range()函数
> for循环本质上是遍历**“序列类型”**，但是，使用**range**函数，可以获得一个简单的**数字序列**

**语法：**
```python
range(num)
# 获得一个从0开始，到num结束的数字序列(不含num本身)
# 例如range(5),获得的数据是[0,1,2,3,4]

range(num1,num2)
# 获取一个从num1开始，到num2结束的数字序列(不含num2本身)
# 例如range(2,8)，获得的数据是[2,3,4,5,6,7]
 
range(num1,num2,step)
# 获取一个从num1开始，到num2结束的数字序列(不含num2本身)
# step 为步长，默认为1
# 例如range(1,10,2)，获取到的数据是[1,3,5,7,9]

num1 = 10
num2 = 0
range(num1,num2,-1)
# 从10到1,依次打印,（不含num2本身）
# range(10,0,-1),获取到的数据是[10,9,8,7,6,5,4,3,2,1]
```
<a name="480c216f"></a>
## 实例
```python
# 输出0~9
for i in range(10):
    print(i)
    
# 输出1~100
for i in range(1,101)

# 输出1~100，每次跳过一个数字
for i in range(1,101,2):
    print(i)
```
<a name="9df708ac"></a>
# for循环的嵌套应用
**生活中的嵌套**
> 和女朋友吵架，每天道歉10遍，持续5天

```python
for 临时变量 in 待处理数据集:
    重复执行代码一
    重复执行代码二
    重复执行代码三
	for 临时变量 in 待处理数据集:
        重复执行代码三
        重复执行代码三
        重复执行代码三
```

- **坚持道歉5天**
- **每天道歉10遍**
```python
for i in range(1,6):
    print(f"这是我第{i}天的道歉")
    for j in range(1,11):
        print(f"老婆，我错了，这是我今天的第{j}次道歉")
    print(f"老婆，第{i}天的道歉结束。。。")

print(f"我已经道歉了{i}天了，老婆不生气了")
```
**for循环和while循环配合使用**
```python
for i in range(1,6):
    print(f"这是我第{i}天的道歉")
    j = 1
    while j<=10:
        print(f"老婆，我错了，这是我今天的第{j}次道歉")
        j+=1
    print(f"老婆，第{i}天的道歉结束。。。")
```

---

<a name="458345fb"></a>
# break和continue
while循环和for循环都是重复性的执行特定的操作，在这个过程中，会出现一些其他情况，让我们不得不

-  跳过这次循环，进入下一次循环 
-  终止当前循环  
<a name="continue"></a>
## continue
> 中断本次循环，进入下一次循环

```python
# 碰见7的倍数直接跳过
for i in range(100):	# 遍历出0~99
    if i % 7 == 0:		# 判断i是7的倍数
        continue		# 满足条件直接跳过
    print(i)			# 打印出其余的数字
```
<a name="break"></a>
## break
> 终止循环，结束当前循环

```python
# 当马自达刷完后直接停止，因为后面是劳斯莱斯
li = ["马自达","马自达","马自达","劳斯莱斯","劳斯莱斯","劳斯莱斯","劳斯莱斯"]
for i in li:
    if i == "劳斯莱斯":
        print("碰见劳斯莱斯了")
        break
    print("正在刷马自达。。。")
```

---

<a name="fSKFP"></a>
# 练习
<a name="VAA3z"></a>
## 1~100偶数的和
<a name="Pt72Y"></a>
## 求5的阶乘！
<a name="wvYFK"></a>
## 9*9乘法表

<a name="69bdc66b"></a>
# 循环
> 将事物循环执行

**作用**<br />思考：假如我有个⼥朋友，有⼀天我们闹⽭盾⽣⽓了，⼥朋友说：道歉，说100遍“媳妇⼉，我错了”。这个时候程序员会怎么做？<br />答：100遍 print('媳妇⼉，我错了')<br />思考：复制粘贴100次吗？<br />答：重复执⾏100次⼀样的代码，程序中循环即可
<a name="a6317b46"></a>
## 循环的分类
> Python 提供了 for 循环和 while 循环

| 循环类型 | 描述 |
| --- | --- |
| while | 在给定的判断条件为 true 时执行循环体，否则退出循环体。 |
| for | 重复执行语句 |

<a name="f5684dce"></a>
### 循环控制语句
| 控制语句 | 描述 |
| --- | --- |
| break 语句 | 在语句块执行过程中终止循环，并且跳出整个循环 |
| continue 语句 | 在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。 |
| pass 语句 | pass是空语句，是为了保持程序结构的完整性。 |

<a name="9861eb98"></a>
## while循环
> Python 编程中 while语句用于循环执行程序，即在某条件下，循环执行某段程序，以处理需要重复处理的相同任务

**语法**
```python
while 判断条件：
     执行语句
```
<a name="98656ea0"></a>
### 应用一：输出100次媳妇，我错了
```python
# 循环的计数器
i = 1
while i < 100:
    print('媳妇⼉，我错了')
    i += 1
print('任务结束')
```
<a name="d71f5036"></a>
### 应用二：计算1-100的和
```python
num = 1
result = 0
while num <= 100:
    result += num
    num+=1
print(result)
```
<a name="394ae44b"></a>
### 应用三：计算1-100偶数和
> **2+4+6+8+10+......**

> **偶数即是和2取余结果为0的数字，可以加⼊条件语句判断是否为偶数，为偶数则累加**

**方法一**
```python
num = 1
result = 0
while inum <= 100:
    # 判断num是否能整除2，如果可以，则和result相加
    if num % 2 == 0:
        result += num
    num += 1
print(result)
```
**方法二**
```python
num = 0
result = 0
while num <= 100:
    result += num
    num += 2
print(result)
```
<a name="534f738b"></a>
## break和continue语句
> **案例：**有100辆汽车需要刷漆，一辆一辆刷，就相当于循环过程
> **break：**当刷到第50辆，完成了当天的任务，刷漆的动作就要停止，**这⾥就是break控制循环流程，即终⽌此循环**
> **continue：**我拿的是马自达的油漆，结果第20辆车是劳斯劳斯，所以直接跳过这辆，继续刷马自达，**这⾥就是continue控制循环流程，即退出当前⼀次循环继⽽执⾏下⼀次循环代码**

<a name="27c0a78c"></a>
### 应用一：刷漆-break
```python
i = 1
while i <= 100:
    if i == 51:
        print('完成今天的任务')
        break
    print(f'今天刷了{i}辆车')
    i += 1
```
<a name="1037d86d"></a>
### 应用二：刷漆-continue
```python
i = 1
while i<=100:
    if i == 33:
        print(f"第{i}辆车是劳斯莱斯，跳过")
        i += 1
        continue
    print(f"今天刷了{i}辆车")
    i+=1
```

---

<a name="e5d67abc"></a>
## while循环嵌套
> 思考：和⼥朋友闹⽭盾⽣⽓了，⼥朋友说：道歉，说10遍“媳妇⼉，我错了”，还不够，还要做家务，而且持续三天，这个程序该怎么写？

**一天**
```python
i = 0
while i <= 10:
    print("媳妇儿，我错了")
    i += 1
```
**三天**
```python
j = 1
while j<=3:
    i = 0
    while i<=10:
        print("媳妇，我错了")
        i+=1
    print(f"做第{j}天的家务")
    j += 1
```
<a name="a94b229e"></a>
### 执行流程
> 当内部循环执⾏完成之后，再执⾏下⼀次外部循环的条件判断。

![嵌套循环.png](https://cdn.nlark.com/yuque/0/2023/png/25414438/1675338226224-1a88fb8a-8ab6-4c2e-829c-22585f585743.png#averageHue=%23f8f5f5&clientId=u8e0c10e8-461c-4&from=ui&id=u446ca702&name=%E5%B5%8C%E5%A5%97%E5%BE%AA%E7%8E%AF.png&originHeight=615&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=32673&status=done&style=none&taskId=u002e0f53-a9f3-45e9-bb3c-6f6224162db&title=)

九九乘法口诀表
```python
j = 1
while j <= 9:
    i = 1
    while i<=j:
        print(f'{i}*{j}={i*j}',end='\t')
        i += 1
    print()
    j += 1
```

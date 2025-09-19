![image.png](https://cdn.nlark.com/yuque/0/2023/png/25414438/1675315062067-80ead610-3d2a-4d32-acd0-f3c51357c727.png#averageHue=%23e9e9e8&clientId=u42503729-203a-4&from=paste&height=235&id=u67e4ae22&name=image.png&originHeight=226&originWidth=767&originalType=binary&ratio=1&rotation=0&showTitle=false&size=17524&status=done&style=none&taskId=u384a4e1e-00ee-4237-95b2-eea7cfe7ee0&title=&width=797.8799743652344)

<a name="nJBhC"></a>
# 运算符

- 算数运算符
- 赋值运算符
- 复合赋值运算符
- ⽐较运算符
- 逻辑运算符
<a name="rpLTJ"></a>
## 算数运算符
| **符号** | **描述** | **实例** |
| --- | --- | --- |
| + | 加 | print(1+1) 输出结果为2 |
| - | 减 | print(1-1) 输出结果为0 |
| * | 乘 | print(2*2) 输出结果为4 |
| / | 除 | print(4/2) 输出结果为2 |
| // | 整除 | print(9//4) 输出结果为2 |
| % | 取余 | print(9//4) 输出结果为1 |
| ** | 乘方 | print(2**4) 输出结果为16 |
| （） | 优先级 | print((1+1)*3) 输出结果为6 |


---


<a name="TD4Mq"></a>
## 赋值运算符
| **运算符** | **描述** | **实例** |
| --- | --- | --- |
| = | 赋值 | 将=右侧的结果赋值给=左侧的变量名 |

**单变量赋值**
```
num = 1
print(num+1)
# 2
```
**多变量赋值**
```python
num1, float1, str1 = 10, 0.5, 'hello world'
print(num1)
print(float1)
print(str1)

# 10
# 0.5
# hello world
```
**多变量相同赋值**
```python
a=b=10
print(a)
print(b)

# 10
# 10
```

---


<a name="YnE6R"></a>
## 复合赋值运算符 
| **运算符** | **描述** | **实例** |
| --- | --- | --- |
| += | 加法赋值运算符 | a+=1等价于a=a+1 |
| -= | 减法赋值运算符 | a-=1等价于a=a-1 |
| *= | 乘法赋值运算符 | a*=1等价于a=ax1 |
| /= | 除法赋值运算符 | a/=1等价于a=a/1 |
| //= | 整除赋值运算符 | a//=1等价于a=a//1 |
| %= | 取余赋值运算符 | a%=1等价于a=a%1 |
| **= | 次方赋值运算符 | a**=1等价于a=axx1 |

**实例**
```python
a = 100
a += 1
# 输出101 a = a + 1,最终a = 100 + 1
print(a)
# 101

b = 2 
b *= 3
# 输出6 b = b * 3,最终b = 2 * 3
print(b) 
c = 10
c += 1 + 2
# 输出13, 先算运算符右侧1 + 2 = 3， c += 3 , 推导出c = 10 + 3
print(c)
```

---


<a name="OlD4a"></a>
## 比较运算符
| **运算符** | **描述** | **实例** |
| --- | --- | --- |
| == | 判断相等。如果两个操作数的结果相等，则条件结果为真(True)，否则条件结果为假(False) | 如a=3,b=3，则（a == b) 为 True |
| != | 不等于 。如果两个操作数的结果不相等，则条件为真(True)，否则条件结果为假(False) | 如a=3,b=3，则（a != b) 为 False |
| > | 运算符左侧操作数结果是否⼤于右侧操作数结果，如果⼤于，则条件为真，否则为假 | 如a=7,b=3，则(a > b) 为 True |
| >= | 运算符左侧操作数结果是否⼤于等于右侧操作数结果，如果⼤于等于，则条件为真，否则为假 | a=3,b=3，则(a >= b) 为 True |
| < | 运算符左侧操作数结果是否小于右侧操作数结果，如果小于，则条件为真，否则为假 | 如a=7,b=3，则(a < b) 为 False |
| <= | 运算符左侧操作数结果是否小于等于右侧操作数结果，如果小于等于，则条件为真，否则为假 | 如a=3,b=3，则(a <= b) 为 True |

**实例**
```python
a = 7 b = 5
print(a == b) # False
print(a != b) # True
print(a < b) # False
print(a > b) # True
print(a <= b) # False
print(a >= b) # True
```

---


<a name="XKuiX"></a>
## 逻辑运算符
| **运算符** | **逻辑表达式** | **描述** | **实例** |
| --- | --- | --- | --- |
| and | a and b | 如果 a 为 False，a and b 返回False | True and False， 返回False。 |
| or | a or b | 如果 a 为 True，a or b 返回True | False or True， 返回True。 |
| not | not b | 如果 b 为 True， not b 返回False | not True 返回 False; not False返回 True |

**实例**
```python
a = 1 
b = 2 
c = 3
print((a < b) and (b < c)) # True
print((a > b) and (b < c)) # False
print((a > b) or (b < c)) # True
print(not (a > b)) # True
```
<a name="h5Ad8"></a>
### 数学之间的逻辑运算符
```python
a = 0 b = 1 c = 2

# and运算符，只要有⼀个值为0，则结果为0，否则结果为最后⼀个⾮0数字
print(a and b) # 0
print(b and a) # 0
print(a and c) # 0
print(c and a) # 0
print(b and c) # 2
print(c and b) # 1

# or运算符，只有所有值为0结果才为0，否则结果为第⼀个⾮0数字
print(a or b) # 1
print(a or c) # 2
print(b or c) # 1
```
<a name="ncJ30"></a>
# 作业
输入两个整型数进行(随便选一个比较运算符)进行比较操作<br />将print(2 and 3 or 4 and 0 or 7 or 8 and 2)每一步的运算拆开

 

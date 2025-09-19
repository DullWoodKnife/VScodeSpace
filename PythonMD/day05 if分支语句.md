<a name="033a52a0"></a>
# 了解条件语句
**假设⼀个场景：**
> 同学们去过⽹吧吗？
> 去⽹吧进⻔想要上⽹必须做的⼀件事是做什么？（考虑重点）
> 为什么要把身份证给⼯作⼈员？
> 是不是就是为了判断是否成年？
> 是不是如果成年可以上⽹？如果不成年则不允许上⽹？

**其实这⾥所谓的判断就是条件语句，即条件成⽴执⾏某些代码，条件不成⽴则不执⾏这些代码。**

---

<a name="6ee2587d"></a>
## if语法
> **如果.... 就....**![if条件.png](https://cdn.nlark.com/yuque/0/2023/png/25414438/1675329449623-5e2582bf-2b0e-41ed-b206-1eb912c9a963.png#averageHue=%23f8f8f8&clientId=u92ad0999-ce9d-4&from=ui&id=u27fa0f09&name=if%E6%9D%A1%E4%BB%B6.png&originHeight=437&originWidth=507&originalType=binary&ratio=1&rotation=0&showTitle=false&size=12346&status=done&style=none&taskId=ua51f2e36-8d8c-41e5-a0bf-edd516fe8a9&title=)

**体验**
```python
if True:
    print('条件成⽴执⾏的代码1')
    print('条件成⽴执⾏的代码2')
# 下⽅的代码没有缩进到if语句块，所以和if条件⽆关
print('我是⽆论条件是否成⽴都要执⾏的代码')
```
**实例**
```python
age = 20
if age >= 18:
    print('已经成年，可以上⽹')
```
```python
# input接受的是字符串，要和18做判断，就要把字符串转化成int类型
age = int(input('请输⼊您的年龄：'))
# 如果输入的数字大于等于18
if age >= 18:
    print(f'您的年龄是{age},已经成年，可以上⽹')
```

---

<a name="if...else..."></a>
## if...else...
> 条件成⽴执⾏if下⽅的代码; 条件不成⽴执⾏else下⽅的代码。
> ![if...else...语法.png](https://cdn.nlark.com/yuque/0/2023/png/25414438/1675329499879-3267093d-8ab8-4492-86ea-322c1a1975ff.png#averageHue=%23f9f9f9&clientId=u92ad0999-ce9d-4&from=ui&id=u7d091657&name=if...else...%E8%AF%AD%E6%B3%95.png&originHeight=523&originWidth=659&originalType=binary&ratio=1&rotation=0&showTitle=false&size=16211&status=done&style=none&taskId=u2eec2adc-fdb2-49d1-8972-d44c67e1e06&title=)

**实例**

```python
age = int(input('请输⼊您的年龄：'))
if age >= 18:
    print('祝您上网愉快')
else:
    print('回家写作业吧')
```

---

<a name="1da5f775"></a>
## if...elif ...else...
当判断条件为多个值时，可以使用以下形式：
```python
# 输入1，玩连连看
# 输入2，玩消消乐
# 输入3，玩贪吃蛇
# 输入4，玩推箱子

game = int(input("请输入你想玩的游戏："))
if game == 1:
    print("已经打开连连看，请开始游戏")
elif game == 2:
    print("已经打开消消乐，请开始游戏")
elif game == 3:
    print("已经打开贪吃蛇，请开始游戏")
elif game == 4:
    print("已经打开推箱子，请开始游戏")

else:
    print("没这个游戏。。。")
```
<a name="2d55d3f1"></a>
## 多重判断
> 思考：中国合法⼯作年龄为18-60岁，即如果年龄⼩于18的情况为童⼯，不合法；如果年龄在18-、60岁之间为合法⼯龄；⼤于60岁为法定退休年龄。

> 多重判断也可以和else配合使⽤。⼀般else放到整个if语句的最后，表示以上条件都不成⽴的时候执⾏的代码。

**实例**
```python
age = int(input('请输⼊您的年龄：'))
if age < 18:
    print('童⼯⼀枚')
elif age >= 18 and age <= 60:
# age >= 18 and age <= 60 可以化简为 18 <= age <= 60
    print('合法⼯龄')
elif age > 60:
    print('可以退休')
```
如果判断需要多个条件需同时判断时，可以使用 or （或），表示两个条件有一个成立时判断条件成功；使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。
<a name="7ef3e52f"></a>
## if嵌套
> 坐公交车，需要花钱，上了车，有座位就坐下，没座位就站着

![](.%5Cimage%5C%E5%B5%8C%E5%A5%97%E6%B5%81%E7%A8%8B.png#id=By2AJ&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)![嵌套流程.png](https://cdn.nlark.com/yuque/0/2023/png/25414438/1675329468716-b2842e77-35dd-48a8-80bb-b1b8923cce6b.png#averageHue=%23f8f8f8&clientId=u92ad0999-ce9d-4&from=ui&id=ue381beaa&name=%E5%B5%8C%E5%A5%97%E6%B5%81%E7%A8%8B.png&originHeight=625&originWidth=679&originalType=binary&ratio=1&rotation=0&showTitle=false&size=28104&status=done&style=none&taskId=u63cce3ec-fcf4-47d9-a07d-eb11033461d&title=)

**实例**

```python
# 假设⽤ money = 1 表示有钱, money = 0表示没有钱; seat = 1 表示有空座，seat = 0 表示没有空座
money = int(input("上车请投币："))
if money == 1:
    print('祝你旅途愉快')
    seat = input("是否有空座：")
    if seat == "yes":
        print('有空座，可以坐下')
    else:
        print('没有空座，站等')
else:
    print('没钱请下车')
```

---

<a name="fe2b5b6e"></a>
## 三目运算

> 三⽬运算符也叫三元运算符或三元表达式。
>  
> 条件成⽴执⾏的表达式 if 条件 else 条件不成⽴执⾏的表达式


**实例**

```python
a = 1
b = 2
c = a if a > b else b
print(c)
```


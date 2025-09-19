# requests

- **图片下载** 
- **post请求**
- **session**



## requests下载图片

**下载图片，需获取到图片的url地址和图片名称，通过向图片url发起请求，之后获取.content**

注意：

> .text返回的是Unicode型的数据。
>
> .content返回的是bytes型也就是二进制的数据。

~~~python
url = “https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png”
response = requests.get(url).content

with open("图片"+".png"，"wb") as f:
    f.write(response)
~~~



## requests发送post请求

**方法：**

~~~python
requests.post(url,data=None)
~~~



### POST请求发送Form表单数据

> **以表单的形式发送post请求**

~~~python
import requests
url = "https://httpbin.org/post"
data = {"json_style":"json_data"}
resp = requests.post(url,json=data)
print(resp.text)

# 结果
"json": null, 
~~~



## json

json.loads()

将json字符串转化为python类型

json.dumps()

将python类型转化为json字符串





## session

session方法是requests库发起请求的一种方法，这种方法会自动保存访问页面得到的cookie值，从而再次访问的时候会自动携带cookie，使得操作cookie方便，不需要我们自己添加cookie了。常用于登录；

**登陆逻辑：**

功能:自动更新请求头信息，常用在账号登录的时候，先访问登录页url，再访问数据提交的url

![](.\image\session逻辑.png)

### session的使用

基本的使用方法与requests.get 相似，使用的session的时候需要先创建session对象

~~~python
session = requests.session()#创建session对象
session.headers=headers#添加请求头
res_ss=session.post(url_login)
~~~

# 作业

获取百度翻译的翻译结果

以面向对象的方式编写






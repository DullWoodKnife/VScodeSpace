# Fiddler 抓包工具



## HTTP代理

所谓的http代理，其实就是代理客户机的http访问，主要代理浏览器访问页面。
代理服务器是介于浏览器和web服务器之间的一台服务器，有了它之后，浏览器不是直接到Web服务器去取回网页而是向代理服务器发出请求，Request信号会先送到代理服务器，由代理服务器来取回浏览器所需要的信息并传送给你的浏览器。

![HTTP代理](./Fiddler 抓包工具/HTTP代理.png)



<center>代理服务器</center>

![Fiddler](Fiddler 抓包工具/Fiddler.png)



## Fiddler

### 安装

官方网站下载安装即可：
	https://www.telerik.com/fiddler

基本可以说目前最为全面和强大的抓包工具就是fiddler了，使用也不算麻烦。

Fiddler也在官网上有提供非常详细的文档和教程，如果使用的时候遇到问题，可以直接查阅官网文档。

### 设置

#### 1.HTTPS的证书

抓包工具抓取HTTPS的包的时候跟HTTP的直接转发是不同的。所以我们需要配置

![http证书1](Fiddler 抓包工具/http证书1.png)





打开后选择HTTPS，勾选上这个选项，然后勾选上下方出现的两个选项。最后再将弹出的窗口都选择yes。

![http证书2](Fiddler 抓包工具/http证书2.png)





#### 2.工具栏

![工具栏](Fiddler 抓包工具/工具栏.png)



1. 给session添加一个注释

   ```python
   comments ---注释
   选择请求然后点击就可以添加注释
   ```

   

2. Replay：将目标session再发送一次

3. 删除session

4. 将断点的session恢复执行

5. Decode：将传输的数据解码成容易阅读的格式

6. Find：查找session

7. Save：将session保存成本地文件

8. Clear Cache：清除缓存

#### 3.Session窗口

![session窗口1](Fiddler 抓包工具/session窗口1.png)



- #：Session的序号
- Result：请求的响应状态码
- Protocol：请求的协议类型
- Host：域名
- URL：请求的url
- Body：响应体的大小
- Caching：缓存方式
- Content-Type：响应的数据类型
- Process：发起请求的进程
- Comments：注释

同时，每一个session都有不同的颜色，不同的颜色代表不一样的session类型

![session窗口2](Fiddler 抓包工具/session窗口2.png)



#### 4.Inspectors标签页

![inspectors](Fiddler 抓包工具/inspectors.png)

**请求数据窗口**

1. Headers：报头
2. TextView：查看文本数据
3. Syntax：根据语法格式查看
4. WebForms：Web表单
5. HexView：查看十六进制数据
6. Cookies：查看请求的Cookies
7. Json：查看json格式数据

**响应数据窗口**

1. Transformer：解压方式
2. Headers：报头
3. TextView：查看文本数据
4. Syntax：根据语法格式查看
5. ImageView：查看图片
6. WebView：网页预览图
7. HexView：查看十六进制数据
8. Cookies：查看响应设置的Cookies
9. Json：查看json格式数据

#### 5.Filters选项

我们在抓包的时候常常会遇到非常杂乱的请求，而我们需要去分析的往往只是其中很小的一部分，那么我们就需要从许多请求中过滤出我们需要的那些请求。

1. 是否使用Filters。
2. Filters的规则是可以保存和加载的，也就是我们可以把规则保存下来以后再用。
3. 根据Host域名来进行筛选。
4. 根据客户端的进程来进行筛选。
5. 根据请求的Headers来进行筛选。
6. 断点：Fiddler的断点功能能够让请求在发送后，或者是在返回时暂停，这时候就能够对请求和响应进行相应的修改。
7. 根据响应的状态码筛选。
8. 根据响应的类型和大小来进行筛选。
9. 根据响应的Headers来进行筛选。

#### 6.Find查找

使用快捷键ctrl+f或者在工具栏中选择find来打开查找窗口，查找窗口可以从所有session中搜索到我们想要的session.

![find查找](Fiddler 抓包工具/find查找.png)

1. 文本输入框。
2. 可以选择搜索的范围，限定在仅Requests或者response中，也可以选择限定在headers或bodies中。
3. 是否区分大小写。
4. 是否用正则表达式来搜索。
5. 仅仅搜索被选中的session。
6. 将搜索到的结果高亮，可以选择颜色。

#### 7.命令行查找

![命令行查找](Fiddler 抓包工具/命令行查找.png)

在Fiddler中同样也是可以使用命令行来进行搜索的，在图中的黑框中输入命令即可。

1. select命令：搜索相应类型的session，也就是content-type。
2. ？命令：根据URL来进行搜索。
3. =命令：根据状态码来进行搜索
4. @ 根据域名来搜索

## app抓包

### 详细步骤

1、安装fiddler，并且进行配置：
    Tools >> options >> connections >> 勾选 allow remote computers to connect

2、查看本机ip地址：    
  在cmd窗口中，输入 ipconfig  ，查看  以太网 ，可以看到
IPv4 地址...............：172.16.210.240
这个172.16.*.***（172.16.210.240） 就是你的本机IP

3、确保手机连接了wifi，并且和电脑是在同一个局域网，
  在手机中，打开浏览器，访问
http://172.16.210.240:8888
IP：是第二步查看到的ip地址，替换成你自己的IP
port：8888是你在fiddler中配置的
注意：有些浏览器会显示打不开，更换其他浏览器就可以了

![fiddler证书](Fiddler 抓包工具\fiddler证书.png)

4、访问成功的话，会显示：

​    Fiddler Echo Service
​    ......
​    ......
​    This page returned a HTTP/200 response
​    .To configure fiddler as a reverse proxy instead of seeing this
​     page, see Reverse Proxy Setup
​    .You can download the FiddlerRoot certificate

5、点击  FiddlerRoot certificate ， 下载 证书

6、安装 证书(不同的手机不同的方式)
    6.1 部分手机可以直接点击 安装
    6.2 部分手机需要 设置 >> wifi(或WLAN) >> 高级设置 >> 安装证书 >>
            选中刚刚下载的 证书文件 FiddlerRoot.cer >> 确定
    6.3 设置(Settings) >> 更多设置 >> 系统安全 >> 从存储设备安装

​    6.4 为证书命名 , 输入自己喜欢的名字，譬如 fiddler  ，确定 ，  显示 证书安装完成

​    6.5 安装完成后，在 设置(Settings) >> 更多设置 >> 系统安全 >> 信任的凭证 >>
​        系统和用户2个tab页 >> 用户 >> 可以查看到 DO_NOT_RUST_FiddlerRoot

![安装证书](Fiddler 抓包工具\安装证书.png)

PS: 不安装证书，抓取http的数据是没问题的，但是抓取不了https的数据

7、手机设置代理(不同的手机不一样)
    手机设置 >> wifi(或WLAN) >>  选中连接的网络 >> 代理 >> 手动
    主机名：172.16.210.240   自己电脑IP
    端口  ：8888
    不使用网址： 这个不用理会
    修改完成后，确认

![设置代理](Fiddler 抓包工具\设置代理.png)

8、打开 fiddler 的抓包，然后在手机端运行要抓包的app，会查看到fiddler中已经可以抓到app的数据了

注意：
1、大部分app都可以直接抓包
2、少部分app没办法直接获取，需要 wireshark、反编译、脱壳 等方式去查找加密算法
3、app抓包一般都是抓取到服务器返回的json数据包

### 大体步骤

1. 手机,电脑同一局域网,设置fiddler
2. 设置代理
3. 安装证书


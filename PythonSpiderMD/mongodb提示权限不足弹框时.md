#### 在安装mongodb时，有遇到权限不足问题时，不要烦恼哦，跟着我按照如下步骤来解决~

### 1、提示权限不足弹框时，我们先不要动这个命令框。

![安装Mongodb提示权限不足的解决方法 _ JavaClub全栈架构师技术笔记](https://www.javaclub.cn/zb_users/upload/2022/10/10/39f67815-d396-4431-bec2-42e629fb330f.jpg)

### 2、window + r 打开运行窗口，输入services.msc命令。

![安装Mongodb提示权限不足的解决方法 _ JavaClub全栈架构师技术笔记](https://www.javaclub.cn/zb_users/upload/2022/10/10/4017720f-09b6-4c14-9c5b-b02ee8d79b04.jpg)

### 3、进去后找到MongoDB右击打开属性。

![安装Mongodb提示权限不足的解决方法 _ JavaClub全栈架构师技术笔记](https://www.javaclub.cn/zb_users/upload/2022/10/10/a6b1c857-9a6c-46ef-b8c3-7fcd5ed8f7a7.jpg)

### 4、点击登录，更改选项。

![安装Mongodb提示权限不足的解决方法 _ JavaClub全栈架构师技术笔记](https://www.javaclub.cn/zb_users/upload/2022/10/10/22cbf87b-5c75-4744-9371-ffcb2b299471.jpg)

### 5、再点击常规，点击启动。（我的已经点击过了，所以是灰色。）

![安装Mongodb提示权限不足的解决方法 _ JavaClub全栈架构师技术笔记](https://www.javaclub.cn/zb_users/upload/2022/10/10/ed1c895b-3342-4aff-a44a-dae09b9177b5.jpg)

### 6、接着就可以回到提示权限不足的那个弹出框那里，点击retry(重试)。就执行继续安装了。这就可以成功了。

![安装Mongodb提示权限不足的解决方法 _ JavaClub全栈架构师技术笔记](https://www.javaclub.cn/zb_users/upload/2022/10/10/4659d90d-c8fd-4761-8a54-c8624d69c93a.jpg)
如果还没有成功，就确认一下第四步那里的 本地系统账户 选项有没有修改成功。
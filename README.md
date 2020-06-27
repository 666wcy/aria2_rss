# Aria2 的Rss推送

基于python3环境，请自行安装环境，python2环境下尚未测试



目前测试支持的网站的Rss链接：

[末日资源库](https://share.acgnx.se/)

[动漫花园](http://dmhy.org/)



安装依赖

```
pip3 install -r requirements
```



修改 rss.py 中的参数



### 第一次运行请注释掉 dowmload(url) 这句代码

### 第一次运行请注释掉 dowmload(url) 这句代码

### 第一次运行请注释掉 dowmload(url) 这句代码

否则会向你的aria2提交当前rss的全部任务

运行

```
python3 rss.py
```



设定定时运行方面请各显神通
##### 使用python的scrapy框架，抓取微博用户昵称以及头像demo
运行项目 

###### 一：
在项目路径下的weibo.py文件

修改start_urls的URL值

修改scrapy.Request(请求URL)

以上两个url相同，在微博网页中进入个人用户面板，点击粉丝列表，打开调试工具，找到请求url
###### 二：
运行命令
```
scrapy crawl weibo -o downing.json
```
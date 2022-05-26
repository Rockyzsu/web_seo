# SEO小工具
#### 1. 查看百度的收录情况

#### 2. 查看网站的权重，用户信息



![](https://pic.kaihu51.com/unixpicgo/20220527002.png)





## 使用

----

在configure文件夹下创建mongodb的用户名和密码

```
{
    "mongo": {
    "qq": {
      "host": "1.1.1.1",
      "port": 27017,
      "user": "root",
      "password": "123456"
    }
    }
}
```

```python
代码中修改你要查询的站点
site_list=[
    'www.gairuo.com',
]

```

```
python main.py
```



随手写的小工具，一次性使用。
# 1. FastAPI简介


# 2. FastAPI快速上手
FastAPI使用步骤是：
1. 创建app实例
2. 注册路由
3. 启动服务

## 2.1 创建app实例
新建一个main.py文件，作为程序启动入口，在该文件中实例化一个FastAPI的app实例对象，它是整个应用程序的对象封装，示例代码如下：
```python
from fastapi import FastAPI
from typing import Optional

app = FastAPI(
    title="FastAPI入门体验",
    description="FastAPI使用描述",
    version="v1",
    debug=True
)
```

## 2.2 注册路由
注册路由就是将URL与后端函数对应，让前端请求的URL能找到后台对应的资源，和绝大部分的框架一样，FastAPI中也是使用装饰器来将路由和视图函数做绑定，即注册路由。
在前面main.py中添加如下示例代码：
```python
@app.get("/hello", tags="示例接口")
async def hello():
    return "Hello FastAPI"
```

## 2.3 启动服务
启动fastapi服务
```python
uvicorn main:app --reload
```
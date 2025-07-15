from fastapi import FastAPI

app =  FastAPI(
    title="测试API文档标题",
    description="关于API文档一些描述信息补充说明",
    version="v1.0.0",
    openapi_prefix="",
    swagger_ui_oauth2_redirect_url="/docs/oauth2-redirect",
    swagger_ui_init_oauth=None,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi/openapi_json.json",
    terms_of_service="https://terms/xxxx/",
    deprecated=True,
    contact={
        "name": "jeffer",
        "url": "https://xx.com",
        "email": "xxxx@163.com",
    },
    license_info={
        "name": "版权信息说明License v3.0",
        "url": "https://xxx.com"
    },
    openapi_tags=[
        {
            "name": "接口分组",
            "description": "接口分组信息说明"
        }
    ],
    # 配置服务请求地址相关的参数信息
    servers=[
        {"url": "/", "description":'本地调试环境'},
        {"url": "https://xxx.com", "description":'线上调试环境'},
        {"url": "https://xxx2.xxx2.com", "description":'线上生产环境'},
    ]
)

@app.get(path="/index")
async def index():
    return {"hello": "FastAPI"}
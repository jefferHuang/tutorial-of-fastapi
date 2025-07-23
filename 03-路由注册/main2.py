from fastapi import FastAPI, APIRouter

app = FastAPI(routes=None)


router_user = APIRouter(prefix="/user", tags=["用户模块"])
@app.get("/")
async def say_hello():
    return {"msg": "Hello FastAPI"}

@router_user.get("/user/login")
async def user_login():
    return {"msg": "登录成功"}

@router_user.api_route("/api/user/login", methods=["GET", "POST"])
async def user_api_route_login():
    return {"msg": "api_route 登录成功"}

async def add_user_api_route_login():
    return {"msg": "add_api_route 登录成功"}

# add_api_route方法必须填写endpoint,来绑定视图函数
router_user.add_api_route("/api2/user/login", methods=["GET", "POST"], endpoint=add_user_api_route_login)


app.include_router(router_user)
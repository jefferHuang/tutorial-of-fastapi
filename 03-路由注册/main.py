from fastapi import FastAPI, APIRouter

app = FastAPI(routes=None)


router_user = APIRouter(prefix="/user", tags=["用户模块"])
router_pay = APIRouter(prefix="/pay", tags=["支付模块"])
@app.get("/")
async def say_hello():
    return {"msg": "Hello FastAPI"}

@router_user.get("/user/login")
async def user_login():
    return {"msg": "登录成功"}

@router_pay.get("/pay/order")
async def pay_order():
    return {"msg": "支付成功"}


app.include_router(router_user)
app.include_router(router_pay)
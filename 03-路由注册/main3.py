from fastapi import FastAPI
import threading
import time
import asyncio

app = FastAPI(routes=None)

@app.get("/sync")
def sync_func():
    time.sleep(5)
    print("当前同步函数运行的线程ID: ", threading.currentThread().ident)
    return {"msg": "sync"}

@app.get("/async")
async def async_func():
    await asyncio.sleep(5)
    print("当前同步函数运行的线程ID: ", threading.currentThread().ident)
    return {"msg": "async"}



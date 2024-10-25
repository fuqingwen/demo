import uvicorn
from fastapi import FastAPI
import redis

app = FastAPI()


@app.get("/")
async def root():
    host = '192.168.10.140'
    rds = redis.Redis(host=host, port=6379, db=0)
    print(f'host:{host}')
    count = rds.incr('count')
    return {"message": f"Hello World, {count}"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)
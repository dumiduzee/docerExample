from fastapi import FastAPI
from redis import Redis

app =  FastAPI()

redis_client = Redis(host="redis",port=6379,db=0,decode_responses=True)



@app.get("/")
def root():
    return "Hello world"


@app.get("/create")
def crete():
    redis_client.set("name","dumidu")



@app.get("/love")
def new():
    data = redis_client.get("name")
    return data



import os

import redis
from dotenv import load_dotenv

load_dotenv("../.env")
def get_redis_connection() -> redis.Redis:
    return redis.Redis(
        host="localhost",
        port= 6379,
        db=0
    )



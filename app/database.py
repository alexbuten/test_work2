import redis

# Подключение к Redis
def get_redis_connection():
    return redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

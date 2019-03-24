import redis
r = redis.Redis(host="192.168.234.136", port=6379)
print(r.get("fuck"))

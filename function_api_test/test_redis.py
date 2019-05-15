import redis
# !!!!!!!!!!!!!!!!! need to of redis "protected" > no
r = redis.Redis(host="192.168.234.133", port=6379)
print(r.get("k1"))

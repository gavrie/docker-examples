import time
import ujson

d = dict(hello="ultima")
print(ujson.dumps(d))

time.sleep(3600)
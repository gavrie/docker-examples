import ujson

if __name__ == '__main__':
    d = dict(hello="ultima")
    print(ujson.dumps(d))

import hashlib
import hmac
import time
import json


def md5():
    s = '1212122'
    return hashlib.md5(s.encode()).hexdigest()


def sha2():
    s = '1212121'
    b = hashlib.sha1(s.encode()).hexdigest()
    print(b)
    return b


def sha333():
    s = '121212'
    b = hashlib.sha256(s).hexdigest()
    s = hmac.new(s.encode(), b.encode(), digestmod=hashlib.sha256).hexdigest()
    print(s)
    return s


def get_headers(data):
    timestamp = str(int(time.time() * 1000))
    content_length = str(len(json.dumps(data)))
    return {
        "openAppId": "aa",
        "openSign": get_sign(timestamp, content_length),
        "openTimestamp": timestamp,
        "algorithm": "hmac-sha256",
        "Content-Length": content_length
    }


def get_sign(timestamp, content_length):
    content = 'ss' + timestamp + content_length
    tmp = hashlib.sha256(content.encode()).hexdigest()
    sign = hmac.new('ss'.encode(), tmp.encode(), digestmod=hashlib.sha256).hexdigest()
    print(sign)
    return sign


sha2()

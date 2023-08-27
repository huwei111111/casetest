import hashlib
import hmac
import time

time = str(int(time.time() * 100000))
s = ''


class Sign:
    def __init__(self, data: str):
        self.data = data

    def md(self):
        global s
        s = str(time + self.data)
        s_md5 = hashlib.md5(s.encode()).hexdigest()
        return s_md5

    def sha2(self):
        s_sha256 = hashlib.sha256(s.encode()).hexdigest()
        return s_sha256

    def sign(self):
        s_hmac = hmac.new(str(s).encode(), digestmod=hashlib.sha256).hexdigest()
        return s_hmac


j = Sign('121212').sign()
print(j)

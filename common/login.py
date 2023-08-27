"""
"登录和封装session的值"
"""
import requests


class Api:
    def __init__(self):
        self.session = requests.Session()

    def login(self, username: str, password: str):
        url = 'https://om-version-test-1.uban360.com:21207/baas-login/AdminLogin/pwdLogin'
        data = {
            "username": username,
            "password": password,
            "validateCode": '2222',
            "os": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/103.0.0.0 Safari/537.36'
        }
        re = self.session.post(url=url, json=data)
        return re.json()


Api().login('sysadmin', "shinemo123")

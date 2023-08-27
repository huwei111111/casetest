import requests

session = requests.session()


class Api:

    def __init__(self, url=None):
        self.url = url

    def login(self):
        url = 'https://test-safe.uban360.com:21007/baas-login/AdminLogin/smsLogin'
        data = {"account": "admin000001", "deviceId": "", "code": "1",
                "os": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
        re = session.post(url=url, json=data)
        print(re.json())

    def get_csrftoken(self):
        url = 'https://test-safe.uban360.com:21007/baas-login/AdminLogin/getCsrfToken'
        b = session.get(
            url=url
        )
        re = session.get(url).json()
        global csrf_token,cookie
        csrf_token = re['data']
        cookie = str(b.cookies.get_dict())
        print(type(csrf_token))
        print(re)

    def add_push(self):
        url = 'https://test-safe.uban360.com:21007/baas-news/news/addAndPublish'
        data = {
            "baasNewsType": 1,
            "categoryId": 911,
            "digest": "",
            "expireDate": "",
            "extend": [],
            "title": "12312",
            "publisher": "1231",
            "fileContent": [
                {
                    "name": "2023-05-24群公告查收情况.xlsx",
                    "size": 3427,
                    "url": "/sfs/bizfile?digest=fid8b053a9f533d79173bf4000d26d223ea3f020373d6b3145d465bdc8b13e73793",
                    "suffix": ".xlsx"
                }
            ],
            "content": ""
        }
        header = {
            "Csrf-Token":csrf_token,
            "Cookie":cookie
        }
        re = session.post(url=url,json=data,headers=header)
        print(re.json())


Api().login()
Api().get_csrftoken()
Api().add_push()

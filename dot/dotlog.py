import requests


class Update:
    def __init__(self):
        """
        基础配置
        """
        self.header = {
            "Cookie": "ticket=4977f53063d13117df53b71f790e7fa6fe75b4020598634f6627ca99362559ae3; admin_login=%7B%22orgId%22%3A%2210008%22%2C%22orgName%22%3A%22%E8%87%AA%E5%8A%A8%E5%8C%96%E5%8D%95%E4%BD%8D%22%2C%22groupId%22%3A%2210008%22%2C%22adminType%22%3A%22%22%2C%22tenantCode%22%3A%22%22%2C%22uid%22%3A%228888888889%22%2C%22token%22%3A%224977f53063d13117df53b71f790e7fa6fe75b4020598634f6627ca99362559ae3%22%2C%22ts%22%3A%221687743953982%22%2C%22platform%22%3A%22admin%22%2C%22account%22%3A%22SysAdmin%22%2C%22accountType%22%3A%221%22%7D",
            "Csrf-Token": "a8eedc50a494c2796f8f058d64d4b84b525771f59a9c4a767cfd39655f5cef08"
        }
        self.update_url = 'https://test-safe.uban360.com:21007/sfs/webUpload/bizfile'

    def update(self):
        data = {
            'fileType': 1,
            "sceneId": "app.license"
        }
        files = {
            "file": open('E:/桌面/test_photo/255.png', 'rb')
        }
        re = requests.post(self.update_url, params=data, files=files, headers=self.header)
        s = re.cookies
        print(re.json())
        print(re.url)
        print(s)


Update().update()

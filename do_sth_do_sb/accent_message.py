import requests
import datetime

session = requests.session()


class API:
    def __init__(self):
        self.session = requests.session()

    def login(self):
        url = 'https://om-version-test-1.uban360.com:21007/baas-login/login/smsLogin'
        data = {"account": "a18893667251", "deviceId": "", "code": "1",
                "os": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
        re = session.post(url=url, json=data)

    def get_csrftoken(self):
        url = 'https://om-version-test-1.uban360.com:21007/baas-login/login/getCsrfToken'
        re = session.get(url).json()
        global csrf_token
        csrf_token = re['data']

    def find_by_status(self):
        """
        获取各类代办的任务及数量
        :return:
        """
        url = 'https://om-version-test-1.uban360.com:21007/baas-todocenter/web/todo-task/findAllGroupByStatus'
        header = {
            'Csrf-Token': csrf_token
        }
        re = session.get(url=url, headers=header)
        print(re.json())

    def finish_batch(self):
        """
        完成待办数据
        :return:
        """
        url = 'https://om-version-test-1.uban360.com:21007/baas-todocenter/web/todo-task/finishBatch'
        data = {
            "accountSource": "uid",
            "appId": "619",
            "appTasks": [
                {
                    "handlerIds": [
                        "8889007195"
                    ],
                    "appTaskId": 81143121326
                }
            ]
        }
        header = {
            'Csrf-Token': csrf_token
        }
        re = session.post(url=url, json=data, headers=header)
        print(re.json())

    def read_done(self):
        """
        已阅
        :return:
        """
        url = 'https://om-version-test-1.uban360.com:21007/baas-todocenter/web/todo-task/readDone'
        data = [1671122094775234561]  # 查询待查阅的主键id
        header = {
            'Csrf-Token': csrf_token
        }
        re = session.post(url=url, json=data, headers=header)
        print(re.json())

    def find_all(self):
        """
        查询当前登录用户所有的代办数据
        :return:
        """
        url = 'https://om-version-test-1.uban360.com:21007/baas-todocenter/web/todo-task/findAll'
        header = {
            'Csrf-Token': csrf_token
        }
        re = session.get(url=url, headers=header)
        print(re.json())


API().login()
API().get_csrftoken()
API().find_by_status()
# API().find_all()
# API().finish_batch()

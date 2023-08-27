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
        print(re.json())

    def get_csrftoken(self):
        url = 'https://om-version-test-1.uban360.com:21007/baas-login/login/getCsrfToken'
        re = session.get(url).json()
        global csrf_token
        csrf_token = re['data']
        print(re)

    def push(self):
        """
        推送待办数据
        :return:
        """
        url = 'https://om-version-test-1.uban360.com:21007/baas-todocenter/web/todo-task/pushBatch'
        data = {
            "accountSource": "uid",
            "appId": "619",
            "appTasks": [
                {
                    "title": "推送待办的数据准备撤回",  # 推送的代办名称
                    "detailUrl": "https://www.baidu.com",
                    "webDetailUrl": "https://www.baidu.com",
                    "coverUrl": "https://om-test.uban360.com:21107/sfs/file?digest=fid7338565f75c41ef22bca3a3ba7182977",
                    "iconUrl": "https://om-test.uban360.com:21107/sfs/file?digest=fid7338565f75c41ef22bca3a3ba7182977",
                    "tvDetailUrl": "https://www.baidu.com",
                    "pcDetailUrl": "https://www.baidu.com",
                    "summary": "xxxxxxx",
                    "customField": [
                        {
                            "key": "测试部门",
                            "val": "知道"
                        }
                    ],
                    "sponsorAccount": "8888888917",  # 推送人的UID
                    "sponsorUnitId": "10120",  # 推送人的单位id
                    "sponsorDepId": "28",  # 推送人的部门id
                    "sponsorTime": "2023-02-21 19:01:01",  # 推送人的时间
                    "businessType": "1",
                    "businessStatus": "1",
                    "appTaskId": "81143121340",  # taskid每次推送的id不一样随机
                    "jumpToDetail": "1",
                    "handleEntry": [
                        {
                            "handleType": 1,  # 1待处理，2待查阅 3处理完成 4已查询
                            "handlerAccount": "8888888918"  # 接收认的id
                        }
                    ],
                    "msgConfig": "1",
                    "deadlineTime": "2023-02-21 19:01:01",
                    "sponsorFromSys": 0
                }
            ]
        }
        header = {
            'Csrf-Token': csrf_token
        }
        re = session.post(url=url, json=data, headers=header)
        print(re.json())

    def get_my_sor(self):
        """
        获取我发起的待办
        :return:
        """
        url = 'https://om-version-test-1.uban360.com:21007/baas-todocenter/web/todo-task/getMySponsor'
        header = {
            'Csrf-Token': csrf_token
        }
        re = session.get(url=url, headers=header)
        print(re.json())

    def get_my_count(self):
        """
        获取我发起的待办数量
        :return:
        """
        url = 'https://om-version-test-1.uban360.com:21207/baas-todocenter/web/todo-task/getMySponsorCount'
        header = {
            'Csrf-Token': csrf_token
        }
        re = session.get(url=url, headers=header)
        print(re.json())

    def remove_batch(self):
        """
        撤回待办
        :return:
        """
        url = 'https://om-version-test-1.uban360.com:21007/baas-todocenter/web/todo-task/revokeBatch'
        header = {
            'Csrf-Token': csrf_token
        }
        date = {
            "accountSource": "uid",
            "appId": "619",
            "appTasks": [
                {
                    "handlerIds": [
                        8889007195  # 接收人的UI的数据
                    ],
                    "appTaskId": 81143121329  # 推送代办的taskid
                }
            ]
        }
        re = session.post(url=url, json=date, headers=header)
        print(re.json())

    def send_task_hand(self):
        """
        发给指定人的待办
        :return:
        """
        url = 'https://om-version-test-1.uban360.com:21007/baas-todocenter/web/todo-task/sendTaskToHandler'
        header = {
            'Csrf-Token': csrf_token
        }
        date = {
            "appId": "619",
            "appTaskId": "81143121329",  # 撤回待办的taskid
            "accountSource": "uid",
            "handlerIds": [
                8889007195  # 指定人的用户id
            ]
        }
        re = session.post(url=url, json=date, headers=header)
        print(re.json())


if __name__ == "__main__":
    s = API()
    s.login()
    s.get_csrftoken()
    s.push()
    s.get_my_sor()
    s.get_my_count()
    s.remove_batch()
    s.send_task_hand()

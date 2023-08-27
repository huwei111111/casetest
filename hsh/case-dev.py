import json

import requests
import time
import hashlib
import hmac
import random

prefix = "http://saas.uban360.net:80/openapi-cgw/baas-todocenter"
app_id = "54666151"
app_secret = "2db250026f314d893ff4dba603a093af83fd3925d8f6e3d56dbd6192c554bdd2"


def push_batch():
    uri = "/web/todo-task/pushBatch"

    data = {
        "accountSource": "uid",
        "appTasks": [
            {
                "title": "验证字段超长字符11",
                "detailUrl": "https://www.baidu.com",
                "webDetailUrl": "https://www.baidu.com",
                "coverUrl": "https://om-icsl.uban360.com:21007/sfs/file?digest=fid7338565f75c41ef22bca3a3ba7182977",
                "iconUrl": "https://om-icsl.uban360.com:21007/sfs/file?digest=fid7338565f75c41ef22bca3a3ba7182977",
                "tvDetailUrl": "https://www.baidu.com",
                "pcDetailUrl": "https://www.baidu.com",
                "summary": "xxxxxxx",
                "customField": [
                    {
                        "key": "发起人",
                        "val": "丁胜利"
                    },
                    {
                        "key": "发起单位",
                        "val": "浙江讯盟科技有限公司"
                    }
                ],
                "sponsorAccount": "8889006337",
                "sponsorUnitId": 10136,
                "sponsorDepId": 523901,
                "sponsorTime": "2023-02-21 19:01:01             ",
                "businessType": "1",
                "businessStatus": "1",
                "appTaskId": random.random(),
                "jumpToDetail": 1,
                "handleEntry": [
                    {
                        "handleType": 1,
                        "handlerAccount": "8889006785"
                    },
                    {
                        "handleType": 1,
                        "handlerAccount": "8889006765"
                    }
                ],
                "operateButton": [
                    {
                        "name": "同意",
                        "actionUrl": "1111",
                        "index": 1,
                        "showInMore": False,
                        "extendDada": "{\"actionBody\":{\"approveId\":\"20230210000012129\",\"buttonType\":1,\"orgId\":10136},\"buttonType\":1,\"h5ActionUrl\":\"/webaace/ApproveSrv/acTodoButton\",\"webActionUrl\":\"/access/ApproveSrv/acTodoButton\"}"
                    },
                    {
                        "name": "拒绝",
                        "actionUrl": "1111",
                        "index": 2,
                        "showInMore": False,
                        "extendDada": "{\"actionBody\":{\"approveId\":\"20230210000012129\",\"buttonType\":1,\"orgId\":10136},\"buttonType\":1,\"h5ActionUrl\":\"/webaace/ApproveSrv/acTodoButton\",\"webActionUrl\":\"/access/ApproveSrv/acTodoButton\"}"
                    }
                ],
                "msgConfig": 1,
                "deadlineTime": "2023-11-11 11:11:11"
            }
        ]
    }
    headers = get_headers(data)
    resp = requests.post(prefix + uri, headers=headers, json=data)
    print(headers, resp.status_code, resp.json())


def revoke_batch():
    uri = "/web/todo-task/revokeBatch"

    data = {
        "accountSource": "uid",
        "appTasks": [
            {
                "appTaskId": 0.762921469057311,
                "handlerAccounts": [
                    "8889006765"
                ]
            }
        ]
    }
    headers = get_headers(data)

    resp = requests.post(prefix + uri, headers=headers, json=data)
    print(headers, resp.status_code, resp.text)


def finish_batch():
    uri = "/web/todo-task/finishBatch"

    data = {
        "accountSource": "uid",
        "appTasks": [
            {
                "appTaskId": "0.9751452426470548",
                "handlerAccounts": [
                    "8889007219"
                ]
            }
        ]
    }
    headers = get_headers(data)

    resp = requests.post(prefix + uri, headers=headers, json=data)
    print(headers, resp.status_code, resp.text)


def send_task():
    uri = "/web/todo-task/sendTaskToHandler"

    data = {
        "accountSource": "uid",
        "appTaskId": "1111",
        "handlerAccounts": [
            "8889007219"
        ]
    }
    headers = get_headers(data)

    resp = requests.post(prefix + uri, headers=headers, json=data)
    print(headers, resp.status_code, resp.text)


def get_headers(data):
    timestamp = str(int(time.time() * 1000))
    content_length = str(len(json.dumps(data)))
    print(json.dumps(data))
    print(len(json.dumps(data)))
    print(content_length)
    return {
        "openAppId": app_id,
        "openSign": get_sign(timestamp, content_length),
        "openTimestamp": timestamp,
        "algorithm": "hmac-sha256",
        "Content-Length": content_length
    }


def get_sign(timestamp, content_length):
    content = app_id + timestamp + content_length
    tmp = hashlib.sha256(content.encode()).hexdigest()
    sign = hmac.new(app_secret.encode(), tmp.encode(), digestmod=hashlib.sha256).hexdigest()
    return sign


if __name__ == '__main__':
    push_batch()


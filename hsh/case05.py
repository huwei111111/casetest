import requests


def save():
    url = 'https://test-safe.uban360.com:21007/baas-app/app/save'
    data = {"id": None, "platformFlagList": [3], "appName": "1212", "appId": "", "appSecret": "",
            "iconUrl": "/sfs/file?digest=fid3f167bd2e6553b31f928260519a246de", "description": "12",
            "approveStatus": False, "versions": [], "modelType": "4", "openMsgChannel": False,
            "config": {"tvIconUrl": "", "pcIconUrl": "", "screenshotUrls": [], "copyrightUrls": [], "providerName": "",
                       "openMsgChannel": False, "platforms": [
                    {"url": "https://test-safe.uban360.com:21007/admin/#/app-manage/subscribe", "type": 1,
                     "resourceType": 2}, {"id": None, "type": 3, "resourceType": 0,
                                          "url": "https://test-safe.uban360.com:21007/admin/#/app-manage/subscribe",
                                          "iosUrl": "", "apkUrl": "", "callbackUrl": "", "description": ""}]},
            "appCategory": "496", "platformFlag": 3, "type": 2, "commit": True}
    

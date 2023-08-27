import requests

url = 'https://om-version-test-1.uban360.com:21207/baas-todocenter/web/todo-task/sendTaskToHandler'
data = {
    "appId": "619",
    "appTaskId": "81143121316",
    "accountSource": "uid",
    "handlerIds": [
        8889007127
    ]
}
headers = {
    "Cookie": "sso_c=591375ce8f6248011712572aeaec475c; sso_u=eyJ1aWRfIjo4ODg5MDA2MzUxLCJuYW1lXyI6IuWxiOWkp+eMmyIsIm1vYmlsZV8iOiIxODM1ODEyOTI1NyIsInRhZ3NfIjowfQ==; userinfo=18:%E5%B1%88%E5%A4%A7%E7%8C%9B:%E6%B5%8B%E8%AF%95:8889006351; ticket=47c5e39641887da5ce1109c188a68c28dc8f4e72598ed2c33a3a258721c026fd8; uid=8889007122; ts=1687243810153; admin_login=%7B%22orgId%22%3A%2210232%22%2C%22orgName%22%3A%22%E6%90%9C%E7%B4%A2%E5%8D%95%E4%BD%8D%E6%B5%8B%E8%AF%95%22%2C%22groupId%22%3A%2210008%22%2C%22adminType%22%3A%22%22%2C%22tenantCode%22%3A%22%22%2C%22uid%22%3A%228889007122%22%2C%22token%22%3A%2247c5e39641887da5ce1109c188a68c28dc8f4e72598ed2c33a3a258721c026fd8%22%2C%22ts%22%3A%221687243810153%22%2C%22platform%22%3A%22admin%22%2C%22account%22%3A%22Admin11%22%2C%22accountType%22%3A%221%22%7D; accountType=9; token=18e80683b5f669679ffdb8f84876bf5a740ec08810075247df986ec0b73ff9fb5; timeStamp=1687245287497; userId=8889007125; account=14422222222; sessionId=8b8dd71737a1bdf5956d40bea2c00f9712b10ac5d8bb1f4822933ec0da6bf1b2; JSESSIONID=54926F8BE2CB98ADD62ADA762D3BAC6B; groupId=10008; orgId=10232; myself={%22groupId%22:10008%2C%22groupName%22:%22%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%22%2C%22groupIcon%22:%22%22%2C%22groupAddress%22:%22%22%2C%22adminType%22:-1%2C%22loginName%22:%22%E6%B5%8B%E8%AF%9501%22%2C%22loginUid%22:8889007125%2C%22account%22:%2214422222222%22%2C%22orgList%22:[{%22id%22:10232%2C%22name%22:%22%E6%90%9C%E7%B4%A2%E5%8D%95%E4%BD%8D%E6%B5%8B%E8%AF%95%22%2C%22icon%22:%22%22}]%2C%22loginMobile%22:%2214422222222%22%2C%22loginOrgId%22:10232%2C%22loginOrgName%22:%22%E6%90%9C%E7%B4%A2%E5%8D%95%E4%BD%8D%E6%B5%8B%E8%AF%95%22%2C%22deptList%22:[{%22id%22:523924%2C%22name%22:%22AA%22}]%2C%22isJump%22:false}; b_name=5bGI5aSn54yb; b_sign=61e26fcfebdaa4b974b48b8f49791d51435ed5d7bdc538805278e46d6204d949; b_mobile=18358129257; b_dev=true; b_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJiX25hbWUiOiLlsYjlpKfnjJsiLCJiX21vYmlsZSI6IjE4MzU4MTI5MjU3IiwiYl9kZXYiOiJ0cnVlIiwiZXhwIjoxNjg3MzMyMzAzLCJiX3VzZXJJZCI6IjEyMDYifQ.xs-p6ZRtjeFE6cNFmv24fZatAGlPFOAEhRG9Felq6lE; b_userId=1206",
    "Csrf-Token": "41a90528204e6bc5af883cd10c5b214dd2b5ffdf0f1f743b9c24fe7bd4172819"
}

re = requests.post(url=url, json=data, headers=headers)

print(re.json())

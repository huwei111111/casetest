import requests


def count_message():
    """
    data =时间 ：对应的时间的数据
    :return:
    """
    url = 'https://10.0.14.11:21007/baas-stat/admin/analysis/doJob?date=2023-04-11'
    cook = "uid=8888888889; ticket=4f4776a88db8d369c79a30cfc74a803f06f048314d83a0aba011c6b20554ae93d; ts=1681816016406; JSESSIONID=CBC4B311D0AA444F88153A66F1B37F7C; admin_login=%7B%22orgId%22%3A%2210008%22%2C%22orgName%22%3A%22%E8%87%AA%E5%8A%A8%E5%8C%96%E5%8D%95%E4%BD%8D%22%2C%22groupId%22%3A%2210008%22%2C%22adminType%22%3A%22%22%2C%22tenantCode%22%3A%22%22%2C%22uid%22%3A%228888888889%22%2C%22token%22%3A%224f4776a88db8d369c79a30cfc74a803f06f048314d83a0aba011c6b20554ae93d%22%2C%22ts%22%3A%221681816016406%22%2C%22platform%22%3A%22admin%22%2C%22account%22%3A%22SysAdmin%22%2C%22accountType%22%3A%221%22%7D"
    s = cook.encode("UTF-8")
    header = {
        "Cookie": s,
        "Host": "10.0.14.11:21007",
        "Csrf-Token": "cdc733f86864201dda76f50a8a98b9e465dbbabb3e14088727e2fe59ced5fd85"
    }
    re = requests.get(url=url, headers=header, verify=False)
    print(re.json())


def app_list():
    url = "https://10.0.14.11:21007/sync-contacts/rest/ide/appList"
    data = {
        "pageSize": 20,
        "pageIndex": 1
    }
    header = {
        "Cookie": "accountType=9; myself={%22groupId%22:10008%2C%22groupName%22:%22%E8%87%AA%E5%8A%A8%E5%8C%96%E5%8D%95%E4%BD%8D%22%2C%22groupIcon%22:%22%22%2C%22groupAddress%22:%22%22%2C%22adminType%22:-1%2C%22loginName%22:%22%E5%BC%A0%E4%B8%80%22%2C%22loginUid%22:8889007044%2C%22account%22:%2218358129257%22%2C%22orgList%22:[{%22id%22:10112%2C%22name%22:%22%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%8D%95%E4%BD%8D%22%2C%22icon%22:%22%22}]%2C%22loginMobile%22:%2218358129257%22%2C%22loginOrgId%22:10112%2C%22loginOrgName%22:%22%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%8D%95%E4%BD%8D%22%2C%22deptList%22:[{%22id%22:523904%2C%22name%22:%22%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E9%83%A8%E9%97%A8%22}]%2C%22isJump%22:false}; open_login=%7B%22orgId%22%3A%22%22%2C%22tenantCode%22%3A%22%22%2C%22uid%22%3A%228889007038%22%2C%22token%22%3A%225eee1615e43e673e605487d7b42a83200eb5bbd1a93d44766dc9bbcb80ef7c16e%22%2C%22ts%22%3A%221681298797745%22%2C%22platform%22%3A%22open%22%2C%22account%22%3A%22dev876%22%2C%22accountType%22%3A%224%22%7D; JSESSIONID=DBE1668F8627DE8A01C6B5A28054FA5C",
        "Csrf-Token": "4278696bbfabfa5315860e6f8e0b945df57e64790d1b9ec8364ce70a8b111d86"
    }
    re = requests.get(url=url, params=data, headers=header, verify=False)
    print(re.json())


count_message()

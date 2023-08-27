import requests

from common.login import Api

login = Api()
session = Api().session

print(login)


def creat_group():
    ulr = 'https://om-version-test-1.uban360.com:21207/baas-admin/sysAdm/org/add'
    data = {"name": "测试单位00001", "code": "121222222", "parentId": "10008", "sequence": "1", "mobile": "14400000232",
            "departName": "23423423423423423", "judgeExist": "false"}
    header = {
        "Cookie": "ticket=4dbe42c5c85951a16f4b47240a2c940aa384ba3338c9c08d331fedb99c3e02531; uid=8888888889; ts=1680156308852; JSESSIONID=B89D5CB75F0F18ECAFEFEF67B027BC0F; admin_login=%7B%22orgId%22%3A%2210008%22%2C%22orgName%22%3A%22%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%22%2C%22groupId%22%3A%2210008%22%2C%22adminType%22%3A%22%22%2C%22tenantCode%22%3A%22%22%2C%22uid%22%3A%228888888889%22%2C%22token%22%3A%224dbe42c5c85951a16f4b47240a2c940aa384ba3338c9c08d331fedb99c3e02531%22%2C%22ts%22%3A%221680156308852%22%2C%22platform%22%3A%22admin%22%2C%22account%22%3A%22SysAdmin%22%2C%22accountType%22%3A%221%22%7D",
        "Csrf-Token": "43cfc093e41d243f86b6b40c6d8e0f2c2d101283bae99567d9647303f01419f8"
    }

    re = session.post(url=ulr, json=data, headers=header)
    print(re.json())


def delete():
    url = "https://om-version-test-1.uban360.com:21207/baas-admin/org/delete"
    data = {

    }
    header = {
        "Cookie": "ticket=4dbe42c5c85951a16f4b47240a2c940aa384ba3338c9c08d331fedb99c3e02531; uid=8888888889; ts=1680156308852; JSESSIONID=B89D5CB75F0F18ECAFEFEF67B027BC0F; admin_login=%7B%22orgId%22%3A%2210008%22%2C%22orgName%22%3A%22%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%22%2C%22groupId%22%3A%2210008%22%2C%22adminType%22%3A%22%22%2C%22tenantCode%22%3A%22%22%2C%22uid%22%3A%228888888889%22%2C%22token%22%3A%224dbe42c5c85951a16f4b47240a2c940aa384ba3338c9c08d331fedb99c3e02531%22%2C%22ts%22%3A%221680156308852%22%2C%22platform%22%3A%22admin%22%2C%22account%22%3A%22SysAdmin%22%2C%22accountType%22%3A%221%22%7D",
        "Csrf-Token": "43cfc093e41d243f86b6b40c6d8e0f2c2d101283bae99567d9647303f01419f8"
    }
    re = requests.post(url=url, json=data, headers=header)
    print(re.json())


creat_group()

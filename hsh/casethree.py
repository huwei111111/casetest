import requests

url = "https://10.0.14.11:21007/baas-permission/menu/assignSystemMenu"
data = {"uid": 8889006965, "orgId": 10016,
        "menus": [1, 2, 5, 6, 23, 24, 26, 25, 1326, 780, 1327, 27, 28, 29, 31, 32, 33, 34, 35, 1435, 1438, 19, 20, 22,
                  21, 828, 827, 829, 36, 37, 40, 42, 781, 782, 853, 854, 855, 856, 857, 858, 860, 812, 813, 1541, 1542,
                  867, 814, 868, 869, 870, 835, 871, 851, 881, 882, 883, 884, 18, 1217, 1563, 1565, 1566, 1567, 1594,
                  1560, 1572, 1573, 1442, 1444, 1477, 1495, 1514, 1515, 1516, 1517, 1499, 1510, 1511, 1512, 1513, 1500,
                  1506, 1507, 1508, 1509, 1474, 1496, 1497, 1498, 1475, 1476, 1501, 1502, 1478, 1503, 1504, 1505]}
header = {
    "Cookie": "ticket=4c1f764aded39e9b453e2f41866a420a614bc5c813a91526c3a39da1f1498c0e0; uid=8888888889; ts=1681191824264; JSESSIONID=5E5A6C7623B850640407311ABFB938C0; admin_login=%7B%22orgId%22%3A%2210008%22%2C%22orgName%22%3A%22%E8%87%AA%E5%8A%A8%E5%8C%96%E5%8D%95%E4%BD%8D%22%2C%22groupId%22%3A%2210008%22%2C%22adminType%22%3A%22%22%2C%22tenantCode%22%3A%22%22%2C%22uid%22%3A%228888888889%22%2C%22token%22%3A%224c1f764aded39e9b453e2f41866a420a614bc5c813a91526c3a39da1f1498c0e0%22%2C%22ts%22%3A%221681191824264%22%2C%22platform%22%3A%22admin%22%2C%22account%22%3A%22SysAdmin%22%2C%22accountType%22%3A%221%22%7D",
    "Csrf-Token": "80c9f6ef1ef5fe90330a999c65807e5dfddf68ff20550424fa4ef2cc96fa61fa",
    "Host": "10.0.14.11:21007",
    "Referer": "https://10.0.14.11:21007/admin/",
    "Content-Type": "application/json"
}

re = requests.post(url=url, json=data, headers=header)
print(re.json())

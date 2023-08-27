import requests

with open('E:/桌面/test_photo/255.png', 'rb') as a:
    s = a.read()
    print(s)


def file_type():
    url = 'https://test-safe.uban360.com:21007/sfs/webUpload/bizfile?fileType=1&sceneId=app.license'
    files = {
        "file": open('E:/桌面/test_photo/255.png', 'rb')
    }
    header = {
        "Cookie": "sso_c=88400226d4a294f0961577eb2c09e85e; sso_u=eyJ1aWRfIjo4ODg5MDA2MzUxLCJuYW1lXyI6IuWxiOWkp+eMmyIsIm1vYmlsZV8iOiIxODM1ODEyOTI1NyIsInRhZ3NfIjowfQ==; ticket=4977f53063d13117df53b71f790e7fa6fe75b4020598634f6627ca99362559ae3; uid=8888888889; ts=1687743953982; admin_login=%7B%22orgId%22%3A%2210008%22%2C%22orgName%22%3A%22%E8%87%AA%E5%8A%A8%E5%8C%96%E5%8D%95%E4%BD%8D%22%2C%22groupId%22%3A%2210008%22%2C%22adminType%22%3A%22%22%2C%22tenantCode%22%3A%22%22%2C%22uid%22%3A%228888888889%22%2C%22token%22%3A%224977f53063d13117df53b71f790e7fa6fe75b4020598634f6627ca99362559ae3%22%2C%22ts%22%3A%221687743953982%22%2C%22platform%22%3A%22admin%22%2C%22account%22%3A%22SysAdmin%22%2C%22accountType%22%3A%221%22%7D; token=1626273a8be49c41d62448f8725d7dbd08746f36ffd986b6b6b8d3e66880b52b4; timeStamp=1687746895048; userId=8889009203; account=14488888889; accountType=9; sessionId=4366a379f9f4b30b44b476c3e30639cf55764bc1018edeb12d52f4e4e889bec5; groupId=10008; orgId=10656; myself={%22groupId%22:10008%2C%22groupName%22:%22%E8%87%AA%E5%8A%A8%E5%8C%96%E5%8D%95%E4%BD%8D%22%2C%22groupIcon%22:%22%22%2C%22groupAddress%22:%22%22%2C%22adminType%22:-1%2C%22loginName%22:%22and%20%5Cn%201=1--%5Ct%22%2C%22loginUid%22:8889009203%2C%22account%22:%2214488888889%22%2C%22orgList%22:[{%22id%22:10656%2C%22name%22:%22%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%8D%95%E4%BD%8D%22%2C%22icon%22:%22%22}]%2C%22loginMobile%22:%2214488888889%22%2C%22loginOrgId%22:10656%2C%22loginOrgName%22:%22%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%8D%95%E4%BD%8D%22%2C%22deptList%22:[]%2C%22isJump%22:false}; userinfo=18:%E5%B1%88%E5%A4%A7%E7%8C%9B:%E6%B5%8B%E8%AF%95:8889006351; open_login=%7B%22orgId%22%3A%22%22%2C%22tenantCode%22%3A%22%22%2C%22uid%22%3A%228889009123%22%2C%22token%22%3A%225423e8319020c5fc0195e236f47269b7d46383c96d87cb2b63923d61e6b5094dd%22%2C%22ts%22%3A%221687765525673%22%2C%22platform%22%3A%22open%22%2C%22account%22%3A%22dev356%22%2C%22accountType%22%3A%224%22%7D; JSESSIONID=D93FF08413FA8A5F25E4E254118A9A77",
        "Csrf-Token": "a8eedc50a494c2796f8f058d64d4b84b525771f59a9c4a767cfd39655f5cef08"
    }
    re = requests.post(url=url, files=files, headers=header)
    print(re.json())


file_type()
# import requests
# # 请求url
# url = "https://127.0.0.1/upload"
# # 请求头
# headers = {
#     "Authorization": "bearer abcde"
# }
# # 上传文件的参数
# files = {
#         "file": ("test.xlsx", open("D:\\test.xlsx", "rb"), "application/octet-stream")
#     }
# # 其他参数
# data = {
#     "id": "1585171115599216642"
# }
# # 发送请求
# response = requests.post(url=url, headers=headers, files=files, data=data)
# # 打印结果
# print(response.text)

accounts = {

}
f = open('account.txt', 'r', encoding='utf-8')
for line in f:
    print(line)
    line = line.strip().split(',')
    print(line)
    accounts[line[0]] = line
print(accounts)
count = 0
while count <= 2:
    user = input('username:').strip()
    if user not in accounts:
        print('用户没有注册')
        continue
    password = input('password:').strip()
    if password == accounts[user][1]:
        print('密码正确')
    else:
        print('密码错误')
    count = count + 1

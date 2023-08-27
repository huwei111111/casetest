# s = open('wenijin.txt', encoding='utf-8')
# for line in s:
#     #     print(line)
#     b = line.split()
#     # print(b)
#     g = int(b[1])
#     if g >= 180:
#         print(line)
#   二进制操作图片
b = open('22.jpg', 'rb')
# rb 是二进制的字节类型
for i in b:
    print(i)

s = open('sile.jpg', "wb")
# 二进制的文件进行写入

d = '路飞'
# s.write(d.encode('utf-8'))

print(s.read())

s = open('wenijin.txt', 'r+', encoding='utf-8')
# 按照字节   一个中文是3个字节，一个数字是1个字节

# seek第一个参数是偏移量：>0,代表向右移动，<0代表向左移动
# seek第二个参数是，0：移动指针到文件开头，1：不移动指针，2：移动指针到末尾
s.seek(0, 2)
s.write('sdf\n')
print(s.read())

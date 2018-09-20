# coding:utf-8
# 测试文件，用于测试各种数据集假设


# 验证1：G:\r5.2\file.csv中没有MMK1532记录
Flag_User_Exist = False
with open(r'G:\r5.2\file.csv', 'r') as f:
    for line in f:
        line_lst = line.strip('\n').strip(',').split(',')
        if line_lst[2] == 'user':
            continue
        if line_lst[2] == 'MMK1532':
            Flag_User_Exist = True
print Flag_User_Exist, '\n'

# 上述验证结果为False，说明MMK1532不存在file记录
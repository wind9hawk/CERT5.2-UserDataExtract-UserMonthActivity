# coding:utf-8
# 测试文件，用于测试各种数据集假设


# 验证1：G:\r5.2\file.csv中没有MMK1532记录
Flag_Idea_0 = False
if Flag_Idea_0 == True:
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


# 验证2：
# CERT5.2的五个行为数据集中不存在时间先后颠倒的情况
# 分别统计五个数据集中的时间序列，如果出现后者比前者小，则判定存在时间逆序；反之则符合我们假设
def Extract_Date(date):
    # date表示要分析的日期字符串，如CERT5.2中的
    # 01/02/2010 06:49:35
    year = date[6:10]
    day= date[3:5]
    month = date[:2]
    return year, month, day
print '开始验证假设2...\n\n'
Flag_Idea_1 = True
Flag_TimeOder = True
TimeOrder = []
if Flag_Idea_1 == True:
    with open(r'G:\r5.2\http.csv', 'r') as f:
        for line in f:
            line_lst = line.strip('\n').strip(',').split(',')
            if line_lst[2] == 'user':
                continue
            year, month, day = Extract_Date(line_lst[1])
            Time = year + '-' + month + '-' + day
            if Time not in TimeOrder:
                TimeOrder.append(Time)
                if len(TimeOrder) > 1:
                    for ele in TimeOrder:
                        if ele > Time:
                            Flag_TimeOder = False
    print  'CERT5.2数据集中记录严格按时间顺序记录为： ', Flag_TimeOder, '\n'
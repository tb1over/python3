# -*- coding:utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


'''
sorted函数的第二个参数key会依次作用于L的每个元素
给by_name和by_score传递的参数是列表的元素
L的每个元素t是一个tuple,t[0]是姓名，t[1]是成绩
'''


def by_name(t):

    return t[0]


def by_score(t):

    return t[1]

L2 = sorted(L, key=by_name)
print('sorted by name', L2)


L2 = sorted(L, key=by_score)
print('sorted by sore', L2)




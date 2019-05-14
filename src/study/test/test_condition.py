#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 15:42
# @Author  : zhouchong
# @Site    : 
# @File    : test_condition.py
# @Software: PyCharm

def five_eight():
    company_users = ['admin','zhouchong','zhangjiulin','chenglei','chenzhen','zhangpeng','wangmin']
    for user in company_users:
        if user is 'admin':
            print('hello admin,would you like to see a status report')
        else:
            print('hello %s,thank you for logging in again' % user)

if __name__ == '__main__':
    five_eight()
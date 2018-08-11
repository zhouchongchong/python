# _*_ coding: utf-8 _*_
import os
import json


def do_flie(file_path):
    try:
        fo = open(file_path, 'r', encoding='UTF-8')
        print(fo.name)
        print(fo.mode)
    except Exception:
        print("无法打开此文件")
    else:
        print("every thing is ok")
        # print('str:', fo.read(10))
        # print('str:', fo.readlines())
        # words = fo.readlines()
        words = fo.read()
        fo.close()
        return words



a  = 1
def do_test():
    global a
    print(a)
    a = 4
    print(a)
    del(a)

# nonlocal 潜逃域使用


def nonlocal_test():
    num = 10

    def inner_area():
        nonlocal num
        print(num)
        num = 5
        print(num)
    inner_area()

sites = ["Baidu", "Google", "Runoob", "Taobao"]
def loop():
    global sites
    for site in sites:
        if site == "Runoob":
            print("菜鸟教程!")
            break
        print("循环数据 " + site)
    else:
        print("没有循环数据!")
    print("完成循环!")

# nonlocal_test()
# loop()
# try:
#     do_test()
#     print(a)
# except NameError as ex:
#     print("exception: %s" % ex)

# with open("auth.py") as f:
#     for line in f: 
#         print(line, end="")    


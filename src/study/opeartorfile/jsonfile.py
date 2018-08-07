# _*_ coding: utf-8 _*_
'''
  @Author: Trent.zhouchong
  @Date: 2018-08-06 16:08:32
  @Last Modified by:   Trent.zhouchong
  @Last Modified time: 2018-08-06 16:08:32
 '''
import json
import file
import sys
sys.path.append('D:\\vscode\python\src\study\mysql')
import mysql_pool as mysql
import timeit

      
def file_db_kv1():
    file_paht = 'D:\\\\vscode\\python\\src\\study\\chinese-xinhua\\data\\\\word.json'
    with open(file_paht, 'r', encoding='UTF-8') as file:
        words = file.read()
        values = []
        value = []
        for word in json.loads(words):
            for k, v in word.items():
                value.append(v)
            values.append(value)


def file_db_for():
    file_paht = 'D:\\\\vscode\\python\\src\\study\\chinese-xinhua\\data\\\\word.json'
    with open(file_paht, 'r', encoding='UTF-8') as file:
        words = file.read()
        values = []
        for i in json.loads(words):
            value = (i['word'], i['oldword'], i['strokes'], i['pinyin'], i['radicals'], i['explanation'], i['more'])
            values.append(value)
       
if __name__ == '__main__':
    print('excute jsonFile')
    # print(timeit.timeit(stmt=file_db_kv)) 
    # print(timeit.timeit(stmt=file_db_for,number=0))
    # print(timeit.timeit(stmt=file_db_kv,number=0))


def file_word_db():
    file_path = 'D:\\vscode\\python\\src\\study\\chinese-xinhua\\data\\word.json'
    words = file.do_flie(file_path)
    print(type(words))
    # print('in file path:%s , have  %d words' % (file_path, len(words)))
    # strs = ''
    # for line in words:
    #       strs +=line.rstrip()
    values = []
    for i in json.loads(words):
        value = (i['word'], i['oldword'], i['strokes'], i['pinyin'], i['radicals'], i['explanation'], i['more'])
        values.append(value)
    sql = 'INSERT INTO word (word,oldword,strokes,spell,radicals,explanation,more) VALUES (%s,%s,%s,%s,%s,%s,%s)'
    ms = mysql.MysqlPool()
    count = ms.insert_many(sql, values)
    print('insert into db influence %s rows' % count)
# _*_ coding: utf-8 _*_
'''
  @Author: Trent.zhouchong 
  @Date: 2018-08-07 11:22:02 
  @Last Modified by:   Trent.zhouchong 
  @Last Modified time: 2018-08-07 11:22:02 
 '''
import timeit

file_db_kv = """
import json
file_paht = 'D:\\\\vscode\\python\\src\\study\\chinese-xinhua\\data\\\\word.json'
with open(file_paht, 'r', encoding='UTF-8') as file:
    words = file.read()
    values = []
    value = []
    for word in json.loads(words):
        for k,v in word.items():
            value.append(v)
        values.append(value)
"""

file_db_for = """
import json
file_paht = 'D:\\\\vscode\\python\\src\\study\\chinese-xinhua\\data\\\\word.json'
with open(file_paht, 'r', encoding='UTF-8') as file:
    words = file.read()
    values = []
    for i in json.loads(words):
        value = (i['word'], i['oldword'], i['strokes'], i['pinyin'], i['radicals'], i['explanation'], i['more'])
        values.append(value)
  """

if __name__ == '__main__':
    print('excute timeit_test')
    print(timeit.timeit(stmt=file_db_for,number=0))
    print(timeit.timeit(stmt=file_db_kv,number=0))

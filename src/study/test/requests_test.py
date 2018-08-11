# _*_ coding: utf-8 _*_
'''
  @Author: Trent.zhouchong 
  @Date: 2018-08-09 11:53:23 
  @Last Modified by:   Trent.zhouchong 
  @Last Modified time: 2018-08-09 11:53:23 
 '''
import requests
import json
from bs4 import BeautifulSoup


def test_spider():
    with requests.get('http://jr.jd.com') as response:
        # print(response.content.decode('utf-8', errors='ignore'))
        # print(type(response.text))
        # html = BeautifulSoup(response.content)
        """ with open('jr_jd.html','wb') as fl:
          for chunk in response.iter_content(chunk_size=1024):
                fl.write(chunk) """
        print(response.status_code)
        # r.heards 是个 dict 
        # print(response.cookies.items)
        print(response.history)
        for kv in response.cookies.items():
            print(kv)


if __name__ == '__main__':
    print('request_test')
    test_spider()

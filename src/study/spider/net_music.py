# _*_ coding: utf-8 _*_ 
'''
  @Author: Trent.zhouchong 
  @Date: 2018-08-07 16:38:26 
  @Last Modified by:   Trent.zhouchong 
  @Last Modified time: 2018-08-07 16:38:26 
 '''
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import csv
import os

#第一个爬虫
def test_spider():
    with urlopen('http://music.163.com/#/discover/playlist') as html:
        # print(html.read().decode(encoding='UTF-8'))
        bs_object = BeautifulSoup(html.read(),'html.parser')
        # print(type(bs_object),bs_object)
        a_text =  bs_object.find_all('span','nb')
        for text in a_text:
            print(text.get_text())

#爬取网易云音乐歌单
def music_max():
    #网易云音乐第一地址 注意 \ 是拼接字符串
    url = 'http://music.163.com/#/discover/playlist/'\
    '?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'
    # print(url)
    chromedriver = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'
    os.environ["webdriver.chrome.driver"] = chromedriver
    # driver 初始化
    options = Options()
    options.set_headless(True)
    options.add_argument('--disable-gpu')
    options.add_argument('lang=zh_CN.gbk')
    driver = webdriver.Chrome(chromedriver,options=options)
    # driver.set_page_load_timeout(1)
    # driver.maximize_window()

    #准备好存储歌单的csv文件
    csv_file = open('playlist.csv','w',newline = '')
    writer =  csv.writer(csv_file)
    writer.writerow(['标题','播放数','链接'])

    # 解析每一页，直到 '下一页' 为空
    while url != 'javascript:void(0)':
        driver.get(url)
        driver.switch_to.frame('contentFrame')
        data = driver.find_element_by_id('m-pl-container').\
        find_elements_by_tag_name('li')
        for i in range(len(data)):
            try:
                nb = data[i].find_element_by_class_name('nb').text
                if '万' in nb and int(nb.split('万')[0]) > 500:
                    msk = data[i].find_element_by_css_selector('a.msk')
                    writer.writerow([msk.get_attribute('title'),nb,msk.get_attribute('href')])
            except Exception as e:
                print(e)
                continue

        url = driver.find_element_by_css_selector('a.zbtn.znxt').get_attribute('href')

    csv_file.close()
            

if __name__ == '__main__':
    print('spider web begain')
    music_max()

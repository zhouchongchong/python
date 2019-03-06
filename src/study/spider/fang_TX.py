# _*_ coding: utf-8 _*_ 
'''
  @Author: Trent.zhouchong 
  @Date: 2019-03-04 11:16:55 
  @Last Modified by:   Trent.zhouchong 
  @Last Modified time: 2019-03-04 11:16:55 
 '''
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import logging
import loggin
import csv
import os

encoding = 'UTF-8'
envGoogleDrivereKye = "webdriver.chrome.driver"
chromeDriverPath = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'


# 爬取房天下 篱笆房 租房信息
def house_libafang():
    url = 'https://zu.fang.com/house/g22-s31-kw%c0%e9%b0%ca%b7%bf/'
    logging.info(url)

    # env google chromedriver 初始化设置
    os.environ[envGoogleDrivereKye] = chromeDriverPath 

    # driver 初始化
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('lang=zh_CN.gbk')
    driver = webdriver.Chrome(chromeDriverPath,chrome_options=options)

    # # 初始化csv 文件 存储获取信息
    csv_file = open('libfang_house.csv', 'w', newline='')
    writer = csv.writer(csv_file)
    writer.writerow(['小区信息', '户型大小', '地理位置','地铁信息','价格','链接'])

    
    
    flag = True
    title = ''
    house_lage= ''
    house_site = ''
    sub_info = ''
    price = ''
    href_pre = 'https://zu.fang.com'
    while flag:
        # 获取单页数据信息
        driver.get(url)
        data = driver.find_element_by_class_name('houseList').\
      	find_elements_by_tag_name('dl')
        list_a = driver.find_element_by_class_name('fanye').\
      	find_elements_by_tag_name('a')
        for i in range(len(data)):
            house=data[i].find_elements_by_tag_name("dd")
            for y in range(len(house)):
                try:
                    ps = house[y].find_elements_by_tag_name('p')
                    links = ps[0].find_elements_by_tag_name('a')
                    title = links[0].get_attribute('title')
                    href = links[0].get_attribute('href')
                    logging.info('title:'+ title)
                    house_lage = ps[1].text
                    logging.info(house_lage)

                    site = ps[2].find_elements_by_tag_name('a')
                    house_site = ''
                    for k in range(len(site)):
                        house_site += site[k].find_elements_by_tag_name('span')[0].text +'-'
                    logging.info(house_site[0:len(house_site)-2])
                    try:
                        sub_info = house[y].find_element_by_css_selector("span.note.subInfor")
                        logging.info("地铁信息：%s " % sub_info.text)
                    except Exception as e:
                        logging.error(e)

                    try:
                        price = house[y].find_element_by_css_selector("span.price")
                        logging.info("价格信息：%s " % price.text)
                    except Exception as e:
                        logging.error(e)
                    writer.writerow([title,house_lage,house_site[0:len(house_site)-1],sub_info.text,price.text+'元/月',href_pre+href])

                except Exception as e:
                    logging.error(e)
                    continue
        
        
        for i in range(len(list_a)):
            if list_a[i].text == '下一页':
                flag = True
                url = list_a[i].get_attribute('href')
                break
            else:
                flag = False
            url = list_a[i].get_attribute('href')
        # 测试控制单元
        # flag = False
        

    csv_file.close()

			 
          




    # for el in range(len(list_a)):
          

          



if __name__ == "__main__":
    loggin.log_config()
    logging.info('sprider of house from libafagn is began')
    # house_libafang()
    logging.error("error")
    logging.info('sprider of house from libafagn is end')


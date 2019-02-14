# _*_ coding: utf-8 _*_
'''
  @Author: Trent.zhouchong 
  @Date: 2018-08-10 17:19:57 
  @Last Modified by:   Trent.zhouchong 
  @Last Modified time: 2018-08-10 17:19:57 
 '''
import logging.config
import yaml
import os


def log_config(def_path='/logging.yaml'):
    file_cof = None
    try:
        file_cof = open(def_path, 'r', encoding='UTF-8')
    except Exception as e:
        print(e)
        path = os.path.dirname(__file__) +def_path
        file_cof = open(path,'r',encoding = 'UTF-8')
        conf = yaml.load(file_cof.read())
        logging.config.dictConfig(conf)
    finally:
        file_cof.close()
    logging.info('logging config is complie!')


def log():
    print(os.path.realpath(__file__))

    if None:
        print(1)
if __name__ == '__main__':
    log_config()
    logging.info('ni guo lai a')

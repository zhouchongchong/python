# _*_ coding: utf-8 _*_ 
'''
  @Author: Trent.zhouchong 
  @Date: 2018-08-03 14:58:51 
  @Last Modified by:   Trent.zhouchong 
  @Last Modified time: 2018-08-03 14:58:51 
 '''
import os
import yaml 

class MysqlConfig(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        dir_path = os.path.dirname(os.path.relpath(__file__))
        config_file = dir_path + '/config.yaml'

        try:
            configs = yaml.load(open(config_file, 'r'))
        except Exception as e:
            print(e)
        else:
            print('open file success')

        mysql_infos = configs.get('mysql.config')['conn']

        self.host = mysql_infos['host']
        self.port = mysql_infos['port']
        self.user = mysql_infos['user']
        self.pwd = mysql_infos['pwd']
        self.db = mysql_infos['db']
        self.charset = mysql_infos['charset']


    def __del__(self):
        print('del souces')





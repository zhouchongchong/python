# _*_ coding: utf-8 _*_ 
'''
  @Author: Trent.zhouchong 
  @Date: 2018-08-03 17:10:56 
  @Last Modified by:   Trent.zhouchong 
  @Last Modified time: 2018-08-03 17:10:56 
 '''
import pymysql
from sources import MysqlConfig
from DBUtils.PooledDB import PooledDB


class MysqlPool(object):
    __pool = None
    __config = None

    def __init__(self):
        self.coon = MysqlPool.getMysqlConnect()
        self.cur = self.coon.cursor(cursor=pymysql.cursors.DictCursor)

    @staticmethod
    def getMysqlConnect():
        msc = MysqlConfig()
        print(msc)
        if MysqlPool.__pool is None:
            __pool = PooledDB(creator=pymysql, mincached=1, maxcached=20, host=msc.host,
            port=msc.port, user=msc.user, password=msc.pwd, db=msc.db,use_unicode=False, charset=msc.charset,setsession=[])
            print(__pool)
        return __pool.connection();


if __name__ == '__main__':
    opm = MysqlPool()
    print(opm)

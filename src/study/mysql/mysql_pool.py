# _*_ coding: utf-8 _*_ 
'''
  @Author: Trent.zhouchong 
  @Date: 2018-08-03 17:10:56 
  @Last Modified by:   Trent.zhouchong 
  @Last Modified time: 2018-08-03 17:10:56 
 '''
import pymysql
from src.study.mysql.sources import MysqlConfig
from DBUtils.PooledDB import PooledDB


class MysqlPool(object):
    __pool = None
    __config = None

    def __init__(self):
        self.conn = MysqlPool.getMysqlConnect()
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    @staticmethod
    def getMysqlConnect():
        msc = MysqlConfig()
        print(msc)
        if MysqlPool.__pool is None:
            __pool = PooledDB(creator=pymysql, mincached=1, maxcached=20, host=msc.host,
            port=msc.port, user=msc.user, password=msc.pwd, db=msc.db,use_unicode=False, charset=msc.charset,setsession=[])
            print(__pool)
        return __pool.connection();


    def add(self):  # 增
        sql = 'insert into testtb values(1,"Tom",18),(2,"Jerry",16),(3,"Hank",24)'
        res = self.cur.execute(sql)
        if res:
            self.conn.commit()
        else:
            self.conn.rollback()
        print(res)

    def insert_many(self,sql,values):
        count = self.cur.executemany(sql,values)
        if count:
            self.conn.commit()
        else:
            self.conn.rollback()
        print(count)
        return count
        


if __name__ == '__main__':
    opm = MysqlPool()
    print(opm)

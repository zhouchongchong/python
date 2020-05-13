#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 16:16
# @Author  : zhouchong
# @Site    : 
# @File    : downloadimage.py
# @Software: PyCharm
import logging.config
import json
from src.study.spider import  loggin
from src.study.opeartorfile import image_util

def vision_image(file_path):
    file =None
    try:
        with open(file_path,'r',encoding='UTF-8') as file:
            lines = file.readlines()
            for line in lines:
                jsonstr = json.loads(line)
                if 'data' in jsonstr:
                    datastr = jsonstr['data']
                    if 'detail' in datastr:
                        detailstr = datastr['detail']
                        if 'imagePath' in detailstr:
                            print(detailstr['imagePath'])
                            image_util.ImageUtil.save_image(detailstr['imagePath'])

    except Exception:
        logging.error("file not find,use default config", exc_info=True)
    finally:
        file.close()


if __name__ == '__main__':
    config = loggin.log_config()

    file_path = 'D:\\bak\\image.log'
    vision_image(file_path)
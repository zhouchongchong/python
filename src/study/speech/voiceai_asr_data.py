# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, division, print_function
from pyvoiceai import *
import sys,time

#   使用说明（支持Python3.0+）:
#   1. 安装 pip install pyvoiceai
#   2. 使用脚本发送数据到服务器进行识别 python voiceai_asr_data.py  ./poiet.wav
#   3. 结果如下：
####################################################
#python3 voiceai_asr_data.py poiet.wav
#start
#debug: 不收
#debug: 不识庐山
#debug: 不识庐山真貌
#debug: 不识庐山真面目
#debug: 不识庐山真面目，只缘
#debug: 不识庐山真面目，只缘身在此
#debug: 不识庐山真面目，只缘身在此山中。
#debug: 不识庐山真面目，只缘身在此山中。
#debug: 不识庐山真面目，只缘身在此山中。
#不识庐山真面目，只缘身在此山中。
####################################################

# 1.设置日志
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s-%(filename)s,[%(name)s:%(funcName)s:%(lineno)d] [%(levelname)s]:%(message)s")

try:
    File_Name = sys.argv[1]
except:
    File_Name = "D:\\vscode\\python\\src\\study\\speech\\poiet.wav"


# 5.辅助回调，可不用，这个只是辅助调试。
def call_back_debug(t):
    print("debug: %s" % t)


if __name__ == '__main__':
    print("start")

    # 2.主要配置
    V_HOST = "wss://cloud.voiceaitech.com:8072"
    V_APP_ID = "cbaad1e7f7594f5da97629003ec85e51"
    V_APP_SECRET = "74c8f9b81d1915cdc119d16e6c06d734"

    # 3.新建一个客户端， 传入配置以及回调函数
    c = ASRClient(V_APP_ID, V_APP_SECRET, V_HOST, None)

    # 4.开始识别，识别过程为阻塞，会一直运行到识别结束，如果音频较长， 请传入回调函数进行观察
    # 16000 			表示采样率
    # MODEL_ASR_POWER 	是电力模型名，常量定义在sdk中
    # File_Name 		需要识别的音频
    # 800 				间歇时间，识别是实时识别，发送间歇800毫秒，当服务器性能良好，可以设置100毫秒
    txt = c.asr(16000, MODEL_ASR_POWER, File_Name, 800)
    print(txt)

    # 5.可以再继续识别
    # txt = c.asr(16000, MODEL_ASR_POWER, File_Name)
    # print(txt)

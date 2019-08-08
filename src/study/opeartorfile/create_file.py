# _*_ coding: utf-8 _*_
import os
import json

def do_file(file_path):
    try:
        file = open(file_path, 'ab+')
        file.write(b'\rgood man')
        file.flush()
        file.close()
    except Exception as e:
        print(e)
        print('%s file not exist' % file_path)
    else:
        print('file is open')
    


if __name__ == '__main__':
    do_file('answer.text')
# !/user/bin/env python
#conding=utf-8

import time
file=r'abc.txt'
with open(file,'r') as file0:
    strs=file0.readlines()
    try:
        for i in strs:
            print(i)
            time.sleep(1)
    finally:
        file0.close()
        print('Cleaning up ... closed the file')
    
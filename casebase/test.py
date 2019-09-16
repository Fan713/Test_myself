# pdb_test.py
#!/usr/bin/env python

import time
# import pdb;pdb.set_trace()

def countdown(number):
    for i in range(number,0,-1):
        import pdb;pdb.set_trace()
        print(i)
        time.sleep(1)
if __name__ == '__main__':
    seconds=10
    countdown(seconds)
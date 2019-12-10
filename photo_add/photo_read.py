#!/usr/bin/env python
#coding=utf-8

from PIL import Image
import cv2
import os
import time
import glob as gb
import numpy as np
# g=os.walk(r"E:\From_ZF\Myself\UU")
# for path,d,filelist in g:
#     for filename in filelist:
#         if filename.endswith('jpg'):
#             print(os.path.join(path,filename))
img_path=r'E:\From_ZF\Myself\UU'
# img_path=r'E:\From_ZF\Myself\UU\20190105105309.jpg'
# for path in img_path:
    
# img=cv2.imread(img_path)
# cv2.imshow('1',img)
# if img.shape[2] ==1:
#     img_rgb=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)

def transfer(img_path,dst_width,dst_height):
    STA=time.time()          
    im=Image.open(img_path)
    print(im.size)
    
    if im.mode !="RGBA":
        im=im.convert('RGBA')
        
    s_w,s_h=im.size
    if s_w < s_h:
        im =im.transpose(Image.ROTATE_90)
            
if __name__=="__main__":
    transfer()

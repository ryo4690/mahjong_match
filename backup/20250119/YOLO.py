# -*- coding: UTF-8 -*-
from xml.dom import minidom
import xml.etree.ElementTree as ET
import cv2
import random   


#パラメータ　はじめ
scale = 0.25
angle = 0
x_origin = 20
y_origin = 100
x_offset = 90
y_offset = 0
num_pai = 8 #配置する牌の数
num_img = 500 #作成する画像の数
#パラメータ　終わり

pai_img = ["img/pai/1m.jpg","img/pai/2m.jpg","img/pai/3m.jpg","img/pai/4m.jpg","img/pai/5m.jpg","img/pai/6m.jpg","img/pai/7m.jpg","img/pai/8m.jpg","img/pai/9m.jpg","img/pai/1p.jpg","img/pai/2p.jpg","img/pai/3p.jpg","img/pai/4p.jpg","img/pai/5p.jpg","img/pai/6p.jpg","img/pai/7p.jpg","img/pai/8p.jpg","img/pai/9p.jpg","img/pai/1s.jpg","img/pai/2s.jpg","img/pai/3s.jpg","img/pai/4s.jpg","img/pai/5s.jpg","img/pai/6s.jpg","img/pai/7s.jpg","img/pai/8s.jpg","img/pai/9s.jpg","img/pai/T.jpg","img/pai/E.jpg","img/pai/H.jpg","img/pai/G.jpg","img/pai/N.jpg","img/pai/S.jpg","img/pai/W.jpg"] 
pai_name = ["1m","2m","3m","4m","5m","6m","7m","8m","9m","1p","2p","3p","4p","5p","6p","7p","8p","9p","1s","2s","3s","4s","5s","6s","7s","8s","9s","T","E","H","G","N","S","W"]

back_img = cv2.imread("img/floor.jpg")
back_h, back_w = back_img.shape[:2]

for k in range(num_img):
    #変数リセット
    object = []
    name_child = []
    pose = []
    truncated = []
    difficult = []
    bndbox = []
    xmin = []
    ymin = []
    xmax = []
    ymax = []

    f = open('result/labels/train'+str(k)+'.txt','w')

    for i in range(num_pai):
        number = random.randrange(34)
        fore_img = cv2.imread(pai_img[number])
        fore_h, fore_w = fore_img.shape[:2]

        x=x_offset*i+x_origin
        #print(x)
        y=y_offset*i+y_origin
        #print(y)
        M = cv2.getRotationMatrix2D((int(x), int(y)), angle, scale)
        img_warped = cv2.warpAffine(fore_img, M, (back_w, back_h), back_img, borderMode=cv2.BORDER_TRANSPARENT)

        xmin = M[0,2]
        ymin = M[1,2]

        xcenter = xmin + (fore_w*scale/2)
        ycenter = ymin + (fore_h*scale/2)

        xcenter_yolo = xcenter/back_w
        ycenter_yolo = ycenter/back_h

        fore_w_yolo = fore_w*scale/back_w
        fore_h_yolo = fore_h*scale/back_h

        f.write(str(number)+' '+str(xcenter_yolo)+' '+str(ycenter_yolo)+' '+str(fore_w_yolo)+' '+str(fore_h_yolo)+'\n')
        
    
    f.close()
    cv2.imwrite('result/img/train'+str(k)+'.jpg', img_warped)
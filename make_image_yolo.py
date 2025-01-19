# -*- coding: UTF-8 -*-
from xml.dom import minidom
import xml.etree.ElementTree as ET
import cv2
import random   
import pandas as pd

num_case = 20

#共通パラメータ
num_img_start = 0
num_img = 3
url_images = 'result/images/train'
url_labels = 'result/labels/train'
pai_name = ["1m","2m","3m","4m","5m","6m","7m","8m","9m","1p","2p","3p","4p","5p","6p","7p","8p","9p","1s","2s","3s","4s","5s","6s","7s","8s","9s","T","E","H","G","N","S","W"]

#パラメータ　はじめ
scale = [0.25,0.25,0.25,0.25,0.25,
         0.25,0.25,0.25,0.25,0.25,
         0.25,0.25,0.25,0.25,0.25,
         0.25,0.25,0.25,0.25,0.25]
angle = [0,0,0,0,0,
         0,0,0,0,0,
         0,0,0,0,0,
         0,0,0,0,0]
x_origin = [20,20,20,20,20,
            20,20,20,200,200,
            200,200,200,200,200,
            200,500,400,300,200]
y_origin = [100,100,100,100,100,
            100,100,100,100,100,
            100,100,100,100,100,
            100,500,600,700,1000]
x_offset = [67,90,67,90,67,
            90,67,90,200,200,
            200,200,200,200,200,
            200,67,100,80,120]
y_offset = [0,0,0,0,0,
            0,0,0,100,100,
            100,100,100,100,100,
            100,0,0,0,0]
num_pai = [11,8,11,8,11,
           8,11,8,15,15,
           15,15,15,10,15,
           10,11,8,11,8] #配置する牌の数
pai_angle = ["0","90","180","270","0",
             "90","180","270","0","90",
             "180","270","0","90","180",
             "270","0","90","180","270"]
url_back_img = ["floor","floor","floor","floor","floor",
                "floor","floor","floor","floor5","floor5",
                "floor5","floor5","floor3","floor3","floor3",
                "floor3","floor4","floor4","floor4","floor4"]

#パラメータ　終わり

for l in range(num_case):
    pai_img = ["img/pai/"+str(pai_angle[l])+"/1m.jpg","img/pai/"+str(pai_angle[l])+"/2m.jpg","img/pai/"+str(pai_angle[l])+"/3m.jpg","img/pai/"+str(pai_angle[l])+"/4m.jpg","img/pai/"+str(pai_angle[l])+"/5m.jpg","img/pai/"+str(pai_angle[l])+"/6m.jpg","img/pai/"+str(pai_angle[l])+"/7m.jpg","img/pai/"+str(pai_angle[l])+"/8m.jpg","img/pai/"+str(pai_angle[l])+"/9m.jpg","img/pai/"+str(pai_angle[l])+"/1p.jpg","img/pai/"+str(pai_angle[l])+"/2p.jpg","img/pai/"+str(pai_angle[l])+"/3p.jpg","img/pai/"+str(pai_angle[l])+"/4p.jpg","img/pai/"+str(pai_angle[l])+"/5p.jpg","img/pai/"+str(pai_angle[l])+"/6p.jpg","img/pai/"+str(pai_angle[l])+"/7p.jpg","img/pai/"+str(pai_angle[l])+"/8p.jpg","img/pai/"+str(pai_angle[l])+"/9p.jpg","img/pai/"+str(pai_angle[l])+"/1s.jpg","img/pai/"+str(pai_angle[l])+"/2s.jpg","img/pai/"+str(pai_angle[l])+"/3s.jpg","img/pai/"+str(pai_angle[l])+"/4s.jpg","img/pai/"+str(pai_angle[l])+"/5s.jpg","img/pai/"+str(pai_angle[l])+"/6s.jpg","img/pai/"+str(pai_angle[l])+"/7s.jpg","img/pai/"+str(pai_angle[l])+"/8s.jpg","img/pai/"+str(pai_angle[l])+"/9s.jpg","img/pai/"+str(pai_angle[l])+"/T.jpg","img/pai/"+str(pai_angle[l])+"/E.jpg","img/pai/"+str(pai_angle[l])+"/H.jpg","img/pai/"+str(pai_angle[l])+"/G.jpg","img/pai/"+str(pai_angle[l])+"/N.jpg","img/pai/"+str(pai_angle[l])+"/S.jpg","img/pai/"+str(pai_angle[l])+"/W.jpg"] 
    back_img = cv2.imread("img/"+str(url_back_img[l])+".jpg")
    back_h, back_w = back_img.shape[:2]

    for k in range(num_img_start,num_img_start+num_img):
        f = open(str(url_labels)+str(k)+'.txt','w')

        for i in range(num_pai[l]):
            number = random.randrange(34)
            fore_img = cv2.imread(pai_img[number])
            fore_h, fore_w = fore_img.shape[:2]

            x=x_offset[l]*i+x_origin[l]
            y=y_offset[l]*i+y_origin[l]
            M = cv2.getRotationMatrix2D((int(x), int(y)), angle[l], scale[l])
            img_warped = cv2.warpAffine(fore_img, M, (back_w, back_h), back_img, borderMode=cv2.BORDER_TRANSPARENT)

            xmin = M[0,2]
            ymin = M[1,2]

            xcenter = xmin + (fore_w*scale[l]/2)
            ycenter = ymin + (fore_h*scale[l]/2)

            xcenter_yolo = xcenter/back_w
            ycenter_yolo = ycenter/back_h

            fore_w_yolo = fore_w*scale[l]/back_w
            fore_h_yolo = fore_h*scale[l]/back_h

            f.write(str(number)+' '+str(xcenter_yolo)+' '+str(ycenter_yolo)+' '+str(fore_w_yolo)+' '+str(fore_h_yolo)+'\n')
            
        f.close()
        cv2.imwrite(str(url_images)+str(k)+'.jpg', img_warped)

    num_img_start = num_img_start+num_img
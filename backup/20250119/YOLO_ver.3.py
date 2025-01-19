# -*- coding: UTF-8 -*-
from xml.dom import minidom
import xml.etree.ElementTree as ET
import cv2
import random   

#共通パラメータ
num_img_start = 0
num_img = 10
url_images = 'result/images/train'
url_labels = 'result/labels/train'
url_back_img = "img/floor3.jpg"

#角度0の麻雀牌
#パラメータ　はじめ
scale = 0.25
angle = 0
x_origin = 20
y_origin = 100
x_offset = 67
y_offset = 0
num_pai = 11 #配置する牌の数

#パラメータ　終わり

pai_img = ["img/pai/0/1m.jpg","img/pai/0/2m.jpg","img/pai/0/3m.jpg","img/pai/0/4m.jpg","img/pai/0/5m.jpg","img/pai/0/6m.jpg","img/pai/0/7m.jpg","img/pai/0/8m.jpg","img/pai/0/9m.jpg","img/pai/0/1p.jpg","img/pai/0/2p.jpg","img/pai/0/3p.jpg","img/pai/0/4p.jpg","img/pai/0/5p.jpg","img/pai/0/6p.jpg","img/pai/0/7p.jpg","img/pai/0/8p.jpg","img/pai/0/9p.jpg","img/pai/0/1s.jpg","img/pai/0/2s.jpg","img/pai/0/3s.jpg","img/pai/0/4s.jpg","img/pai/0/5s.jpg","img/pai/0/6s.jpg","img/pai/0/7s.jpg","img/pai/0/8s.jpg","img/pai/0/9s.jpg","img/pai/0/T.jpg","img/pai/0/E.jpg","img/pai/0/H.jpg","img/pai/0/G.jpg","img/pai/0/N.jpg","img/pai/0/S.jpg","img/pai/0/W.jpg"] 
pai_name = ["1m","2m","3m","4m","5m","6m","7m","8m","9m","1p","2p","3p","4p","5p","6p","7p","8p","9p","1s","2s","3s","4s","5s","6s","7s","8s","9s","T","E","H","G","N","S","W"]

back_img = cv2.imread(str(url_back_img))
back_h, back_w = back_img.shape[:2]

for k in range(num_img_start,num_img_start+num_img):

    f = open(str(url_labels)+str(k)+'.txt','w')

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
    cv2.imwrite(str(url_images)+str(k)+'.jpg', img_warped)

#角度90の麻雀牌
num_img_start = num_img_start+num_img

#パラメータ　はじめ
scale = 0.25
angle = 0
x_origin = 20
y_origin = 100
x_offset = 90
y_offset = 0
num_pai = 8 #配置する牌の数

#パラメータ　終わり

pai_img = ["img/pai/90/1m.jpg","img/pai/90/2m.jpg","img/pai/90/3m.jpg","img/pai/90/4m.jpg","img/pai/90/5m.jpg","img/pai/90/6m.jpg","img/pai/90/7m.jpg","img/pai/90/8m.jpg","img/pai/90/9m.jpg","img/pai/90/1p.jpg","img/pai/90/2p.jpg","img/pai/90/3p.jpg","img/pai/90/4p.jpg","img/pai/90/5p.jpg","img/pai/90/6p.jpg","img/pai/90/7p.jpg","img/pai/90/8p.jpg","img/pai/90/9p.jpg","img/pai/90/1s.jpg","img/pai/90/2s.jpg","img/pai/90/3s.jpg","img/pai/90/4s.jpg","img/pai/90/5s.jpg","img/pai/90/6s.jpg","img/pai/90/7s.jpg","img/pai/90/8s.jpg","img/pai/90/9s.jpg","img/pai/90/T.jpg","img/pai/90/E.jpg","img/pai/90/H.jpg","img/pai/90/G.jpg","img/pai/90/N.jpg","img/pai/90/S.jpg","img/pai/90/W.jpg"] 
pai_name = ["1m","2m","3m","4m","5m","6m","7m","8m","9m","1p","2p","3p","4p","5p","6p","7p","8p","9p","1s","2s","3s","4s","5s","6s","7s","8s","9s","T","E","H","G","N","S","W"]

back_img = cv2.imread(str(url_back_img))
back_h, back_w = back_img.shape[:2]

for k in range(num_img_start,num_img_start+num_img):

    f = open(str(url_labels)+str(k)+'.txt','w')

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
    cv2.imwrite(str(url_images)+str(k)+'.jpg', img_warped)

#角度180の麻雀牌
num_img_start = num_img_start+num_img

#パラメータ　はじめ
scale = 0.25
angle = 0
x_origin = 20
y_origin = 100
x_offset = 67
y_offset = 0
num_pai = 11 #配置する牌の数

#パラメータ　終わり

pai_img = ["img/pai/180/1m.jpg","img/pai/180/2m.jpg","img/pai/180/3m.jpg","img/pai/180/4m.jpg","img/pai/180/5m.jpg","img/pai/180/6m.jpg","img/pai/180/7m.jpg","img/pai/180/8m.jpg","img/pai/180/9m.jpg","img/pai/180/1p.jpg","img/pai/180/2p.jpg","img/pai/180/3p.jpg","img/pai/180/4p.jpg","img/pai/180/5p.jpg","img/pai/180/6p.jpg","img/pai/180/7p.jpg","img/pai/180/8p.jpg","img/pai/180/9p.jpg","img/pai/180/1s.jpg","img/pai/180/2s.jpg","img/pai/180/3s.jpg","img/pai/180/4s.jpg","img/pai/180/5s.jpg","img/pai/180/6s.jpg","img/pai/180/7s.jpg","img/pai/180/8s.jpg","img/pai/180/9s.jpg","img/pai/180/T.jpg","img/pai/180/E.jpg","img/pai/180/H.jpg","img/pai/180/G.jpg","img/pai/180/N.jpg","img/pai/180/S.jpg","img/pai/180/W.jpg"] 
pai_name = ["1m","2m","3m","4m","5m","6m","7m","8m","9m","1p","2p","3p","4p","5p","6p","7p","8p","9p","1s","2s","3s","4s","5s","6s","7s","8s","9s","T","E","H","G","N","S","W"]

back_img = cv2.imread(str(url_back_img))
back_h, back_w = back_img.shape[:2]

for k in range(num_img_start,num_img_start+num_img):

    f = open(str(url_labels)+str(k)+'.txt','w')

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
    cv2.imwrite(str(url_images)+str(k)+'.jpg', img_warped)

#角度270の麻雀牌
num_img_start = num_img_start+num_img

#パラメータ　はじめ
scale = 0.25
angle = 0
x_origin = 20
y_origin = 100
x_offset = 90
y_offset = 0
num_pai = 8 #配置する牌の数

#パラメータ　終わり

pai_img = ["img/pai/270/1m.jpg","img/pai/270/2m.jpg","img/pai/270/3m.jpg","img/pai/270/4m.jpg","img/pai/270/5m.jpg","img/pai/270/6m.jpg","img/pai/270/7m.jpg","img/pai/270/8m.jpg","img/pai/270/9m.jpg","img/pai/270/1p.jpg","img/pai/270/2p.jpg","img/pai/270/3p.jpg","img/pai/270/4p.jpg","img/pai/270/5p.jpg","img/pai/270/6p.jpg","img/pai/270/7p.jpg","img/pai/270/8p.jpg","img/pai/270/9p.jpg","img/pai/270/1s.jpg","img/pai/270/2s.jpg","img/pai/270/3s.jpg","img/pai/270/4s.jpg","img/pai/270/5s.jpg","img/pai/270/6s.jpg","img/pai/270/7s.jpg","img/pai/270/8s.jpg","img/pai/270/9s.jpg","img/pai/270/T.jpg","img/pai/270/E.jpg","img/pai/270/H.jpg","img/pai/270/G.jpg","img/pai/270/N.jpg","img/pai/270/S.jpg","img/pai/270/W.jpg"] 
pai_name = ["1m","2m","3m","4m","5m","6m","7m","8m","9m","1p","2p","3p","4p","5p","6p","7p","8p","9p","1s","2s","3s","4s","5s","6s","7s","8s","9s","T","E","H","G","N","S","W"]

back_img = cv2.imread(str(url_back_img))
back_h, back_w = back_img.shape[:2]

for k in range(num_img_start,num_img_start+num_img):

    f = open(str(url_labels)+str(k)+'.txt','w')

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
    cv2.imwrite(str(url_images)+str(k)+'.jpg', img_warped)

#角度0の麻雀牌
num_img_start = num_img_start+num_img

#パラメータ　はじめ
scale = 0.2
angle = 0
x_origin = 20
y_origin = 100
x_offset = 67
y_offset = 0
num_pai = 8 #配置する牌の数

#パラメータ　終わり

pai_img = ["img/pai/0/1m.jpg","img/pai/0/2m.jpg","img/pai/0/3m.jpg","img/pai/0/4m.jpg","img/pai/0/5m.jpg","img/pai/0/6m.jpg","img/pai/0/7m.jpg","img/pai/0/8m.jpg","img/pai/0/9m.jpg","img/pai/0/1p.jpg","img/pai/0/2p.jpg","img/pai/0/3p.jpg","img/pai/0/4p.jpg","img/pai/0/5p.jpg","img/pai/0/6p.jpg","img/pai/0/7p.jpg","img/pai/0/8p.jpg","img/pai/0/9p.jpg","img/pai/0/1s.jpg","img/pai/0/2s.jpg","img/pai/0/3s.jpg","img/pai/0/4s.jpg","img/pai/0/5s.jpg","img/pai/0/6s.jpg","img/pai/0/7s.jpg","img/pai/0/8s.jpg","img/pai/0/9s.jpg","img/pai/0/T.jpg","img/pai/0/E.jpg","img/pai/0/H.jpg","img/pai/0/G.jpg","img/pai/0/N.jpg","img/pai/0/S.jpg","img/pai/0/W.jpg"] 
pai_name = ["1m","2m","3m","4m","5m","6m","7m","8m","9m","1p","2p","3p","4p","5p","6p","7p","8p","9p","1s","2s","3s","4s","5s","6s","7s","8s","9s","T","E","H","G","N","S","W"]

back_img = cv2.imread(str(url_back_img))
back_h, back_w = back_img.shape[:2]

for k in range(num_img_start,num_img_start+num_img):

    f = open(str(url_labels)+str(k)+'.txt','w')

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
    cv2.imwrite(str(url_images)+str(k)+'.jpg', img_warped)

#角度90の麻雀牌
num_img_start = num_img_start+num_img

#パラメータ　はじめ
scale = 0.2
angle = 0
x_origin = 20
y_origin = 100
x_offset = 90
y_offset = 0
num_pai = 7 #配置する牌の数

#パラメータ　終わり

pai_img = ["img/pai/90/1m.jpg","img/pai/90/2m.jpg","img/pai/90/3m.jpg","img/pai/90/4m.jpg","img/pai/90/5m.jpg","img/pai/90/6m.jpg","img/pai/90/7m.jpg","img/pai/90/8m.jpg","img/pai/90/9m.jpg","img/pai/90/1p.jpg","img/pai/90/2p.jpg","img/pai/90/3p.jpg","img/pai/90/4p.jpg","img/pai/90/5p.jpg","img/pai/90/6p.jpg","img/pai/90/7p.jpg","img/pai/90/8p.jpg","img/pai/90/9p.jpg","img/pai/90/1s.jpg","img/pai/90/2s.jpg","img/pai/90/3s.jpg","img/pai/90/4s.jpg","img/pai/90/5s.jpg","img/pai/90/6s.jpg","img/pai/90/7s.jpg","img/pai/90/8s.jpg","img/pai/90/9s.jpg","img/pai/90/T.jpg","img/pai/90/E.jpg","img/pai/90/H.jpg","img/pai/90/G.jpg","img/pai/90/N.jpg","img/pai/90/S.jpg","img/pai/90/W.jpg"] 
pai_name = ["1m","2m","3m","4m","5m","6m","7m","8m","9m","1p","2p","3p","4p","5p","6p","7p","8p","9p","1s","2s","3s","4s","5s","6s","7s","8s","9s","T","E","H","G","N","S","W"]

back_img = cv2.imread(str(url_back_img))
back_h, back_w = back_img.shape[:2]

for k in range(num_img_start,num_img_start+num_img):

    f = open(str(url_labels)+str(k)+'.txt','w')

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
    cv2.imwrite(str(url_images)+str(k)+'.jpg', img_warped)

#角度180の麻雀牌
num_img_start = num_img_start+num_img

#パラメータ　はじめ
scale = 0.2
angle = 0
x_origin = 20
y_origin = 100
x_offset = 67
y_offset = 0
num_pai = 8 #配置する牌の数

#パラメータ　終わり

pai_img = ["img/pai/180/1m.jpg","img/pai/180/2m.jpg","img/pai/180/3m.jpg","img/pai/180/4m.jpg","img/pai/180/5m.jpg","img/pai/180/6m.jpg","img/pai/180/7m.jpg","img/pai/180/8m.jpg","img/pai/180/9m.jpg","img/pai/180/1p.jpg","img/pai/180/2p.jpg","img/pai/180/3p.jpg","img/pai/180/4p.jpg","img/pai/180/5p.jpg","img/pai/180/6p.jpg","img/pai/180/7p.jpg","img/pai/180/8p.jpg","img/pai/180/9p.jpg","img/pai/180/1s.jpg","img/pai/180/2s.jpg","img/pai/180/3s.jpg","img/pai/180/4s.jpg","img/pai/180/5s.jpg","img/pai/180/6s.jpg","img/pai/180/7s.jpg","img/pai/180/8s.jpg","img/pai/180/9s.jpg","img/pai/180/T.jpg","img/pai/180/E.jpg","img/pai/180/H.jpg","img/pai/180/G.jpg","img/pai/180/N.jpg","img/pai/180/S.jpg","img/pai/180/W.jpg"] 
pai_name = ["1m","2m","3m","4m","5m","6m","7m","8m","9m","1p","2p","3p","4p","5p","6p","7p","8p","9p","1s","2s","3s","4s","5s","6s","7s","8s","9s","T","E","H","G","N","S","W"]

back_img = cv2.imread(str(url_back_img))
back_h, back_w = back_img.shape[:2]

for k in range(num_img_start,num_img_start+num_img):

    f = open(str(url_labels)+str(k)+'.txt','w')

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
    cv2.imwrite(str(url_images)+str(k)+'.jpg', img_warped)

#角度270の麻雀牌
num_img_start = num_img_start+num_img

#パラメータ　はじめ
scale = 0.2
angle = 0
x_origin = 20
y_origin = 100
x_offset = 90
y_offset = 0
num_pai = 7 #配置する牌の数

#パラメータ　終わり

pai_img = ["img/pai/270/1m.jpg","img/pai/270/2m.jpg","img/pai/270/3m.jpg","img/pai/270/4m.jpg","img/pai/270/5m.jpg","img/pai/270/6m.jpg","img/pai/270/7m.jpg","img/pai/270/8m.jpg","img/pai/270/9m.jpg","img/pai/270/1p.jpg","img/pai/270/2p.jpg","img/pai/270/3p.jpg","img/pai/270/4p.jpg","img/pai/270/5p.jpg","img/pai/270/6p.jpg","img/pai/270/7p.jpg","img/pai/270/8p.jpg","img/pai/270/9p.jpg","img/pai/270/1s.jpg","img/pai/270/2s.jpg","img/pai/270/3s.jpg","img/pai/270/4s.jpg","img/pai/270/5s.jpg","img/pai/270/6s.jpg","img/pai/270/7s.jpg","img/pai/270/8s.jpg","img/pai/270/9s.jpg","img/pai/270/T.jpg","img/pai/270/E.jpg","img/pai/270/H.jpg","img/pai/270/G.jpg","img/pai/270/N.jpg","img/pai/270/S.jpg","img/pai/270/W.jpg"] 
pai_name = ["1m","2m","3m","4m","5m","6m","7m","8m","9m","1p","2p","3p","4p","5p","6p","7p","8p","9p","1s","2s","3s","4s","5s","6s","7s","8s","9s","T","E","H","G","N","S","W"]

back_img = cv2.imread(str(url_back_img))
back_h, back_w = back_img.shape[:2]

for k in range(num_img_start,num_img_start+num_img):

    f = open(str(url_labels)+str(k)+'.txt','w')

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
    cv2.imwrite('result/images/val'+str(k)+'.jpg', img_warped)
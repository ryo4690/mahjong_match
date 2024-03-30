import cv2
import random   

#設定
size = 0.25
angle = 0
x_origin = 10
y_origin = 100
x_offset = 65
y_offset = 0
num_pai = 12
num_img = 10
#設定ここまで

pai = ["img/pai/1m.jpg","img/pai/2m.jpg","img/pai/3m.jpg","img/pai/4m.jpg","img/pai/5m.jpg","img/pai/6m.jpg","img/pai/7m.jpg","img/pai/8m.jpg","img/pai/9m.jpg","img/pai/1p.jpg","img/pai/2p.jpg","img/pai/3p.jpg","img/pai/4p.jpg","img/pai/5p.jpg","img/pai/6p.jpg","img/pai/7p.jpg","img/pai/8p.jpg","img/pai/9p.jpg","img/pai/1s.jpg","img/pai/2s.jpg","img/pai/3s.jpg","img/pai/4s.jpg","img/pai/5s.jpg","img/pai/6s.jpg","img/pai/7s.jpg","img/pai/8s.jpg","img/pai/9s.jpg","img/pai/C.jpg","img/pai/E.jpg","img/pai/H.jpg","img/pai/K.jpg","img/pai/N.jpg","img/pai/S.jpg","img/pai/W.jpg"]
 
back_img = cv2.imread("img/floor.jpg")
back_h, back_w = back_img.shape[:2]
 
for k in range(num_img):
    for i in range(num_pai):
        number = random.randrange(34)
        fore_img = cv2.imread(pai[number])
        fore_h, fore_w = fore_img.shape[:2]
        x=x_offset*i+x_origin
        y=y_offset*i+y_origin
        M = cv2.getRotationMatrix2D((int(x), int(y)), angle, size)
        img_warped = cv2.warpAffine(fore_img, M, (back_w, back_h), back_img, borderMode=cv2.BORDER_TRANSPARENT)

    cv2.imwrite('result/result_'+str(k)+'.jpg', img_warped)
# -*- coding: UTF-8 -*-
from xml.dom import minidom
import xml.etree.ElementTree as ET
import cv2
import random   


#パラメータ　はじめ
scale = 0.25
angle = 0
x_origin = 10
y_origin = 100
x_offset = 65
y_offset = 0
num_pai = 12
num_img = 10
#パラメータ　終わり

pai = ["img/pai/1m.jpg","img/pai/2m.jpg","img/pai/3m.jpg","img/pai/4m.jpg","img/pai/5m.jpg","img/pai/6m.jpg","img/pai/7m.jpg","img/pai/8m.jpg","img/pai/9m.jpg","img/pai/1p.jpg","img/pai/2p.jpg","img/pai/3p.jpg","img/pai/4p.jpg","img/pai/5p.jpg","img/pai/6p.jpg","img/pai/7p.jpg","img/pai/8p.jpg","img/pai/9p.jpg","img/pai/1s.jpg","img/pai/2s.jpg","img/pai/3s.jpg","img/pai/4s.jpg","img/pai/5s.jpg","img/pai/6s.jpg","img/pai/7s.jpg","img/pai/8s.jpg","img/pai/9s.jpg","img/pai/T.jpg","img/pai/E.jpg","img/pai/H.jpg","img/pai/G.jpg","img/pai/N.jpg","img/pai/S.jpg","img/pai/W.jpg"]
 
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

    #xmlデータ　共通部分
    annotation = ET.Element('annotation')
    folder = ET.SubElement(annotation, 'folder')
    folder.text = 'XXX'
    filename = ET.SubElement(annotation, 'filename')
    filename.text = 'result/img/result_'+str(k)+'.jpg'
    source = ET.SubElement(annotation, 'source')
    owner = ET.SubElement(annotation, 'owner')
    size = ET.SubElement(annotation, 'size')
    segmented = ET.SubElement(annotation, 'segmented')
    segmented.text = '0'

    #xmlデータ　共通部分　子ノードを追加
    database = ET.SubElement(source, 'database')
    database.text = 'XXX' 
    annotation_child = ET.SubElement(source, 'annotation')
    annotation_child.text = 'XXX' 
    image = ET.SubElement(source, 'image')
    image.text = 'XXX' 
    flickrid = ET.SubElement(source, 'flickrid')
    flickrid.text = 'XXX' 

    #xmlデータ　共通部分　子ノードを追加
    flickrid_child = ET.SubElement(owner, 'flickrid')
    flickrid_child.text = 'XXX'
    name = ET.SubElement(owner, 'name')
    name.text = '?' 

    # 子ノードを追加
    width = ET.SubElement(size, 'width')
    width.text = str(back_w)
    height = ET.SubElement(size, 'height')
    height.text = str(back_h)
    depth = ET.SubElement(size, 'depth')
    depth.text = 'RGB'

    for i in range(num_pai):
        number = random.randrange(34)
        fore_img = cv2.imread(pai[number])
        fore_h, fore_w = fore_img.shape[:2]
        x=x_offset*i+x_origin
        y=y_offset*i+y_origin
        M = cv2.getRotationMatrix2D((int(x), int(y)), angle, scale)
        img_warped = cv2.warpAffine(fore_img, M, (back_w, back_h), back_img, borderMode=cv2.BORDER_TRANSPARENT)

        object.append(ET.SubElement(annotation, 'object'))

        # 子ノードを追加
        name_child.append(ET.SubElement(object[i], 'name'))
        name_child[i].text = str(pai[number]).replace('img/pai/', '').replace('.jpg', '')
        pose.append(ET.SubElement(object[i], 'pose'))
        pose[i].text = 'Unspecifited'
        truncated.append(ET.SubElement(object[i], 'truncated'))
        truncated[i].text = '0'
        difficult.append(ET.SubElement(object[i], 'difficult'))
        difficult[i].text = '1'
        bndbox.append(ET.SubElement(object[i], 'bndbox'))

        # 子ノードを追加
        xmin.append(ET.SubElement(bndbox[i], 'xmin'))
        xmin[i].text = str(M[0,2])
        ymin.append(ET.SubElement(bndbox[i], 'ymin'))
        ymin[i].text = str(M[1,2])
        xmax.append(ET.SubElement(bndbox[i], 'xmax'))
        xmax[i].text = str(M[0,2]+(fore_w*scale))
        ymax.append(ET.SubElement(bndbox[i], 'ymax'))
        ymax[i].text = str(M[1,2]+(fore_h*scale))

    # インデントを付けて保存
    doc = minidom.parseString(ET.tostring(annotation, 'utf-8'))
    with open('result/xml/test_'+str(k)+'.xml','w') as f:
        doc.writexml(f, encoding='utf-8', newl='\n', indent='', addindent='  ')

    cv2.imwrite('result/img/result_'+str(k)+'.jpg', img_warped)
from PIL import Image
import cv2
import numpy as np
import os
import glob

"""
#画像の読み込み
im = Image.open("img/1m.jpg")

plt.imshow(im)
plt.show()
"""
from matplotlib import pyplot as plt

#新しいフォルダ名
new_fol='.\\img\\pai\\270_tip'
#新しいフォルダを作成
#os.makedirs(new_fol, exist_ok=True)
#画像ファイル一覧を取得
pics=glob.glob('.\\img\\pai\\270\\*.jpg')

for pic in pics:
    print(pic)                   # 画像のパス
    i = cv2.imread(pic, 1)       # 画像読み込み

    # 変換前後の対応点を設定
    #p_original = np.float32([[0,0], [189,0], [0, 259], [189, 259]])
    #p_original = np.float32([[0,0], [259,0], [0, 189], [259, 189]])
    #p_original = np.float32([[0,0], [189,0], [0, 259], [189, 259]])
    p_original = np.float32([[0,0], [259,0], [0, 189], [259, 189]])

    #p_trans = np.float32([[40,70], [149,70], [0,189], [189,189]])
    #p_trans = np.float32([[40,40], [219,40], [0,119], [259,119]])
    #p_trans = np.float32([[40,70], [149,70], [0,189], [189,189]])
    p_trans = np.float32([[40,40], [219,40], [0,119], [259,119]])

    # 変換マトリクスと射影変換
    M = cv2.getPerspectiveTransform(p_original, p_trans)
    i_trans = cv2.warpPerspective(i, M, (259,189))

    # 画像保存
    pic = pic.replace('.\\img\\pai\\270','')
    cv2.imwrite(new_fol+pic, i_trans)
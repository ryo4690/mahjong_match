#ライブラリのインポート
import cv2
import numpy as np
import os
import glob
#新しいフォルダ名
new_fol='.\\img\\pai\\270'
#新しいフォルダを作成
#os.makedirs(new_fol, exist_ok=True)
#画像ファイル一覧を取得
pics=glob.glob('.\\img\\pai\\90\\*.jpg')
#回転角度を指定
rot_angle=180
#画像回転処理開始
for pic in pics:
    print(pic)
    pic1=cv2.imread(pic,cv2.IMREAD_COLOR)
    h,w=pic1.shape[:2]
    ROT= cv2.getRotationMatrix2D(center=(w/2,h/2),angle=rot_angle,scale=1)
    pic1 = cv2.warpAffine(pic1,ROT,dsize=(w,h))
    pic = pic.replace('.\\img\\pai\\90','')
    cv2.imwrite(new_fol+pic,pic1)
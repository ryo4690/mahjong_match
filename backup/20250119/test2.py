import cv2

cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')
img = cv2.imread('img/test4.jpg')

#グレースケール化
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#顔の検出
faces = cascade.detectMultiScale(gray,1.1,5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

cv2.imshow('facial recognition', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import urllib.request
import numpy as np
face_cascade =cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
url ='http://192.168.1.9/cam-lo.jpg'
cv2.namedWindow("gotcha", cv2.WINDOW_AUTOSIZE)
while True:
	imgResponse= urllib.request.urlopen(url)
	imgnp=np.array(bytearray(imgResponse.read()),dtype=np.uint8)
	img=cv2.imdecode(imgnp,-1)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	face=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
	for x,y,w,h in face:
		img=cv2.rectangle(img(x,y),(x+w,y+w),(0,0,255),0)
	cv2.imshow("gotcha",img)
	key=cv2.waitKey(5)
	if key==ord('q'):
		break
cv2.destroyAllwindows 
from sre_constants import SUCCESS
import cv2
from cv2 import CHAIN_APPROX_NONE

print("package imported")

ig = cv2.imread("2.jpg")
imgg = cv2.cvtColor(ig, cv2.COLOR_BGR2GRAY)
#print(img)
img1=cv2.resize(imgg,(800,800))

def getcontours(img):
    contours,hierarchy =cv2.findContours(img,cv2.RETR_EXTERNAL,CHAIN_APPROX_NONE)

    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)
        cv2.drawContours(imgcontour,cnt,-1,(0,0,255),25)
        peri=cv2.arcLength(cnt,True)
        approx=cv2.approxPolyDP(cnt,0.02*peri,True)
        x,y,w,h=cv2.boundingRect(approx)
        cv2.rectangle(imgcontour,(x,y),(x+w,y+h),(255,0,0),3)

imgcontour=img1.copy()
getcontours(img1)
cv2.imshow("output",imgcontour)
cv2.waitKey(1000000)

##cap=cv2.VideoCapture(0)
#cap.set(3,480)
#cap.set (4,300)
#cap.set(10,1000)

#while True:    -
 #   SUCCESS,img=cap.read()
  #  cv2.imshow("vdeo",img)

   # if cv2.waitKey(1) & 0xff ==ord(''):
    #    break
##
 

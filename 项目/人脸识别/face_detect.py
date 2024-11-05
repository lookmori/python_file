import cv2 as cv



def face_find(img):
    gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face_img = cv.CascadeClassifier('C:/Users/Administrator/AppData/Local/Programs/Python/Python312/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')
    result_img = face_img.detectMultiScale(gray_img,1.1)
    for x,y,w,h in result_img:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
    cv.imshow('find',img)



cap = cv.VideoCapture(0)
while True:
    flag,frame = cap.read()
    if not flag:
        break
    face_find(frame)
    if ord('q') == cv.waitKey(1):
        break

cap.release()
cv.destroyAllWindows()


import cv2 as cv 
import numpy
count = 0


def savImageToFolder(img):
    cv.imwrite("images/image.jpg",img)

def crop_img(img,x,y):
    cropped_img = img[y:y+h, x:x+w]
    cv.imshow('cropped',cropped_img)

    return cropped_img

    # count += 1 

def detection(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # print(faces)
    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
    return faces


cap = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier('C:\\Users\\samir\\AppData\\Local\\conda\\conda\\pkgs\\libopencv-3.4.1-h875b8b8_3\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('C:\\Users\\samir\\AppData\\Local\\conda\\conda\\pkgs\\libopencv-3.4.1-h875b8b8_3\\Library\\etc\\haarcascades\\haarcascade_eye.xml')

while(True):
    ret,img = cap.read()
    faces = detection(img)
    for (x,y,w,h) in faces:

        if w > 200 and h > 200 and count == 0:
            cropped_image = crop_img(img,x,y)
            count += 1
        cv.imshow('img',img)
        if count == 1:
            savImageToFolder(cropped_image)

            faces2 = detection(cropped_image)
            pass

    if cv.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv.destroyAllWindows()
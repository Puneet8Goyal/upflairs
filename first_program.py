from time import sleep
import cv2


fd=cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
sd=cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_smile.xml')

vid=cv2.VideoCapture(0)

seq=0
captured=False
while not captured:
    flag, img=vid.read()
    if flag:
        img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        
        x1,y1,w,h=(200,400,300,400)
        faces=fd.detectMultiScale(
            img_gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(150,150)
        )
        for x1,y1,w,h in faces:
            face=img_gray[y1:y1+h,x1:x1+w].copy()
            smiles=sd.detectMultiScale(face,1.1,15,minSize=(20,20))

            print(len(smiles))
            if len(smiles)==1:
                seq+=1
                if seq==5:
                    captured=cv2.imwrite('i.png',img)
                    break
                xs,ys,ws,hs=smiles[0]
                cv2.rectangle(
                    img,
                    pt1=(xs+x1,ys+y1),
                    pt2=(xs+ws+x1,ys+hs+y1),
                    color=(255,0,0),
                    thickness=8
                )
            else:
                seq=0
           
           
            cv2.rectangle(
                img,
                pt1=(x1,y1),
                pt2=(x1+w,y1+h),
                color=(0,0,255),
                thickness=10
            )

            
        cv2.imshow('Preview',img)
        key=cv2.waitKey(1)
        if key == ord('x'):
            break
    else:
        break

        
    
    
vid.release()
cv2.destroyAllWindows()
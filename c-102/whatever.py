import cv2

def takesnapshot():
    vco=cv2.VideoCapture(0)
    result=True
    while (result):
        ret,frame=vco.read()
        print (ret)
        cv2.imwrite("SS_PICS.jpg",frame)
        result=False 
    vco.release()
    cv2.destroyAllWindows()
takesnapshot()
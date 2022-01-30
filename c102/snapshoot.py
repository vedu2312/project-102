import cv2

def catchvideo():
    vc=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=vc.read()
        cv2.imwrite("newpicture1.jpg",frame)
        result=False
        
    vc.release()
    cv2.destroyAllWindows()
    
    
    
catchvideo()            

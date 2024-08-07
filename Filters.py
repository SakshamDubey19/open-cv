import cv2
path = r"C:\Users\saksham dubey\Videos\Captures\WhatsApp Video 2024-08-05 at 09.33.34_4b6f418a.mp4"
video = cv2.VideoCapture(path)

while True:
    state , frame = video.read()
    if not state:
        break
    
    frame = cv2.resize(frame,(0,0),fx=1,fy=1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV_FULL)

    # Stacking frame
    s1 = cv2.hconcat([frame, cv2.merge([gray,gray,gray])])
    s2 = cv2.hconcat([rgb,hsv])
    f = cv2.vconcat([s1,s2])
    h,w,_ = f.shape

    # adding text
    f = cv2.putText(f,'Original',(50,100),
                    cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),5)
    f = cv2.putText(f,'GrayScale',(w//2+50,100),
                    cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,255),5)
    f = cv2.putText(f,'RGB',(50,h//2+100),
                    cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),5)
    f = cv2.putText(f,'HSV',(w//2+50,h//2+100),
                    cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,255),5)
    
    cv2.imshow('frame',f)

    




    if cv2.waitKey(1) ==ord('q'):
        break
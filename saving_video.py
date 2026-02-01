import cv2

camera=cv2.VideoCapture(0)

frame_width=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_hight=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec=cv2.VideoWriter_fourcc(*"XVID")
recorded=cv2.VideoWriter("my video.mp4",codec,20,(frame_width,frame_hight))

while True:
    sucess,image= camera.read()
    if not sucess:
        break
    recorded.write(image)
    cv2.imshow("recording_video",image)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
camera.release()
recorded.release()
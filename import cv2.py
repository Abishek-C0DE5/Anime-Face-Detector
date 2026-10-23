import cv2 
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera is not opened")
    exit()

while True:
    sucess, frame = camera.read()

    if not sucess:
       break

    cv2.imshow("Prail Camera",frame)

    if cv2.waitKey(1) & 0xFF0 == ord("c"):
        break

camera.release()
cv2.destroyAllWindows
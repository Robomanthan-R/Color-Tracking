import numpy as np
import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow('Trackbars')
# cv2.resizeWindow('Trackbars', 600, 250)
cv2.createTrackbar('Huemin', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('Huemax', 'Trackbars', 255, 255, nothing)
cv2.createTrackbar('Satmin', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('Satmax', 'Trackbars', 255, 255, nothing)
cv2.createTrackbar('Valmin', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('Valmax', 'Trackbars', 255, 255, nothing)

while True:
    #image = cv2.imread(r'C:\Users\DELL\Downloads\Srijan_profile.jpg')
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hmin = cv2.getTrackbarPos('Huemin', 'Trackbars')
    hmax = cv2.getTrackbarPos('Huemax', 'Trackbars')
    smin = cv2.getTrackbarPos('Satmin', 'Trackbars')
    smax = cv2.getTrackbarPos('Satmax', 'Trackbars')
    vmin = cv2.getTrackbarPos('Valmin', 'Trackbars')
    vmax = cv2.getTrackbarPos('Valmax', 'Trackbars')
    
    min_b = np.array([hmin, smin, vmin])
    max_b = np.array([hmax, smax, vmax])
    
    mask = cv2.inRange(hsv, min_b, max_b)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Output", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Res", res)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to break the loop
        break
cap.release()
cv2.destroyAllWindows()
import cv2
import numpy as np

# Wheel identification tester (with video)
cap = cv2.VideoCapture(0)

if (cap.isOpened() == False):
    print("Error opening video stream or file")

while (cap.isOpened()):
    ret, img_orig = cap.read()
    if ret == True:

        img = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 2000, param1=100, param2=42, minRadius=300, maxRadius=0)
        try:
                circles = np.uint16(np.around(circles))
                print(circles)

                for i in circles[0, :]:
                        cv2.circle(img_orig, (i[0], i[1]), i[2], (0, 255, 0), 6)
                        cv2.circle(img_orig, (i[0], i[1]), 2, (0, 0, 255), 3)
                cv2.imshow("a", img_orig)
        except:
                cv2.imshow("a", img_orig)


        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()

cv2.destroyAllWindows()
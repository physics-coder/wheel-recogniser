import math

import cv2
import numpy as np

# Wheel marker identification tester (with video):
def dist(a,b,c,d):
    return math.sqrt((a-c)**2+(b-d)**2)
cap = cv2.VideoCapture(0)

if (cap.isOpened() == False):
    print("Error opening video stream or file")

while (cap.isOpened()):
    ret, img_orig = cap.read()
    if ret == True:

        img = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)
        ret, th = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 2000, param1=100, param2=37, minRadius=300, maxRadius=0)


        try:
                circles = np.uint16(np.around(circles))
                for n, cnt in enumerate(contours):
                    epsilon = 100 / 1000 * cv2.arcLength(cnt, True)
                    poly = cv2.approxPolyDP(cnt, epsilon, True)
                    flag = True
                    for i in range(0, len(poly)):
                        for j in range(0, len(poly[i])):
                            if dist(circles[0][0][0], circles[0][0][1], poly[i][j][0], poly[i][j][1]) > circles[0][0][2]+50:
                                flag = False
                    if flag:
                        cv2.drawContours(img_orig, [poly], -1, (128, 255, 128), 5)

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






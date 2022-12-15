import pyautogui
import math
import cv2
import numpy as np
import time
# import threading
pyautogui.PAUSE = 0
class Point():
    def __init__(self, x, y=None, polar=False):
        if type(x) == Point:
            self.x = x.x
            self.y = x.y
        else:
            if not polar:
                self.x = x
                self.y = y
            else:
                self.y = math.sin(y) * x
                self.x = math.cos(y) * x

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def dist(self, x=None, y=None):
        if not x and not y:
            return self.__abs__()
        elif x and not y:
            return math.hypot((self.x - x.x), (self.y - x.y))
        else:
            return math.hypot((self.x - x), (self.y - y))

    def __str__(self):
        return f"({self.x}, {self.y})"


class Vector(Point):
    def __init__(self, a, b=None, a1=None, b1=None):
        super().__init__(a1 - a, b1 - b)

    def __mul__(self, v):
        return self.x * v.x + self.y * v.y

    def dot_product(self, v):
        return self.__mul__(v)

    def __xor__(self, v):
        return self.x * v.y - self.y * v.x

    def cross_product(self, v):
        return self.__xor__(v)

    def mul(self, a):
        return (self.x * a, self.y * a)

    def __rmul__(self, a):
        return self.mul(a)

def dist(a,b,c,d):
    return math.sqrt((a-c)**2+(b-d)**2)
time.sleep(5)
cap = cv2.VideoCapture(0)

if (cap.isOpened() == False):
    print("Error opening video stream or file")


dir = "None"
while (cap.isOpened()):
    ret, img_orig = cap.read()
    if ret == True:
        image_hsv = cv2.cvtColor(img_orig, cv2.COLOR_BGR2HSV)
        lower1 = np.array([150 * 179 / 360, 60 * 255 / 100, 25 * 255 / 100])
        upper1 = np.array([240 * 179 / 360, 117 * 255 / 100, 100 * 255 / 100])
        mask_tick = cv2.inRange(image_hsv, lower1, upper1)
        full_mask = mask_tick
        tick_img = cv2.bitwise_and(img_orig, img_orig, mask=full_mask)
        # cv2.imshow("mask", tick_img)
        tick_img = cv2.cvtColor(tick_img, cv2.COLOR_BGR2GRAY)
        ret, th = cv2.threshold(tick_img, 70, 255, cv2.THRESH_BINARY)
        # cv2.imshow("thresh", th)
        contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        img= cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 2000, param1=100, param2=40, minRadius=200, maxRadius=0)
        try:
                circles = np.uint16(np.around(circles))
                for n, cnt in enumerate(contours):
                    epsilon = 100 / 1000 * cv2.arcLength(cnt, True)
                    poly = cv2.approxPolyDP(cnt, epsilon, True)
                    flag = True
                    print(len(poly))
                    if len(poly) > 4:
                        flag = False
                    for i in range(0, len(poly)):
                        for j in range(0, len(poly[i])):
                            if dist(circles[0][0][0], circles[0][0][1], poly[i][j][0], poly[i][j][1]) > circles[0][0][2]:
                                flag = False
                    if flag:
                        cv2.drawContours(img_orig, [poly], -1, (128, 255, 128), 5)
                    if flag:
                        for i in circles[0, :]:
                                cv2.circle(img_orig, (i[0], i[1]), i[2], (0, 255, 0), 6)
                                cv2.circle(img_orig, (i[0], i[1]), 2, (0, 0, 255))
                        v1 = Vector(circles[0][0][0], circles[0][0][1], circles[0][0][0], -3)
                        # cv2.line(img_orig, (circles[0][0][0], circles[0][0][1]), (circles[0][0][0], -10), (0,255,0), 8)
                        M = cv2.moments(cnt)
                        x = int(M["m10"] / M["m00"])
                        y = int(M["m01"] / M["m00"])
                        cv2.circle(img_orig, (x, y), 7, (255, 255, 255), -1)
                        v2 = Vector(circles[0][0][0], circles[0][0][1], x, y)
                        if v1.cross_product(v2) > 20000:
                            if dir == "a":
                                if v1.cross_product(v2) < 30000:
                                    pyautogui.keyUp("a")
                                    time.sleep(0.09)
                                    pyautogui.keyDown("a")
                                elif v1.cross_product(v2) < 40000:
                                    pyautogui.keyUp("a")
                                    time.sleep(0.07)
                                    pyautogui.keyDown("a")
                                elif v1.cross_product(v2) < 50000:
                                    pyautogui.keyUp("a")
                                    time.sleep(0.06)
                                    pyautogui.keyDown("a")
                                elif v1.cross_product(v2) < 6000:
                                    pyautogui.keyUp("a")
                                    time.sleep(0.04)
                                    pyautogui.keyDown("a")
                                else:
                                    pyautogui.keyUp("a")
                                    time.sleep(0.01)
                                    pyautogui.keyDown("a")
                            else:
                                pyautogui.keyUp("d")
                                pyautogui.keyDown("a")
                            dir = "a"
                        #
                        elif v1.cross_product(v2) < -20000:
                            if dir == "d":
                                if v1.cross_product(v2) > -30000:
                                    pyautogui.keyUp("d")
                                    time.sleep(0.09)
                                    pyautogui.keyDown("d")
                                elif v1.cross_product(v2) > -40000:
                                    pyautogui.keyUp("d")
                                    time.sleep(0.07)
                                    pyautogui.keyDown("d")
                                elif v1.cross_product(v2) > -50000:
                                    pyautogui.keyUp("d")
                                    time.sleep(0.05)
                                    pyautogui.keyDown("d")
                                elif v1.cross_product(v2) > -60000:
                                    pyautogui.keyUp("d")
                                    time.sleep(0.04)
                                    pyautogui.keyDown("d")
                                else:
                                    pyautogui.keyUp("d")
                                    time.sleep(0.01)
                                    pyautogui.keyDown("d")
                            else:
                                pyautogui.keyUp("a")
                                pyautogui.keyDown("d")
                            dir = "d"
                        else:
                            dir = "none"
                            pyautogui.keyUp("a")
                            pyautogui.keyUp("d")
                        break
                # cv2.imshow("a", img_orig)
        except:
            pass
                # cv2.imshow("a", img_orig)


        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()

cv2.destroyAllWindows()






import math
import time

import cv2
import numpy as np
import pyautogui

from geometry import Vector
from graphics import Graphics

graphics = Graphics()
pyautogui.PAUSE = 0
values = [[9, 7, 6, 4, 1], [7, 6, 4, 3, 1], [5, 4, 3, 2, 0]]


def dist(a, b, c, d):
    return math.sqrt((a - c) ** 2 + (b - d) ** 2)


detected = False
upright = False
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

direction = "None"
while cap.isOpened():
    graphics.update(detected, upright)
    ret, img_orig = cap.read()
    upright = False
    detected = False
    if ret:
        image_hsv = cv2.cvtColor(img_orig, cv2.COLOR_BGR2HSV)
        lower1 = np.array([130 * 179 / 360, 60 * 255 / 100, 25 * 255 / 100])
        upper1 = np.array([240 * 179 / 360, 117 * 255 / 100, 100 * 255 / 100])
        mask_tick = cv2.inRange(image_hsv, lower1, upper1)
        full_mask = mask_tick
        tick_img = cv2.bitwise_and(img_orig, img_orig, mask=full_mask)
        # cv2.imshow("mask", tick_img)
        tick_img = cv2.cvtColor(tick_img, cv2.COLOR_BGR2GRAY)
        ret, th = cv2.threshold(tick_img, 50, 255, cv2.THRESH_BINARY)
        # cv2.imshow("thresh", th)
        contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        img = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 2000, param1=100, param2=20, minRadius=50, maxRadius=150)
        if type(circles) != "NoneType" and contours:
            circles = np.uint16(np.around(circles))
            # print(circles[0][0][2])
            for n, cnt in enumerate(contours):
                epsilon = 100 / 1000 * cv2.arcLength(cnt, True)
                poly = cv2.approxPolyDP(cnt, epsilon, True)
                flag = True
                if len(poly) > 4:
                    flag = False
                for i in range(0, len(poly)):
                    for j in range(0, len(poly[i])):
                        if dist(circles[0][0][0], circles[0][0][1], poly[i][j][0], poly[i][j][1]) > circles[0][0][2]:
                            flag = False
                if flag:
                    detected = True
                    cv2.drawContours(img_orig, [poly], -1, (128, 255, 128), 5)
                else:
                    detected = False
                    upright = False
                if flag:
                    for i in circles[0, :]:
                        cv2.circle(img_orig, (i[0], i[1]), i[2], (0, 255, 0), 6)
                        cv2.circle(img_orig, (i[0], i[1]), 2, (0, 0, 255))
                    v1 = Vector(circles[0][0][0], circles[0][0][1], circles[0][0][0], -3)
                    M = cv2.moments(cnt)
                    x = int(M["m10"] / M["m00"])
                    y = int(M["m01"] / M["m00"])
                    cv2.circle(img_orig, (x, y), 7, (255, 255, 255), -1)
                    v2 = Vector(circles[0][0][0], circles[0][0][1], x, y)
                    val = v1.cross_product(v2) / abs(v1) / abs(v2)
                    if -0.2 < val < 0.2:
                        upright = True
                    # print(val)
                    if graphics.get_start():
                        if val > 0.2:
                            if direction == "a":
                                if val < 0.3:
                                    pyautogui.keyUp("a")
                                    time.sleep(values[graphics.get_sensitivity()][0] / 100)
                                    pyautogui.keyDown("a")
                                elif val < 0.4:
                                    pyautogui.keyUp("a")
                                    time.sleep(values[graphics.get_sensitivity()][1] / 100)
                                    pyautogui.keyDown("a")
                                elif val < 0.5:
                                    pyautogui.keyUp("a")
                                    time.sleep(values[graphics.get_sensitivity()][2] / 100)
                                    pyautogui.keyDown("a")
                                elif val < 0.6:
                                    pyautogui.keyUp("a")
                                    time.sleep(values[graphics.get_sensitivity()][3] / 100)
                                    pyautogui.keyDown("a")
                                else:
                                    pyautogui.keyUp("a")
                                    time.sleep(values[graphics.get_sensitivity()][4] / 100)
                                    pyautogui.keyDown("a")
                            else:
                                pyautogui.keyUp("d")
                                pyautogui.keyDown("a")
                            direction = "a"

                        elif v1.cross_product(v2) < -0.2:
                            if direction == "d":
                                if val > -0.3:
                                    pyautogui.keyUp("d")
                                    time.sleep(values[graphics.get_sensitivity()][0] / 100)
                                    pyautogui.keyDown("d")
                                elif val > -0.4:
                                    pyautogui.keyUp("d")
                                    time.sleep(values[graphics.get_sensitivity()][1] / 100)
                                    pyautogui.keyDown("d")
                                elif val > -0.5:
                                    pyautogui.keyUp("d")
                                    time.sleep(values[graphics.get_sensitivity()][2] / 100)
                                    pyautogui.keyDown("d")
                                elif val > -0.6:
                                    pyautogui.keyUp("d")
                                    time.sleep(values[graphics.get_sensitivity()][3] / 100)
                                    pyautogui.keyDown("d")
                                else:
                                    pyautogui.keyUp("d")
                                    time.sleep(values[graphics.get_sensitivity()][4] / 100)
                                    pyautogui.keyDown("d")
                            else:
                                pyautogui.keyUp("a")
                                pyautogui.keyDown("d")
                            direction = "d"
                        else:
                            direction = "none"
                            pyautogui.keyUp("a")
                            pyautogui.keyUp("d")
                        break
        graphics.upd_img(img_orig)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()

import cv2 as cv
import numpy as np


def extrace_object_demo():
    capture = cv.VideoCapture("C:/Users/Mark/Desktop/CubicRobot/extrace color demo.mp4")
    while True:
        ret, frame = capture.read()
        if ret is False:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([37, 43, 46])
        upper_hsv = np.array([77, 255, 255])
        mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
        cv.imshow("video", frame)
        cv.imshow("mask", mask)
        c = cv.waitKey(40)
        if c is 27:
            break


def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hsv_full = cv.cvtColor(image, cv.COLOR_BGR2HSV_FULL)
    print(np.array(hsv_full))


img = cv.imread("C:/Users/Mark/Desktop/CubicRobot/RobotVision/1.jpg")
cv.namedWindow("1")
cv.imshow("1", img)
color_space_demo(img)

b, g, r = cv.split(img)

cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)

src = cv.merge([r, g, b])
# src[:, :, 2] = 0
cv.imshow("changed", src)

# extrace_object_demo()

cv.waitKey(0)

cv.destroyAllWindows()

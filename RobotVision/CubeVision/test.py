import cv2 as cv


img = cv.imread("C:/Users/Mark/Desktop/CubicRobot/RobotVision/1.jpg")
cv.namedWindow("1")
cv.imshow("1", img)
cv.waitKey(0)

cv.destroyAllWindows()

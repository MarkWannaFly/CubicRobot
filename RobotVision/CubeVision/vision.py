import cv2 as cv
import numpy as np

'''
命名：
    函数命名：小写加下划线
    变量命名：驼峰法
'''


def show_location(image, row, col, windowname="init_location"):
    """
    显示init_location()的结果，不需要调用
    :param image:
    :param row:
    :param col:
    :param windowname:
    :return:
    """
    height = image.shape[0]
    width = image.shape[1]
    channel = image.shape[2]

    tmp = np.zeros([height, width, channel], np.uint8)
    tmp[:, :, :] = image[:, :, :]
    tmp[row - 10:row + 10, col - 10:col + 10, :] = 0

    cv.imshow(windowname, tmp)


def init_location():
    """
    调用这个函数来调试标定位置
    :return:
    """
    img = cv.imread("C:/Users/Mark/Desktop/CubicRobot/RobotVision/1.jpg")
    name = "image"
    cv.namedWindow(name)
    cv.createTrackbar("row", name, 250, 1000, nothing)
    cv.createTrackbar("col", name, 250, 1000, nothing)
    while (True):
        row = cv.getTrackbarPos("row", name)
        col = cv.getTrackbarPos("col", name)
        show_location(img, row, col, name)
        k = cv.waitKey(50)
        if k == 27:
            break


def nothing(x):
    pass


# def get_pixel_hsv(image, row, col):
#     tmp = np.zeros([1, 1, 3], np.uint8)
#     tmp[0, 0, :] = image[row, col]
#     hsv = cv.cvtColor(tmp, cv.COLOR_BGR2HSV)
#     print(hsv)


# init_location()
location = [[0, 0] for i in range(9)]
data = ['X' for i in range(9)]
location[0] = [186, 275]
location[1] = [183, 412]
location[2] = [180, 545]
location[3] = [322, 281]
location[4] = [316, 414]
location[5] = [313, 544]
location[6] = [449, 287]
location[7] = [443, 414]
location[8] = [440, 542]

img = cv.imread("C:/Users/Mark/Desktop/CubicRobot/RobotVision/1.jpg")
name = "image"
cv.namedWindow(name)
cv.imshow(name, img)

t1 = cv.getTickCount()
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lower_hsv = np.array([37, 43, 46])
upper_hsv = np.array([77, 255, 255])
green = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
for i in range(9):
    if green[location[i][0], location[i][1]] == 255:
        data[i] = 'D'

lower_hsv = np.array([11, 43, 46])
upper_hsv = np.array([25, 255, 255])
green = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
for i in range(9):
    if green[location[i][0], location[i][1]] == 255:
        data[i] = 'R'

lower_hsv = np.array([0, 0, 200])
upper_hsv = np.array([180, 30, 255])
green = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
for i in range(9):
    if green[location[i][0], location[i][1]] == 255:
        data[i] = 'B'

lower_hsv = np.array([0, 43, 46])
upper_hsv = np.array([10, 255, 255])
green = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
for i in range(9):
    if green[location[i][0], location[i][1]] == 255:
        data[i] = 'L'
lower_hsv = np.array([156, 43, 46])
upper_hsv = np.array([180, 255, 255])
green = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
for i in range(9):
    if green[location[i][0], location[i][1]] == 255:
        data[i] = 'L'

lower_hsv = np.array([100, 43, 46])
upper_hsv = np.array([124, 255, 255])
green = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
for i in range(9):
    if green[location[i][0], location[i][1]] == 255:
        data[i] = 'U'

lower_hsv = np.array([26, 43, 46])
upper_hsv = np.array([34, 255, 255])
green = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
for i in range(9):
    if green[location[i][0], location[i][1]] == 255:
        data[i] = 'F'

print(data)
t2 = cv.getTickCount()
time = (t2 - t1) / cv.getTickFrequency() * 1000
print("time : %s ms" % time)

cv.waitKey(0)

cv.destroyAllWindows()

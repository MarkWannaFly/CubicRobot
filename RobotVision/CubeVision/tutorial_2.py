import cv2 as cv
import numpy as np


def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channel = image.shape[2]
    print("width : %s, height : %s, channel : %s" % (width, height, channel))
    for row in range(height):
        for col in range(width):
            for c in range(channel):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow("pixels_demo", image)


def inverse(image):
    '''
    这个函数可以完成上面函数的功能，速度为上面函数的万分级
    上面的代码是python的解释执行，这里是调用C的api
    :param image:
    :return:
    '''

    dst = cv.bitwise_not(image)
    cv.imshow("inverse demo", dst)


def create_image():
    # img = np.zeros([400, 400, 3], np.uint8)
    # img[:, :, 0] = np.ones([400, 400]) * 255
    # cv.imshow("new image", img)

    img = np.ones([400, 400, 1], np.uint8)
    img = img * 128
    cv.imshow("new image", img)


img = cv.imread("C:/Users/Mark/Desktop/CubicRobot/RobotVision/1.jpg")
# cv.namedWindow("1")
# cv.imshow("1", img)

# create_image()

t1 = cv.getTickCount()
inverse(img)
t2 = cv.getTickCount()

time = (t2 - t1) / cv.getTickFrequency()
print("time : %s ms" % time)

cv.waitKey(0)

cv.destroyAllWindows()

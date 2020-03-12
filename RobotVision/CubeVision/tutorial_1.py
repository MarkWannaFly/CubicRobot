import cv2 as cv
import numpy as np

def video_demo():
    capture = cv.VideoCapture(0)
    while(True):
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        if c == 27:
            break


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(type(image.shape))
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)


img = cv.imread("C:/Users/Mark/Desktop/CubicRobot/RobotVision/1.jpg")
cv.namedWindow("1")
cv.imshow("1", img)
get_image_info(img)
# cv.imwrite("C:/Users/Mark/Desktop/CubicRobot/RobotVision/1.png", img)
# video_demo()
cv.waitKey(0)

cv.destroyAllWindows()

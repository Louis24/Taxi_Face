import os
import cv2
import numpy as np

"""
@param rho Distance resolution of the accumulator in pixels.
与象素相关单位的距离精度，一般取1
@param theta Angle resolution of the accumulator in radians.
弧度测量的角度精度
@param threshold Accumulator threshold parameter. Only those lines are returned that get enough
阈值参数。如果相应的累计值大于threshold，则函数返回的这个线段.
"""

"""
@param dp Inverse ratio of the accumulator resolution to the image resolution. 
dp为检测内侧圆心的累加器图像的分辨率于输入图像之比的倒数
@param minDist Minimum distance between the centers of the detected circles.
minDist表示两个圆之间圆心的最小距离
@param param1 First method-specific parameter. In case of #HOUGH_GRADIENT , it is the higher 
threshold of the two passed to the Canny edge detector (the lower one is twice smaller).
param1有默认值100，它表示传递给canny边缘检测算子的高阈值，而低阈值为高阈值的一半
@param param2 Second method-specific parameter. In case of #HOUGH_GRADIENT , it is the accumulator threshold
for the circle centers at the detection stage. The smaller it is, the more false circles may be detected. .
param2有默认值100，它表示在检测阶段圆心的累加器阈值，它越小，就越可以检测到更多根本不存在的圆，
而它越大的话，能通过检测的圆就更加接近完美的圆形了
minRadius有默认值0，圆半径的最小值
maxRadius有默认值0，圆半径的最大值
"""


def detect(file):
    """
    r = 1
    t = depends on the image size w
    filter:
    α= 60~90 0~30
    tan(30) = 0.57
    tan(60) = 1.73
    tan(90) = inf
    """

    img = cv2.imread("taxi_in/" + file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    w, h = gray.shape
    # print(w, h)
    edges = cv2.Canny(gray, 128, 256)  # 用这组参数细节更少一些
    cv2.imshow('edges', edges)

    lines = cv2.HoughLines(edges, 1, np.pi / 180, w // 3)

    if len(lines) != 0:

        for i in range(0, len(lines)):
            rho, theta = lines[i][0][0], lines[i][0][1]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho

            x1 = int(x0 + 1000 * -b)
            y1 = int(y0 + 1000 * a)
            x2 = int(x0 - 1000 * -b)
            y2 = int(y0 - 1000 * a)

            k = abs((y2 - y1) / (x2 - x1 + 0.001))

            if k >= 1.732 or k <= 0.57:
                cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,
                               dp=1,
                               minDist=w // 3,
                               param1=100,
                               param2=30,
                               minRadius=h // 30,
                               maxRadius=h // 10)

    if circles is not None:
        circles = np.uint16(np.around(circles))

        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv2.circle(img, center, 1, (0, 255, 0), 2)
            # circle outline
            radius = i[2]
            cv2.circle(img, center, radius, (0, 255, 0), 2)

    # cv2.imshow('lines', img)
    # cv2.waitKey(0)
    print("taxi_out/" + file)
    cv2.imwrite("taxi_out/" + file, img)


def traverse():
    x = os.listdir("taxi_in/")

    for i in x:
        detect(i)


if __name__ == '__main__':
    # detect('06.jpg')
    traverse()

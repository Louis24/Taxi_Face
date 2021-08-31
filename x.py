#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2020/6/23 10:02
#  @Author  : Louis Li
#  @Email   : vortex750@hotmail.com


import cv2
import numpy as np
import matplotlib.pyplot as plt


def hist(image, color):
    hist = cv2.calcHist([image], [0], None, [256], [0, 255])
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
    hist = np.zeros([256, 256, 3], np.uint8)
    hpt = int(0.9 * 256)

    for h in range(256):
        intensity = int(hist[h] * hpt / maxVal)
        cv2.line(hist, (h, 256), (h, 256 - intensity), color)
    return hist


def draw():
    img = cv2.imread("color/1.png")
    img = cv2.resize(img, None, fx=0.6, fy=0.6, interpolation=cv2.INTER_CUBIC)
    b, g, r = cv2.split(img)

    histB = hist(b, [255, 0, 0])
    histG = hist(g, [0, 255, 0])
    histR = hist(r, [0, 0, 255])

    cv2.imshow("histB", histB)
    cv2.imshow("histG", histG)
    cv2.imshow("histR", histR)
    cv2.imshow("Img", img)
    cv2.waitKey(0)


def gray():
    img = cv2.imread("color/1.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # plt.imshow(gray, cmap='gray')
    # plt.axis('off')
    # plt.title('Gray')

    gray_hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

    plt.plot(gray_hist)
    plt.title('Grayscale Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of Pixels')
    plt.show()


def channel():
    img = cv2.imread("color/2.png")

    # 按R、G、B三个通道分别计算颜色直方图
    b_hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    g_hist = cv2.calcHist([img], [1], None, [256], [0, 256])
    r_hist = cv2.calcHist([img], [2], None, [256], [0, 256])

    # 显示3个通道的颜色直方图
    plt.plot(b_hist, label='B', color='blue')
    plt.plot(g_hist, label='G', color='green')
    plt.plot(r_hist, label='R', color='red')
    plt.legend(loc='best')
    plt.xlim([0, 256])
    plt.show()


def hsv():
    img = cv2.imread("color/1.png")
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_hist = cv2.calcHist([hsv], [0], None, [256], [0, 256])
    s_hist = cv2.calcHist([hsv], [1], None, [256], [0, 256])
    v_hist = cv2.calcHist([hsv], [2], None, [256], [0, 256])

    plt.plot(h_hist, label='H', color='blue')
    plt.plot(s_hist, label='S', color='green')
    plt.plot(v_hist, label='V', color='red')
    plt.legend(loc='best')
    plt.xlim([0, 256])
    plt.show()


def main():
    # draw()
    # gray()
    # channel()
    hsv()


if __name__ == '__main__':
    main()

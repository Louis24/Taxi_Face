#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2020/6/23 14:00
#  @Author  : Louis Li
#  @Email   : vortex750@hotmail.com

import cv2
import numpy as np


def hsv():
    img = cv2.imread("color/2.png")
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (0, 0, 221), (180, 30, 255))
    imask = mask > 0
    white = np.zeros_like(img, np.uint8)
    white[imask] = img[imask]

    cv2.imshow('white', white)
    cv2.imwrite('color/2.jpg', white)
    cv2.waitKey()

hsv()

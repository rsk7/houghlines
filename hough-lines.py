# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html

import sys
import cv2
import numpy as np

# usage: python hough-lines.py [img_path] [output_path]

if len(sys.argv) < 3:
  print("Usage: python hough-lines.py [img_path] [output_path]")
  sys.exit()

imgIn, imgOut = sys.argv[1], sys.argv[2]

img = cv2.imread(imgIn)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

for l in lines:
  for rho, theta in l:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imwrite(imgOut, img)



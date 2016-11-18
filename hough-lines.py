# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html

import sys
import cv2
import numpy as np
import itertools

import intersection

from functools import reduce


# usage: python hough-lines.py [img_path] [output_path]

if len(sys.argv) < 3:
  print("Usage: python hough-lines.py [img_path] [output_path]")
  sys.exit()

imgIn, imgOut = sys.argv[1], sys.argv[2]

img = cv2.imread(imgIn)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

def l2p(rt):
  return line2point(rt[0][0], rt[0][1])

def line2point(rho, theta):
  a = np.cos(theta)
  b = np.sin(theta)
  x0 = a * rho
  y0 = b * rho
  x1 = int(x0 + 1000 * (-b))
  y1 = int(y0 + 1000 * ( a))
  x2 = int(x0 - 1000 * (-b))
  y2 = int(y0 - 1000 * ( a))
  return ((x1, y1), (x2, y2))

# find lines that are close
# prb better way to write this in python
lines_to_remove = []
for idx, l in enumerate(lines):
  for l2 in lines[idx+1:]:
    # within +- 5
    threshold = 5;
    difference = abs(l[0][0] - l2[0][0])
    if difference <= threshold and l[0][1] == l2[0][1]:
      lines_to_remove.append(l2[0][0])

# filter lines that are close
lines = [x for x in lines if x[0][0] not in lines_to_remove]

for l in lines:
  for rho, theta in l:
    line = line2point(rho, theta)
    cv2.line(img, line[0], line[1], (0, 0, 255), 2)


thetas = set([x[0][1] for x in lines])

# reduce thetas to two values
# or group thetas together
groupedlines = []
for t in thetas:
  groupedlines.append([x for x in lines if x[0][1] == t])

# compute cartesian product of line groupings
cartesian = list(itertools.product(*groupedlines))

# convert cartesian to line point form
# might contain too many entries
pointform = [(l2p(c[0]), l2p(c[1])) for c in cartesian]

# convert to line form
lineform = [(intersection.line(p[0][0], p[0][1]), intersection.line(p[1][0], p[1][1])) for p in pointform]

# points of intersection
points = [intersection.intersection(l[0], l[1]) for l in lineform]


print(points)







#cv2.imwrite(imgOut, img)






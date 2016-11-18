# from http://stackoverflow.com/a/20679579
from __future__ import division

def line(p1, p2):
  A = (p1[1] - p2[1])
  B = (p2[0] - p1[0])
  C = (p1[0]*p2[1] - p2[0]*p1[1])
  return A, B, -C

def intersection(L1, L2):
  D  = L1[0] * L2[1] - L1[1] * L2[0]
  Dx = L1[2] * L2[1] - L1[1] * L2[0]
  Dy = L1[0] * L2[2] - L1[2] * L2[0]
  if D != 0:
    x = Dx / D
    y = Dy / D
    return (x, y)
  else:
    return False

'''
# Usage:

L1 = line([0,1], [2,3])
L2 = line([2,3], [0,4])

R = intersection(L1, L2)
if R:
    print "Intersection detected:", R
else:
    print "No single intersection point detected"
'''



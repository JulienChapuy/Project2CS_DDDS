# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 19:51:36 2021

@author: Lloyd
"""

import numpy as np

from architecture.coordinates import Coordinates

def line_equation(x1, y1, x2, y2):
    '''(y2-y1)x + (x1-x2)y + (x2y1-x1y2) = 0'''
    a = y2 - y1
    b = x1 - x2
    c = x2*y1 - x1*y2
    return a, b, c
        
def find_intersection(A, B, C, D):
    '''solving MX = Y'''
    a1, b1, c1 = line_equation(A.x, A.y, B.x, B.y)
    a2, b2, c2 = line_equation(C.x, C.y, D.x, D.y)
    
    Y = - np.array([[c1],
                    [c2]])
    M = np.array([[a1, b1],
                  [a2, b2]])
    # invM = np.linalg.inv(M)
    # X = np.dot(invM, Y)
    X = np.linalg.solve(M, Y)
    
    return Coordinates(X[0], X[1])

def intersects_segment(A, B, X):
    AX = np.array([X.x - A.x, X.y - A.y])
    XB = np.array([B.x - X.x, B.y - X.y])
    equal_signs = np.array_equal(np.sign(AX), np.sign(XB))

    return equal_signs
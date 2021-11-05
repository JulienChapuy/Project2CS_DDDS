# -*- coding: utf-8 -*-

"""
This scripts implements tools for checking if two segments (not lines)
intersect with each other.

Functions:
---------
line_equation(x1, y1, x2, y2)
    Returns the parameters of the line equation 
    passing through the point (x1, y1) and (x2, y2)
    
find_intersection(A, B, C, D)
    Returns the intersection of lines (AB) and (CD)
    
intersects_segment(A, B, X)
    Checks if point X is included in the segment [AB]
"""

import numpy as np

from architecture.coordinates import Coordinates

def line_equation(x1, y1, x2, y2):
    """Returns the parameters (a, b, c) of the line equation ax + by + c = 0
    passing through the point (x1, y1) and (x2, y2), where:
        a = y2 - y1
        b = x1 - x2
        c = x2*y1 - x1*y2
    
    Parameters
    ----------
    x1 : float
        the x value of the first point
    y1 : float
        the y value of the first point
    x2 : float
        the x value of the second point
    y2 : float
        the y value of the second point
            
    Returns
    -------
    (a, b, c) : tuple of floats
        the parameters of the line equation
    """
    
    a = y2 - y1
    b = x1 - x2
    c = x2*y1 - x1*y2
    return a, b, c
        
def find_intersection(A, B, C, D):
    """Returns the intersection of lines (not segments) (AB) and (CD) 
    where A, B, C, D are coordinates (x, y).
    
    To find the intersection X, we solve the equation MX = Y where:
        M = [[a1, b1],
             [b1, b2]]
        Y = [[-c1],
             [-c2]]
        
    with:
        a1, b1, c1 = line_equation(A.x, A.y, B.x, B.y)
        a2, b2, c2 = line_equation(C.x, C.y, D.x, D.y)
    
    Parameters
    ----------
    A, B : Coordinates
        the coordinates defining the first line
    C, D : Coordinates
        the coordinates defining the second line
            
    Returns
    -------
    intersection : Coordinates
        the coordinates of the intersection
    """
    
    a1, b1, c1 = line_equation(A.x, A.y, B.x, B.y)
    a2, b2, c2 = line_equation(C.x, C.y, D.x, D.y)
    
    Y = - np.array([[c1],
                    [c2]])
    M = np.array([[a1, b1],
                  [a2, b2]])

    X = np.linalg.solve(M, Y)
    intersection = Coordinates(X[0], X[1])
    
    return intersection

def intersects_segment(A, B, X):
    """Checks if point X is inside the segment [AB].
    
    To check the inclusion of X in [AB], 
    we check the equality of the signs 
    of the vectors AX and XB.
    
    Parameters
    ----------
    A, B : Coordinates
        the coordinates defining the segment
    X : Coordinates
        the point for which we wish to know if it is contained in [AB]
            
    Returns
    -------
    equal_signs : bool
        True if X is in [AB], False otherwise
    """
    
    AX = np.array([X.x - A.x, X.y - A.y])
    XB = np.array([B.x - X.x, B.y - X.y])
    equal_signs = np.array_equal(np.sign(AX), np.sign(XB))

    return equal_signs
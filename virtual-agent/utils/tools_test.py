# -*- coding: utf-8 -*-

import unittest
from architecture.coordinates import Coordinates
from utils.tools import line_equation, find_intersection, intersects_segment

class TestStringMethods(unittest.TestCase):

    def test_line_equation(self):
        x1 = -1
        y1 = 0
        x2 = 1
        y2 = 2
        a, b, c = 2, -2, 2
        self.assertEqual(line_equation(x1, y1, x2, y2), (a, b, c))

    def test_find_intersection(self):
        A = Coordinates(0, 2)
        B = Coordinates(0, 3)
        C = Coordinates(-1, 0)
        D = Coordinates(1, 2)
        
        intersection = find_intersection(A, B, C, D)
        
        self.assertEqual(intersection.x, 0)
        self.assertEqual(intersection.y, 1)
        

    def test_intersects_segment(self):
        A = Coordinates(-1, 0)
        B = Coordinates(1, 2)
        X1 = Coordinates(0, 1)
        X2 = Coordinates(0, 0)
        
        self.assertTrue(intersects_segment(A, B, X1))
        self.assertFalse(intersects_segment(A, B, X2))

        pass

if __name__ == '__main__':
    unittest.main()
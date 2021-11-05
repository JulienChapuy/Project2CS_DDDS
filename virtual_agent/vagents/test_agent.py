# -*- coding: utf-8 -*-

import unittest
from architecture.coordinates import Coordinates
from vagents.agent import Agent

class TestAgent(unittest.TestCase):

    def test_move(self):
       a = Agent(1, 1)
       a.move(0, 1)
       self.assertEqual(a.x, 1)
       self.assertEqual(a.y, 2)

if __name__ == '__main__':
    unittest.main()
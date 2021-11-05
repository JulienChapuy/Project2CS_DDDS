# -*- coding: utf-8 -*-

import unittest
from architecture.coordinates import Coordinates
from vagents.agent import Agent
from vagents.agents import Agents

class TestAgent(unittest.TestCase):

    def test_move(self):
       a1 = Agent(1, 1)
       a2 = Agent(0, 0)
       agents = Agents([a1, a2])
       agents.move()
       self.assertNotEqual(a1.x, 1)
       self.assertNotEqual(a1.y, 1)
       self.assertNotEqual(a2.x, 0)
       self.assertNotEqual(a2.y, 0)

if __name__ == '__main__':
    unittest.main()
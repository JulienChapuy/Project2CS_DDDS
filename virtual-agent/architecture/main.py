# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 13:57:24 2021

@author: Lloyd
"""

import matplotlib.pyplot as plt

from architecture.wall import Wall
from architecture.walls import Walls
from architecture.room import Room
from architecture.floor import Floor
from architecture.building import Building


if __name__ == '__main__':
    walls = Walls([Wall(),
                   Wall(),
                   Wall(),
                   Wall()])
    
    # plots
    plt.figure()
    walls.plot()
    plt.show()
    
    # bb1 = BoundingBox(0, 0, 5, 5)
    # bb2 = BoundingBox(1, 5, 2, 6)
    # bbs = BoundingBoxes([bb1, bb2])
    # print(bbs)
    # bbs.plot()
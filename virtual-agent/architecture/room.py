# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:03:21 2021

@author: Lloyd
"""
import matplotlib.pyplot as plt

from architecture.coordinates import Coordinates
from architecture.wall import Wall
from architecture.walls import Walls, WallsGenerator
from architecture.windows import Windows
from architecture.door import Door
from architecture.doors import Doors

class Room():
    def __init__(self, walls=Walls()):
        # doors = Doors()
        # windows = Windows()
        # for wall in walls.wall_list:
            # print(wall.doors)
            # doors.myadd(wall.doors)
            # self.windows.myadd(wall.windows)
            
        self.walls = walls
        # self.doors = doors
        # self.windows = windows
   
    def __str__(self):
        s = 'walls:' + '\n'
        s = s + str(self.walls)
        # s = s + '\n' + 'doors: \n'
        # for door in self.doors.door_list:
        #     s = s + str(door)
        # s = s + '\n' + 'windows: \n'
        # for window in self.windows.window_list:
        #     s = s + str(window)

        return s
    
    def plot(self):
        self.walls.plot()
        # self.doors.plot()
        # self.windows.plot()
    
    
if __name__ == '__main__':
    # wg = WallsGenerator()
    # walls = wg.generate([(0, 0), (0, 10), (10, 10), (10, 0)])
    # room1 = Room(walls)
    
    shared_wall = Wall(0, 5, 5, 5)
    
    doors = Doors([Door(1, 5, 2, 5),
                    Door(3, 5, 4, 5)])
    
    shared_wall.doors = doors
    
    walls0 = Walls([Wall(0, 5, 0, 0),
                    Wall(0, 0, 5, 0),
                    Wall(5, 0, 5, 5),
                    shared_wall])
    
    # print(walls0)
    
    # walls1 = Walls([Wall(0, 5, 0, 10),
    #                 Wall(0, 10, 5, 10),
    #                 Wall(5, 10, 5, 5),
    #                 shared_wall])

    
    # print(walls1)
    
    room0 = Room(walls0)
    print(room0)
    # room1 = Room(walls1)
    # print(room1)
    
    # plots
    plt.figure()
    room0.plot()
    plt.show() 
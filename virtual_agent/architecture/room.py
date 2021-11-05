# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

from architecture.coordinates import Coordinates
from architecture.wall import Wall
from architecture.walls import Walls
from architecture.windows import Windows
from architecture.door import Door
from architecture.doors import Doors

class Room():
    """A class that implements a room composed of walls, doors and windows

    Attributes
    ----------
    walls : Walls()
        the walls of the room
    doors : Doors()
        the doors of the room
    windows: Windows()
        the windows of the room
        
    Methods
    -------
    plot()
        Plots the walls, doors and windows as segments
    """
    def __init__(self, walls=Walls(), doors=Doors(), windows=Windows()):
        self.walls = walls
        self.doors = doors
        self.windows = windows
   
    def __str__(self):
        s = 'walls:' + '\n'
        s = s + str(self.walls)
        s = s + '\n' + 'doors: \n'
        for door in self.doors.door_list:
            s = s + str(door)
        s = s + '\n' + 'windows: \n'
        for window in self.windows.window_list:
            s = s + str(window)

        return s
    
    def plot(self):
        """Plots the walls, doors and windows as segments"""
        self.walls.plot()
        self.doors.plot()
        self.windows.plot()
    
    
if __name__ == '__main__':
    shared_wall = Wall(5, 5, 0, 5)
    
    doors = Doors([Door(1, 5, 2, 5),
                   Door(3, 5, 4, 5)])
    
    shared_wall.doors = doors
    
    walls0 = Walls([Wall(0, 0, 5, 0),
                    Wall(5, 0, 5, 5),
                    shared_wall,
                    Wall(0, 5, 0, 0)])

    room0 = Room(walls0)
    print(room0)
    
    # plots
    plt.figure()
    room0.plot()
    plt.show() 
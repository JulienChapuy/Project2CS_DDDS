# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:01:26 2021

@author: Lloyd
"""
from architecture.coordinates import CoordinatesPair
from architecture.doors import Doors
from architecture.windows import Windows


class Wall(CoordinatesPair):
    """A class that implements a wall

    Attributes
    ----------
    x1 : float
        the x value of the first coordinates
    y1 : float
        the y value of the first coordinates
    x2 : float
        the x value of the second coordinates
    y2 : float
        the y value of the second coordinates
    height : float
        the height of the wall
    doors : Doors
        the doors inside the wall
    windows : Windows
        the windows inside the wall

    Methods
    -------
    plot()
        Plots the wall as a segment
    """
    
    def __init__(self, x1=0, y1=0, x2=1, y2=0, height=3, doors=Doors(), windows=Windows(), color='black'):
        super().__init__(x1, y1, x2, y2)
        self.doors = doors
        self.windows = windows
        self.color = color
        
    def __str__(self):
        s = '-----wall-----: \n'
        s = s + super().__str__() + '\n\n'
        s = s + 'doors: \n\n'
        s = s + str(self.doors) + '\n'
        s = s + 'windows: \n'
        s = s + str(self.windows)
        return s
    
    def plot(self):
        """Plots the wall as a segment"""
        super().plot(color=self.color)
        self.doors.plot()
        self.windows.plot()
            
if __name__ == '__main__':
    w1 = Wall(0, 0, 10, 0)
    w2 = Wall(0, 0, 0, 10)
    w1.plot()
    w2.plot()
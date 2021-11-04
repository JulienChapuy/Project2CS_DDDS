# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 23:04:10 2021

@author: Lloyd
"""

from architecture.door import Door

class Doors():
    """A class that implements several doors

    Attributes
    ----------
    door_list : list
        a list of doors
        
    Methods
    -------
    plot()
        Plots the doors as segments
    """
    
    def __init__(self, door_list=[]):
        self.door_list = door_list
        
    def __str__(self):
        s = ''
        for door in self.door_list:
            s = s + str(door)
        return s
    
    def plot(self):
        """Plots the doors as segments"""
        for door in self.door_list:
            door.plot()
        
        
if __name__ == '__main__':
    door1 = Door(1, 1, 2, 2, height=2.0)
    door2 = Door(1, 1, 2, 1, height=2.0)
    doors = Doors([door1, door2])
    doors.plot()
    print(doors)
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 12:03:51 2021

@author: Julien
"""

class Area():
    """A class that implements a general Area class

    Attributes
    ----------
    walls: list
        a list of walls that describe the Area
        
    Methods
    -------
    plot()
        Plot the Area
    """
    def __init__(self, walls):
        self.walls = walls
        
    def plot(self):
        for w in self.walls:
            w.plot()
    
class Room(Area):
    """A class that implements a room class from Area

    Attributes
    ----------
    walls: list
        a list of walls in the room
    doors: list
        a list of doors in the room
    windows: list
        a list of windows in the room
        
    Methods
    -------
    plot()
        Plot the room
    """
    
    def __init__(self, walls):
        super().__init__(walls)
        self.doors = []
        self.windows = []
            
        i = 0 
        for w in self.walls:
            
            if 'doors' in w.__dict__ and w.doors != []:
                k = []
                for door in w.doors:
                    k.append(door)
                    
                k.append(i)
                self.doors.append(k)
            if 'windows' in w.__dict__:
                t = []
                for window in w.windows:
                    t.append(window)
                    
                t.append(i)
                self.windows.append(t)
                    
            i+=1
            
        
    
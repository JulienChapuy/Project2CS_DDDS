# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 12:03:51 2021

@author: Julien
"""

class Area():
    def __init__(self, walls):
        self.walls = walls
        
    def plot(self):
        for w in self.walls:
            w.plot()
    
class Room(Area):
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
            
        
    
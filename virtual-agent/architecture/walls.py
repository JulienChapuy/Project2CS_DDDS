# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 23:19:51 2021

@author: Lloyd
"""

from architecture.wall import Wall


class Walls():
    """A class that implements several walls

    Attributes
    ----------
    wall_list : list
        a list of walls
        
    Methods
    -------
    plot()
        Plots the walls as segments
    """
    def __init__(self, wall_list=[Wall()]):
        self.wall_list = wall_list
        
    def __str__(self):
        s = ''
        for wall in self.wall_list:
            s = s + str(wall) + '\n'
        s = s + '\n'
        return s
    
    def plot(self):
        """Plots the walls as segments"""
        for wall in self.wall_list:
            wall.plot()
        
        
if __name__ == '__main__':
    walls = Walls([Wall(0, 0, 5, 0),
                    Wall(5, 0, 5, 5),
                    Wall(5, 5, 0, 5),
                    Wall(0, 5, 0, 0)])
    walls.plot()
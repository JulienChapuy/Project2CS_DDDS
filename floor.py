# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:17:06 2021

@author: Julien
"""

#a file where we define the floor class

class Floor():
    """A class that implements a Floor

    Attributes
    ----------
    length: numeric
        length of a floor
    width: numeric
        width of a floor
    height: numeric
        length of a floor
    floor_number: int
        the number of the floor in the building
        
    areas: list
        list of the areas in the floor
    walls: list
        list of the walls in the floor
        
    Methods
    -------
    plot()
        Plot the floor
    """
    def __init__(self, length, width, height, floor_number, areas = [], walls = []):
        
        self.length = length
        self.width = width
        self.height = height
        self.floor_number = floor_number
        
        self.areas = areas
        self.walls = walls
        
    def plot(self):
        for area in self.areas:
            area.plot()
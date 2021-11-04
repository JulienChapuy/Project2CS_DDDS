# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:05:05 2021

@author: Lloyd
"""

class Building():
    """A class that implements a building composed of floors

    Attributes
    ----------
    rooms_list : list
        the list of rooms of the floor
        
    Methods
    -------
    plot()
        Plots the floors of the building
    """
    
    def __init__(self, floor_list):
        self.floor_list = floor_list
        
    def __str__(self):
        s = ''
        for i, floor in enumerate(self.floor_list):
            s = s + 'floor ' + i + ': ' + str(floor) + '\n'
        return s
    
    def plot(self):
        """Plots the floors of the building"""
        for floor in self.floor_list:
            floor.plot()
            
            
if __name__ == '__main__':
    pass
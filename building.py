# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:18:02 2021

@author: Julien
"""

#a file where we define the building class

import matplotlib.pyplot as plt

class Building():
    """A class that implements a Floor

    Attributes
    ----------
    length: numeric
        length of a floor
    width: numeric
        width of a floor
    height: numeric
        length of a floor
    floors_list: list
        list of the floors in the building
        
    Methods
    -------
    plot()
        Plot the floor
    """
    def __init__(self, length, width, height, floors_list = []):
        self.length = length
        self.width = width
        self.height = height
        self.floors_list = floors_list
        self.nb_floors = len(floors_list)
        
        
    def add_floor(self, floor):
        self.floors_list.append(floor)
        self.nb_floors += 1
        
    def plot(self):
        for f in self.floors_list:
            f.plot()
            plt.title('Floor number : ' + str(f.floor_number))
            plt.show()
            

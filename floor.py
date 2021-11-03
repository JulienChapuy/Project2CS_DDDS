# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:17:06 2021

@author: Julien
"""

class Floor():
    def __init__(self, floor_number, areas = [], walls = []):
        
        # self.length = length
        # self.width = width
        # self.height = height
        self.floor_number = floor_number
        
        self.areas = areas
        self.walls = walls
        
    def plot(self):
        for area in self.areas:
            area.plot()
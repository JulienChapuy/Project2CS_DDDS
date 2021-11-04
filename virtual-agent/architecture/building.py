# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:05:05 2021

@author: Lloyd
"""

class Building():
    def __init__(self, floors):
        self.floors = floors
        
    def __str__(self):
        s = ''
        for i, floor in enumerate(self.floors):
            s = s + 'floor ' + i + ': ' + str(floor) + '\n'
        return s
    
    def plot(self):
        for floor in self.floors:
            floor.plot()
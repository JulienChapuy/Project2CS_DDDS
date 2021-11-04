# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:03:01 2021

@author: Lloyd
"""

from architecture.coordinates import CoordinatesPair

class Window(CoordinatesPair):
    def __init__(self, x1, y1, x2, y2, height=0, height_above_floor=0, color='green', linestyle='--'):
        super().__init__(x1, y1, x2, y2)
        self.height = height
        self.height_above_floor = height_above_floor
        self.color = color
        self.linestyle  = linestyle 
        
    def __str__(self):
        s = super().__str__() + '\n'
        s += 'height: {}m'.format(self.height) + '\n'
        s += 'height above floor: {}m'.format(self.height_above_floor) + '\n'
        s += 'color: {}'.format(self.color) + '\n'
        return s
    
    def plot(self):
        super().plot(linestyle=self.linestyle, color=self.color)
        
        
if __name__ == '__main__':
    window = Window(1, 1, 2, 2, height=0.5, height_above_floor=1.0)
    window.plot()
    print(window)
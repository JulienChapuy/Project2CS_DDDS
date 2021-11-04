# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:02:08 2021

@author: Lloyd
"""
    
from architecture.coordinates import CoordinatesPair      
        
class Door(CoordinatesPair):
    def __init__(self, x1, y1, x2, y2, height=2, color='blue', linestyle='--'):
        super().__init__(x1, y1, x2, y2)
        self.height = height
        self.color = color
        self.linestyle  = linestyle 
        
    def __str__(self):
        s = super().__str__() + '\n'
        # s += 'height: {}m'.format(self.height) + '\n'
        # s += 'color: {}'.format(self.color) + '\n'
        return s
            
    def plot(self):
        super().plot(linestyle=self.linestyle, color=self.color)
        
        
if __name__ == '__main__':
    door = Door(5, 0, 1, 4)
    door.plot()
    print(door)
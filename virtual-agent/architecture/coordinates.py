# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 13:58:00 2021

@author: Lloyd
"""

import matplotlib.pyplot as plt

class Coordinates():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return str([self.x, self.y])
    
    def plot(self, color='black', marker='o'):
        plt.plot(self.x, self.y, color=color, marker=marker)
        
    def change(self, x):
        self.x = x
        
class CoordinatesPair():
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    def __str__(self):
        return str([self.x1, self.y1, self.x2, self.y2])
    
    def plot(self, linestyle='-', color='black', marker='o'):
        plt.plot([self.x1, self.x2], [self.y1, self.y2], 
                 linestyle=linestyle , color=color, marker=marker)
        
    def has_crossed_border(self, old_x, old_y, new_x, new_y):
        if self.x1 == self.x2:
            return (old_x - self.x1) * (new_x - self.x1) <= 0 # take 0 into account
        else:
            def f(x):
                '''y = ax + b'''                
                a = (self.y2 - self.y1) / (self.x2 - self.x1)
                return a * (x - self.x1) + self.y1
            
            return (old_y - f(old_x)) * (new_y - f(new_x)) <= 0 # take 0 into account

        
if __name__ == '__main__':
    c = Coordinates(3, 4)
    cp = CoordinatesPair(0, 0, 1, 1)
    
    assert str(c) == '[3, 4]'
    assert str(cp) == '[0, 0, 1, 1]'

    print(c)
    print(cp)
    
    c.plot()
    cp.plot()
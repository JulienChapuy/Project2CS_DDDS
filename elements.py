# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 11:11:07 2021

@author: Julien
"""
import matplotlib.pyplot as plt
import numpy as np

class Elements():
    def __init__(self, bound1, bound2, material):
        self.bound1 = bound1
        self.bound2 = bound2
        self.length = np.sqrt((bound1[0]-bound2[0])**2 + (bound1[1]-bound2[1])**2)
        self.material = material
        self.color = 'white'
        
    def plot(self):
        t = np.linspace(self.bound1, self.bound2, 1000)
        plt.plot(t[:,0], t[:,1], color = self.color)
        
        if type(self) == Wall:
            for d in self.doors:
                d.plot()
            for w in self.windows:
                w.plot()
        
            
class Wall(Elements):
    def __init__(self, bound1, bound2, material, elements = None):
        super().__init__(bound1, bound2, material)
        self.doors = []
        self.windows = []
        self.color = 'gray'
        
        if elements != None:
            
            for i in range(len(elements)):
                
                if type(elements[i]) == Door:
                    self.doors.append(elements[i])
                elif type(elements[i]) == Window:
                    self.windows.append(elements[i])
                else:
                    pass
                
        else:
            pass
        
        
class Window(Elements):
    def __init__(self, bound1, bound2, material):
        super().__init__(bound1, bound2, material)
        self.color = 'blue'
        
class Door(Elements):
    def __init__(self, bound1, bound2, material):
        super().__init__(bound1, bound2, material)
        self.color = 'red'
        

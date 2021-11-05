# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 11:11:07 2021

@author: Julien
"""
import matplotlib.pyplot as plt
import numpy as np

#we define here Elements a general class of objects that are used to build an area

#we then define Wall, Door, Window 3 classes that inherit from Elements

class Elements():
    """A class that implements a general class Elements

    Attributes
    ----------
    bound1: tuple
        first boundary of an element
    bound2: tuple
        second boundary of an element
    length: int
        length of an element
    material: str
        name of the material
    color: str
        color of the element for plot
        
    Methods
    -------
    plot()
        Plot the element
    """
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
        
#the Wall class. It is somehow special since a Wall can contains other elements (door, window)
      
class Wall(Elements):
    """A class that implements a Wall class from Elements
    
    Attributes
    ----------
    bound1: tuple
        first boundary of a wall
    bound2: tuple
        second boundary of a wall
    length: int
        length of an element
    material: str
        name of the material
    color: str
        color of the element for plot
    doors: list
        the list of doors in the wall
    windows: list
         the list of windows in the wall   
         
    Methods
    -------
    plot()
        Plot the wall
    """
    
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
        

#the Window class

class Window(Elements):
    """A class that implements a Window class from Elements

    Attributes
    ----------
    bound1: tuple
        first boundary of a window
    bound2: tuple
        second boundary of a window
    length: int
        length of an element
    material: str
        name of the material
    color: str
        color of the window for plot
        
    Methods
    -------
    plot()
        Plot the window
    """
    
    def __init__(self, bound1, bound2, material):
        super().__init__(bound1, bound2, material)
        self.color = 'blue'
   
#the Door class
class Door(Elements):
    """A class that implements a Door class from Elements

    Attributes
    ----------
    bound1: tuple
        first boundary of a door
    bound2: tuple
        second boundary of a door
    length: int
        length of an element
    material: str
        name of the material
    color: str
        color of the door for plot
        
    Methods
    -------
    plot()
        Plot the window
    """
    
    def __init__(self, bound1, bound2, material):
        super().__init__(bound1, bound2, material)
        self.color = 'red'
        

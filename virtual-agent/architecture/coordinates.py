# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

class Coordinates():
    """A class that implements coordinates in 2D space

    Attributes
    ----------
    x : float
        the value of the x axis
    y : float
        the value of the y axis


    Methods
    -------
    plot(color='black')
        Plots the coordinates as a point.
    """
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return str([self.x, self.y])
    
    def plot(self, color='black'):
        """Plots the coordinates as a point.
        
        Parameters
        ----------
        color : str
            The point's color
        
        Returns
        -------
        """

        plt.plot(self.x, self.y, color=color, marker='o')

        
class CoordinatesPair():
    """A class that implements a pairs of coordinates in 2D space

    Attributes
    ----------
    x1 : float
        the x value of the first coordinates
    y1 : float
        the y value of the first coordinates
    x2 : float
        the x value of the second coordinates
    y2 : float
        the y value of the second coordinates

    Methods
    -------
    plot(color='black')
        Plots the pair of coordinates as a segment
        
    has_crossed(old_x, old_y, new_x, new_y)
        Returns whether an old point has changed sides of the wall 
        after moving to the new point
    """
    
    def __init__(self, x1=0.0, y1=0.0, x2=0.0, y2=0.0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    def __str__(self):
        return str([self.x1, self.y1, self.x2, self.y2])
    
    def plot(self, linestyle='-', color='black', marker='o'):
        """
        Plots the pair of coordinates as a segment
        
        Parameters
        ----------
        linestyle : str
            the style of the segment
        color : str
            the color of the segment
        marker : str
            the marker of the segment's extremities
            
        Returns
        -------
        """
        
        plt.plot([self.x1, self.x2], [self.y1, self.y2], 
                 linestyle=linestyle , color=color, marker=marker)
        
    def has_crossed(self, old_x, old_y, new_x, new_y):
        """Returns whether an old point has changed sides of the wall 
        after moving to the new point
        
        Parameters
        ----------
        old_x : float
            x value of the old point
        old_y : float
            y value of the old point
        new_x : float
            x value of the new point
        new_y : float
            y value of the new point 
            
        Returns
        -------
        has_crossed_wall : bool
            Returns True if the wall has been crossed, else False
        """
        
        has_crossed_wall = False
        if self.x1 == self.x2:
            has_crossed_wall = (old_x - self.x1) * (new_x - self.x1) <= 0 # take 0 into account
        else:
            def f(x):
                '''y = ax + b'''                
                a = (self.y2 - self.y1) / (self.x2 - self.x1)
                return a * (x - self.x1) + self.y1
            
            has_crossed_wall = (old_y - f(old_x)) * (new_y - f(new_x)) <= 0 # take 0 into account
        return has_crossed_wall
        
if __name__ == '__main__':
    c = Coordinates(3.0, 4.0)
    cp = CoordinatesPair(0.0, 0.0, 1.0, 1.0)
    
    assert str(c) == '[3.0, 4.0]'
    assert str(cp) == '[0.0, 0.0, 1.0, 1.0]'

    print(c)
    print(cp)
    
    c.plot()
    cp.plot()
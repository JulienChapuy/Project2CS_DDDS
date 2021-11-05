# -*- coding: utf-8 -*-

from architecture.coordinates import CoordinatesPair

class Window(CoordinatesPair):
    """A class that implements a window

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
    height : float
        the height of the window
    height_above_floor : float
        the height above the floor of the bottom of the window
    color : str
        the color of the door
    linestyle : str
        the style of the segment when plotted
        
    Methods
    -------
    plot()
        Plots the window as a segment
    """
    
    def __init__(self, x1, y1, x2, y2, height=1.0, height_above_floor=1.0, color='green', linestyle='--'):
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
        """Plots the window as a segment"""
        super().plot(linestyle=self.linestyle, color=self.color)
        
        
if __name__ == '__main__':
    window = Window(1, 1, 2, 2, height=0.5, height_above_floor=1.0)
    window.plot()
    print(window)
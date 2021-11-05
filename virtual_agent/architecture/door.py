# -*- coding: utf-8 -*-

from architecture.coordinates import CoordinatesPair      
        
class Door(CoordinatesPair):
    """A class that implements a door
    
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
        the height of the wall
    closed : bool
        True/False if the door is closed/open
    color : str
        the color of the door
    linestyle : str
        the style of the segment when plotted
        
    Methods
    -------
    plot()
        Plots the door as a segment
    """
    def __init__(self, x1, y1, x2, y2, height=2, closed=False, color='red', linestyle='--'):
        super().__init__(x1, y1, x2, y2)
        self.height = height
        self.closed = closed
        self.color = color
        self.linestyle  = linestyle 
        
    def __str__(self):
        s = super().__str__() + '\n'
        s += 'height: {}m'.format(self.height) + '\n'
        s += 'color: {}'.format(self.color) + '\n'
        return s
            
    def plot(self):
        """Plots the door as a segment"""
        super().plot(linestyle=self.linestyle, color=self.color)
        
        
if __name__ == '__main__':
    door = Door(5, 0, 1, 4)
    door.plot()
    print(door)
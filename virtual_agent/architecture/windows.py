# -*- coding: utf-8 -*-


from architecture.window import Window

class Windows():
    """A class that implements several windows

    Attributes
    ----------
    window_list : list
        a list of windows
        
    Methods
    -------
    plot()
        Plots the windows as segments
    """
    def __init__(self, window_list=[]):
        self.window_list = window_list
        
    def __str__(self):
        s = ''
        for window in self.window_list:
            s = s + str(window) + '\n'
        s = s + '\n'
        return s
    
    def plot(self):
        """Plots the windows as segments"""
        for window in self.window_list:
            window.plot()
        
if __name__ == '__main__':
    window1 = Window(1, 1, 2, 2)
    window2 = Window(3, 2, 2, 4)
    windows = Windows([window1, window2])
    windows.plot()
    print(windows)
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 23:13:12 2021

@author: Lloyd
"""


from architecture.window import Window

class Windows():
    def __init__(self, window_list=[]):
        self.window_list = window_list
        
    def __str__(self):
        s = ''
        for window in self.window_list:
            s = s + str(window) + '\n'
        s = s + '\n'
        return s
    
    def plot(self):
        for window in self.window_list:
            window.plot()
        
    def add(self, windows):
        for window in windows.window_list:
            self.window_list.append(window)
        
if __name__ == '__main__':
    window1 = Window(1, 1, 2, 2, 0.5, 1.0)
    window2 = Window(1, 2, 2, 1, 0.5, 1.0)
    windows = Windows([window1, window2])
    windows.plot()
    print(windows)
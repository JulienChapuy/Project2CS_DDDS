# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:00:16 2021

@author: Lloyd
"""
import matplotlib.pyplot as plt

class BoundingBox():
    def __init__(self, xmin, ymin, xmax, ymax):
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax
        
    def __str__(self):
        return str([self.xmin, self.ymin, self.xmax, self.ymax])
        
    def plot(self, color='black'):
        plt.plot([self.xmin, self.xmax], [self.ymin, self.ymin], c=color)
        plt.plot([self.xmin, self.xmax], [self.ymax, self.ymax], c=color)
        plt.plot([self.xmin, self.xmin], [self.ymin, self.ymax], c=color)
        plt.plot([self.xmax, self.xmax], [self.ymin, self.ymax], c=color)
        
        
class BoundingBoxes():
    def __init__(self, bbs):
        self.bbs = bbs
    
    def __str__(self):
        s = ''
        for bb in self.bbs:
            s = s + '\n' + str(bb)
        return s
    
    def plot(self, color='black'):
        plt.figure()
        for bb in self.bbs:
            bb.plot()
        plt.show()
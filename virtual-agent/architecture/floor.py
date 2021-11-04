# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:04:08 2021

@author: Lloyd
"""
import matplotlib.pyplot as plt

from coordinates import Coordinates
from wall import Wall
from walls import Walls, WallsGenerator
from room import Room


class Floor():
    def __init__(self, rooms):
        self.rooms = rooms
    
    def __str__(self):
        s = ''
        for i, room in enumerate(self.rooms):
            s = s + 'room ' + i + ': ' + str(room) + '\n'
        return s
    
    def plot(self):
        for room in self.rooms:
            room.plot()
            
            
            
if __name__ == '__main__':
    wg = WallsGenerator()
    
    # room 1
    walls1 = wg.generate([(0, 0), (0, 4), (4, 6), (6, 4)])
    room1 = Room(walls1)
        
    # room 2
    walls2 =wg.generate([(7, 5), (10, 5), (10, 8), (7, 8)])
    room2 = Room(walls2)

    
    # plots
    plt.figure(figsize=(8, 8))
    room1.plot()
    room2.plot()
    plt.show() 
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
    """A class that implements a floor (of a buidling) composed of rooms

    Attributes
    ----------
    rooms_list : list
        the list of rooms of the floor
        
    Methods
    -------
    plot()
        Plots the rooms
    """
    
    def __init__(self, room_list):
        self.room_list = room_list
    
    def __str__(self):
        s = ''
        for i, room in enumerate(self.room_list):
            s = s + 'room ' + i + ': ' + str(room) + '\n'
        return s
    
    def plot(self):
        """Plots the rooms"""
        for room in self.room_list:
            room.plot()
            
            
if __name__ == '__main__':
    pass
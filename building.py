# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:18:02 2021

@author: Julien
"""

class Building():
    def __init__(self, length, width, height, floors_list = []):
        self.length = length
        self.width = width
        self.height = height
        self.floors_list = floors_list
        self.nb_floors = len(floors_list)
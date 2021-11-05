# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 12:08:00 2021

@author: Julien
"""

import sys

from building import Building    
from floor import Floor
from generator import generate_rooms_3doors as gen_3doors

#Constants

b_length = 40 #building's length
b_width = 30 #building's width
b_height = 15 #building's height
n_x = 15 #number of areas along the x axis
n_y = 10 #number of areas along the y axis

n_levels = 5 #number of floors in the building

#Creating a building

myBuilding = Building(b_length, b_width, b_height)

for i in range(n_levels):
    
    areas, walls = gen_3doors(b_length, b_width, n_x, n_y)
    
    f = Floor(b_length, b_width, b_height/n_levels, i,areas, walls)
    
    myBuilding.add_floor(f)
    

myBuilding.plot()

#One can also directly execute the python file (cf code below)

if __name__ == '__main__':
    
    if len(sys.argv) != 7:
        print('Usage : ' + sys.argv[0] + 'b_length b_width b_height n_x n_y n_levels')
        sys.exit(1)
        
    myBuilding = Building(sys.argv[1], sys.argv[2], sys.argv[3])

    for i in range(sys.argv[6]):
        
        areas, walls = gen_3doors(sys.argv[1], sys.argv[2], sys.argv[4], sys.argv[5])
        
        f = Floor(sys.argv[1], sys.argv[2], sys.argv[3]/sys.argv[6], i,areas, walls)
        
        myBuilding.add_floor(f)
        
    myBuilding.plot()
                
            
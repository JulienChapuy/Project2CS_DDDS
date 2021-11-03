# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 12:08:00 2021

@author: Julien
"""
import matplotlib.pyplot as plt
import numpy as np

from floor import Floor
from areas import Area, Room
from elements import Wall, Door, Window
from generator import generate_random as gen
from generator import generate_rooms as gen_rooms
from generator import generate_rooms_3doors as gen_3doors

        
w1 = Wall((0,0),(5,0), 'concrete',  [Window((2,0),(2.5,0),'glass')])
w2 = Wall((5,0), (5,5),'concrete')
w3 = Wall((5,5), (0,5), 'concrete', [Door((2,5), (3,5), 'wood')])
w4 = Wall((0,5),(0,2), 'concrete')

# w5 = Wall((0,2), (2,2), 'concrete', [Door((0.5,2), (1.5,2), 'wood')])
# w6 = Wall((2,2),(0,0), 'concrete')

# r = Room([w1, w2, w3, w4, w5, w6])

# r.plot()

# w = gen(100,100,5,3)

# for l in w:
#     l.plot()
f_length = 40
f_width = 30
n_x = 15
n_y = 10

rooms, walls = gen_3doors(f_length, f_width, n_x, n_y)

f = Floor(0,rooms, walls)

robot_room = 0
rooms_visited = []
for i in range(50):
    

    rooms_visited.append(robot_room)
    
    A = np.zeros((2,2))
    
    for i in range(2):
        for j in range(2):
            if f.areas[robot_room].walls[2*i+j].doors != []:
                A[i][j] = 1 
            else:
                pass
            
    c = np.random.randint(np.sum(A==1))
    
    d = 0
    for i in range(2):
        for j in range(2):
            if A[i][j] == 1:
                d+=1
                
                if d == c:
                    next_room = i,j
                    
                else:
                    pass
            else:
                pass
            
           
            
    print(A)
    print(next_room)
            
    if next_room == (0,0):
        robot_room = robot_room - n_x +1
        
    elif next_room == (0,1):
        robot_room = robot_room - 1
        
        
    elif next_room == (1,0):
        robot_room = robot_room + 1
        
    else:
        robot_room = robot_room + n_x - 1
        
    rooms_visited.append(robot_room)
    
    
    
    
                
            
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 08:24:44 2021

@author: Julien
"""

# Mr Guiblind
# Digital twin of a building
    #Elements
        # -walls
        # -doors
        # -windows
        # -floors
            #room, patio, corridor
            
            # room = 4 walls +  windows + a door
            
            # walls can be shared between rooms and patio for example
            
            #elements can have specific attributes
            #they have coordinates 
            
    #Purposes
        #Drawing a map
        
        #tracking a visitor
import numpy as np
import matplotlib.pyplot as plt 




class Area():
    def __init__(self, length, width, center = (0,0), shape = 'Rectangular'):
        if shape == 'Rectangular':
            self.shape = 'Rectangular'
            self.center = center
            self.length = length
            self.width = width
            self.elements_list = []
        else: 
            pass
    
class Room(Area):
    def __init__(self, length, width, center, shape, walls = []):
        #Walls : North > East > South > West
        super().__init__(length, width, center, shape)
        if self.shape == 'Rectangular':
            self.walls = walls
            self.doors = []
            self.windows = []
            
            i = 0 
            for w in self.walls:
                if 'door' in w.__dict__:
                    self.doors.append([w.door, i])
                if 'window' in w.__dict__:
                    self.windows.append([w.window, i])
                    
                i+=1
            
        else:
            pass
        
    def display(self):
        # t1 = np.linspace(-self.length/2, self.length/2, 1000)
        # t2 = np.linspace(-self.width/2, self.width/2, 1000)
        # plt.plot([self.length/2]*1000,t2, color = 'black')
        # plt.plot([-self.length/2]*1000, t2, color = 'black')
        # plt.plot(t1, [self.width/2]*1000,color = 'black')
        # plt.plot(t1, [-self.width/2]*1000, color = 'black')
    
        for w in self.walls:
            t = np.linspace(-w.width/2, w.width/2, 1000)
            
            if w.boundaries[0][0] == w.boundaries[1][0]:
                a = w.boundaries[0][0]
                plt.plot(self.center[0] + np.linspace(a,a,1000),self.center[1] + t, color = 'green', alpha = 0.3)
                for d in w.doors:
                    t_d = np.linspace(d[1][0]-d[0].width/2, d[1][0] + d[0].width/2, 1000)
                    plt.plot(self.center[0] + np.linspace(a,a,1000), self.center[1] + t_d, color = 'blue')
                    
                for w in w.windows:
                    t_w = np.linspace(w[1][0]-w[0].width/2, w[1][0] + w[0].width/2, 1000)
                    plt.plot(self.center[0] + np.linspace(a,a,1000), self.center[1] + t_w, color = 'red')
                    
            else:
                b = w.boundaries[0][1]
                plt.plot(self.center[0] + t, self.center[1] + np.linspace(b,b,1000), color = 'green', alpha = 0.3)
                for d in w.doors:
                    t_d = np.linspace(d[1][0]-d[0].width/2, d[1][0] + d[0].width/2, 1000)
                    plt.plot(self.center[0] + np.linspace(b,b,1000), self.center[1] + t_d, color = 'blue')
                    
                for w in w.windows:
                    t_w = np.linspace(w[1][0]-w[0].width/2, w[1][0] + w[0].width/2, 1000)
                    plt.plot(self.center[0] + np.linspace(b,b,1000), self.center[1] + t_w, color = 'red')
                    
                
                    
        
        
class Floor():
    def __init__(self, length, width, height, floor_number, areas = []):
        
        self.length = length
        self.width = width
        self.height = height
        self.floor_number = floor_number
        
        self.areas = areas
        
    def display(self):
        for area in self.areas:
            area.display()
        
class Building():
    def __init__(self, length, width, height, floors_list = []):
        self.length = length
        self.width = width
        self.height = height
        self.floors_list = floors_list
        self.nb_floors = len(floors_list)

        
#Let's create a Room with 4 Walls, dimension 6m * 5m
#one window on left wall centered
#one door on right wall centered

door1 = Door(2.5, 0.9, 0.1, 'wood')
window1 = Window(0.3,0.2,0.1,'glass')

w1 = Wall(3,5,0.2,'concrete', ((-3, -2.5),(-3,2.5)), [[window1, (0,0)]])
w2 = Wall(3,6,0.2,'concrete', ((-3,2.5), (3,2.5)))
w3 = Wall(3,5,0.2,'concrete', ((3,2.5),(3,-2.5)),[[door1, (0,(door1.height-3)/2)]])
w4 = Wall(3,6,0.2,'concrete', ((3,-2.5),(-3,-2.5)))

room1 = Room(6,5,(0,0), 'Rectangular', [w1,w2,w3,w4])

w5 = Wall(3,5,0.2,'concrete', ((-3, -2.5),(-3,2.5)), [[window1, (0,0)]])
w6 = Wall(3,6,0.2,'concrete', ((-3,2.5), (3,2.5)))
w7 = Wall(3,5,0.2,'concrete', ((3,2.5),(3,-2.5)),[[door1, (0,(door1.height-3)/2)]])
w8 = Wall(3,6,0.2,'concrete', ((3,-2.5),(-3,-2.5)))

room2 = Room(6,5,(10,10), 'Rectangular', [w5,w6,w7,w8])


# w9 = Wall(3,5,0.2,'concrete', ((-3, 13),(2,13)), [[window1, (0,0)],[door1, (1,1)]])
# w10 = Wall(3,2,0.2,'concrete', ((2,13), (2,11)))
# w11 = Wall(3,2,0.2,'concrete', ((2,11),(0,11)),[[door1, (0,(door1.height-3)/2)]])
# w12 = Wall(3,3,0.2,'concrete', ((0,11),(0,8)))
# w13 = Wall(3,3,0.2,'concrete', ((0,8),(-3,8)),[[door1, (0,(door1.height-3)/2)]])
# w14 = Wall(3,5,0.2,'concrete', ((-3,8),(-3,13)))

# room3 = Room(5,5, (0,0), 'Rectangular', [w9,w10,w11,w12,w13,w14])
f1 = Floor(30,20,3,1,[room1, room2])

b1 = Building(30,20,15, [f1])
    
    
def display(b, num_floor):
    b.floors_list

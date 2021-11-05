# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

from architecture.coordinates import Coordinates
from architecture.room import Room
from utils.tools import find_intersection, intersects_segment 

class Agent(Coordinates):
    def __init__(self, x, y, ID=None, room_ID=None):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.trajectory = [[x, y]]
        self.ID = ID
        self.room_ID = room_ID
        self.thirsty = False
        self.hungry = False
        
    def move(self, dx, dy, room_dict=None):
        # get the room
        room = room_dict[self.room_ID]
        
        # define new coordinates
        new_x = self.x + dx
        new_y = self.y + dy
        
        # check if it has crossed a wall
        do_move = True
        crossed_wall = None
        room = room_dict[self.room_ID]
        for wall in room.walls.wall_list:
            if wall.has_crossed(self.x, self.y, new_x, new_y):
                do_move = False
                crossed_wall = wall
                break
        
        # if it has crossed a wall, check if it was a door
        if do_move == False:
            for door in crossed_wall.doors.door_list:
                
                A = Coordinates(door.x1, door.y1)
                B = Coordinates(door.x2, door.y2)
                C = Coordinates(self.x, self.y)
                D = Coordinates(new_x, new_y)
                
                intersection = find_intersection(A, B, C, D)
                segment_intersected = intersects_segment(A, B, intersection)
                
                if segment_intersected:
                    do_move = True
                
        if do_move == True: 
            # update coordinates
            self.x = new_x
            self.y = new_y
            self.trajectory.append([self.x, self.y])
            
        
    def sleep(self):
        pass
    
    def eat(self):
        pass
    
    def drink(self):
        pass
    
    def plot(self, show_trajectory=False):
        super().plot()
        if show_trajectory:
            trajectory = np.array(self.trajectory)
            plt.plot(trajectory[:,0], trajectory[:,1], 'r')
        
        
if __name__ == '__main__':
    room = Room()
    room_dict = {0: room}
    a = Agent(0, 2, room_ID=0)
    a.plot()
    a.move(1, 0, room_dict)
    a.plot()
    a.move(0, -1, room_dict)
    a.plot()
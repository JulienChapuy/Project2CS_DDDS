# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

from architecture.coordinates import Coordinates
from architecture.room import Room
from utils.tools import find_intersection, intersects_segment 

class Agent(Coordinates):
    """A class that implements an agent moving in 2D space

    Attributes
    ----------
    x : float
        the x value of the agent's position
    y : float
        the y value of the agent's position
    ID : int
        the identifier of the agent
    room_ID : int
        the ID of the room in which the agent is


    Methods
    -------
    move(dx, dy, room_dict=None)
        move the agent from (x, y) to (x + dx, y + dy)
    
    plot(show_trajectory=False)
        Plots the coordinates as a point
    """
    def __init__(self, x, y, ID=None, room_ID=None):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.trajectory = [[x, y]]
        self.ID = ID
        self.room_ID = room_ID
        
    def move(self, dx, dy, room_dict=None):
        """move the agent from (x, y) to (x + dx, y + dy)
        
        Parameters
        ----------
        dx : float
            the x axis movement
        dy : float
            the y axis movement
        room_dict : dict {int: Room}
            the dictionnary of rooms
            serves to get the room in which the agent is with room_ID
        """
        
        # define new coordinates
        do_move = True
        
        new_x = self.x + dx
        new_y = self.y + dy
        
        if room_dict:
            # get the room
            room = room_dict[self.room_ID]

            # check if the agent has crossed a wall
            crossed_wall = None
            room = room_dict[self.room_ID]
            for wall in room.walls.wall_list:
                if wall.has_crossed(self.x, self.y, new_x, new_y):
                    do_move = False
                    crossed_wall = wall
                    break
            
            # if the agent has crossed a wall, check if it was a door
            if do_move == False:
                for door in crossed_wall.doors.door_list:
                    
                    # door coordinates
                    A = Coordinates(door.x1, door.y1)
                    B = Coordinates(door.x2, door.y2)
                    
                    #agent coordinates
                    C = Coordinates(self.x, self.y)
                    D = Coordinates(new_x, new_y)
                    
                    intersection = find_intersection(A, B, C, D)
                    segment_intersected = intersects_segment(A, B, intersection)
                    
                    if segment_intersected:
                        do_move = True
                        self.room_ID = 1 - self.room_ID # temporary solution, only works for 2 rooms with ID 0 and 1
        
                
        # update coordinates if appropriate
        if do_move == True: 
            self.x = new_x
            self.y = new_y
            self.trajectory.append([self.x, self.y])
            
    def plot(self, show_trajectory=False):
        """Plots the agent as a point.
        
        Parameters
        ----------
        show_trajectory : bool
            plot the trajectory of the agent (the path it walked)
        """
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
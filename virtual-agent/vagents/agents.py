# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import warnings

from vagents.agent import Agent

from architecture.door import Door
from architecture.doors import Doors
from architecture.wall import Wall
from architecture.walls import Walls
from architecture.room import Room


class Agents():
    def __init__(self, agents_list):
        self.agents_list = agents_list        
        
    def move(self, rooms_dict=None):
        for p in self.agents_list:
            dx = np.random.random() - np.random.random() 
            dy = np.random.random() - np.random.random() 
            p.move(dx / 4, dy / 4, rooms_dict)
    
    def get_coordinates(self):
        X = np.zeros((len(self.agents_list)))
        Y = np.zeros((len(self.agents_list)))
        for i, agent in enumerate(self.agents_list):
            X[i] = agent.x
            Y[i] = agent.y
        return X, Y


if __name__ == '__main__':
    # initialize figure
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim([-1, 6])
    ax.set_ylim([-1, 11])
    
    # initalize buildind    
    shared_wall = Wall(0, 5, 5, 5)
    
    doors = Doors([Door(1, 5, 2, 5),
                    Door(3, 5, 4, 5)])
    
    shared_wall.doors = doors
    
    walls0 = Walls([shared_wall,
                    Wall(0, 5, 0, 0),
                    Wall(0, 0, 5, 0),
                    Wall(5, 0, 5, 5)])
    
    room0 = Room(walls0)
    print(room0)
    
    room_dict = {0:room0}
    
    # plot building
    for wall in walls0.wall_list:
        ax.plot([wall.x1, wall.x2], [wall.y1, wall.y2], color='black')
        
    for door in doors.door_list:
        ax.plot([door.x1, door.x2], [door.y1, door.y2], color='white')
    
    # initialize parameters
    it = 500
    N = 100
    n_clusters = 4
    
    # initialize objects (agents, kmeans)
    agents_list = [Agent(3, 3, room_ID=0) for i in range(N)]
    agents = Agents(agents_list)
    agents.move(room_dict)
    X, Y = agents.get_coordinates()
    C = np.array([X, Y]).T
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(C)

    # get cluster centers and agents coordinates
    centers_ = kmeans.cluster_centers_
    centers, = ax.plot(centers_[:,0], centers_[:,1], 
                       linestyle='', marker='o', markersize=15)
    coordinates = []
    for k in range(n_clusters):
        coord, = ax.plot(X, Y, linestyle='', marker='o', markersize=2)
        coordinates.append(coord)

    for i in range(it):
        # time.sleep(0.02)
        
        # move and get coordinates of agents
        agents.move(room_dict)
        X, Y = agents.get_coordinates()
        C = np.array([X, Y]).T
        
        # fit kmeans and predict clusters
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            kmeans = KMeans(n_clusters=n_clusters, 
                        init=kmeans.cluster_centers_)
            kmeans.fit(C)
        pred = kmeans.predict(C)
        centers_ = kmeans.cluster_centers_
        
        # set cluster centers and coordinates
        centers.set_xdata(centers_[:,0])
        centers.set_ydata(centers_[:,1])        
        for j, coord in enumerate(coordinates):
            coord.set_xdata(X[np.where(pred == j)])
            coord.set_ydata(Y[np.where(pred == j)])

        # update canvas
        ax.set_title('iter nb {}'.format(i))
        fig.canvas.draw()
        fig.canvas.flush_events()
        
        
        
        
        
        
        
        
        
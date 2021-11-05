# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import warnings

from vagents.agent import Agent
from vagents.agents import Agents
from architecture.door import Door
from architecture.doors import Doors
from architecture.wall import Wall
from architecture.walls import Walls
from architecture.room import Room

def run():
    # initialize figure
    fig = plt.figure(figsize=(6, 6))
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
    
    walls1 = Walls([shared_wall,
                    Wall(5, 5, 5, 8),
                    Wall(5, 8, 0, 5)])
    
    room0 = Room(walls0)
    room1 = Room(walls1)    
    room_dict = {0:room0,
                 1:room1}
    
    # plot building
    for wall in walls0.wall_list:
        ax.plot([wall.x1, wall.x2], [wall.y1, wall.y2], color='black')
        
    for wall in walls1.wall_list:
        ax.plot([wall.x1, wall.x2], [wall.y1, wall.y2], color='black')
        
    for door in doors.door_list:
        ax.plot([door.x1, door.x2], [door.y1, door.y2], color='white')
    
    # initialize parameters
    N_iterations = 500
    N_agents = 100
    n_clusters = 4
    
    # initialize objects (agents, kmeans)
    agents_list = [Agent(3, 3, room_ID=0) for i in range(N_agents)]
    agents = Agents(agents_list)
    agents.move(room_dict)
    X, Y = agents.get_coordinates()
    C = np.array([X, Y]).T
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(C)
    
    # get cluster centers
    centers_ = kmeans.cluster_centers_
    
    # plot cluster centers and agents
    colors = {0:'blue',
              1:'red',
              2:'green',
              3:'orange'}
    coordinates = []
    centers_toplot = []
    for k in range(n_clusters):
        coord, = ax.plot(X, Y, linestyle='', marker='o', 
                         markersize=3, c=colors[k])
        coordinates.append(coord)
        centers, = ax.plot(centers_[k,0], centers_[k,1], 
                       linestyle='', marker='o', 
                       markersize=15, c=colors[k])
        centers_toplot.append(centers,)
    
    for i in range(N_iterations):
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
        for k, ctp in enumerate(centers_toplot):
            ctp.set_xdata(centers_[k,0])
            ctp.set_ydata(centers_[k,1])        
        for j, coord in enumerate(coordinates):
            coord.set_xdata(X[np.where(pred == j)])
            coord.set_ydata(Y[np.where(pred == j)])
    
        # update canvas
        ax.set_title('iteration number {}'.format(i))
        fig.canvas.draw()
        fig.canvas.flush_events()
            
        
        
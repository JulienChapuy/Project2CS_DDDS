# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 23:19:51 2021

@author: Lloyd
"""

from architecture.wall import Wall

class Walls():
    def __init__(self, wall_list=[Wall()]):
        self.wall_list = wall_list
        
    def __str__(self):
        s = ''
        for wall in self.wall_list:
            s = s + str(wall) + '\n'
        s = s + '\n'
        return s
    
    def plot(self):
        for wall in self.wall_list:
            wall.plot()
            
    def get_walls(self):
        return self.wall_list
            
    def get_wall(self, i):
        return self.wall_list[i]
            
class WallsGenerator():
    def __init__(self):
        pass
    
    def generate(self, coordinates):
        walls = []
        for i in range(-1, len(coordinates) - 1):
            c1 = coordinates[i]
            c2 = coordinates[i+1]
            wall = Wall(c1[0], c1[1], c2[0], c2[1])
            walls.append(wall)
        return Walls(walls)
        
        
if __name__ == '__main__':
    wg = WallsGenerator()
    walls = wg.generate([(0, 0), (0, 5), (5, 5), (5, 0)])
    walls2 = wg.generate([(3, 3), (3, 5), (5, 5), (5, 3)])
    walls.plot()
    walls2.plot()
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
        
class BuildingObjects():
    def __init__(self, height, width, depth, material, obj_type = 'Rectangular'):
        
        if obj_type == 'Rectangular': 
            self.height = height
            self.width = width
            self.depth = depth
            
            self.size = height*width
            self.volume = height*width*depth
            
            self.material = material 
            
        else:pass
    
class Wall(BuildingObjects):
    def __init__(self, height, width, depth, material, obj_type = 'Rectangular'):
        super().__init__(height, width, depth, material, obj_type = 'Rectangular')
        
        
    
    
        

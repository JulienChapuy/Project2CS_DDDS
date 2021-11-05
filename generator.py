# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:32:07 2021

@author: Julien
"""
from elements import Wall, Window, Door
from areas import Room
import numpy as np 

#We will define below multiple generators of areas / floors, etc.
#We detailled more the function generate_rooms_3doors since it is the one 
#we used in the main file.

#generate a list of walls, randomly created (can contains elements)
def generate_random(f_length = 20, f_width = 15, n_x = 3, n_y = 2):
    
    
    a_length = f_length / n_x
    a_width = f_width/ n_y
    
    walls = []
    x,y = 0,0
    
    y = 0
    for i in range(n_y+1):
        x = 0 
        for j in range(n_x):
            #with probability 0.5 we put no features in w
            #with probability 0.3 we put a window in w
            #with probability 0.2 we put a door in w
            
            rng = np.random.rand()
            
            if rng < 0.5:
                
                w = Wall((x,y), (x+a_length,y),'concrete')
                walls.append(w)
                
            elif 0.5 <= rng < 0.9:
                wind = Window((x + a_length/2 - 0.2,y),(x + a_length/2 + 0.2,y),'glass')
                w = Wall((x,y), (x+a_length,y),'concrete',[wind])
                walls.append(w)
                
            else:
                door = Door((x + a_length/2 - 0.4,y),(x + a_length/2 + 0.4,y),'wood')
                w = Wall((x,y), (x+a_length,y),'concrete',[door])
                walls.append(w)
            x += a_length
        y+= a_width
        
        
    x = 0
    for i in range(n_x+1):
        y = 0 
        for j in range(n_y):
            rng = np.random.rand()
            
            if rng < 0.5:
                
                w = Wall((x,y), (x,y + a_width),'concrete')
                walls.append(w)
                
            elif 0.5 <= rng < 0.8:
                wind = Window((x, y+a_width/2 - 0.2),(x, y+a_width/2 + 0.4),'glass')
                w = Wall((x,y), (x,y + a_width),'concrete',[wind])
                walls.append(w)
                
            else:
                door = Door((x, y+a_width/2 - 0.4),(x, y+a_width/2 + 0.4),'wood')
                w = Wall((x,y), (x,y + a_width),'concrete',[door])
                walls.append(w)
            y += a_width
        x += a_length
        
    return(walls)

#generate a random_wall

def random_wall(x_0, y_0, x_1, y_1, material):
    rng = np.random.rand()
    a,b = 0,0
    
    if x_0 != x_1:
        a = 1
    elif y_0 != y_1:
        b = 1
    else:
        pass
    
    if rng < 0.5:
        
        w = Wall((x_0, y_0), (x_1,y_1), material)
        
    elif 0.5 <= rng < 0.9:
        wind = Window(((x_0 + x_1)/2 - 0.2*a,(y_0+y_1)/2 - 0.2*b,),((x_0 + x_1)/2 + 0.2*a,(y_0+y_1)/2 + 0.2*b),'glass')
        w = Wall((x_0, y_0), (x_1,y_1), material,[wind])
        
    else:
        door = Door(((x_0 + x_1)/2 - 0.4*a,(y_0+y_1)/2 - 0.4*b,),((x_0 + x_1)/2 + 0.4*a,(y_0+y_1)/2 + 0.4*b),'wood')
        w = Wall((x_0, y_0), (x_1,y_1), material,[door])
        
    return(w)
    
#generate a wall that can't contain a door (e.g. for walls on the boundaries of the floor)    
def doorless_wall(x_0, y_0, x_1, y_1, material):
    rng = np.random.rand()
    a,b = 0,0
    
    if x_0 != x_1:
        a = 1
    elif y_0 != y_1:
        b = 1
    else:
        pass
    
    if rng < 0.5:
        
        w = Wall((x_0, y_0), (x_1,y_1), material)
        
    else:
        wind = Window(((x_0 + x_1)/2 - 0.2*a,(y_0+y_1)/2 - 0.2*b,),((x_0 + x_1)/2 + 0.2*a,(y_0+y_1)/2 + 0.2*b),'glass')
        w = Wall((x_0, y_0), (x_1,y_1), material,[wind])
        
    return(w)

#generate a wall that automatically contains a door
def door_wall(x_0, y_0, x_1, y_1, material):
    a,b = 0,0
    
    if x_0 != x_1:
        a = 1
    elif y_0 != y_1:
        b = 1
    else:
        pass
    
    door = Door(((x_0 + x_1)/2 - 0.4*a,(y_0+y_1)/2 - 0.4*b,),((x_0 + x_1)/2 + 0.4*a,(y_0+y_1)/2 + 0.4*b),'wood')
    w = Wall((x_0, y_0), (x_1,y_1), material,[door])
        
    return(w)

#generate a list of rooms with random walls
def generate_random_rooms(f_length = 20, f_width = 15, n_x = 3, n_y = 2):
    a_length = f_length / n_x
    a_width = f_width/ n_y
    
    rooms = []
    
    y = 0
    
    for i in range(n_y):
        x = 0
        for j in range(n_x):
            
            w1 = random_wall(x, y, x+a_length, y, 'concrete')
            w2 = random_wall(x, y, x, y + a_width, 'concrete')
            w3 = random_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
            w4 = random_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
            
            r = Room([w1,w2, w3, w4])
            rooms.append(r)
            
            x+= a_length
            
        y += a_width
    
    return(rooms)

#generate rooms in a intelligent way : no doors on the boundaries,
#and at least one door by area.
def generate_rooms_individually(f_length = 20, f_width = 15, n_x = 3, n_y = 2):
    a_length = f_length / n_x
    a_width = f_width/ n_y
    
    rooms = []
    
    y = 0
    
    for i in range(n_y):
        x = 0
        for j in range(n_x):
            
            if i == 0 :
                w1 = doorless_wall(x, y, x+a_length, y, 'concrete')
                w4 = random_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                
                if j == 0:
                    w2 = doorless_wall(x, y, x, y + a_width, 'concrete')
                    w3 = random_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
                    
                    if len(r.doors) == 0:
                        a = np.random.randint(3)
                        
                        if a == 0:
                            w4 = door_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                        else:
                            w3 = door_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                          
                    r = Room([w1, w2, w3, w4]) 
                
                elif j == n_x-1:
                    w2 = random_wall(x, y, x, y + a_width, 'concrete')
                    w3 = doorless_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
                    
                    if len(r.doors) == 0:
                        a = np.random.randint(3)
                        
                        if a == 0:
                            w4 = door_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                        else:
                            w2 = door_wall(x, y, x, y + a_width, 'concrete')
                          
                    r = Room([w1, w2, w3, w4]) 
                    
                else:
                    w2 = random_wall(x, y, x, y + a_width, 'concrete')
                    w3 = random_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
                    
                    if len(r.doors) == 0:
                        a = np.random.randint(3)
                        
                        if a == 0:
                            w4 = door_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                        elif a == 1:
                            w2 = door_wall(x, y, x, y + a_width, 'concrete')
                        else:
                            w3 = door_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                          
                    r = Room([w1, w2, w3, w4]) 
                    
                    
                    
            elif i == n_y -1:
                w1 = random_wall(x, y, x+a_length, y, 'concrete')
                w4 = doorless_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                
                if j == 0:
                    w2 = doorless_wall(x, y, x, y + a_width, 'concrete')
                    w3 = random_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
                    
                    if len(r.doors) == 0:
                        a = np.random.randint(2)
                        
                        if a == 0:
                            w1 = door_wall(x, y, x+a_length, y, 'concrete')
                        else:
                            w3 = door_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                          
                    r = Room([w1, w2, w3, w4]) 
                
                elif j == n_x-1:
                    w2 = random_wall(x, y, x, y + a_width, 'concrete')
                    w3 = doorless_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
                    
                    if len(r.doors) == 0:
                        a = np.random.randint(2)
                        
                        if a == 0:
                            w1 = door_wall(x, y, x+a_length, y, 'concrete')
                        else:
                            w2 = door_wall(x, y, x, y + a_width, 'concrete')
                          
                    r = Room([w1, w2, w3, w4]) 
                    
                
                else:
                    w2 = random_wall(x, y, x, y + a_width, 'concrete')
                    w3 = random_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
                    
                    if len(r.doors) == 0:
                        a = np.random.randint(3)
                        
                        if a == 0:
                            w1 = door_wall(x, y, x+a_length, y, 'concrete')
                        elif a == 1:
                            w2 = door_wall(x, y, x, y + a_width, 'concrete')
                        else:
                            w3 = door_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                          
                    r = Room([w1, w2, w3, w4]) 
            else:
                w1 = random_wall(x, y, x+a_length, y, 'concrete')
                w4 = random_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                
                if j == 0:
                                        
                    w2 = doorless_wall(x, y, x, y + a_width, 'concrete')
                    w3 = random_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
                    
                    if len(r.doors) == 0:
                        a = np.random.randint(3)
                        
                        if a == 0:
                            w1 = door_wall(x, y, x+a_length, y, 'concrete')
                        elif a == 1:
                            w3 = door_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                        else:
                            w4 = door_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                          
                    r = Room([w1, w2, w3, w4]) 
                    
                elif j == n_x -1:
                    
                    w2 = random_wall(x, y, x, y + a_width, 'concrete')
                    w3 = doorless_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
                    
                    if len(r.doors) == 0:
                        a = np.random.randint(3)
                        
                        if a == 0:
                            w1 = door_wall(x, y, x+a_length, y, 'concrete')
                        elif a == 1:
                            w2 = door_wall(x, y, x, y + a_width, 'concrete')
                        
                        else:
                            w4 = door_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                          
                    r = Room([w1, w2, w3, w4])
                    
                else:
                    
                    w2 = random_wall(x, y, x, y + a_width, 'concrete')
                    w3 = random_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                
                    r = Room([w1, w2, w3, w4])
                    
                    if len(r.doors) == 0:
                        a = np.random.randint(4)
                        
                        if a == 0:
                            w1 = door_wall(x, y, x+a_length, y, 'concrete')
                        elif a == 1:
                            w2 = door_wall(x, y, x, y + a_width, 'concrete')
                        elif a == 2:
                            w3 = door_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                        else:
                            w4 = door_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                          
                    r = Room([w1, w2, w3, w4]) 
                    
            
            rooms.append(r)
            
            x+= a_length
            
        y += a_width
    
    return(rooms)

#same function than above but also returns the list of walls 
#in addition to the list of areas

def generate_rooms(f_length = 20, f_width = 15, n_x = 3, n_y = 2):
    a_length = f_length / n_x
    a_width = f_width/ n_y
    
    rooms = []
    walls = []
    
    y = 0
    
    for i in range(n_y):
        x = 0
        for j in range(n_x):
            
            if i == 0 :
                w1 = doorless_wall(x, y, x+a_length, y, 'concrete')
                w4 = random_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                
                if j == 0:
                    w2 = doorless_wall(x, y, x, y + a_width, 'concrete')
                    w3 = random_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
                    
                    if len(r.doors) == 0:
                        a = np.random.randint(3)
                        
                        if a == 0:
                            w4 = door_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                        else:
                            w3 = door_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                          
                    r = Room([w1, w2, w3, w4]) 
                    
                    walls.append(w1)
                    walls.append(w2)
                    walls.append(w3)
                    walls.append(w4)
                    
                elif j == n_x-1:
                    w2 = rooms[-1].walls[2]
                    w3 = doorless_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
                    
                    if len(r.doors) == 0:
                        w4 = door_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                          
                    r = Room([w1, w2, w3, w4]) 
                    
                    walls.append(w1)
                    walls.append(w3)
                    walls.append(w4)
                    
                else:
                    w2 = rooms[-1].walls[2]
                    w3 = random_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
                    
                    if len(r.doors) == 0:
                        a = np.random.randint(2)
                        
                        if a == 0:
                            w4 = door_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                        else:
                            w3 = door_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                          
                    r = Room([w1, w2, w3, w4]) 
                    
                    walls.append(w1)
                    walls.append(w3)
                    walls.append(w4)
                    
                    
                    
            elif i == n_y -1:
                w1 = rooms[-n_x].walls[3]
                w4 = doorless_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                
                if j == 0:
                    w2 = doorless_wall(x, y, x, y + a_width, 'concrete')
                    w3 = random_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
                    
                    if len(r.doors) == 0:
                        w3 = door_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                          
                    r = Room([w1, w2, w3, w4]) 
                    
                    walls.append(w2)
                    walls.append(w3)
                    walls.append(w4)
                
                elif j == n_x-1:
                    w2 = rooms[-1].walls[2]
                    w3 = doorless_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
                    
                    if len(r.doors) == 0:
                        
                        w2 = door_wall(x, y, x, y + a_width, 'concrete')
                        rooms[-1] = Room([rooms[-1].walls[0], rooms[-1].walls[1], w2, rooms[-1].walls[3]])
                          
                    r = Room([w1, w2, w3, w4]) 
                    
                    walls.append(w3)
                    walls.append(w4)
                
                else:
                    w2 = rooms[-1].walls[2]
                    w3 = random_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
                    
                    if len(r.doors) == 0:
                        w3 = door_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                          
                    r = Room([w1, w2, w3, w4]) 
                    
                    walls.append(w3)
                    walls.append(w4)
                    
            else:
                w1 = rooms[-n_x].walls[3]
                w4 = random_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                
                if j == 0:
                                        
                    w2 = doorless_wall(x, y, x, y + a_width, 'concrete')
                    w3 = random_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
                    
                    if len(r.doors) == 0:
                        a = np.random.randint(3)
                        
                        if a == 0:
                            w3 = door_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                            
                        else:
                            w4 = door_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                          
                    r = Room([w1, w2, w3, w4]) 
                    
                    walls.append(w2)
                    walls.append(w3)
                    walls.append(w4)
                    
                elif j == n_x -1:
                    
                    w2 = rooms[-1].walls[2]
                    w3 = doorless_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
                    
                    if len(r.doors) == 0:
                        w4 = door_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                          
                    r = Room([w1, w2, w3, w4])
                    
                    walls.append(w3)
                    walls.append(w4)
                    
                else:
                    
                    w2 = rooms[-1].walls[2]
                    w3 = random_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                
                    r = Room([w1, w2, w3, w4])
                    
                    if len(r.doors) == 0:
                        a = np.random.randint(4)
                        
                        if a == 0:
                            w3 = door_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                        else:
                            w4 = door_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                        
                          
                    r = Room([w1, w2, w3, w4]) 
                    
                    walls.append(w3)
                    walls.append(w4)
                    
            
            rooms.append(r)
            
            x+= a_length
            
        y += a_width
    
    return(rooms, walls)

#generate a floor using the function above

def generate_floor(f_length = 20, f_width = 15, n_x = 3, n_y = 2):
    rooms, walls = generate_rooms(f_length, f_width, n_x, n_y)
    
    walls_tmp = []
    
    for w in walls:
        if len(w.doors) == 0:
            walls_tmp.append(w)
        else:
            pass
        
    for w_tmp in walls_tmp:
        a = 0
        
        for r in rooms:
            if w_tmp in r.walls:
                a+=1
            else:
                pass
            
        if a == 1:
            walls_tmp.remove(w_tmp)
            
        else:
            pass
                
    return(walls_tmp)
    
#generate a path between a room n°n and room n°m

def path(n,m):
    
    reached = np.zeros((n,m)).astype('int')
    doors = []
    x,y = 0,0
    x_0, y_0 = x,y
    
    while (reached == 0).any():
        if x == 0:
            if y == 0:
                l = np.array([reached[x+1,y], reached[x,y+1]])
                
                if (l == 0).any() and (l == 1).any(): 
                    
                    pass
                
                else:
                    
                
                    a = np.random.randint(2)
                    
                    if a == 0:
                        x+=1
                        
                    else:
                        y+=1
                    
                
            elif y == m-1:
                a = np.random.randint(2)
                
                if a == 0:
                    x+=1
                    
                else:
                    y-=1
                    
                
            else:
                a = np.random.randint(3)
                
                if a == 0:
                    x+=1
                    
                elif a == 1:
                    y-=1
                    
                else:
                    y+=1
                    
        elif x == n-1:
            if y == 0:
                a = np.random.randint(2)
                
                if a == 0:
                    x-=1
                    
                else:
                    y+=1
                    
                
            elif y == m-1:
                a = np.random.randint(2)
                
                if a == 0:
                    x-=1
                    
                else:
                    y-=1
                    
                
            else:
                a = np.random.randint(3)
                
                if a == 0:
                    x-=1
                    
                elif a == 1:
                    y-=1
                    
                else:
                    y+=1
                     
            
            
        else:
            
            if y == 0:
                a = np.random.randint(3)
                
                if a == 0:
                    x+=1
                    
                elif a == 1:
                    x-=1
                    
                else:
                    y+=1
                    
                
            elif y == m-1:
                a = np.random.randint(3)
                
                if a == 0:
                    x+=1
                    
                elif a == 1:
                    x-=1
                    
                else:
                    y-=1
                    
                 
                
            else:
                a = np.random.randint(4)
                
                if a == 0:
                    x+=1
                    
                elif a == 1:
                    x-=1
                    
                elif a == 2:
                    y-=1
                    
                else:
                    y+=1
           
        reached[x,y] = 1
    
        d = [(x_0+x)/2, (y_0 + y)/2]
        
        if d not in doors:
            doors.append(d)
            
        x_0 = x
        y_0 = y
    return(reached, doors)

#generate rooms that contain at least 2 doors if they are on the boundaries 
#and 3 doors otherwise

#we decided to use this generator since with this configuration 
#we are sure that any room is reached with a construction algorithm that is 
# is easy and time efficient

def generate_rooms_3doors(f_length = 20, f_width = 15, n_x = 3, n_y = 2):
    """A function that generates a floor with:
        -at least 3 doors in the areas in the interior
        -at least 2 doors in the areas on the boundary

    Attributes
    ----------
    f_length: numeric
        length of a floor
    f_width: numeric
        width of a floor
    n_x: numeric
        number of rooms along the length dimension
    n_y: numeric
        number of rooms along the width dimension
        
    Returns
    -------
    areas: list
        a list of the areas in the floor
        
    walls: list
        a list of the walls in the floor
        
    """
    a_length = f_length / n_x
    a_width = f_width/ n_y
    
    rooms = []
    walls = []
    
    y = 0
    
    for i in range(n_y):
        x = 0
        for j in range(n_x):
            
            if i == 0 :
                w1 = doorless_wall(x, y, x+a_length, y, 'concrete')
                w4 = door_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                
                if j == 0:
                    w2 = doorless_wall(x, y, x, y + a_width, 'concrete')
                    w3 = door_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
                    
                    walls.append(w1)
                    walls.append(w2)
                    walls.append(w3)
                    walls.append(w4)
                    
                    
                elif j == n_x-1:
                    w2 = rooms[-1].walls[2]
                    w3 = doorless_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
                    
                    walls.append(w1)
                    walls.append(w3)
                    walls.append(w4)
                    
                else:
                    w2 = rooms[-1].walls[2]
                    w3 = door_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
                    
                    walls.append(w1)
                    walls.append(w3)
                    walls.append(w4)
                    
            elif i == n_y -1:
                w1 = rooms[-n_x].walls[3]
                w4 = doorless_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                
                if j == 0:
                    w2 = doorless_wall(x, y, x, y + a_width, 'concrete')
                    w3 = door_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
                    
                    walls.append(w2)
                    walls.append(w3)
                    walls.append(w4)
                
                elif j == n_x-1:
                    w2 = rooms[-1].walls[2]
                    w3 = doorless_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
                    
                    walls.append(w3)
                    walls.append(w4)
                
                else:
                    w2 = rooms[-1].walls[2]
                    w3 = door_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
        
                    
                    walls.append(w3)
                    walls.append(w4)
                    
            else:
                w1 = rooms[-n_x].walls[3]
                
                
                if j == 0:
                                        
                    w2 = doorless_wall(x, y, x, y + a_width, 'concrete')
                    w3 = door_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    w4 = door_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
                    
                    walls.append(w2)
                    walls.append(w3)
                    walls.append(w4)
                    
                elif j == n_x -1:
                    
                    w2 = rooms[-1].walls[2]
                    w3 = doorless_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    w4 = door_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                    
                    r = Room([w1, w2, w3, w4])
                    
                    walls.append(w3)
                    walls.append(w4)
                    
                else:
                    
                    w2 = rooms[-1].walls[2]
                    w3 = random_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                    w4 = random_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                
                    r = Room([w1, w2, w3, w4])
                    
                    if len(r.doors) < 3:
                        
                        if len(w3.doors) == 0 and len(w4.doors) == 1:
                            w3 = door_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                        elif len(w3.doors) == 1 and len(w4.doors) == 0:
                            w4 = door_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                        elif len(w3.doors) == 0 and len(w4.doors) == 0:
                            if len(r.doors) == 1:
                                w3 = door_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                                w4 = door_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')
                            else:
                                a = np.random.randint(2)
                                
                                if a == 0:
                                    w3 = door_wall(x + a_length, y, x+a_length, y + a_width, 'concrete')
                                else:
                                    w4 = door_wall(x, y + a_width, x+a_length, y + a_width, 'concrete')          
                                
                        else:
                            pass
                        
                          
                    r = Room([w1, w2, w3, w4]) 
                    
                    walls.append(w3)
                    walls.append(w4)
                    
            
            rooms.append(r)
            
            x+= a_length
            
        y += a_width
    
    return(rooms, walls)
    
    
    
    
    
            
    
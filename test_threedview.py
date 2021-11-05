# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 14:35:18 2021

@author: Julien
"""

#Some test code to plot a cube in 3D. 
#Could be explored to plot a 3D view of our building

import matplotlib.pyplot as plt
import numpy as np


R = plt.Rectangle((0,0), 3, 5)

fig = plt.figure(figsize = (12,10))

ax = plt.axes(projection = '3d')

t = np.linspace(0,10,1000)
a = np.array([t,t,t])

ax.plot3D(a[0,:], [0]*1000, [0]*1000, 'o', color = 'green')
ax.plot3D([0]*1000, a[1,:], [0]*1000, 'o', color = 'green')
ax.plot3D([0]*1000, [0]*1000, a[2,:], 'o', color = 'green')
ax.plot3D(a[0,:], [10]*1000, [10]*1000, 'o', color = 'green')
ax.plot3D([10]*1000, a[1,:], [10]*1000, 'o', color = 'green')
ax.plot3D([10]*1000, [10]*1000, a[2,:], 'o', color = 'green')

ax.plot3D(a[0,:], [0]*1000, [10]*1000, 'o', color = 'green')
ax.plot3D([0]*1000, a[1,:], [10]*1000, 'o', color = 'green')
ax.plot3D([0]*1000, [10]*1000, a[2,:], 'o', color = 'green')
ax.plot3D(a[1,:], [10]*1000, [0]*1000, 'o', color = 'green')
ax.plot3D([10]*1000, a[1,:], [0]*1000, 'o', color = 'green')
ax.plot3D([10]*1000, [0]*1000, a[2,:], 'o', color = 'green')

plt.axis('off')
plt.show()
# Welcome to Project2CS_DDDS!

You will find here the documention of the project.

# Goal

The aim is to build a **random building generator** and to simulate **virtual agents** walking (randomly for now) around this buidling.

# Project structure
# virtual-agent directory

This directory implements the virtual agents simulation, where agents randomly walk through a room and its doors. 
It is comprised of 3 subfolders:

- architecture
- vagents
- utils

We'll go into the details of each of them in the next packages section.

## Packages

### architecture

This package contains the following mudules:

- coordinates.py
- wall.py
- walls.py
- door.py
- doors.py
- window.py
- windows.py
- room.py
- floor.py
- building.py

The goal is to be able to create a building with several floors, each of which have several rooms. Each room are made of walls, doors and windows. The coordinates module is used to position walls, doors and windows in space.

### vagents

This package contains the following mudules:

- agent.py
- agents.py

An virtual agent is simply a person walking around from room to room through doors. 
We are interested in clusters of agents. In the animation window, the little points correspond to agents and the big points to clusters of agents (using the sklearn implementation of KMeans).

### utils

This package contains the following mudules:

- tools.py

The tools.py module implements tools for checking if two segments (not lines) intersect with each other. This is useful for checking if an agent has illegally crossed a wall when moving.

## random generator

### element.py

A file where are defined the basic elements that create a building (walls, doors, windows)

### areas.py

A file where are defined the different type of areas

### floor.py

A file where we implement a Floor class to define the floor of a building

### building.py

A file where we implement a Building class to define a building

### generator.py

In this file we implemented multiple generator of a floor of a building.

N.B. : In the following we decided to keep the generator that creates at least 3 doors for rooms inside the floor and at 2 least 2 doors for those on the boundaries.

### main.py

A file that you can launch from command line with the following syntax: 'python main.py b_length b_width b_height n_x n_y n_levels'.
- b_length: length of a building
- b_width: width of a building
- b_height: height of a building
- n_x: number of rooms along the length axis
- n_y: number of rooms along the width axis
- n_leves: number of levels in the building

### test_threedview.py

A draft of file that should be explored to plot 3D view of the building

# Running the project
## Virtual agents simulation

To simulate agents moving around (randomly as of now), the script to run is agents.py.
If a separate window doesn't appear in which to visualize the moving agents,  type <code>%matplotlib qt</code> in the console and rerun the script.

## Wall generation 

To generate walls launch the main.py file with command line with the folowing syntax 'python main.py b_length b_width b_height n_x n_y n_levels'.
- b_length: length of a building
- b_width: width of a building
- b_height: height of a building
- n_x: number of rooms along the length axis
- n_y: number of rooms along the width axis
- n_leves: number of levels in the building

e.g. python main.py 30 40 15 10 20 6



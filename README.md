# Welcome to Project2CS_DDDS!

You will find here the documention of the project.

# Goal

The aim is to build a **random buidling generator** and to simulate **virtual agents** walking (randomly for now) around this buidling.

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


# Running the project
## Virtual agents simulation

To simulate agents moving around (randomly as of now), the script to run is agents.py.
If a separate window doesn't appear in which to visualize the moving agents,  type <code>%matplotlib qt</code> in the console and rerun the script.

## Wall generation 





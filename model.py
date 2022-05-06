# -*- coding: utf-8 -*-
"""
Created on Thu May  5 09:23:45 2022

@author: allyl


This project will:
    build a series of agents in space
    
    each agent has a list of the other agents to allow them
    to communicate with them
    
    each agents knows about the environemnt they are in and 
    able to query and / or change the environment
    
    agents move about the environment checking other agents
    aren't already in the neighbourhood before eating it
    
    environment is created by taking data in from the provided
    file - in.txt
    
    display the environment and further data once this file 
    has run
    
    save the environment data as results after this file has 
    run

"""

import matplotlib.pyplot
import agentframework
import csv




# creation of variables for the number of agents, and the
# number of iterations / moves made
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20


# read in the in.txt file to create the environment
# in.txt is comma separated numbers representing pixel data - raster data
f = open('in.txt', 'r')
data = []
for line in f:
    parsed_line = str.split(line, ",")
    data_line = []
    for word in parsed_line:
        data_line.append(float(word))
    data.append(data_line)
print(data)
f.close()


environment = []

for row in data:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
    
    
# to check raster data read in correctly
"""
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show() 
"""

agents = []

# Make desired number of agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

# Move each agent the desired number of times
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        # print("move made")
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

# plot / display the agents
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()


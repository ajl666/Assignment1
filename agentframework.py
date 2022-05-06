# -*- coding: utf-8 -*-
"""
Created on Thu May  5 09:51:34 2022

@author: allyl
"""

import random

class Agent():
    
    def __init__(self, environment, agents):
        self.x = random.randint(0, 99)
        self.y = random.randint(0, 99)
        self.environment = environment
        self.agents = agents
        self.store = 0
    
    
    
    # function for moving agents
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
            # print("move made 1")
        else:
            self.y = (self.y - 1) % 100
            # print("move made 2")
            
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
            # print("move made 3")
        else:
            self.x = (self.x - 1) % 100
            # print("move made 4")
            
    # function to eat up environmnent
    def eat(self):
        if self.environment [self.y][self.x] > 10:
            self.environment [self.y][self.x] -= 10
            self.store += 10
            
    # function agents search for neighbours closeby and share resources
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= (neighbourhood):
                sum = self.store + agent.store
                ave = sum / 2
                self.store = ave
                agent.store = ave 
                print("Sharing " + str(dist) + " " + str(ave))
                
    #calculate distance
    def distance_between(self, agent):
        return(((self.x - agent.x)**2) + ((self.y - agent.y)**2)) **0.5
    
                
    
         


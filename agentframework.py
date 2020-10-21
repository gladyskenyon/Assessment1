# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 12:17:43 2020

@author: gladys
"""

import random 

class Agent:
    def __init__ (self, environment, agents):
        
        self.x = random.randint(0,100)
        self.y = random.randint(0,100)
        
        self.environment = environment
        self.store = 0 
        self.agents = agents
        
    def move(self):
        
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
        
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100


    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
        
    def share_with_neighbours(self, neighbourhood): 
        self.neighbourhood = neighbourhood
        
        
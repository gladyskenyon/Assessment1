# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 11:57:30 2020

@author: sggkenyo
"""

import random 


# Create the Agent class
class Agent:
    def __init__ (self, environment, agents, neighbourhood):
        
        self.environment = environment
        self.store = 0 
        self.agents = agents
        
        self._x = random.randint(0,300)
        self._y = random.randint(0,300)
        
# Protect x and y using get and set properties

    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value

    def gety(self):
        return self._y
    def sety(self, value):
        self._y = value

      
    def move(self):
        
        if random.random() < 0.5:
            self._x = (self._x + 1) % 300
        else:
            self._x = (self._x - 1) % 300
        
        if random.random() < 0.5:
            self._y = (self._y + 1) % 300
        else:
            self._y = (self._y - 1) % 300


    def eat(self):
        
        if self.environment[self._y][self._x] > 10:
            
            self.environment[self._y][self._x] -= 10
            
            self.store += 20
            
        elif self.environment[self._y][self._x] >0:
            
            self.environment[self._y][self._x] -= 1
            self.store += 1
    
    
    def sick(self):
        
        if self.store >= 100:
            if self.store + self.environment[self._y][self._x] <250:
                self.environment[self._y][self._x] += (self.store)
                self.store -= (250 - self.store)
        
    def share_with_neighbours(self, neighbourhood): 
        
        self.neighhbourhood = neighbourhood
        
        for agent in self.agents:
            
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                

    def distance_between(self, agent):
        return (((self._x- agent._x)**2) + ((self._y- agent._y)**2))**0.5    
        
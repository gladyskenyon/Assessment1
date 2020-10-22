# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 11:55:21 2020

@author: sggkenyo
"""

import random 
import operator
import matplotlib.pyplot
from matplotlib.animation import FuncAnimation
import agentframework1
import csv


# Create environment, upload file, read csv
environment = []
f = open('in.txt', newline = '')
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)


# join environment to rowlist
for line in reader:	
    rowlist = [] 
    for value in line:
        rowlist.append(value)
    environment.append(rowlist)
    
f.close()    

#create variables
agents = []

num_of_agents = 50

num_of_iterations = 100

neighbourhood = 20


# set figure and axis parameters
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#ax.set_autoscale_on(False)

#sharelist of agents with each agent
for i in range(num_of_agents):
   agents.append(agentframework1.Agent(environment, agents, neighbourhood))


# check the agentframework file is connected
a = agentframework1.Agent(environment, agents, neighbourhood)
print(a.y, a.x)

a.move()
print(a.y, a.x)


 #plot axis and environment 
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.xlim(0,300)


#activate agent methods
for j in range(num_of_iterations):
    
    random.shuffle(agents)    
            
    for i in range(num_of_agents):
                
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

#Animate model

#carry_on = True

def update(frame_number):
    
    fig.clear()
    
    global carry_on
    
    
    for i in range(num_of_agents):
        
            if random.random() < 0.5:
                
                agents[i].x  = (agents[i].x + 1) % 300
                
            else:
                
                agents[i].x  = (agents[i].x - 1) % 300
            
            if random.random() < 0.5:
                
                agents[i].y  = (agents[i].y + 1) % 300
                
            else:
                
                agents[i].y  = (agents[i].y - 1) % 300
                
            if random.random() < 0.1: 
                
                carry_on = False
                print("stopping condition")
       
    matplotlib.pyplot.imshow(environment)
    
    for i in range(num_of_agents):
        
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, marker='x', color='deeppink') 
        matplotlib.pyplot.show()
        
        
# create stopping function
def gen_function(b = [0]):
    
    a = 0
    global carry_on
    
    while (a < 10) & (carry_on) :
        
        yield a 
        a = a + 1


animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=5)

matplotlib.pyplot.show()
fig.show()



#save environment as csv
f2= open('environmentout.csv', 'w', newline='')
writer= csv.writer(f2, delimiter=' ')

for row in environment:
    writer.writerow(row)
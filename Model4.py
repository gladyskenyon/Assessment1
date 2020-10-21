# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 12:15:17 2020

@author: gladys
"""
import random 
import operator
import matplotlib.pyplot
import agentframework 
import csv



# Create environment, upload file
environment = []
f = open('in.txt', newline = '')
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)

# join environment to rowlist
for row in reader:	
    rowlist = [] 
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)

#create variables
agents = []
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

# check the agentframework file is connected
a = agentframework.Agent(environment, agents)
print(a.y, a.x)
a.move()
print(a.y, a.x)


for i in range(num_of_agents):
   agents.append(agentframework.Agent(environment, agents))

for j in range(num_of_iterations):
#    random.shuffle(agents)    
    for i in range(num_of_agents):
        
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)


#plot axis and environment 
matplotlib.pyplot.ylim(0,100)
matplotlib.pyplot.xlim(0,100)
matplotlib.pyplot.imshow(environment)

# plot agents
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y, marker='x', color='deeppink')   
matplotlib.pyplot.show()


#save environment as csv
f2= open('environmentout.csv', 'w', newline='')
writer= csv.writer(f2, delimiter=' ')

for row in environment:
    writer.writerow(row)



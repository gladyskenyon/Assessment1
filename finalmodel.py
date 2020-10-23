# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 11:55:21 2020

@author: sggkenyo
"""

# Upload required libraries
import random 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib 
matplotlib.use('TkAgg')
import tkinter
import csv
# Import agent class
import agentframework1



# Create environment 
# Use CSV reader code to read in text file
f = open('in.txt', newline = '')
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)

# Create empty environment list
environment = []

# Shift data into 2-D list
for line in reader:	
    rowlist = []
# Append each value to rowlist, then rowlist to environment list   
    for value in line:
        rowlist.append(value)
    environment.append(rowlist)
    
    

# Set Variables    
# For the number of agents
num_of_agents = 50

# For the number of model iterations
num_of_iterations = 50

# For the proximity of agents to share resources
neighbourhood = 40



# Set up figure and axis
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Define x and y axis scale
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.xlim(0,300)

# Set autoscaling on plots
ax.set_autoscale_on(False)



# Create agents
# Create empty list for agents
agents = []

# Give each agent access to info on others
for i in range(num_of_agents):
    agents.append(agentframework1.Agent(environment, agents, neighbourhood))

# Check the agentframework file is connected using print
a = agentframework1.Agent(environment, agents, neighbourhood)
print(a._y, a._x)

# Check the co-ordinates move
a.move()
print(a._y, a._x)


# Activate agents
for j in range(num_of_iterations):
    # Use this to randomize
    random.shuffle(agents)    
            
    for i in range(num_of_agents):
                
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours
        agents[i].sick()
        agents[i].distance_between


# Animate model
# Create update function
def update(frame_number):
    
    fig.clear()
          
       
    for i in range(num_of_agents):
        
            if random.random() < 0.5:
                
                agents[i]._x  = (agents[i]._x + 1) % 300
                
            else:
                
                agents[i]._x  = (agents[i]._x - 1) % 300
            
            if random.random() < 0.5:
                
                agents[i]._y  = (agents[i]._y + 1) % 300
                
            else:
                
                agents[i]._y  = (agents[i]._y - 1) % 300


     
       
    plt.imshow(environment)

    for i in range(num_of_agents):    
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y, marker='x', color='blue') 


# Start animation for 10 frames
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)  
    # Use becuase of GUI 
    canvas.draw()

# Set up GUI
# Build the main window
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


# Build menu bar with option to run model
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)





# Write out Files
totalstore = 0 
for agent in agents:
    totalstore = agent.store + totalstore
print("Total consumption:", totalstore)

# Write out environment as file
f2= open('environmentout.csv', 'w', newline='')
writer= csv.writer(f2, delimiter=',')
'''
# Write out total amount stored by each agent
f3= open('agentout.csv', 'w', newline='')
writer= csv.writer(f3, delimiter=',')

'''

for row in environment:
    writer.writerow(row)
f2.close 

tkinter.mainloop()
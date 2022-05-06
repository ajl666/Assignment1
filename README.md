# Assignment1
Assignment 1 of GEOG5003 module

The main project is contained within model.py.  this then accesses the agentframework.py and also reads in data from the in.txt file.
The in.txt file contains raster data for an environment.
the agentframework.py file contains a 'class' profile and functions that the 'main' model.py program accesses and makes use of.

a set number of agents (num_of_agents) are created which in the model.py file.  Each agent then moves a set number of times in random directions (the number of steps
taken are specified in the model.py (num_of_iterations)
The agents communicate with other agents.  When an agent steps into a pixel that doesn't contain an agent, it 'eats' the pixel.

the environment is displayed via the 'plots' screeen within the 'spyder' application.  this shows where the agents are and which pixels have been eaten.

import numpy as np
import sys
from Agent import Agent
'''
Every agents plays the prisoners dilemma. 
When all agents have played, the agent with the highest score is determined
and copied to the other squared in his neighbourhood

Matrix:
      c      d
  c  3 3    1 4
  d  4 1    2 2


'''
    

class World:
    def __init__(self, size):
        self.size = size
        self.grid = self.generateGrid(size)

    def generateGrid(self, size):
        gr = np.full((size, size), Agent)
        for x in range(size):
            for y in range(size):
                gr[x][y] = Agent(x, y)
        return gr

    def updateAgents(self):
        for x in range(self.size):
            for y in range(self.size):
                agent = self.grid[x][y]
                agent.updateStatus(self.grid)

    def runSimulation(self, epochs):
        for epoch in range(epochs):
            for x in range(self.size):
                for y in range(self.size):
                    agent = self.grid[x][y]
                    if x+1 < self.size:
                        agent1 = self.grid[x+1][y]
                        self.prisonersDilemma(agent, agent1)
                    if x+1 < self.size and y+1 < self.size:
                        agent2 = self.grid[x+1][y+1]
                        self.prisonersDilemma(agent, agent2)                       
                    if y+1 < self.size:
                        agent3 = self.grid[x][y+1]
                        self.prisonersDilemma(agent, agent3)
                    if x-1 >= 0 and y-1 >= 0:
                        agent4 = self.grid[x-1][y-1]
                        self.prisonersDilemma(agent, agent4)
        self.updateAgents()
        print(self.grid[1][1].points)
                    
                        
    def prisonersDilemma(self, agent1, agent2):
        if agent1.strategy == 0:
            if agent2.strategy == 0:
                agent1.points += 3
                agent2.points += 3
                print("HELLO")
            elif agent2.strategy() == 1:
                agent1.points += 1
                agent2.points += 4
                print("HELLO")
        elif agent1.strategy == 1:
            if agent2.strategy == 0:
                agent1.points += 4
                agent2.points += 1
            elif agent2.strategy == 1:
                agent1.points += 3
                agent2.points += 3
        
    


def main():
    world = World(10)
    world.runSimulation(10)


main()
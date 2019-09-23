import numpy as np
import sys
from Agent import Agent
'''
Every agents plays the prisoners dilemma. 
When all agents have played, the agent with the highest score is determined
and copied to the other squared in his neighbourhood

Matrix:
      s      b
  s  4 4    2 5
  b  5 2    3 3


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
                print(agent.strategy, end=" ")
            print()
        print("-----------------------")

    def runSimulation(self, epochs):
        for epoch in range(epochs):
            for x in range(self.size):
                for y in range(self.size):
                    agent = self.grid[x][y]
                    agent1 = self.grid[(x+1)%10][y]
                    self.prisonersDilemma(agent, agent1)
                    agent2 = self.grid[(x+1)%10][(y+1)%10]
                    self.prisonersDilemma(agent, agent2)                       
                    agent3 = self.grid[x][(y+1)%10]
                    self.prisonersDilemma(agent, agent3)
                    agent4 = self.grid[x-1][(y+1)%10]
                    self.prisonersDilemma(agent, agent4)
            self.updateAgents()
        for x in range(self.size):
            for y in range(self.size):
                print(self.grid[x][y].points, end=" ")
            print()
            
    def prisonersDilemma(self, agent1, agent2):
        agent1.plays += 1
        agent2.plays += 1
        if agent1.strategy == 0:
            if agent2.strategy == 0:
                agent1.points += 4
                agent2.points += 4
            elif agent2.strategy == 1:
                agent1.points += 2
                agent2.points += 5
        elif agent1.strategy == 1:
            if agent2.strategy == 0:
                agent1.points += 5
                agent2.points += 2
            elif agent2.strategy == 1:
                agent1.points += 3
                agent2.points += 3

    def getTotalPoints(self):
        sum = 0
        for x in range(self.size):
            for y in range(self.size):
                sum += self.grid[x][y].points
        return sum

def main():
    world = World(10)   
    world.runSimulation(10)
    points = world.getTotalPoints()
    print("Total points =", points)

main()
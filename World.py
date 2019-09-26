import numpy as np
import sys
from Agent import Agent
from constants import *
from copy import deepcopy
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
        if (size < 3):
            sys.exit("ERROR: Size should be larger than 3")
        self.size = size
        self.grid = self.generateGrid(size)

    def generateGrid(self, size):
        gr = np.full((size, size), Agent)
        for x in range(size):
            for y in range(size):
                gr[x][y] = Agent(x, y, COOPERATOR)
        return gr

    def neighbours(self, agent):
        #generator that yields the neighbours of an agent with rounding
        for i in range(-1, 2):
            yield self.grid[(agent.posx + i) % self.size][agent.posy - 1]
        yield self.grid[agent.posx - 1][agent.posy]
        yield self.grid[(agent.posx + 1) % self.size][agent.posy]
        for i in range(-1, 2):
            yield self.grid[(agent.posx + i) % self.size][(agent.posy + 1) % self.size]

    def countJoy(self, agent):
        joy = 0
        for neighbour in self.neighbours(agent):
            if neighbour.emotion == JOY:
                joy += 1
        return joy

    def countDistress(self, agent):
        #counts the number of distressed neighbours
        distress = 0
        for neighbour in self.neighbours(agent):
            if neighbour.emotion == DISTRESS:
                distress += 1
        return distress


    def runSimulation(self, epochs):
        for epoch in range(epochs):
            print("EPOCH =", epoch)
            for x in range(self.size):
                for y in range(self.size):
                    agent = self.grid[x][y]
            
                    agent1 = self.grid[(x+1)%self.size][y]
                    self.prisonersDilemma(agent, agent1)
                    agent2 = self.grid[(x+1)%self.size][(y+1)%self.size]
                    self.prisonersDilemma(agent, agent2)
                    agent3 = self.grid[x][(y+1)%self.size]
                    self.prisonersDilemma(agent, agent3)
                    agent4 = self.grid[x-1][(y+1)%self.size]
                    self.prisonersDilemma(agent, agent4)
            self.evolution()
        
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

    def evolution(self):
        grid_copy = deepcopy(self.grid)
        for x in range(self.size):
            for y in range(self.size):
                agent = self.grid[x][y]
                best_type = agent.type
                highest = agent.round_points
                for neighbour in self.neighbours(agent):
                    if neighbour.round_points > highest:
                        best_type = neighbour.type
                grid_copy[x][y].type = best_type
                self.grid = grid_copy
        

                
                    
                

    def getTotalPoints(self):
        sum = 0
        for x in range(self.size):
            for y in range(self.size):
                sum += self.grid[x][y].points
        return sum



def main():
    print(type)
    world = World(10)
    world.runSimulation(10)
    points = world.getTotalPoints()
    print("Total points =", points)
    print(type)

main()

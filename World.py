import numpy as np
import sys
from Agent import Agent
from constants import *
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
        if (size%3 != 0):
            sys.exit("ERROR: Size should be divisible by 3")
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
        for i in range(-1, 0):
            yield self.grid[(agent.posx + i) % self.size][agent.posy - 1]
        yield self.grid[agent.posx - 1][agent.posy]
        yield self.grid[(agent.posx + 1) % self.size][agent.posy]
        for i in range(-1, 0):
            yield self.grid[(agent.posx + i) % self.size][(agent.posy + 1) % self.size]


    def countDistress(self, agent):
        #counts the number of distressed neighbours
        distressed = 0
        for agent in self.neighbours(agent):
            if agent.emotion == DISTRESS:
                distressed += 1
        return distressed

    def updateEmotion(self, agent):
        if agent.points >= POINTS_THRESHOLD:
            agent.emotion = JOY
        if agent.points < POINTS_THRESHOLD or self.countDistress(agent) > DISTRESS_THRESHOLD:
            agent.emotion = DISTRESS


    def updateAgents(self):
        for x in range(self.size):
            for y in range(self.size):
                agent = self.grid[x][y]
                agent.updateStatus()
                self.updateEmotion(agent)

                print(agent.emotion, end=" ")
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
        self.evolution()

    def prisonersDilemma(self, agent1, agent2):
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
        best_agent = None
        highest = -1
        for x in range(1, self.size - 1, 3):
            for y in range(1, self.size - 1, 3):
                for x_ in range(x-1, x+1):
                    for y_ in range(y-1, y+1):
                        if self.grid[x_][y_].round_points > highest:
                            highest = self.grid[x][y].round_points
                            best_agent = self.grid[x][y]
                            print("HIGHEST", x_, y_)

    def getTotalPoints(self):
        sum = 0
        for x in range(self.size):
            for y in range(self.size):
                sum += self.grid[x][y].points
        return sum



def main():
    #Make sure its divisible by 3 for evolution. Also done in bazzan paper
    world = World(12)
    world.runSimulation(10)
    points = world.getTotalPoints()
    print("Total points =", points)

main()

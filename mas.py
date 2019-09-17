import numpy as np


'''
Every agents plays the prisoners dilemma. 
When all agents have played, the agent with the highest score is determined
and copied to the other squared in his neighbourhood

Matrix:
      c      d
  c  3 3    1 4
  d  4 1    2 2


'''
    
class Agent:
    def __init__(self, x, y):
        self.posx = x
        self.posy = y
        self.points = 0
        self.hasPlayed = False
        


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

    def runSimulation(self, epochs):
        for epoch in epochs:
            for x in range(self.size):
                for y in range(self.size):
                    agent = self.grid[x][y]
                    if not agent.hasPlayed:
                        self.prisonersDilemma(x, y)
                        
    def prisonersDilemma(self, agent_x, agent_y):
        pass
        

def main():
    world = World(10)



main()
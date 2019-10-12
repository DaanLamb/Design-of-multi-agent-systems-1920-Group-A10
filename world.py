import numpy as np
import sys
from agent import *
from constants import *
import copy
import random
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
    def __init__(self, size = SIZE):
        '''
        initialize the world with a size and a (size x size) grid filled with agents
        the size has to be at least 3 in order for the agents to have 8 neighbours
        '''
        if (size < 3):
            sys.exit("ERROR: Size should be larger than 3")
        self.size = size
        self.grid = self.generateGrid(size)

    def generateGrid(self, size):
        #generate a numpy array with agents, for now the agent type is random
        gr = np.full((size, size), Agent)
        for x in range(size):
            for y in range(size):
                if random.random() < 0.2:
                    if random.random() < 0.5:
                        gr[x][y] = Agent(x, y, COOPERATOR)
                    else:
                        gr[x][y] = Agent(x, y, DEFECTOR)
                else:
                    gr[x][y] = Agent(x, y, EMOTIONAL)
        return gr

    def neighbours(self, agent):
        #generator that yields the neighbours of an agent with rounding
        for i in range(-1, 2):
            yield self.grid[(agent.posx + i) % self.size][agent.posy - 1]
        yield self.grid[agent.posx - 1][agent.posy]
        yield self.grid[(agent.posx + 1) % self.size][agent.posy]
        for i in range(-1, 2):
            yield self.grid[(agent.posx + i) % self.size][(agent.posy + 1) % self.size]

    def resetAgents(self):
        #reset the round points of all agents
        for x in range(self.size):
            for y in range(self.size):
                self.grid[x][y].round_points = 0

    def playGames(self, agent, opponents):
        for adversary in opponents:
            if agent.agent_type == EMOTIONAL:
                agent.update(self.neighbours(agent), adversary)
            if adversary.agent_type == EMOTIONAL:
                adversary.update(self.neighbours(adversary), agent)
            self.prisonersDilemma(agent, adversary)

    def runSimulation(self, epochs = EPOCHS):
        '''
        main loop of the simulation,
        every iteration every agent, updated and the prisoner's dilemma
        is played with 8 neighbours, after this there is an evolution step
        '''
        for epoch in range(epochs):
            print("EPOCH =", epoch)
            x_rand = random.randint(0, SIZE)
            y_rand = random.randint(0, SIZE)
            for i in range(self.size):
                for j in range(self.size):
                    x = i + x_rand
                    y = j + y_rand
                    opponents = []
                    agent = self.grid[x%self.size][y%self.size]
                    opponents.append(self.grid[(x+1)%self.size][y%self.size])
                    opponents.append(self.grid[(x+1)%self.size][(y+1)%self.size])
                    opponents.append(self.grid[x%self.size][(y+1)%self.size])
                    opponents.append(self.grid[(x-1)%self.size][(y+1)%self.size])

                    random.shuffle(opponents)
                    self.playGames(agent, opponents)

            self.evolution()
            self.resetAgents()
            print("Agent types")
            for x in range(self.size):
                for y in range(self.size):
                    print(self.grid[x][y].agent_type, end=" ")
                print()
            print("=============================")
            print("EMOTIONS")
            for x in range(self.size):
                for y in range(self.size):
                    #self.grid[x][y].updateEmotion(self.neighbours(self.grid[x][y]), self.grid[(x+1)&self.size][(y+1)&self.size])
                    print(self.grid[x][y].emotion, end=" ")
                print()
            print("=============================")


        print("END SIMULATION")
        print("Points")
        for x in range(self.size):
            for y in range(self.size):
                print(self.grid[x][y].points, end=" ")
            print()


    def prisonersDilemma(self, agent1, agent2):
        #prisoner's dillema according to the matrix on top of this file
        if agent1.strategy == COOPERATE:
            if agent2.strategy == COOPERATE:
                agent1.points += 4
                agent1.round_points += 4
                agent2.points += 4
                agent2.round_points += 4
            elif agent2.strategy == DEFECT:
                agent1.points += 2
                agent1.round_points += 2
                agent2.points += 5
                agent2.round_points += 5
        elif agent1.strategy == DEFECT:
            if agent2.strategy == COOPERATE:
                agent1.points += 5
                agent1.round_points += 5
                agent2.points += 2
                agent2.round_points += 2
            elif agent2.strategy == DEFECT:
                agent1.points += 3
                agent1.round_points += 3
                agent2.points += 3
                agent2.round_points += 3
        agent1.prev_strat_neighbours[agent2.id] = agent2.strategy
        agent2.prev_strat_neighbours[agent1.id] = agent1.strategy
        agent1.plays += 1
        agent2.plays += 1


    def evolution(self):
        '''
        evolution step, for every agent, him and his 8 neighbours are compared
        and the agent type with the most points during the iteration is copied to the middle
        '''
        grid_copy = copy.deepcopy(self.grid)
        counter = 0
        for x in range(self.size):
            for y in range(self.size):
                agent = self.grid[x][y]
                best_type = agent.agent_type
                highest = agent.round_points
                for neighbour in self.neighbours(agent):
                    if neighbour.round_points > highest:
                        if agent.agent_type != best_type:
                            counter += 1
                        highest = neighbour.round_points
                        best_type = neighbour.agent_type
                grid_copy[x][y].agent_type = best_type
        self.grid = copy.deepcopy(grid_copy)
        #print(counter)

    def getTotalPoints(self):
        #get the total points of all agents
        sum = 0
        for x in range(self.size):
            for y in range(self.size):
                sum += self.grid[x][y].points
        return sum



def main():
    world = World()
    print("Simulation params:")
    print("Epochs = 10, grid_size = (10,10), pct cooperator/defector and emotional = 50/50")
    print("Points_threshold = 15, neighbour_threshold = 5")
    print("INITIAL GRID")
    for x in range(world.size):
        for y in range(world.size):
            print(world.grid[x][y].agent_type, end=" ")
        print()
    print("=============================")
    world.runSimulation()
    points = world.getTotalPoints()
    print("Total points =", points)
    print("=============================")
    print("Agent types")
    for x in range(world.size):
        for y in range(world.size):
            print(world.grid[x][y].agent_type, end=" ")
        print()
    for x in range(world.size):
        for y in range(world.size):
            print(world.grid[x][y].emotion, end=" ")
        print()
    '''
    print("** PLAYS: **************")
    for x in range(world.size):
        for y in range(world.size):
            print(world.grid[x][y].plays, end=" ")
        print()

    for x in range(world.size):
        for y in range(world.size):
            print(world.grid[x][y].joy, end=" ")
            print(world.grid[x][y].distress, end=" ")
            print(world.grid[x][y].pity, end=" ")
            print(world.grid[x][y].anger, end=" ")
        print()
    '''
main()

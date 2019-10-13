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
        self.file = open("gain_per_type.csv", "w")
        self.countStrategy = 2 * [0]

    def generateGrid(self, size):
        #generate a numpy array with agents, for now the agent type is random
        gr = np.full((size, size), Agent)
        for x in range(size):
            for y in range(size):
                if random.random() < 0.5:
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

    def outputGains(self, epoch):
        total_emotion_gain = 6 * [0]
        for x in range(self.size):
            for y in range(self.size):
                for type in range(6):
                    total_emotion_gain[type] += self.grid[x][y].typedGains[type]
        self.file.write(str(epoch) + ",")
        for type in range(6):
            self.file.write(str(total_emotion_gain[type]) + ",")
        self.file.write("\n")

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
            self.outputGains(epoch)
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
                agent1.updateScore(4)
                agent2.updateScore(4)
            elif agent2.strategy == DEFECT:
                agent1.updateScore(2)
                agent2.updateScore(5)
        elif agent1.strategy == DEFECT:
            if agent2.strategy == COOPERATE:
                agent1.updateScore(5)
                agent2.updateScore(2)
            elif agent2.strategy == DEFECT:
                agent1.updateScore(3)
                agent2.updateScore(3)
        self.countStrategy[agent1.strategy] +=1
        self.countStrategy[agent2.strategy] +=1
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
                best_emotion = agent.emotion
                for neighbour in self.neighbours(agent):
                    if neighbour.round_points > highest:
                        if agent.agent_type != best_type:
                            counter += 1
                        highest = neighbour.round_points
                        best_type = neighbour.agent_type
                        best_emotion = neighbour.emotion
                agent.agent_type = best_type
                agent.emotion = best_emotion
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
    print("Simulation params:", flush=True)
    world = World()
    print("Epochs =",EPOCHS," grid_size = (",SIZE,",",SIZE,"), pct cooperator/defector and emotional = 50/50")
    print("Points_threshold =",POINTS_THRESHOLD," neighbour_threshold =",NEIGHBOUR_THRESHOLD)
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
    print("=============================")
    print("EMOTIONS")
    for x in range(world.size):
        for y in range(world.size):
            print(world.grid[x][y].emotion, end=" ")
        print()


    #calculate total amount of gain per emotion
    total_emotion_gain = 6 * [0]
    for x in range(world.size):
        for y in range(world.size):
            for type in range(6):
                total_emotion_gain[type] += world.grid[x][y].typedGains[type]

    #print total gain per emotion and types
    print("Emotional gain")
    for type in range(6):
        print(total_emotion_gain[type])

    print("strategies played")
    print("Cooperating: " + str(total_emotion_gain[COOPERATE]))
    print("Defecting: " + str(total_emotion_gain[DEFECT]))

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

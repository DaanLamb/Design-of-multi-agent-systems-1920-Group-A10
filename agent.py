import random
from constants import *


class Agent:
    def __init__(self, x, y, agent_type):
        #initialize the agent with its own position, zero points, starting emotion and strategy
        self.id = str(x) + str(y) # to make dictionary works better
        self.posx = x
        self.posy = y
        self.points = 0
        self.round_points = 0
        self.emotion = None
        self.agent_type = agent_type
        self.prev_strat_neighbours = {}
        self.strategy = COOPERATE if agent_type == COOPERATOR else DEFECT
        self.joy = 0
        self.distress = 0
        self.pity = 0
        self.anger = 0


    def update(self, neighbours, opponent):
        '''
        update the agents by updating the emotion and updating
        the strategy, which depends on the emotion
        '''
        self.updateEmotion(neighbours, opponent)
        self.updateStrategy()

    def updateEmotion(self, neighbours, opponent):
        #updates the emotion of the agent based on the rules of the Bazzan, 2001 paper
        if self.round_points >= POINTS_THRESHOLD or self.countJoy(neighbours) >= NEIGHBOUR_THRESHOLD:
            self.emotion == JOY
            self.joy += 1
        if self.round_points < POINTS_THRESHOLD or self.countDistress(neighbours) >= NEIGHBOUR_THRESHOLD:
            self.emotion = DISTRESS
            self.distress += 1
        if opponent.round_points < POINTS_THRESHOLD:
            self.emotion = PITY
            self.pity += 1
        if self.round_points < POINTS_THRESHOLD and opponent.id in self.prev_strat_neighbours and self.prev_strat_neighbours[opponent.id] == DEFECT:
            self.emotion = ANGER
            self.anger += 1

    def countJoy(self, neighbours):
        #counts the number of joyous neighbours
        joy = 0
        for neighbour in neighbours:
            if neighbour.emotion == JOY:
                joy += 1
        return joy

    def countDistress(self, neighbours):
        #counts the number of distressed neighbours
        distress = 0
        for neighbour in neighbours:
            if neighbour.emotion == DISTRESS:
                distress += 1
        return distress

    def updateStrategy(self):
        #update the strategy depending on the rules of the Bazzan, 2001 paper
        if self.emotion == JOY:
            self.strategy = COOPERATE
        elif self.emotion == DISTRESS:
            self.strategy = DEFECT
        elif self.emotion == PITY:
            self.strategy = COOPERATE
        elif self.emotion == ANGER:
            self.strategy == DEFECT

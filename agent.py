import random
from constants import *

class Agent:
    def __init__(self, x, y, agent_type):
        #initialize the agent with its own position, zero points, starting emotion and strategy
        self.posx = x
        self.posy = y
        self.plays = 0
        self.points = 0
        self.round_points = 0
        self.emotion = JOY
        self.agent_type = agent_type
        self.strategy = None
        if agent_type == COOPERATOR:
            self.strategy == COOPERATE
        elif agent_type == DEFECTOR:
            self.strategy == DEFECT
        else:
            self.updateStrategy()

    def update(self, neighbours):
        '''
        update the agents by updating the emotion and updating
        the strategy, which depends on the emotion
        '''
        self.updateEmotion(neighbours)
        self.updateStrategy()

    def updateEmotion(self, neighbours):
        #updates the emotion of the agent based on the rules of the Bazzan, 2001 paper
        if self.round_points >= POINTS_THRESHOLD or self.countJoy(neighbours) >= JOY_THRESHOLD:
            self.emotion == JOY
        if self.round_points < POINTS_THRESHOLD or self.countDistress(neighbours) >= DISTRESS_THRESHOLD:
            self.emotion = DISTRESS
        if self.hasPoorNeighbour(neighbours):
            self.emotion = PITY

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

    def hasPoorNeighbour(self, neighbours):
        #checks to see if there is a neighbour with less than POINTS_THRESHOLD points
        for neighbour in neighbours:
            if neighbour < POINTS_THRESHOLD:
                return True
        return False

    def updateStrategy(self):
        #update the strategy depending on the rules of the Bazzan, 2001 paper
        if self.emotion == JOY:
            self.strategy = COOPERATE        
        elif self.emotion == DISTRESS:
            self.strategy = DEFECT
        elif self.emotion == PITY:
            self.strategy = COOPERATE
        else:
            print("ANGER")
        

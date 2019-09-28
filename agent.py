import random
from constants import *

class Agent:
    def __init__(self, x, y, agent_type):
        #initialize the agent with its own position and zero points
        self.posx = x
        self.posy = y
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
        self.updateEmotion(neighbours)
        self.updateStrategy()

    def updateEmotion(self, neighbours):
        if self.round_points >= POINTS_THRESHOLD or self.countJoy(neighbours) >= JOY_THRESHOLD:
            self.emotion == JOY
        if self.round_points < POINTS_THRESHOLD or self.countDistress(neighbours) >= DISTRESS_THRESHOLD:
            self.emotion = DISTRESS
        if self.hasPoorNeighbour(neighbours):
            self.emotion = PITY

    def countJoy(self, neighbours):
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
        for neighbour in neighbours:
            if neighbour < POINTS_THRESHOLD:
                return True
        return False

    def updateStrategy(self):
        if self.emotion == JOY:
            self.strategy = COOPERATE
        
        elif self.emotion == DISTRESS:
            self.strategy = DEFECT
        
        elif self.emotion == PITY:
            self.strategy = COOPERATE
        

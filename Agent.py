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
        self.strategy = DEFECT if agent_type == DEFECTOR else COOPERATE
        self.plays = 0

    def update(self, world):
        self.updateEmotion(world)
        self.updateStrategy()

    def updateEmotion(self, world)
        if self.round_points >= POINTS_THRESHOLD or world.countJoy(self) >= JOY_THRESHOLD:
            self.emotion == JOY
        if self.round_points < POINTS_THRESHOLD or world.countDistress(self) >= DISTRESS_THRESHOLD:
            self.emotion = DISTRESS
        if self.

    
    def updateStrategy(self):
        #updates the status of the strategy
        if self.type == COOPERATOR or self.type == DEFECTOR:
            return
        if self.emotion == JOY or self.emotion == PITY:
            self.strategy = COOPERATE
            return
        if self.emotion == ANGER or self.emotion == DISTRESS:
            self.strategy = DEFECT
        return

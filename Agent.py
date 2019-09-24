import random
from constants import *

class Agent:
    def __init__(self, x, y, type):
        #initialize the agent with its own position and zero points
        self.posx = x
        self.posy = y
        self.points = 0
        self.round_points = 0
        self.emotion = JOY
        self.type = type
        self.strategy = DEFECT if type == DEFECTOR else COOPERATE

    def updateStatus(self, grid):
        #self.updateEmotion
        self.updateStrategy()

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

    from Emotions import updateEmotion

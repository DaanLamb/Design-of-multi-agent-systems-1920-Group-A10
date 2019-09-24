import random
from constants import *

class Agent:
    def __init__(self, x, y):
        #initialize the agent with its own position and zero points
        self.posx = x
        self.posy = y
        self.points = 0
        self.emotion = JOY
        self.strategy = COOPERATE



    def updateStatus(self, grid):
        #self.updateEmotion
        self.updateStrategy()

    def updateStrategy(self):
        #updates the status of the strategy
        self.strategy = random.randint(0,1)

    from Emotions import updateEmotion

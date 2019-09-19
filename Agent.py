import random

class Agent:
    def __init__(self, x, y):
        #initialize the agent with its own position and zero points
        self.posx = x
        self.posy = y
        self.points = 0
        self.emotion = 0
        self.strategy = 0

    def updateStatus(self, grid):
        #self.updateEmotion
        self.updateStrategy()

    def updateStrategy(self):
        #, and returns wether to cooperate or defect
        self.strategy = random.randint(0,1)

    def updateEmotion(self):
        #updates emotional states
        pass

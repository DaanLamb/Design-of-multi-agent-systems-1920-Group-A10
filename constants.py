#simulation parameters
SIZE = 10
EPOCHS = 10

#agent types
COOPERATOR = 0
DEFECTOR = 1
EMOTIONAL = 2

#emotions
JOY = 0
DISTRESS = 1
PITY = 2
ANGER = 3

#strategy
COOPERATE = 0
DEFECT = 1

#emotion thresholds
POINTS_THRESHOLD = 20 # threshold of amount of points required for JOY
NEIGHBOUR_THRESHOLD = 3 # number of neighbours that have to have the same emotion in order for the agent to copy it

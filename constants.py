#simulation parameters
SIZE = 30
EPOCHS = 100

#agent types
COOPERATOR = 0
DEFECTOR = 1
EMOTIONAL = 2

#emotions
JOY = 0
DISTRESS = 1
PITY = 2
ANGER = 3
COOP = 4
DEF = 5

#strategy
COOPERATE = 0
DEFECT = 1

#Payoff matrix
R = 1
T = 1.9
S = P = 0

#emotion thresholds
POINTS_THRESHOLD = 20 # threshold of amount of points required for JOY
NEIGHBOUR_THRESHOLD = 3 # number of neighbours that have to have the same emotion in order for the agent to copy it

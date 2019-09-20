import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from matplotlib import colors

# waarschijnlijk agent array uitlezen en nieuwe (value) array maken
# array (grid) is accessed [y][x]

lData = np.random.randint(0,7,size=(30,30))
lMap = colors.ListedColormap(['red','orange','yellow','green','blue','purple','pink'])

img = plt.imshow(lData, cmap=lMap, interpolation='nearest')

# eventuele legenda (moeten nog labels bij)
plt.colorbar(img, cmap=lMap, ticks=[])

plt.title('Spatial representation of agents in IDP grid')

# histogram for plotting ratio bar graph
hist = [0,0,0,0,0,0,0]
for i in range(len(lData)):
    for j in range(len(lData[i])):
        hist[lData[i][j]] +=1

plt.show()

# TODO
# ------------------
# bar fiksen met verhoudingen
# legenda labels
# ruimte tussen agents
# assen opmaak
# waardes (cooperation / defect) onder de grafiek
# verloop lijn grafieken maken (elke iteratie?)

# GREEN LANTERN EMOTION COLOUR SCHEME
# ------------------
# anger = RED
# greed = ORANGE
# fear = GEEL
# willpower = GREEN
# hope = BLUE
# compassion = PURPLE
# lief = PINK
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import colors

import matplotlib.image as mpimg

# Python Cheat Sheet
# https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf



# waarschijnlijk agent array uitlezen en nieuwe (value) array maken
# array (grid) is accessed [y][x]

# Functie voor het tekenen van de grid met de agents en de emoties
def drawGrid():
    lData = np.random.randint(0, 7, size=(30, 30))
    lMap = colors.ListedColormap(['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink'])

    img = plt.imshow(lData, cmap=lMap, interpolation='nearest')

    # eventuele legenda (moeten nog labels bij)
    plt.colorbar(img, cmap=lMap, ticks=[])

    plt.title('Spatial representation of agents in IDP grid')

    plt.show()

# Functie voor het uitrekenen van de proporties van de emoties in de grid
def countGrid():
    # histogram for plotting ratio bar graph
    hist = [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(lData)):
        for j in range(len(lData[i])):
            hist[lData[i][j]] += 1

# Plot de stacked barplot met de ratio's van emoties
def drawStackedBar():
    #Taken from https://python-graph-gallery.com/12-stacked-barplot-with-matplotlib/



    # y-axis in bold
    rc('font', weight='bold')

    # Values of each group
    emotion1 = [12]
    emotion2 = [28]
    emotion3 = [25]
    emotion4 = [35]

    # Heights of bars1 + bars2
    emotions12 = np.add(emotion1, emotion2).tolist()
    emotions123 = np.add(emotions12, emotion3).tolist()

    # The position of the bars on the x-axis
    r = [0]

    # Names of group and bar width
    names = ['A']
    barWidth = 0.5

    # Create brown bars
    plt.bar(r, emotion1, color='#7f6d5f', edgecolor='white', width=barWidth)
    # Create green bars (middle), on top of the firs ones
    plt.bar(r, emotion2, bottom=emotion1, color='#557f2d', edgecolor='white', width=barWidth)
    # Create green bars (top)
    plt.bar(r, emotion3, bottom=emotions12, color='#2d7f5e', edgecolor='white', width=barWidth)
    # Create next bar
    plt.bar(r, emotion4, bottom=emotions123, color='#c6c6c6', edgecolor='white', width=barWidth)

    # Custom X axis
    plt.xticks(r, names, fontweight='bold')
    plt.xlabel("group")

    # Show graphic
    plt.show()


drawGrid()
drawStackedBar()

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
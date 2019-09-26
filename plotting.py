import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rc
from matplotlib import colors

import matplotlib.image as mpimg

# Python Cheat Sheet
# https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf

lData = np.random.randint(0, 7, size=(30, 30))
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']
emotions = ['Anger', 'Greed', 'Fear', 'Willpower', 'Hope', 'Compassion', 'Love']

# waarschijnlijk agent array uitlezen en nieuwe (value) array maken
# array (grid) is accessed [y][x]

# Functie voor het tekenen van de grid met de agents en de emoties
def drawGrid():
    lMap = colors.ListedColormap(colours)
    
    fig, ax = plt.subplots()    
    
    img = ax.imshow(lData, cmap=lMap, interpolation='nearest')

    # ticks is niet dynamisch, dus moet evt nog veranderd worden
    cbar = fig.colorbar(img, cmap=lMap, ticks=[0.45, 1.25, 2.1, 3, 3.85, 4.7, 5.5])
    cbar.ax.set_yticklabels(emotions)
    
    plt.title('Spatial representation of agents in IDP grid')

    plt.show()

# Functie voor het uitrekenen van de proporties van de emoties in de grid
def countGrid():
    # histogram for plotting ratio bar graph
    hist = [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(lData)):
        for j in range(len(lData[i])):
            hist[lData[i][j]] += 1
    # normalize by dividing by total amount of agents
    return [x / 900 for x in hist] 

# Plot de stacked barplot met de ratio's van emoties
def drawStackedBar(hist):
    #Taken from https://python-graph-gallery.com/12-stacked-barplot-with-matplotlib/

    # y-axis in bold
    rc('font', weight='bold')

    # The position of the bars on the x-axis
    r = [0] 
    
    # Names of group and bar width
    barWidth = 0.5
    start = 0
    
    for i in range(len(hist)):
        plt.bar(r, hist[i], bottom=start, color=colours[i], edgecolor='white', width=barWidth)
        start += hist[i]
    
    # Custom X axis
    plt.xticks(r, [], fontweight='bold')
    plt.xlabel("Emotion")

    # Show graphic
    plt.show()

drawGrid()
drawStackedBar(countGrid())

# TODO
# ------------------
# ruimte tussen agents
# assen opmaak
# waardes (cooperation / defect) onder de grafiek
# verloop lijn grafieken maken (elke iteratie?)
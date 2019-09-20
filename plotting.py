# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

#import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import colors

data = np.random.randint(0,6,size=(30,30))

#cdict = {
#'red'  :  ((0., 0., 0.), (0.5, 0.25, 0.25), (1., 1., 1.)),
#'green':  ((0., 1., 1.), (0.7, 0.0, 0.5), (1., 1., 1.)),
#'blue' :  ((0., 1., 1.), (0.5, 0.0, 0.0), (1., 1., 1.))
#}

cmap = colors.ListedColormap(['red','blue','green','orange','black','white'])
bounds=[0,5,10]
norm = colors.BoundaryNorm(bounds, cmap.N)

#print(data[0][0])
#print(data[29][0])
#print(data[0][29])
#print(data[29][29])

img = plt.imshow(data, cmap=cmap, interpolation='nearest')

plt.colorbar(img, cmap=cmap, norm=norm, boundaries=bounds, ticks=[0, 5, 10])

plt.show()

# bar fiksen met verhoudingen
# legenda?
# ruimte tussen agents
# titel, assen opmaak
# waardes onder de grafiek

# anger = RED
# greed = ORANGE
# fear = GEEL
# willpower = GREEN
# hope = BLUE
# compassion = PURPLE
# lief = PINK


#plt.plot(data)
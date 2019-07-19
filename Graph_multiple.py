import matplotlib.pyplot as plt
import numpy as np
import math
import itertools
colors = itertools.cycle(["r", "b", "g"])

def graph_multiple(*args, parametric=False):

    plt.figure()
    ax = plt.gca()
    vectors = tuple([x for x in args])
    for v in vectors:
            ax.quiver(0,0, v[0], v[1], angles='xy',scale_units='xy',scale=1,color=next(colors))
            x,y = zip(*vectors)
            ax.set_xlim([min(x)-2, max(x)+2])
            ax.set_ylim([min(x)-2,max(x)+2])

            if parametric:
                ax.quiver(v[0]*-10,v[1]*-10, v[0]*10, v[1]*10, angles='xy',alpha=.4,scale=1,color='red')

    x,y = zip(*vectors)
    ax.set_xlim([min(x)-3, max(x)+3])
    ax.set_ylim([min(x)-3,max(x)+3])

    plt.axvline(color='black')
    plt.axhline(color='black')
    plt.grid()
    plt.draw()
    plt.show()

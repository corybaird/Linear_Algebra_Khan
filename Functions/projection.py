import numpy as np
import matplotlib.pyplot as plt
import math
def unit_vector(vector):
    coords_squared = tuple([x**2 for x in vector])
    magnitude = math.sqrt(sum(coords_squared))
    normalized = (1/magnitude)
    unit_vector = np.multiply(vector, normalized)
    return unit_vector

def projection_length(line, x_vec):
    unit = unit_vector(line)
    equation = (np.dot(x_vec,unit))*unit
    return equation

def connect(line, x_vec):
    solution = x_vec-projection_length(line, x_vec)
    return solution

def projection(vecs):

    plt.figure()
    ax = plt.gca()

    line, x = [np.array(i) for i in vecs]

    #Equation for line
    ax.quiver(line[0]*-10,line[1]*-10, line[0]*10, line[1]*10, angles='xy',alpha=.4,scale=1,color='green')

    #Equation for grapX
    ax.quiver(0,0,x[0],x[1],angles='xy',scale_units='xy',scale=1, color='orchid')

    #Projection of X on L
    ax.quiver(0,0,projection_length(line, x)[0], projection_length(line, x)[1]
              ,angles='xy',scale_units='xy',scale=1, color='red')
    ax.text((projection_length(line, x)[0])*1.1, (projection_length(line, x)[1])*1.1,
            'Projection vector'+str(projection_length(line, x)), color='red')


    #X-(Projection of X on L)
    ax.quiver(projection_length(line, x)[0], projection_length(line, x)[1],connect(line, x)[0], connect(line, x)[1]
              ,angles='xy',scale_units='xy',scale=1, color='orange')
    ax.text(x[0]*1.1, x[1]*1.1, 'Projection - X', color='orange')


    plt.axvline(color='black')
    plt.axhline(color='black')
    plt.ylim(0,5)
    plt.xlim(0,5)
    plt.grid()
    plt.draw()
    plt.show()

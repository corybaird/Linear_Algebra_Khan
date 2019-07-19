import numpy as np
import matplotlib.pyplot as plt

def vector(vecs, parametric= False, addition=False, subtract=False, scalar = None):

    plt.figure()
    ax = plt.gca()

    if len(vecs)< 2:
        vec = np.array(vecs[0])
        ax.quiver(0,0, vec[0], vec[1], angles='xy',scale_units='xy',scale=1,color='green')

        if parametric:
            ax.quiver(vec[0]*-10,vec[1]*-10, vec[0]*10, vec[1]*10, angles='xy',alpha=.4,scale=1,color='red')
            ax.set_title('Vec_1 '+'['+str(vec[0])+','+str(vec[1])+']'+' with parametric line', color='green')


        if scalar:
            scaled = scalar*vec
            ax.quiver(0,0, scaled[0],scaled[1], angles='xy',scale_units='xy',scale=1,color='green')
            ax.quiver(0,0, vec[0], vec[1], angles='xy',scale_units='xy',scale=1,color='red')
            ax.set_title('Vec_1 '+'['+str(vec[0])+','+str(vec[1])+']'+' scaled by '+str(scalar), color='green')

    else:
        a,b = [np.array(i) for i in vecs]
        ax.quiver(0,0,a[0],a[1],angles='xy',scale_units='xy',scale=1, color='red')
        ax.quiver(0,0,b[0],b[1],angles='xy',scale_units='xy',scale=1, color='orchid')

        if parametric:
            ax.quiver(b[0]*-10,b[1]*-10, b[0]*10, b[1]*10, angles='xy',alpha=.4,scale=1,color='green')
            ax.quiver(a[0]*-10,a[1]*-10, a[0]*10, a[1]*10, angles='xy',alpha=.4,scale=1,color='green')


        if addition:
            a_plus_b = np.add(a,b)
            ax.quiver(0,0, a_plus_b[0], a_plus_b[1], angles='xy',scale_units='xy',scale=1, color='green')
            ax.set_title('Vec_1+Vec_2: ['+str(a_plus_b[0])+','+str(a_plus_b[1])+']', color='green')

        if subtract:
            a_minus_b = np.subtract(a,b)
            ax.quiver(0,0, a_minus_b[0], a_minus_b[1], angles='xy',scale_units='xy',scale=1, color='green')
            ax.set_title('Vec_1+Vec_2: ['+str(a_minus_b[0])+','+str(a_minus_b[1])+']', color='green')


    plt.axvline(color='black')
    plt.axhline(color='black')
    plt.ylim(-5,5)
    plt.xlim(-5,5)
    plt.grid()
    plt.draw()
    plt.show()

from matplotlib import pyplot as plt
import numpy as np
import math

def basis(vecs):

    plt.figure()
    ax = plt.gca()
    x,y= zip(*vecs)
    ax.set_xlim([min(x)-3, max(x)+3])
    ax.set_ylim([min(y)-3,max(y)+3])

    v1,v2, a = [np.array(i) for i in vecs]

    #v1
    ax.quiver(0,0,v1[0],v1[1],angles='xy',scale_units='xy',scale=1, color='Orange')

    #v2
    ax.quiver(0,0,v2[0],v2[1],angles='xy',scale_units='xy',scale=1, color='Orange')

    #v1 & v2 in displayed in titled as basis vetors
    ax.set_title('Basis vectors: '+str(np.ravel(v1)) +' , '+ str(np.ravel(v2)),  color='orange')

    #Plot A vector
    ax.quiver(0,0,a[0],a[1],angles='xy',scale_units='xy',scale=1, color='orchid')

    #Coordinates of vector A with respect to B
    c = np.concatenate([v1, v2], axis=1)
    c_inv = np.linalg.inv(c)
    b_vecs = np.dot(c_inv, a) #Coordinates with respect to basis b

    ax.text(a[0]*1.1,a[1]*1.1,
            'A='+str(round(b_vecs[0],2))+'*v1+'+str(round(b_vecs[1],2))+'*v2',
            color='orchid', weight='bold')

    v1_b = b_vecs[0]*v1
    v2_b = b_vecs[1]*v2
    ax.quiver(0,0,v1_b[0],v1_b[1],angles='xy',scale_units='xy',scale=1, color='pink')
    ax.text(v1_b[0]*1.1,v1_b[1]*1.1, 'V1 w.r.t B', color='pink')
    ax.quiver(0,0,v2_b[0],v2_b[1],angles='xy',scale_units='xy',scale=1, color='pink')
    ax.text(v2_b[0]*1.1,v2_b[1]*1.1, 'V2 w.r.t B', color='pink')


    plt.axvline(color='black')
    plt.axhline(color='black')
    plt.grid()
    plt.draw()
    plt.show()

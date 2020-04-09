import numpy as np
import matplotlib.pyplot as plt
import math

class vectors(object):

    def __init__(self, basis_vecs):
        self.coordinates = tuple([i for i in basis_vecs])

    def current_vectors(self):
        vecs = tuple(self.coordinates)
        for idx, vec in enumerate(vecs):
            print(f'Vector_{idx+1} coordinates are: {np.ravel(vec)}')

    def scalar_multiply(self, c):
        new_coords = tuple([c*x for x in self.coordinates])
        return new_coords

    def magnitude(self):
        coords_squared = tuple([x**2 for x in self.coordinates])
        mag = tuple([math.sqrt(sum(x)) for x in coords_squared])
        return mag

    def normalize(self):
        magn = self.magnitude()
        norm = tuple([1/x for x in magn])
        return norm

    def unit_vector(self):
        norm = tuple(self.normalize())
        unit_vector = [a*b for a,b in zip(norm, self.coordinates)]
        return unit_vector

    def Angle_between_vectors(self):
        if len(self.coordinates) ==2:
            v1_m,v2_m = self.magnitude()
            v1,v2 = self.coordinates
            print(f'Vector1 magnitude: {round(v1_m,2)}')
            print(f'Vector2 magnitude: {round(v2_m,2)}')
            inner_product = np.dot(np.ravel(v1), np.ravel(v2))
            print(f'Inner product of vectors: {inner_product}')
            angle_rad = math.acos((inner_product/ (v1_m*v2_m)))
            degrees_per_radian = 180/math.pi
            solution = angle_rad* degrees_per_radian
            print(f'Angle between vector 1 & 2 is: {round(solution,2)}°')

        else:
            print('Method only works for two vector input')

class graph(vectors):

    def __init__(self, basis_vecs):
        self.coordinates = tuple([i for i in basis_vecs])
        super().__init__(basis_vecs)

    def plot(self, magnitude=False, unit_vector=False):
        plt.figure()
        ax = plt.gca()
        vectors = tuple([x for x in self.coordinates])
        for v in vectors:
                ax.quiver(0,0, v[0], v[1], angles='xy',scale_units='xy',scale=1)
        x,y = zip(*vectors)
        ax.set_xlim([min(x)-3, max(x)+3])
        ax.set_ylim([min(y)-3,max(y)+3])


        if magnitude:
            mag = tuple(self.magnitude())
            vectors = tuple([x for x in self.coordinates])
            for idx, (v,m) in enumerate(zip(vectors,mag)):
                ax.text(v[0]*1.1, v[1]*1.1,
                        'Vector'+ str(idx+1)+ ': magnitude of ' +str(round(m,2)), color='blue')

        if unit_vector:
            norm = tuple(self.unit_vector())
            for idx,n in enumerate(norm):
                ax.quiver(0,0, n[0], n[1], angles='xy',scale_units='xy',scale=1, color='orange')
                ax.text(n[0]*2, n[1]*2,
                        'Unit_vec'+ str(idx+1)+ ':'+ str((np.ravel(n).round(2))), color='orange', weight='bold')

        plt.axvline(color='black')
        plt.axhline(color='black')
        plt.grid()
        plt.draw()
        plt.show()

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv

#def randrange(n, vmin, vmax):
#    return (vmax-vmin)*np.random.rand(n) + vmin

class CoOrd():
    def __init__(self):
        self.x = None
        self.y = None
        self.z = None
    def print_all(self):
        print self.x, self.y, self.z

class Reader():
    def __init__(self):
        self.x_coords = []
        self.y_coords = []
        self.h_coords = []
        self.z_values = []
        self.coord_list = []
        
    def magFieldReader(self):
        f=open('MagFieldReadings.csv','rb')
        reader=csv.reader(f)
        for line in reader:
            co = CoOrd() #0: atomic number, 1: atomic mass 2: name, 3: symbol
            co.z = float(line[0])
            co.x = float(line[1])
            co.y = float(line[2])
            co.h = float(line[3])
            self.x_coords.append(co.x)
            self.y_coords.append(co.y)
            self.z_values.append(co.z)
            self.h_coords.append(co.h)
            self.coord_list.append(co)

rdr = Reader()
rdr.magFieldReader()

print rdr.x_coords
print rdr.y_coords
print rdr.z_values

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#n = 100

#ax.scatter(rdr.x_coords, rdr.y_coords, rdr.h_coords, c='r', marker='o')
ax.scatter(rdr.x_coords, rdr.y_coords, rdr.z_values, c='r', marker='o')
for i in range(len(rdr.x_coords)):
    ax.plot([rdr.x_coords[i],rdr.x_coords[i]],[rdr.y_coords[i],rdr.y_coords[i]],[0.0,rdr.z_values[i]])
#for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
#    xs = randrange(n, 23, 32)
#    ys = randrange(n, 0, 100)
#    zs = randrange(n, zl, zh)
#    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
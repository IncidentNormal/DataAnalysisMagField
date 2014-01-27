from mpl_toolkits.mplot3d import Axes3D

from matplotlib.mlab import griddata
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import csv
from mpl_toolkits.mplot3d import Axes3D

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
            if line[1] == ' %LOC':
                print 'ignore this value'
            else:
                co.z = float(line[0])
                co.x = float(line[1])
                co.y = float(line[2])
                co.h = float(line[3])
    #            if co.z > 150.0:
    #                co.z = 150.0
                self.x_coords.append(co.x)
                self.y_coords.append(co.y)
                self.z_values.append(co.z)
                self.h_coords.append(co.h)
                self.coord_list.append(co)

rdr = Reader()
rdr.magFieldReader()

x_min = np.min(rdr.x_coords)
x_max = np.max(rdr.x_coords)
y_min = np.min(rdr.y_coords)
y_max = np.max(rdr.y_coords)
z_min = np.min(rdr.h_coords)
z_max = np.max(rdr.h_coords)
#z_min = np.min(rdr.z_values)
#z_max = np.max(rdr.z_values)

xi = np.linspace(x_min, x_max, 200)
yi = np.linspace(y_min, y_max, 200)
zi = griddata(rdr.x_coords, rdr.y_coords, rdr.z_values, xi, yi, interp='nn')
#zi = griddata(rdr.x_coords, rdr.y_coords, rdr.h_coords, xi, yi, interp='nn')

print xi
print yi
print zi

CS = plt.contour(xi,yi,zi,15,linewidths=0.5,colors='k')
#CS = plt.contourf(xi,yi,zi,15,cmap=plt.cm.rainbow,
#                  vmax=abs(zi).max(), vmin=-abs(zi).max())
plt.colorbar() # draw colorbar
# plot data points.
plt.scatter(rdr.x_coords,rdr.y_coords,marker='o',c='b',s=5,zorder=10)
plt.xlim(x_min,x_max)
plt.ylim(y_min,y_max)
plt.title('griddata test')
plt.show()

#X, Y = np.meshgrid(rdr.x_coords,rdr.y_coords)
#
#
#fig = plt.figure()
#ax = fig.gca(projection='3d')
##R = np.sqrt(X**2 + Y**2)
##Z = np.sin(R)
#surf = ax.plot_surface(xi, yi, zi, rstride=1, cstride=1, cmap=cm.coolwarm,
#        linewidth=0, antialiased=False)
#ax.set_zlim(z_min, z_max)
#
#ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
#
#fig.colorbar(surf, shrink=0.5, aspect=5)
#
#plt.show()
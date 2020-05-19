import numpy as np
from scipy.integrate import odeint
from math import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#inital conditions
t = np.linspace(0.0, 3200) #start and end time
mu = 398600.446 #gravitational constant
r0 = np.array([1711.3, 3347.9, 276.5]) #position vector at time 0
v0 = np.array([-9.6088, 4.8696, 0.050783]) #velocity vector at time 0

x0 = np.array([r0, v0])
x = x0.flatten()

#empty array to be filled with function output
dx = np.zeros(6)

#defining orbit function
def orbit(x, t):

    r_x = x[0]
    r_y = x[1]
    r_z = x[2]
    r = sqrt(r_x**2+r_y**2+r_z**2)

    dx[0] = x[3]
    dx[1] = x[4]
    dx[2] = x[5]

    dx[3] = -(mu/r**3)*r_x
    dx[4] = -(mu/r**3)*r_y
    dx[5] = -(mu/r**3)*r_z

    return dx

#intgetating function output
int0 = odeint(orbit, x, t)
int = int0.flatten()

#selecting 'coloumn' of x, y and z values
r_x = int[0::6]
r_y = int[1::6]
r_z = int[2::6]

#plotting results
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(r_x, r_y, r_z)
ax.set_title('Near Earth Orbit')
ax.set_xlabel('X-Axis (km)')
ax.set_ylabel('Y-Axis (km)')
ax.set_zlabel('Z-Axis (km)')
plt.show()

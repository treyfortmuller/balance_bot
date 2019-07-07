# simulation of an inverted pendulum fixed to an axis using scipy's "odeint"
# including torque terms for gravity, damping, and a motor acting at the axis
# of rotation of the pendulum

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# define constants
g = 9.81 # m/s^2
m = 5 # kg
l = 1.0 # meters
k = 0.5 # N*m*s 

# define the diff eq to simulate - note it doesn't actually make use of t
def model(U, t):
	# theta = U[0]
	# theta_dot = U[1]
	
	omega = U[1]
	# open loop dynamics
	# omega_dot = (g/l)*np.sin(U[0]) - (k/(m*l**2))*U[1]

	# with motor input
	motor_torque = 0
	omega_dot = (g/l)*np.sin(U[0]) - (k/(m*l**2))*U[1] - (1/(m*l**2))*motor_torque

	return [omega, omega_dot]

# initial conditions
theta0 = 0.1
omega0 = 0
U0 = [theta0, omega0]

# discrete time to simulate over
t = np.linspace(0, 50, num=1000)

# solve ODE
soln = odeint(model, U0, t)

# pendulum mass positions
x = l*np.sin(soln[:,0])
y = l*np.cos(soln[:,0])

# or in polar
theta = soln[:,0]

# plot results
# angle over time
plt.figure(0)
plt.plot(t, soln[:,0])

plt.title('Pendulum Angle vs. Time')
plt.ylabel('pend ang [rad]')
plt.xlabel('time [s]')

# position
plt.figure(1)
plt.scatter(x, y)

plt.axis('scaled') # ensure the circular path of the pend appears circular

plt.title('Pendulum Mass Position')
plt.ylabel('y position [m]')
plt.xlabel('x position [m]')

# polar
plt.figure(2)
plt.polar(theta, [l]*len(theta))

# ax.set_theta_zero_location("N")

plt.show()

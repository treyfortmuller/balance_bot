# simulation of an inverted pendulum fixed to an axis using scipy's "odeint"
# including torque terms for gravity, damping, and a motor acting at the axis
# of rotation of the pendulum

# TODO: incorporate motor torque input connected to the controller

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation

# define constants
g = 9.81 # m/s^2
m = 5 # kg
l = 0.5 # meters
k = 0.5 # N*m*s

SIM_TIME = 30 # seconds
UPDATE_FREQ = 100 # Hz

# define the diff eq to simulate - note it doesn't actually make use of t
def model(U, t):
	# theta = U[0]
	# theta_dot = U[1]
	
	omega = U[1]
	# open loop dynamics
	# omega_dot = (g/l)*np.sin(U[0]) - (k/(m*l**2))*U[1]

	# with motor input
	motor_torque = 1
	omega_dot = (g/l)*np.sin(U[0]) - (k/(m*l**2))*U[1] - (1/(m*l**2))*motor_torque

	return [omega, omega_dot]

# initial conditions
theta0 = 0.5
omega0 = 0
U0 = [theta0, omega0]

# discrete time to simulate over
t = np.linspace(0, SIM_TIME, num=SIM_TIME*UPDATE_FREQ)

# solve ODE
soln = odeint(model, U0, t)

# pendulum mass positions
x = l*np.sin(soln[:,0])
y = l*np.cos(soln[:,0])

# real time animation of the simulated system
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

# animation function to call at each frame
def animate(i):
	ax1.clear()

	plt.axis('scaled') # ensure the circular path of the pend appears circular
	plt.grid()
	
	plt.title('Pendulum Mass Position')
	plt.ylabel('y position [m]')
	plt.xlabel('x position [m]')

	ax1.set_ylim(-1.2, 1.2)
	ax1.set_xlim(-1.2, 1.2)
	
	ax1.scatter(x[i], y[i], s=200)

# the interval between frames in milliseconds
ms_interval = (1.0/UPDATE_FREQ)*(10**3)

ani = FuncAnimation(fig, animate, interval=ms_interval)
plt.show()


import springParam as P
from signalGenerator import signalGenerator
from springAnimation import massSpringAnimation
from dataPlotter import dataPlotter
from springDynamics import massSpringDynamics
from springController import massSpringController
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
sys.path.append('..')  # add parent directory
matplotlib.use('TkAgg')

# instantiate reference input classes
massSpring = massSpringDynamics()
controller = massSpringController()
reference = signalGenerator(amplitude=4.0, frequency=0.1)
zRef = signalGenerator(amplitude=60.0*np.pi/180.0, frequency=0.05)
fRef = signalGenerator(amplitude=0.0)

# instantiate the simulation plots and animation
dataPlot = dataPlotter()
animation = massSpringAnimation()

t = P.t_start
y = massSpring.h()
while t < P.t_end:
    # Propagate dynamics in between plot samples
    t_next_plot = t + P.t_plot
    # updates control and dynamics at faster simulation rate
    while t < t_next_plot:
        # Get referenced inputs from signal generators
        r = zRef.square(t)
        d = fRef.step(t)
        x = massSpring.state
        u = controller.update(r, x)
        z = massSpring.update(u + d)
        t = t + P.Ts
    # update animation and data plots
    #state = np.array([[z], [0.0]])
    animation.update(massSpring.state)
    dataPlot.update(t, r, massSpring.state, u)
    plt.pause(0.0001)

'''
t = P.t_start# time starts at t_start
while t < P.t_end:  # main simulation loop
    # set variables
    r = reference.sawtooth(t)
    z = zRef.sin(t)
    f = fRef.sin(t)
    # update animation
    state = np.array([[z], [0.0]])
    animation.update(state)
    dataPlot.update(t, r, state, f)
    t = t + P.t_plot  # advance time by t_plot
    plt.pause(0.0001)
'''
# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()

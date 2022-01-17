from dataPlotterObserver import dataPlotterObserver
from springController import massSpringController
from springDynamics import massSpringDynamics
from dataPlotter import dataPlotter
from springAnimation import massSpringAnimation
from signalGenerator import signalGenerator
import springParam as P
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
sys.path.append('..')  # add parent directory

# instantiate reference input classes
massSpring = massSpringDynamics(alpha=0.0)
controller = massSpringController()
reference = signalGenerator(amplitude=57.0*np.pi/180, frequency=0.05)
zRef = signalGenerator(amplitude=0.25)
fRef = signalGenerator(amplitude=0.01)

# instantiate the simulation plots and animation
dataPlot = dataPlotter()
dataPlotObserver = dataPlotterObserver()
animation = massSpringAnimation()

t = P.t_start
z = massSpring.h()
while t < P.t_end:
    # Propagate dynamics in between plot samples
    t_next_plot = t + P.t_plot
    # updates control and dynamics at faster simulation rate
    while t < t_next_plot:
        # Get referenced inputs from signal generators
        r = reference.square(t)
        d = zRef.step(t)  # 0
        n = fRef.random(t)
        u, xhat, dhat = controller.update(r, z + n)
        z = massSpring.update(u + d)
        t = t + P.Ts
    # update animation and data plots
    #state = np.array([[z], [0.0]])
    animation.update(massSpring.state)
    dataPlot.update(t, r, massSpring.state, u)
    dataPlotObserver.update(t, massSpring.state, xhat, d, dhat)

    # the pause causes the figure to display during simulation
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

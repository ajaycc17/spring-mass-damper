import simpy
import numpy as np
import matplotlib
import springParam as P
from systemAnimation import massSpringAnimation
from signalGenerator import signalGenerator
import import_ipynb
import statistics
import random
import systemDynamics
import dataPlotter
import simCart
import sineSignalInputCart
import matplotlib.pyplot as plt
matplotlib.use('TKAgg')

# instantiate system, controller and refernce classes

reference = signalGenerator(amplitude=1.0, frequency=0.05)
disturbance = signalGenerator(amplitude=1.0, frequency=0.5)
noise = signalGenerator(amplitude=0.01, frequency=0.1)

# instantiate the simulation plots and animation
animation = massSpringAnimation()

t = P.t_start

while t < P.t_end:
    r = reference.square(t)
    d = disturbance.step(t)
    n = noise.random(t)
    u = reference.sawtooth(t)
    states = np.array([[d], [n]])
    animation.update(states)

    t = t + P.t_plot
    plt.pause(0.05)

print('Press any Key to close')
plt.waitforbuttonpress()
plt.close

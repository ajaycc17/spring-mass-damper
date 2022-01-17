# Spring Mass Damper Parameters

k = 3.74            # N/m
b = 0.57            # Ns/m
m = 5.7             # kg
g = 9.8
ell = 0.1
h = 0.3
w = 0.015
gap = 0.007
ww = 0.35
hh = .3

# Initial Conditions
z = 0.0
zdot = 0.0
theta = 0.0
thetadot = 0.0

# Simulation Parameters
t_start = 0.0           # Start time
t_end = 20.0            # End time
Ts = 0.01               # sample time
t_plot = 0.1            # updating time for plot and animation

# Dirty derivatives parameters
sigma = 0.05                            # cutoff freq for dirty derivative
beta = (2.0*sigma-Ts)/(2.0*sigma+Ts)    # dirty derivative gain

# saturation limits
F_max = 2.0

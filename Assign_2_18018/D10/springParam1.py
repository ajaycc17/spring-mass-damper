# Mass Spring Damper System Parameters
import springParam as P
import numpy as np
import sys
sys.path.append('..')  # add parent directory

Ts = P.Ts  # sample rate of the controller
beta = P.beta  # dirty derivative gain
tau_max = P.tau_max  # limit on control signal

#  tuning parameters
# tr = 2 # part (a)
tr = 1.6  # tuned to get fastest possible rise time before saturation.
zeta = 0.7
ki = 0.1  # integrator gain

# desired natural frequency
wn = 2.2/tr
alpha1 = 2.0*zeta*wn
alpha0 = wn**2

# compute PD gains
kp = P.m*(alpha0 - (P.k/P.m))
kd = P.m*(alpha1 - (P.b/P.m))

print('kp: ', kp)
print('kd: ', kd)
print('ki: ', ki)
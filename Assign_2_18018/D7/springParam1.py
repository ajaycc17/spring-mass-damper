import numpy as np
import springParam as P
#import control as cnt
import sys
sys.path.append('..')  # add parent directory

Ts = P.Ts  # sample rate of the controller
beta = P.beta  # dirty derivative gain
tau_max = P.tau_max  # limit on control signal

# PD gains
kp = 4.822
kd = 13.714

print('kp: ', kp)
print('kd: ', kd)

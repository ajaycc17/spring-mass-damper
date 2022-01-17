from PIDControl import PIDControl
import springParam as P0
import numpy as np
import springParam1 as P
import sys
sys.path.append('..')  # add parent directory
'''
class massSpringController:
    def __init__(self):

        # Instantiates the PD object
        self.kp = P.kp
        self.kd = P.kd
        self.limit = P.tau_max

    def update(self, z_r, x):
        z = x.item(0)
        zdot = x.item(1)

        # feedback linearized force
        tau_fl = P0.k*z

        # equilibrium for around z_e = 0
        #z_e = 0.0
        #tau_e = P0.k*z_e

        # compute the linearized force using PD control
        tau_tilde = self.kp * (z_r - z) - self.kd * zdot

        # compute total force
        tau = tau_fl + tau_tilde

        #tau = tau_e + tau_tilde
        # always saturate to protect hardware
        tau = self.saturate(tau)

        return tau

    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u
'''


class massSpringController:

    def __init__(self):
        # Instantiates the PD object
        self.zCtrl = PIDControl(P.kp, P.ki, P.kd,
                                P0.tau_max, P.beta, P.Ts)
        self.limit = P0.tau_max

    def update(self, z_r, y):
        z = y.item(0)

        # compute feedback linearized torque tau_fl
        tau_fl = P0.k*z

        # compute the linearized torque using PD
        tau_tilde = self.zCtrl.PID(z_r, z, False)

        # compute total torque
        tau = tau_fl + tau_tilde
        tau = self.saturate(tau)

        return tau

    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)

        return u

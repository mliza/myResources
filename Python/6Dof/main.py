import matplotlib.pyplot as plt
import numpy as np
import math
import IPython

from numerical_integrators import numerical_integration_methods
from governing_equations import flat_earth_eom


# --------------------------------#
## Part 1: Initialize simulation ##
# --------------------------------#

# Define Vehicle (a sphere for now)
r_sphere_m = 0.08
m_sphere_kg = 5
J_sphere_kgm2 = 0.4 * m_sphere_kg * r_sphere_m**2

# Aircraft Properties
amod = { "m_kg" : 1,
        "Jxz_b_kgm2" : 0,
        "Jxx_b_kgm2" : J_sphere_kgm2,
        "Jyy_b_kgm2" : J_sphere_kgm2,
        "Jzz_b_kgm2" : J_sphere_kgm2 }

# Set initial conditions (these conditions may be loaded from an aircraft
# trim routine in future versions of the code)
u0_bf_mps = 0.0
v0_bf_mps = 0.0
w0_bf_mps = 0.0
p0_bf_rps = 0.0
q0_bf_rps = 0.0
r0_bf_rps = 0.0
r0_rad = np.deg2rad(0.0)
p0_rad = np.deg2rad(0.0)
y0_rad = np.deg2rad(0.0)
p10_n_m = 0.0
p20_n_m = 0.0
p30_n_m = 0.0

# Assign initial conditions to an array
x0 = np.array([
                u0_bf_mps,  # x-axis body-fixed velocity [m/s]
                v0_bf_mps,  # y-axis body-fixed velocity [m/s] 
                w0_bf_mps,  # z-axis body-fixed velocity [m/s] 
                p0_bf_rps,  # roll rate [rad/s] 
                q0_bf_rps,  # pitch rate [rad/s]
                r0_bf_rps,  # yaw rate [rad/s] 
                r0_rad,     # roll angle [rad] 
                p0_rad,     # pitch angle [rad] 
                y0_rad,     # yaw angle [rad] 
                p10_n_m,    # x-axis position [Nm]
                p20_n_m,    # y-axis position [Nm]
                p30_n_m     # z-axis position [Nm]
                ])

# Make the initial condition array a column vector 
x0 = x0.transpose()
nx0 = x0.size

# Set time Conditions
t0_s = 0.0
tf_s = 10.0
h_s  = 0.005


# -----------------------------------------------------------------------#
## Part 2: Numerically approximate solutions to the governing equations ##
# -----------------------------------------------------------------------#
# Preallocate the solution array
t_s = np.arange(t0_s, tf_s + h_s, h_s)
nt_s = t_s.size
x = np.zeros((nx0, nt_s))

# Assign the initial condition x0, to solution array, x
x[:,0] = x0

# Perform forward Euler integration
t_s, x = numerical_integration_methods.forward_euler(
                                            flat_earth_eom.flat_earth_eom, 
                                            t_s, x, h_s, amod)

# Data post-processing

# -------------------##
## Part 3: Plot Data ## 
# -------------------##




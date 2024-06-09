import matplotlib.pyplot as plt
import numpy as np
import math
import ussa1976
import IPython

from numerical_integrators import numerical_integration_methods
from governing_equations import flat_earth_eom
from tools.Interpolators import fastInterp1
from vehicle_models.sphere import spheres


# --------------------------------#
## Part 1: Initialize simulation ##
# --------------------------------#

# A. Atmospheric data
atmosphere = ussa1976.compute()

# Get essential gravity and atmospheric data
alt_m    = atmosphere["z"].values
rho_kgm3 = atmosphere["rho"].values
c_mps    = atmosphere["cs"].values
g_mps2   = ussa1976.core.compute_gravity(alt_m)

amod    = { "alt_m"    : alt_m,
            "rho_kgm3" : rho_kgm3,
            "c_mps"    : c_mps,
            "g_mps2"   : g_mps2 } # Atmosphere and gravity data

# B. Define vehicle
#vmod = spheres.BowlingBall()
vmod = spheres.Mustketball1150()

print(f"The analytical terminal velocity is {vmod['Vterm_mps']:.2f} m/s.")


"""
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
"""

# Set initial conditions (these conditions may be loaded from an aircraft
# trim routine in future versions of the code)
u0_bf_mps = 0.001   # Avoids dividing by zero
v0_bf_mps = 0.0
w0_bf_mps = 0.0
p0_bf_rps = 0.0
q0_bf_rps = 0.0
r0_bf_rps = 0.0
r0_rad = np.deg2rad(0.0)
p0_rad = np.deg2rad(-90.0)
y0_rad = np.deg2rad(0.0)
p10_n_m = 0.0
p20_n_m = 0.0
p30_n_m = -3E4

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

# Get number of elements in x0 
nx0 = x0.size

# Set time conditions
t0_s = 0.0
tf_s = 185.0
h_s  = 0.01


# -----------------------------------------------------------------------#
## Part 2: Numerically approximate solutions to the governing equations ##
# -----------------------------------------------------------------------#
# Preallocate the solution array
t_s = np.arange(t0_s, tf_s + h_s, h_s)
nt_s = t_s.size
x = np.zeros((nx0, nt_s))

# Assign the initial condition x0, to solution array, x
x[:,0] = x0

# A. Perform forward Euler integration
t_s, x = numerical_integration_methods.forward_euler(
                                            flat_earth_eom.flat_earth_eom,
                                            t_s, x, h_s, amod)

# B. Data post-processing

# Airspeed
True_Airspeed_mps = np.zeros((nt_s, 1))
for i, element in enumerate(t_s):
    True_Airspeed_mps[i,0] = np.sqrt(x[0,i]**2 + x[1,i]**2 + x[2,i]**2)

# Altitude, speed of sound, and air density
Altitude_m = np.zeros((nt_s, 1))
Cs_mps     = np.zeros((nt_s, 1))
Rho_kgm3   = np.zeros((nt_s, 1))

for i, element in enumerate(t_s):
    Altitude_m[i,0] = -x[11,i]
    Cs_mps[i,0]     = fastInterp1(amod["alt_m"], amos["c_mps"],
                                 Altitude_m[i,6])
    Rho_kgpm3[i,0]  = fastInterp1(amod["alt_m"], amos["rho_kgpm3"],
                                 Altitude_m[i,6])

# Angle of attack
Alpha_rad = np.zeros((nt_s,1))
for i, element in enumerate(t_s):
    if x[0,i] == 0 and x[2,i] == 0:
        w_over_v = 0.0
    else:
        w_over_v = x[2,i] / x[0,i]

    Alpha_rad[i,0] = np.atan(w_over_v)

# Angle of side slip
Beta_rad = np.zeros((nt_s,1))
for i, element in enumerate(t_s):
    if x[1,i] == 0 and True_Airspeed_mps[i,0] == 0:
        v_over_VT = 0.0
    else:
        v_over_VT = x[1,i] / True_Airspeed_mps[i,0]

    Beta_rad[i,0] = np.asin(v_over_VT)

# Mach number
Mach = np.zeros((nt_s, 1))
for i, elemntm in enumerate(t_s):
    Mach[i,0] = True_Airspeed_mps[i,0] / Cs_mps[i,0]

print(f"The numerical terminal velocity is {x[0,-1]:.2f} m/s.")

# -------------------##
## Part 3: Plot Data ## 
# -------------------##




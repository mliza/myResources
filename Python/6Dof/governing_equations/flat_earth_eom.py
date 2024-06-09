import math
import numpy as np
from tools.Interpolators import fastInterp1

def flat_earth_eom(time_s:float,
                  state_vector:np.ndarray,
                   vmod, amod) -> np.ndarray:
    """
        Arguments
        state_vector at time t [various units] 
        state_vector[0] = u_b_mps, axial velocity of CM wrt inertial CS 
                          resolved in aircraft body fixed CS
        state_vector[1] = v_b_mps, axial velocity of CM wrt inertial CS 
                          resolved in aircraft body fixed CS
        state_vector[2] = w_b_mps, axial velocity of CM wrt inertial CS 
                          resolved in aircraft body fixed CS
        state_vector[3] = p_b_rsp, roll angular velocity of body fixed CS 
                          with respect to inertial CS
        state_vector[4] = q_b_rsp, pitch angular velocity of body fixed CS 
                          with respect to inertial CS
        state_vector[5] = r_b_rsp, yaw angular velocity of body fixed CS 
                          with respect to inertial CS
        state_vector[6] = r_rad, roll angle
        state_vector[7] = p_rad, pitch angle
        state_vector[8] = y_rad, yaw angle
        state_vector[9] = p1_NED, x-axis position of aircraft resolved in NED CS
        state_vector[9] = p2_NED, y-axis position of aircraft resolved in NED CS
        state_vector[9] = p3_NED, z-axis position of aircraft resolved in NED CS
        vmod  = aircraft model data stored as a dictionary containing
                          various parameters
        amod = atmospheric model data stored as a dictionary containing
                          various parameters
        return derivative_state_vector (RHS of governing equations)  
    """

    # Preallocate left hand side of equations 
    derivative_state_vector = np.empty((12,), dtype=float)

    # Assign current state values to variable names
    u_b_mps = state_vector[0]
    v_b_mps = state_vector[1]
    w_b_mps = state_vector[2]
    p_b_rsp = state_vector[3]
    q_b_rsp = state_vector[4]
    r_b_rsp = state_vector[5]
    r_rad   = state_vector[6]
    p_rad   = state_vector[7]
    y_rad   = state_vector[8]
    p1_NED  = state_vector[9]
    p2_NED  = state_vector[10]
    p3_NED  = state_vector[11]

    # Compute trig operations on euler angles
    c_phi   = np.cos(r_rad)
    c_theta = np.cos(p_rad)
    c_psi   = np.cos(y_rad)
    s_phi   = np.sin(r_rad)
    s_theta = np.sin(p_rad)
    s_psi   = np.sin(y_rad)
    t_theta = np.tan(p_rad)

    # Get mass and moments of inertia
    m_kg = vmod['m_kg']
    Jxz_b_kgm2 = vmod['Jxz_b_kgm2']
    Jxx_b_kgm2 = vmod['Jxx_b_kgm2']
    Jyy_b_kgm2 = vmod['Jyy_b_kgm2']
    Jzz_b_kgm2 = vmod['Jzz_b_kgm2']

    # Get current altitude
    h_m = -p3_n_m

    # US Standard Atmosphere 1976
    rho_interp_kgpm3 = fastInterp1(amod["alt_m"], amod["rho_kgpm3"], h_m)
    #rho_interp_kgpm3 = 1.20 
    c_interp_mps2    = fastInterp1(amod["alt_m"], amod["c_mps"], h_m)

    # Air data calculation (Mach, AoA, AoS)
    true_airspeed_mps = np.sqrt(u_b_mps**2 + v_b_mps**2 + w_b_mps**2)
    qbar_kgpms2       = 0.5 * rho_interp_kgpm3 * true_airspeed_mps**2

    if u_b_mps == 0 and w_b_mps == 0:
        w_over_u = 0.0
    else:
        w_over_u = w_b_mps / u_b_mps

    if true_airspeed_mps == 0 and v_b_mps == 0:
        v_over_VT = 0.0
    else:
        v_over_VT = v_b_mps / true_airspeed_mps

    alpha_rad = np.atan(w_over_u)
    beta_rad  = np.asin(v_over_VT)
    s_alpha   = np.sin(alpha_rad)
    c_alpha   = np.cos(alpha_rad)
    s_beta    = np.sin(beta_rad)
    c_beta    = np.cos(beta_rad)

    # Gravity acts normal to earth tangent CS
    gz_interp_n_mps2 = fastInterp1(amod["alt_m"], amod["g_mps2"],  h_m)
    # gz_interp_n_mps2 = 9.81

    # Resolve gravity in body coordinates
    gx_b_mps2 = -gz_interp_n_mps2 * s_theta
    gy_b_mps2 = gz_interp_n_mps2 * s_phi * c_theta 
    gz_b_mps2 = gz_interp_n_mps2 * c_phi * c_theta 

    # Aerodynamic forces
    drag_kgmps2 = vmode["CD_approx"] * qbar_kgpms2 * vmod["Aref_m2"]
    side_kgmps2 = 0.0
    lift_kgmps2 = 0.0

    # External forces (Angles might be off)
    Fx_b_kgmps2 = -( c_alpha * c_beta * drag_kgmps2 - 
                     c_alpha * s_beta * side_kgmps2 - 
                     s_alpha * lift_kgmps2 )
    Fy_b_kgmps2 = -( s_beta * drag_kgmps2 + 
                     c_beta * side_kgmps2 +
                     0.0 * lift_kgmps2 )
    Fz_b_kgmps2 = -( s_alpha * c_beta * drag_kgmps2 - 
                     s_alpha * s_beta * side_kgmps2 +
                     c_alpha * lift_kgmps2 )

    # External moments
    l_b_kgm2ps2 = 0.0
    m_b_kgm2ps2 = 0.0
    n_b_kgm2ps2 = 0.0

    # Denominator in roll and yaw rotational equations
    den = Jxx_b_kgm2 * Jzz_b_kgm2 - Jxz_b_kgm2**2 

    ## Write Translational State Equations ##
    # Linear-x velocity
    derivative_state_vector[0] = (1 / m_kg) * Fx_b_kgmps2 + gx_b_mps2 - \
                                 w_b_mps * q_b_rsp + v_b_mps * r_b_rsp

    # Linear-y velocity
    derivative_state_vector[1] = (1 / m_kg) * Fy_b_kgmps2 + gy_b_mps2 - \
                                 u_b_mps * r_b_rsp + w_b_mps * p_b_rsp

    # Linear-z velocity
    derivative_state_vector[2] = (1 / m_kg) * Fz_b_kgmps2 + gz_b_mps2 - \
                                 v_b_mps * p_b_rsp + u_b_mps * q_b_rsp

    ## Write Rotational State Equations ## 
    # Roll angular velocity
    derivative_state_vector[3] = (Jxz_b_kgm2 * (Jxx_b_kgm2 - Jyy_b_kgm2 + \
                                 Jzz_b_kgm2) * r_rad * p_rad  - \
                                 (Jzz_b_kgm2 * (Jzz_b_kgm2 - Jyy_b_kgm2) + \
                                 Jxz_b_kgm2**2) * p_rad * y_rad + Jzz_b_kgm2 * \
                                 l_b_kgm2ps2 + Jxz_b_kgm2 * n_b_kgm2ps2) / den

    # Pitch angular velocity
    derivative_state_vector[4] = ((Jzz_b_kgm2 - Jxx_b_kgm2) * y_rad * r_rad - \
                                 Jxz_b_kgm2 * (r_rad**2 - y_rad**2) + \
                                 m_b_kgm2ps2) / Jyy_b_kgm2

    # Yaw angular velocity
    derivative_state_vector[5] = (-Jxz_b_kgm2 * (Jxx_b_kgm2 - Jyy_b_kgm2 + \
                                 Jzz_b_kgm2) * p_rad * y_rad + (Jxx_b_kgm2 * \
                                 (Jxx_b_kgm2 - Jyy_b_kgm2) + Jxz_b_kgm2**2) *\
                                 r_rad * y_rad + Jxz_b_kgm2 * l_b_kgm2ps2 + \
                                 Jxx_b_kgm2 * n_b_kgm2ps2) / den

    ## Kinematic equations ##
    # Roll angular rate
    derivative_state_vector[6] = p_b_rsp + \
                                 q_b_rsp * s_phi * t_theta + \
                                 r_b_rsp * c_phi * t_theta
    # Pitch angular rate
    derivative_state_vector[7] = q_b_rsp * c_phi - \
                                 r_b_rsp * s_phi 
    # Yaw angular rate
    derivative_state_vector[8] = q_b_rsp * s_phi / c_theta + \
                                 r_b_rsp * c_phi / c_theta 
                
    # Position (Navigation) equations
    # xPosition-rate
    derivative_state_vector[9] = u_b_mps * c_theta * c_phi + \
                                 v_b_mps * (-c_phi * s_psi + \
                                            s_phi * s_theta * c_psi) + \
                                 w_b_mps * (s_phi * s_psi + \
                                            c_phi * s_theta * c_psi) 

    # yPosition-rate
    derivative_state_vector[10] = u_b_mps * (c_phi * s_psi) + \
                                  v_b_mps * (c_phi * c_psi + \
                                             s_phi * s_theta * s_psi) + \
                                  w_b_mps * (-s_phi * c_psi + \
                                            c_phi * s_theta * s_psi)

    # zPosition-rate
    derivative_state_vector[11] = u_b_mps * -s_theta + \
                                  v_b_mps * (s_phi * c_theta) + \
                                  w_b_mps * (c_phi * c_theta)

    return derivative_state_vector



import math
import numpy as np

def flat_earth_eom(time_s:float,
                  state_vector:np.ndarray,
                  aircraft_model:dict) -> np.ndarray:
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
        aircraft_model  = aircraft model data stored as a dictionary containing
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

    # Get mass and moments of inertia
    m_kg = aircraft_model['m_kg']
    Jxz_b_kgm2 = aircraft_model['Jxz_b_kgm2']
    Jxx_b_kgm2 = aircraft_model['Jxx_b_kgm2']
    Jyy_b_kgm2 = aircraft_model['Jyy_b_kgm2']
    Jzz_b_kgm2 = aircraft_model['Jzz_b_kgm2']

    # Air data Calculation (Mach, altitude, AoA, AoS)

    # Atmosphere model

    # Gravity acts normal to earth tangent CS
    gz_n_mps2 = 9.81

    # Resolve gravity in body coordinates
    gx_b_mps2 = - gz_n_mps2 * np.sin(p_rad)
    gy_b_mps2 = gz_n_mps2 * np.sin(r_rad) * np.cos(p_rad)
    gz_b_mps2 = gz_n_mps2 * np.cos(r_rad) * np.cos(p_rad) 

    # External forces
    Fx_b_kgmps2 = 0.0
    Fy_b_kgmps2 = 0.0
    Fz_b_kgmps2 = 0.0

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
    derivative_state_vector[6] = p_b_rsp + np.sin(r_rad) * np.tan(p_rad) * \
                                 q_b_rsp + np.cos(r_rad) * np.tan(p_rad) * \
                                 r_b_rsp
    # Pitch angular rate
    derivative_state_vector[7] = q_b_rsp * np.cos(r_rad) - \
                                 r_b_rsp * np.sin(r_rad) 
    # Yaw angular rate
    derivative_state_vector[8] = q_b_rsp * np.sin(r_rad) / np.cos(p_rad) + \
                                 r_b_rsp * np.cos(r_rad) / np.cos(p_rad)
                
    # Position (Navigation) equations
    derivative_state_vector[9] = 0.0 
    derivative_state_vector[10] = 0.0 
    derivative_state_vector[11] = 0.0

    return derivative_state_vector



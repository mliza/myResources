#!/opt/homebrew/bin/python3
'''
    Date:   03/31/2023 
    Author: Martin E. Liza
    File:   aerodynamics_class.py
    Def:    Contains aerodynamics helper functions. 

    Author		    Date		Revision
    -----------------------------------------------------------------
    Martin E. Liza	07/25/2022	Initial version.
    Martin E. Liza	08/04/2022	Added normal and oblique 
                                shock relation functions. 
    Martin E. Liza  03/25/2023  Added air molecular mass function. 
    Martin E. Liza  03/31/2023  Removed non useful functions.  

'''
import os 
import molmass
import numpy as np 
import scipy.constants as s_consts
from dataclasses import dataclass

@dataclass 
class Aero:  
    pass 

# Sutherland law
    def sutherland_law(self, temperature_field_K): 
        # https://doc.comsol.com/5.5/doc/com.comsol.help.cfd/cfd_ug_fluidflow_high_mach.08.27.html
        mu_ref  = 1.716e-5 # [kg/m*s] 
        T_ref   = 273      # [K]
        S_const = 111      # [K] 
        mu      = mu_ref * ( (temperature_field_K / T_ref)**(3/2) * ( 
                  (T_ref + S_const) / (temperature_field_K + S_const) ) )
        return mu #[kg/m*s] 

# Air molecular mass
    def air_atomic_mass(self):
        N2        = molmass.Formula('N2').mass # [g/mol] 
        O2        = molmass.Formula('O2').mass # [g/mol]
        N         = molmass.Formula('N').mass  # [g/mol]
        O         = molmass.Formula('O').mass  # [g/mol]
        NO        = molmass.Formula('NO').mass # [g/mol]

        air_mol_mass_dict = {'N2' : N2,
                             'O2' : O2,
                             'N'  : N,
                             'O'  : O,
                             'NO' : NO}
        return air_mol_mass_dict 

# Speed of sound 
    def speed_of_sound(self, temperature_K, specific_heat = 1.4):
        gas_const          = s_consts.R                  # [J/mol*K]
        air_atomic_mass    = self.air_atomic_mass()      # [g/mol] 
        air_molecular_mass = (0.7803 * air_atomic_mass['N2'] + 
                            0.2099 * air_atomic_mass['O2'] + 
                            0.0003 * air_atomic_mass['CO2']) * 1E-3 # [kg/mol]
        spd_of_sound       = np.sqrt(specific_heat * temperature_K * 
                                     gas_const / air_molecular_mass)  
        return spd_of_sound # [m/s]

# Normal shock relations  
    def normal_shock_relations(self, mach_1):
        # REF: https://www.grc.nasa.gov/www/k-12/airplane/normal.html
        # NOTE: ratio = var_1 / var_2
        gamma   = 1.4                                      
        mach_2  = np.sqrt( ((gamma - 1) * mach_1**2 + 2) / 
                           (2 * gamma * mach_1**2 - (gamma - 1)) )
        P_ratio = ( (2 * gamma / (gamma + 1)) * mach_1**2 - 
                    (gamma - 1) / (gamma + 1) ) 
        T_ratio = ( ((2 * gamma * mach_1**2 - (gamma - 1)) * 
            ((gamma - 1) * mach_1**2 + 2)) / ((gamma + 1)**2 * mach_1**2) )
        R_ratio = ( ((gamma + 1) * mach_1**2) / 
                    ((gamma - 1) * mach_1**2 + 2) )
        # Return Dictionary 
        normal_shock_dict = { 'mach_2'    : mach_2,
                              'P_ratio'   : P_ratio, 
                              'T_ratio'   : T_ratio,
                              'Rho_ratio' : R_ratio }
        return normal_shock_dict

# Oblique shock relations
    def oblique_shock_relations(self, mach_1, shock_angle_deg):
    # REF : Modern Compressible Flows With Historical Ref., eq 4.7 - 4.11 
    # NOTE: Equations only work for weak shocks 
    # Note ratio = var_1 / var_2
        gamma       = 1.4                                        
        shock_angle = np.radians(shock_angle_deg)  
        sin2_shock  = np.sin(shock_angle)**2
        mach_n1     = mach_1 * np.sin(shock_angle) #normal mach number 
        # Calculates Deflection angle 
        deflection_angle = ( np.tan(shock_angle) * (
                          ((gamma + 1) * mach_1**2) / 
                          (2 * (mach_n1**2  - 1)) - 1) ) 
        deflection_angle_deg = np.degrees(np.arctan(1 / deflection_angle)) 
        # Calculates properties downstream the shock  
        R_ratio = ( ((gamma + 1) * mach_n1**2) / 
                    ((gamma - 1) * mach_n1**2 + 2) )
        P_ratio = 1 + 2 * gamma * (mach_n1**2 - 1) / (gamma + 1) 
        T_ratio = P_ratio * 1 / R_ratio 
        # Calculates mach 2 
        mach_n2 = np.sqrt( (mach_n1**2 + (2 / (gamma - 1))) / 
                    ((2 * gamma / (gamma - 1)) * mach_n1**2 - 1) )
        mach_2  = mach_n2 / np.sin(np.radians(shock_angle_deg - 
                                  deflection_angle_deg)) 
        # Dictionary 
        oblique_shock_dict = { 'mach_2'    : mach_2,
                               'P_ratio'   : P_ratio, 
                               'T_ratio'   : T_ratio,
                               'Rho_ratio' : R_ratio }
        return oblique_shock_dict

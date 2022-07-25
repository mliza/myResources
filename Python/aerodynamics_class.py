#!/opt/homebrew/bin/python3
'''
    Date:   07/18/2022
    Author: Martin E. Liza
    File:   aerodynamics_class.py
    Def:    Contains aerodynamics helper functions. 

    Author		    Date		Revision
    ----------------------------------------------------
    Martin E. Liza	07/25/2022	Initial version.
'''
import os 
import molmass
import numpy as np 
import scipy.constants as s_consts
from dataclasses import dataclass
import IPython 

@dataclass 
class Aero:  
    pass 

# Sutherland Law
    def sutherland_law(self, temperature_field_K): 
        # https://doc.comsol.com/5.5/doc/com.comsol.help.cfd/cfd_ug_fluidflow_high_mach.08.27.html
        mu_ref  = 1.716e-5 # [kg/m*s] 
        T_ref   = 273      # [K]
        S_const = 111      # [K] 
        mu = mu_ref * ( (temperature_field_K / T_ref)**(3/2) * ( 
                        (T_ref + S_const) / (temperature_field_K + S_const) ) )
        return mu #[kg/m*s] 

# Speed of Sound 
    def speed_of_sound(self, temperature_field_K):
        gas_const = s_consts.R                  # [J/mol*K]
        gamma     = 1.4                         # [ ] 
        N2        = molmass.Formula('N2').mass  # [g/mol] 
        O2        = molmass.Formula('O2').mass  # [g/mol]
        Ar        = molmass.Formula('Ar').mass  # [g/mol]
        CO2       = molmass.Formula('CO2').mass # [g/mol]
        dry_air_m = (0.7803 * N2 + 
                     0.2099 * O2 + 
                     0.0094 * Ar + 
                     0.0003 * CO2) * 1E-3       # [kg/mol]
        spd_of_sound = np.sqrt(gamma * temperature_field_K * 
                               gas_const / dry_air_m) # [m/s]
        return spd_of_sound #[m/s]

# Turbulent Mach number
    def turbulent_mach_number(self, kinetic_energy, speed_of_sound): 
        kinetic_energy_fluctuation = np.sqrt( (kinetic_energy - 
                                      np.mean(kinetic_energy))**2 )   # [m^2 / s^2]
        turbulent_mach_number = (np.sqrt(2 * kinetic_energy_fluctuation) / 
                                 np.mean(speed_of_sound)) # [ ]
        return turbulent_mach_number





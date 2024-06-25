from ambiance import Atmosphere 
import numpy as np
import IPython

# Define Initial Condition, calculates kappa, epsilon and omega
def initial_conditions(velocity, characteristic_length,
                        altitude=np.linspace(-5.e3, 80e3, num=100)): 

    atmosphere = Atmosphere(altitude)
    reynolds_number = (atmosphere.density * velocity * 
                       characteristic_length / atmosphere.dynamic_viscosity)
    turbulent_length_scale = 0.07 * characteristic_length
    turbulent_intensity = 0.16 * reynolds_number ** (-1/8)

    # Calculates kappa, epsilon, omega
    turbulent_kinetic_energy = (3/2) * (velocity * turbulent_intensity)**2
    turbulent_dissipation = (0.09 ** (3/4) * (turbulent_kinetic_energy ** 3/2)  
                            / turbulent_length_scale)
    specific_dissipation = turbulent_dissipation / turbulent_kinetic_energy
    
    dict_out =  { 'kappa' : turbulent_kinetic_energy,
               'epsilon' : turbulent_dissipation,
               'omega': specific_dissipation }

    return dict_out

if __name__ == "__main__":
    #initial_condition = initial_conditions(velocity=140, characteristic_length=0.032)
    initial_condition = initial_conditions(velocity=1198.12,
                                           altitude=10000,
                                           characteristic_length=0.3)
    IPython.embed(colors = 'Linux')

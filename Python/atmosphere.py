from ambiance import Atmosphere
import matplotlib.pyplot as plt
import numpy as np
import IPython 



altitude = np.linspace(-5.e3, 80e3, num=100)
atmosphere = Atmosphere(altitude)
layers = atmosphere.layer_name
layer_index = np.unique(layers, return_index=True)
altitude_layers = altitude[layer_index[1]]


# Generating Plots
fix, axs= plt.subplots(2,3)

"""
axs[0,0].axhline(y=altitude[layer_index[1][0]]*1E-3, linestyle='--',
                 color='orange', label='Troposphere') 
axs[0,0].text(4, 1, 'Hellox', ha='right', va='top')

axs[0,0].axhline(y=altitude[layer_index[1][1]]*1E-3, linestyle='--',
                 color='orange', label='Tropopause') 

axs[0,0].text(4, 1, f'layer_index[-2]', ha='center', va='center')
axs[0,0].axhline(y=altitude[layer_index[1][3]]*1E-3, linestyle='--',
                 color='orange', label='Stratosphere') 

axs[0,0].text(4, 1, f'layer_index[-1]', ha='center', va='center')
axs[0,0].axhline(y=altitude[layer_index[1][4]]*1E-3, linestyle='--',
                 color='orange', label='Stratopause') 
axs[0,0].yticks(np.arange(0, 10*1E10, 10*1E3))
"""

axs[0,0].plot(atmosphere.pressure*1E-3, altitude*1E-3, linewidth=3)
axs[0,0].set(xlabel='Pressure $[kPa]$', ylabel='Altitude $[km]$')

axs[0,1].plot(atmosphere.density, altitude*1E-3, linewidth=3)
axs[0,1].set(xlabel='Density $[kg/m^3]$', ylabel='Altitude $[km]$')

axs[0,2].plot(atmosphere.kinematic_viscosity, altitude*1E-3, linewidth=3)
axs[0,2].set(xlabel='Kinematic Viscosity $[m^2/s]$', ylabel='Altitude $[km]$')

axs[1,0].plot(atmosphere.temperature, altitude*1E-3, linewidth=3)
axs[1,0].set(xlabel='Temperature $[K]$', ylabel='Altitude $[km]$')

axs[1,1].plot(atmosphere.speed_of_sound, altitude*1E-3, linewidth=3)
axs[1,1].set(xlabel='Speed of Sound $[m/s]$', ylabel='Altitude $[km]$')

axs[1,2].plot(atmosphere.dynamic_viscosity, altitude*1E-3, linewidth=3)
axs[1,2].set(xlabel='Dynamic Viscosity $[Pa\,s]$', ylabel='Altitude $[km]$')


#plt.tight_layout()
plt.show() 

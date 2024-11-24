from ambiance import Atmosphere
import matplotlib.pyplot as plt
import numpy as np
import IPython 
import os



altitude = np.linspace(0, 80e3, num=200)
atmosphere = Atmosphere(altitude)
layers = atmosphere.layer_name
layer_index = np.unique(layers, return_index=True)
altitude_layers = altitude[layer_index[1]]

## Figure Config ##
fig_width = 14
fig_height = 8
line_width = 3
dpi_size = 600
color_layers = 'darkviolet'
color_atm = 'black'

# Generating Plots
fix, axs= plt.subplots(2,4, figsize=(fig_width, fig_height), dpi=dpi_size)

# Plot properties ##
# Plot top 4 #
axs[0,0].plot(atmosphere.pressure*1E-3, altitude*1E-3, linewidth=line_width,
              color=color_atm)
axs[0,0].set(xlabel='Pressure $[kPa]$', ylabel='Altitude $[km]$')

axs[0,1].plot(atmosphere.density, altitude*1E-3, linewidth=line_width,
              color=color_atm)
axs[0,1].set(xlabel='Density $[kg/m^3]$', ylabel='Altitude $[km]$')

axs[0,2].plot(atmosphere.kinematic_viscosity, altitude*1E-3,
              linewidth=line_width, color=color_atm)
axs[0,2].set(xlabel='Kinematic Viscosity $[m^2/s]$', ylabel='Altitude $[km]$')

axs[0,3].plot(atmosphere.mean_free_path, altitude*1E-3,
              linewidth=line_width, color=color_atm)
axs[0,3].set(xlabel='Mean Free Path $[m]$', ylabel='Altitude $[km]$')

# Plot bottom 4 #
axs[1,0].plot(atmosphere.temperature, altitude*1E-3, linewidth=line_width,
              color=color_atm)
axs[1,0].set(xlabel='Temperature $[K]$', ylabel='Altitude $[km]$')

axs[1,1].plot(atmosphere.speed_of_sound, altitude*1E-3, linewidth=line_width,
              color=color_atm)
axs[1,1].set(xlabel='Speed of Sound $[m/s]$', ylabel='Altitude $[km]$')

axs[1,2].plot(atmosphere.dynamic_viscosity, altitude*1E-3,
              linewidth=line_width, color=color_atm)
axs[1,2].set(xlabel='Dynamic Viscosity $[Pa\,s]$', ylabel='Altitude $[km]$')

axs[1,3].plot(atmosphere.thermal_conductivity, altitude*1E-3,
              linewidth=line_width, color=color_atm)
axs[1,3].set(xlabel='Thermal Conductivity $[W/mK]$', ylabel='Altitude $[km]$')

"""
axs[0,0].set_xscale('log')
axs[0,1].set_xscale('log')
"""
axs[0,2].set_xscale('log')
axs[0,3].set_xscale('log')

for i in range(2):
    for j in range(4):
        for k, val in enumerate(layer_index[0]):
            axs[i,j].axhline(y=altitude[layer_index[1][k]]*1E-3,
                             linestyle='--', 
                             color=color_layers)
             # Dynamically determine the x position based on the subplot's x-axis range
            x_min, x_max = axs[i, j].get_xlim()  # Get current x-axis limits
            x_pos_left = x_min + 0.05 * (x_max - x_min)  # Set text position as 5% from the left
            x_pos_right = x_max - 0.05 * (x_max - x_min)  # Set text position as 5% from the left


            # Left
            if ( (val == layer_index[0][-1] and (i==0 and j==0)) or 
                 (val == layer_index[0][-1] and (i==0 and j==1)) or
                 (val == layer_index[0][-1] and i==1) or
                 (i==1 and val == layer_index[0][0]) or 
                 (i==1 and val == layer_index[0][1]) ):
                # Add the layer name at the calculated position
                axs[i, j].text(
                    x=x_pos_left,  #[x_pos_left, x_pos_right]
                    y=altitude[layer_index[1][k]] * 1E-3,  # Altitude for the text
                    s=val,  # Layer name
                    color=color_layers,
                    fontsize=10,
                    ha='left',  #[right,left] 
                    va='bottom'  # Align text below the line
                )
            else:
                # Right
                axs[i,j].text(
                    x=x_pos_right,  #[x_pos_left, x_pos_right]
                    y=altitude[layer_index[1][k]] * 1E-3,  # Altitude for the text
                    s=val,  # Layer name
                    color=color_layers,
                    fontsize=10,
                    ha='right',  #[right,left] 
                    va='bottom'  # Align text below the line
                )



for ax in axs.flat:
    ax.set_yticks(np.arange(0, 90, 10))  # From -5 to 80 km in 10 km increments
    ax.grid(visible=True, which='both', linestyle='--', linewidth=0.5,
            alpha=0.6)




plt.tight_layout()
#plt.show() 
desk_path = '/Users/martin/Desktop'
plt.savefig(os.path.join(desk_path,'atm.png'), format='png',
            bbox_inches='tight', dpi=dpi_size)

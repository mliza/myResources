#!/opt/homebrew/bin/python3
'''
    Date:   12/25/2023
    Author: Martin E. Liza
    File:   helper_class.py
    Def:    Contains some helper functions 
            for data processing and manipulation.  

    Author          Date        Revision
    -----------------------------------------------------
    Martin E. Liza  05/23/2022  Initial version.
    Martin E. Liza  07/18/2022  Added pickle_dict_add.
    Martin E. Liza  09/21/2022  Added smoothing_function.
    Martin E. Liza  10/28/2022  Added matlab flag to pickle manager.
    Martin E. Liza  12/25/2023  Made it a function instead of a class.
'''
import os 
import pickle 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import IPython 
import scipy.io 

# Loading unformatted fortran data  
def fortran_data_loader(variable_in, abs_path_in, d_type=float): 
    data_in = os.path.join(abs_path_in, f'{variable_in}')
    f_in    = scipy.io.FortranFile(data_in, 'r')
    data    = f_in.read_reals(dtype=d_type)
    f_in.close() 
    return data

# Loading solution_flow.csv from tecplot
def flow_loader(flow_file_in : str, flow_file_path : str) -> dict:
    abs_path_to_file = os.path.join(flow_file_path, flow_file_in)
    df_in = pd.read_csv(abs_path_to_file, index_col=False)
    dict_out = {i:df_in[i].to_numpy() for i in df_in.keys()}
    return dict_out

# Saves solution_flow.csv from dict 
def flow_save(dict_out : dict, flow_file_out : str, flow_file_path : str):
    df_out = pd.DataFrame.from_dict(dict_out)
    df_out.to_csv(os.path.join(flow_file_path, flow_file_out), index=False)

# Plots the raw input and noise data for each modified field
def plot_flow_noise(flow_in : dict, flow_noise : dict):
    fig, axs = plt.subplots(4,1) 
    # Plot Momentum_x
    axs[0].plot(flow_noise['PointID'], flow_noise['Momentum_x'],
                label='Perturbed')
    axs[0].plot(flow_in['PointID'], flow_in['Momentum_x'], label='Steady')
    axs[0].set_ylabel('Momentum_x')
    axs[0].legend()

    # Plot Momentum_y
    axs[1].plot(flow_noise['PointID'], flow_noise['Momentum_y'],
               label='Perturbed')
    axs[1].plot(flow_in['PointID'], flow_in['Momentum_y'], label='Steady')
    axs[1].set_ylabel('Momentum_y')
    axs[1].legend()

    # Plot Momentum_z
    axs[2].plot(flow_noise['PointID'], flow_noise['Momentum_z'],
               label='Perturbed')
    axs[2].plot(flow_in['PointID'], flow_in['Momentum_z'], label='Steady')
    axs[2].set_ylabel('Momentum_z')
    axs[2].legend()

    # Energy
    axs[3].plot(flow_noise['PointID'], flow_noise['Energy'],
               label='Perturbed')
    axs[3].plot(flow_in['PointID'], flow_in['Energy'], label='Steady')
    axs[3].set_ylabel('Energy')
    axs[3].legend()

    plt.xlabel('Iterations')
    IPython.embed(colors = 'Linux')

# Add noise to flow fields
def add_noise(dict_in : dict) -> dict: 
    vel_x = dict_in['Momentum_x'] / dict_in['Density']
    vel_y = dict_in['Momentum_y'] / dict_in['Density']
    vel_z = dict_in['Momentum_z'] / dict_in['Density']
    
    # Lambda-function to create a normal distribution to the field
    normal_noise = lambda field_in : np.random.normal(np.mean(field_in),
                            np.std(field_in), dict_in['PointID'][-1] + 1)

    # Perturbed velocity fields
    vel_x += normal_noise(vel_x/np.max(vel_x))
    vel_y += normal_noise(vel_y/np.max(vel_y))
    vel_z += normal_noise(vel_z/np.max(vel_z))
    dict_in['Energy'] +=
    normal_noise(dict_in['Energy']/np.max(dict_in['Energy'])

    # Make momentum perturbed momentum fields 
    dict_in['Momentum_x'] = vel_x * dict_in['Density']
    dict_in['Momentum_y'] = vel_y * dict_in['Density']
    dict_in['Momentum_z'] = vel_z * dict_in['Density']

    return dict_in


# Save data as pickle and loads data as a pickle 
def pickle_manager(pickle_name_file, pickle_path, data_to_save=None,
                   matlab_flag=None):
    # Loads pickle file if data_to_save is empty  
    if data_to_save is None:  
        file_in   = os.path.join(f'{pickle_path}',f'{pickle_name_file}.pickle') 
        pickle_in = open(file_in, 'rb')
        return pickle.load(pickle_in)
    # Creates pickle file if data_in has a path and saves it in that path  
    else:
        file_out   = os.path.join(f'{pickle_path}',f'{pickle_name_file}')
        if matlab_flag is None:
            pickle_out = open(f'{file_out}.pickle', 'wb') 
            pickle.dump(data_to_save, pickle_out)
            pickle_out.close() 
        else:
            scipy.io.savemat(f'{file_out}.mat', mdict=data_to_save) 

# Opens pickle dictionary, adds a variable and saves it
def pickle_dict_add(var_in_data, var_in_str, pickle_path, 
                    pickle_dict_in, pickle_dict_out):
    # Open pickle dictionary 
    dict_in = pickle_manager(pickle_dict_in, pickle_path) 
    dict_in[var_in_str] = var_in_data
    pickle_manager(pickle_dict_out, pickle_path, dict_in)

# Smoothing function 
def smoothing_function(data_in, box_pts):
    box         = np.ones(box_pts) / box_pts
    data_smooth = np.convolve(data_in, box, mode='same')
    return data_smooth 

if __name__ == "__main__":
    flow_file = 'solution_flow.csv'
    abs_path = '/Users/martin/Desktop/LES/converged_RANS'
    flow_out = 'perturbated_solution_flow.csv'
    dict_ = flow_loader(flow_file, abs_path) 
    dict_out = add_noise(dict_)
    flow_save(dict_out, flow_out, abs_path) 

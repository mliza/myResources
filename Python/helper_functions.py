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
import numpy as np 
import IPython 
import scipy.io 

# Loading unformatted fortran data  
def fortran_data_loader(variable_in, abs_path_in, d_type=float): 
    data_in = os.path.join(abs_path_in, f'{variable_in}')
    f_in    = scipy.io.FortranFile(data_in, 'r')
    data    = f_in.read_reals(dtype=d_type)
    f_in.close() 
    return data

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
